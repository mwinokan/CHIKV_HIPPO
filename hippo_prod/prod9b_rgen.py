
import hippo

from sqlite3 import DatabaseError

from mlog import setup_logger

logger = setup_logger("CHIKV_prod9b")

animal = hippo.HIPPO("CHIKV_prod9b", "CHIKV_prod9b.sqlite", copy_from="CHIKV_prod8b.sqlite", overwrite_existing=True)

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="CHIKV_prod8b_rgen.json")

# for j in range(2):

j=0
    
for i in range(500):
    logger.header(f'{j=} A {i=}')
    r = gen.generate(shuffle=True, budget=10000, max_products=1200, max_reactions=3000, max_iter=5000, currency='EUR', debug=False)

for i in range(250):
    logger.header(f'{j=} B {i=}')
    r = gen.generate(shuffle=True, budget=11000, max_products=1200, max_reactions=3000, max_iter=5000, currency='EUR', debug=False)

for i in range(250):
    logger.header(f'{j=} C {i=}')
    r = gen.generate(shuffle=True, budget=12000, max_products=1200, max_reactions=3000, max_iter=5000, currency='EUR', debug=False)
    
animal.db.close()

# sb.sh --job-name CHIKV_prod9b_rgen -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh prod9b_rgen.py