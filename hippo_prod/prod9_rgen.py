
import hippo

from sqlite3 import DatabaseError

from mlog import setup_logger

logger = setup_logger("CHIKV_prod9")

animal = hippo.HIPPO("CHIKV_prod9", "CHIKV_prod9.sqlite", copy_from="CHIKV_prod8.sqlite", overwrite_existing=True)

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="CHIKV_prod8_rgen.json")

for j in range(3):
    
    for i in range(250):
        logger.header(f'{j=} A {i=}')
        r = gen.generate(shuffle=True, budget=15000, max_products=1200, max_reactions=3000, max_iter=5000, currency='EUR', debug=False)
    
    for i in range(250):
        logger.header(f'{j=} B {i=}')
        r = gen.generate(shuffle=True, budget=10000, max_products=1200, max_reactions=3000, max_iter=5000, currency='EUR', debug=False)
    
animal.db.close()

# sb.sh --job-name CHIKV_prod9_rgen -pgpu --exclusive $HOME2/slurm/run_python.sh prod9_rgen.py