import pandas as pd
import tqdm
from crpapi import CRP

crp = CRP(API_KEY)


def get_data_for_org_ids(org_ids):
    data = []
    for org_id in tqdm.tqdm(org_ids, desc="Downloading Org Id data"):
        data.append(crp.orgs.summary(org_id=org_id))
    return pd.DataFrame(data)


def get_ids_for_orgs(org_names):
    pass
