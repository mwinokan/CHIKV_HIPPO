
import hippo
import mrich

animal = hippo.HIPPO("CHIKV_prod14", "CHIKV_prod14_batch.sqlite", copy_from="CHIKV_prod13.sqlite", overwrite_existing=True)

recipe = hippo.Recipe.from_json(animal.db, 'CHIKV_prod11c_recipes/Recipe_1GJWBFH.json', allow_db_mismatch=True)

gen = hippo.RandomRecipeGenerator(db=animal.db, start_with=recipe, suppliers=['Stock', 'Enamine'])

for i in range(20):
    mrich.header("i=", i)
    r = gen.generate(
            shuffle=True,  
            budget=11000, 
            max_products=1200, 
            max_reactions=3000, 
            max_iter=len(gen.route_pool), 
            currency='EUR', 
            debug=False,
            balance_clusters=True,
            permitted_clusters={
                93,
                95,
                104,
                653,
                796,
                1001,
                1012,
                1128,
                1192,
                1316,
                1473,
                1917,
                2188,
                2916,
                2919,
                2924,
                2925,
                2944,
                3284,
                3611,
                3624,
                3625,
                3627,
                3628
            },
        )
    
animal.db.close()

# sb.sh --job-name CHIKV_prod14_rgen -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh prod14_rgen.py
