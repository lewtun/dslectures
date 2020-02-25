# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/00_core.ipynb (unless otherwise specified).

__all__ = ['get_dataset']

# Cell
from nbdev.showdoc import *
import wget
import os

# Cell
def get_dataset(dataset_name: str):
    """
    Download datasets from Google Drive.
    """

    name_to_id = {'embeddings': '1dRwSXbFTcQbn8c3V24G92wFY4DXZ1SDt',
                  'imdb': '1wF0YEmQOwceJz2d6w4CfhBgydU87dPGl',
                  'housing': '1d7oOKdDmZFx8wf0c8OfuTW1FpUyJHABh',
                  'housing_gmaps': '1R1RUHAXxzrIngRJMFwyp4vZRVICd-I6T'}

    if dataset_name in name_to_id:
        try:
            file_url = 'https://docs.google.com/uc?export=download&id=' + name_to_id[dataset_name]
            wget.download(file_url, out='../data/')
        except Exception as e:
            print('Something went wrong during download. Try again.')
            raise e
        print(f'Download of {dataset_name} dataset complete.')
    else:
        raise KeyError('File not on Google Drive.')