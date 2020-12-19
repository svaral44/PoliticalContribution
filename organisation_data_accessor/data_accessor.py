from typing import AnyStr, List

import pandas as pd
import tqdm
from crpapi import CRP

import  logging
logging.getLogger().setLevel(logging.ERROR)


def get_summary_for_org_ids(api_key: AnyStr, org_ids: List):
    """This gets the OrgSummary for the list of OrgIds

    :param api_key: string of  your API id
    :param org_ids: list of strings of the org ids
    :return: a pandas dataframe of the summary data for each org
    """
    crp = CRP(api_key)
    data = []
    for org_id in tqdm.tqdm(org_ids, desc="Downloading Org Id data"):
        data.append(crp.orgs.summary(org_id=org_id))
    return pd.DataFrame(data)


def get_ids_for_orgs(api_key: AnyStr, org_names: List):
    """
    Gets IDs for a list of org names
    :param api_key:
    :param org_names:
    :return:
    """
    crp = CRP(api_key)
    data = []

    for org_name in tqdm.tqdm(org_names, desc="Downloading Org name data"):
        try:
            api_return = crp.orgs.get(org_name=org_name)  # list of crap from API
            org_id = api_return['@attributes']['orgid']
        except Exception as e:
            logging.warning(dict(org_names=org_name, exception=e))
            org_id = 0
        data.append(dict(org_name=org_name, org_id=org_id))
    return pd.DataFrame(data)


def get_org_names():
    sp500firms_data = pd.read_csv("data/sp500firms.csv")
    return sp500firms_data.name.values
