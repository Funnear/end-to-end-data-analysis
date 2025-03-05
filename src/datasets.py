import pandas as pd
import logging
import os
import json

PROJECT_ROOT = os.path.abspath("..")
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
DATASETS_PATH = f'{PROJECT_ROOT}/datasets'
PACK_BACKUP = f'{DATASETS_PATH}/_dataset_pack_{PROJECT_NAME}.json'

class Dataset:
    def __init__(self, label: str, source=None):
        """
        Only for calling from notebooks or modules.
        Only local relative paths to csv files are supported.
        
        Create new instance:
        dataset1 = Dataset("datasets/filename.csv", 'df1')
        df1 = dataset1.dataframe.copy()

        Class methods:
        dataset1.backup(df1)
        df1 = dataset1.restore().copy()

        TODO:
        - differ url from local path
        - support JSON, etc.
        - download from Kaggle using API
        """

        self.label = label
        self.path_pkl = f'{DATASETS_PATH}/{self.label}.pkl'

        if source: 
            self.source = f'{DATASETS_PATH}/{source}'
            self.dataframe = pd.read_csv(self.source)
        else:
            logging.info(f"No source provided, restoring from backup: {self.path_pkl}")
            self.source = None
            self.restore()

    def backup(self):
        self.dataframe.to_pickle(self.path_pkl)
        logging.info(f"Backup file is created: {self.path_pkl}")

    def restore(self):
        self.dataframe = pd.read_pickle(self.path_pkl)

class DatasetPack:
    def __init__(self, restore=False):
        """
        project_pack = DatasetPack()
        project_pack.add_dataset(dataset1)
        """
        if restore:
            self.restore_pack()
        else:
            self.dictionary = dict()

    def add_dataset(self, dataset: Dataset) -> None:
        self.dictionary[dataset.label] = dataset

    def backup_pack(self):
        backup_dictionary = dict()
        for key, value in self.dictionary.items():
            backup_dictionary[key] = value.source

        with open(PACK_BACKUP, "w") as json_file:
            json.dump(backup_dictionary, json_file, indent=4)

        logging.info(f"Backup file is created: {PACK_BACKUP}")

    def restore_pack(self):
        logging.info(f"Restoring backup: {PACK_BACKUP}")
        with open(PACK_BACKUP, "r") as json_file:
            self.dictionary = json.load(json_file)
        
        for key, value in self.dictionary.items():
            self.dictionary[key] = Dataset(key)

        

