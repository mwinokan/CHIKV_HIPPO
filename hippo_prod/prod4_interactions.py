import hippo
# import pandas as pd
# from pathlib import Path
import os
from tqdm import tqdm
# import numpy as np

from mlog import setup_logger
logger = setup_logger('CHIKV_prod4')

logger.var('hippo', hippo.__file__)

os.system("cp -v CHIKV_prod3.sqlite CHIKV_prod4.sqlite")

animal = hippo.HIPPO("CHIKV_prod4", "CHIKV_prod4.sqlite")

poses = animal.poses.get_by_tag(tag='deprecated', inverse=True)

for i,pose in tqdm(enumerate(poses)):
    pose.calculate_interactions(commit=False, force=True)

    if i%5000 == 0:
        animal.db.commit()

animal.db.close()

# sb.sh --job-name CHIKV_prod4_interactions $HOME2/slurm/run_python.sh prod4_interactions.py
