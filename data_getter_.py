{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# potlical candidates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "This notebook gets data from the OpenSecretes API "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: opensecrets-crpapi in /Users/avaj0001/anaconda3/envs/alexa/lib/python3.7/site-packages (0.2.2)\r\n",
      "Requirement already satisfied: httplib2 in /Users/avaj0001/anaconda3/envs/alexa/lib/python3.7/site-packages (from opensecrets-crpapi) (0.18.1)\r\n"
     ]
    }
   ],
   "source": [
    "! pip install opensecrets-crpapi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from organisation_data_accessor import data_accessor\n",
    "org_names = data_accessor.get_org_names()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Downloading Org name data:  53%|█████▎    | 250/469 [10:21<09:07,  2.50s/it]"
     ]
    }
   ],
   "source": [
    "org_ids_and_names= data_accessor.get_ids_for_orgs(api_key=\"12c67c00da09f0ba7593c6c7b300e975\", org_names=org_names)\n",
    "org_ids_and_names.to_csv(\"org_ids_and_names.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "org_ids_and_names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summaries = data_accessor.get_data_for_org_ids(api_key=\"12c67c00da09f0ba7593c6c7b300e975\", org_ids=org_ids_and_names.org_ids.values)\n",
    "summaries.to_csv(\"summaries.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summaries\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
