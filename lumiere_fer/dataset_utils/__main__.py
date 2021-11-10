import os
from pathlib import Path
from lumiere_fer.constants.generic import FERG_DB_LOCATION, FER_2013_LOCATION
from lumiere_fer.dataset_utils.download_kaggle_dataset import \
    download_kaggle_dataset
from lumiere_fer.models.kaggle_dataset_metadata import KaggleDatasetMetadata
from glob import iglob


def download_kaggle_datasets():
    """
    Downloads all datasets needed for training and testing
    if they have not already been downloaded
    """
    dataset_metadata = [
        KaggleDatasetMetadata(
            dataset_name='msambare/fer2013',
            download_location=FER_2013_LOCATION,
        )
    ]
    
    for metadata in dataset_metadata:
        download_kaggle_dataset(
            dataset_name=metadata.dataset_name,
            download_to=metadata.download_location,
            log=True,
        )

def setup_ferg_dataset():
    for item_path in iglob(FERG_DB_LOCATION + '/**', recursive=True):
        if not os.path.isdir(item_path):
            continue

        folder_name = item_path.split('\\')[-1]
        if '_' in folder_name:
            emotion_alias = folder_name.split('_')[-1]
            os.rename(item_path, f'{str(Path(item_path).parent)}/{emotion_alias}')


if __name__ == '__main__':
    download_kaggle_datasets()
    setup_ferg_dataset()
