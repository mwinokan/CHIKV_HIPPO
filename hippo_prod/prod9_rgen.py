import os

os.system("cp -v CHIKV_prod8.sqlite CHIKV_prod9.sqlite")

import hippo

from sqlite3 import DatabaseError

from mlog import setup_logger

logger = setup_logger("CHIKV_prod9")

animal = hippo.HIPPO("CHIKV_prod9", "CHIKV_prod9.sqlite")

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="CHIKV_prod8_rgen.json")

for i in range(2000):
    logger.header(f'{i=}')
    r = gen.generate(shuffle=True, budget=30000, max_products=1600, max_reactions=3000, currency='EUR', debug=False)

animal.db.close()

# sb.sh --job-name CHIKV_prod9_rgen -pgpu --exclusive $HOME2/slurm/run_python.sh prod9_rgen.py