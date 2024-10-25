
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
        )
    
animal.db.close()

# sb.sh --job-name CHIKV_prod14_rgen -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh prod14_rgen.py
