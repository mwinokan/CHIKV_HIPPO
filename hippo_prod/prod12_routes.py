import hippo

from sqlite3 import DatabaseError

from mlog import setup_logger

logger = setup_logger("CHIKV_prod12")

animal = hippo.HIPPO("CHIKV_prod12", "CHIKV_prod12.sqlite", copy_from="CHIKV_prod10.sqlite", overwrite_existing=True)

from tqdm import tqdm

bases = animal.compounds(tag="Syndirella base")
elabs = bases.elabs
products = bases + elabs

logger.var("products", products)

lookup = animal.db.get_route_id_product_dict()
existing_product_ids = set(lookup.values())

logger.var("#existing routes", len(lookup))
logger.var("#products with existing routes", len(existing_product_ids))

new_ids = [i for i in products.ids if i not in existing_product_ids]

products = animal.compounds[new_ids]

logger.var("remaining products", products)

for i, c in tqdm(enumerate(products), total=len(products)):

    try:
        reactions = c.reactions
    except DatabaseError:
        logger.error(f"Error getting {c}'s reactions")
        continue

    for reaction in reactions:

        try:
            recipes = reaction.get_recipes()
        except DatabaseError:
            logger.error(f"Error getting {reaction}'s ({c}) recipes")
            continue

        for recipe in recipes:

            route = animal.register_route(recipe=recipe)

            logger.info(f"registered {route=}")

    if i % 100 == 99:
        logger.success("Committing...")
        animal.db.commit()

animal.db.close()

# sb.sh --job-name CHIKV_prod12_routes -pmain --exclusive $HOME2/slurm/run_python.sh prod12_routes.py