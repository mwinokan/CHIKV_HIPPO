
import hippo
import mrich

animal = hippo.HIPPO("CHIKV_prod13", "CHIKV_prod13_batch.sqlite", copy_from="CHIKV_prod13.sqlite", overwrite_existing=True)

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="CHIKV_prod13_rgen.json")

for i in range(200):
    mrich.header("i=", i)
    r = gen.generate(
            shuffle=True,  
            budget=10000, 
            max_products=1200, 
            max_reactions=3000, 
            max_iter=5000, 
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

# sb.sh --job-name CHIKV_prod13_rgen -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh prod13_rgen.py
