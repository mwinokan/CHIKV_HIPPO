
import hippo

from sqlite3 import DatabaseError

from mlog import setup_logger

from tqdm import tqdm

logger = setup_logger("CHIKV_prod10")

animal = hippo.HIPPO("CHIKV_prod10_batch", "CHIKV_prod10b.sqlite")

gen = hippo.RandomRecipeGenerator.from_json(db=animal.db, path="CHIKV_prod8b_rgen.json")

poses = gen.route_pool.products.poses.get_by_tag("deprecated", inverse=True)

logger.var("poses", poses)

for pose in tqdm(poses):
    pose.calculate_interactions()
    
animal.db.close()

# sb.sh --job-name CHIKV_prod10b_interactions -pgpu --exclusive --no-requeue $HOME2/slurm/run_python.sh prod10b_interactions.py