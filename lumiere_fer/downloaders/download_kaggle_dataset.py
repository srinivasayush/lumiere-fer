from lumiere_fer.constants.generic import FER_2013_LOCATION
import os
from typing import Optional
from lumiere_fer.constants.kaggle_api import kaggle_api



def download_kaggle_dataset(
    dataset_name: str,
    download_to: str,
    log: Optional[bool] = True,
):
    if not os.path.exists(download_to):
        if log:
            print(f'Downloading {dataset_name}')
        kaggle_api.dataset_download_files(dataset_name, path=download_to, unzip=True)
        if log:
            print(f'{dataset_name} Dataset has finished downloading.')
    else:
        if log:
            print(f'{dataset_name} Dataset already downloaded.')
