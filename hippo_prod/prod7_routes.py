import hippo

from sqlite3 import DatabaseError

from mlog import setup_logger

logger = setup_logger("CHIKV_prod7")

animal = hippo.HIPPO("CHIKV_prod7", "CHIKV_prod7.sqlite", copy_from="CHIKV_prod6.sqlite", overwrite_existing=True)

from tqdm import tqdm

recipe = hippo.Recipe.from_json(animal.db, 'CHIKV_starting_recipe_yields.json', allow_db_mismatch=True)

products = recipe.products.elabs

logger.var("products", products)

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

# sb.sh --job-name CHIKV_prod7_routes -pgpu --exclusive $HOME2/slurm/run_python.sh prod7_routes.py