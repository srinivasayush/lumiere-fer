import os
from typing import Optional
from kaggle import KaggleApi

api = KaggleApi()
api.authenticate()

def download_fer_2013(
    download_to: Optional[str] = './lumiere_fer/datasets/fer2013'
):
    if not os.path.exists(download_to):
        api.dataset_download_files('msambare/fer2013', path=download_to, unzip=True)
