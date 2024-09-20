import hippo
import pandas as pd
from pathlib import Path
import os
import numpy as np

from mlog import setup_logger
logger = setup_logger('CHIKV_prod2')

logger.var('hippo', hippo.__file__)

os.system("cp -v CHIKV_prod1.sqlite CHIKV_prod2.sqlite")

animal = hippo.HIPPO("CHIKV_prod2", "CHIKV_prod2.sqlite")

df = pd.read_csv(
    "/opt/xchem-fragalysis-2/kfieseler/CHIKV-Mac-syndirella-run/sept9_syndirella_final_output.csv"
)

ref_lookup = {}

for i, row in df.iterrows():
    to_hippo, template = row["to_hippo"], row["template"]
    if to_hippo is np.nan:
        continue
    ref_lookup[to_hippo] = Path(template).name.split("_")[0].replace("x", "")

from hippo.fragalysis import parse_observation_longcode
import functools

@functools.cache
def obs_mapper(longcode):
    result = parse_observation_longcode(longcode)
    return animal.poses[f'c{result["crystal"]}a']

for i, (to_hippo, template) in enumerate(ref_lookup.items()):

    # if i < 75:
    #     continue
    
    logger.title(i)
    logger.reading(to_hippo)
    df = animal.add_syndirella_elabs(to_hippo, inspiration_map=obs_mapper, reference=animal.poses[template])

animal.db.close()
