from lumiere_fer.models.kaggle_dataset_metadata import KaggleDatasetMetadata
from lumiere_fer.constants.generic import CK_PLUS_LOCATION, FER_2013_LOCATION
from lumiere_fer.downloaders.download_kaggle_dataset import download_kaggle_dataset

def download_kaggle_datasets():
    """
    Downloads all datasets needed for training and testing
    if they have not already been downloaded
    """
    dataset_metadata = [
        KaggleDatasetMetadata(
            dataset_name='msambare/fer2013',
            download_location=FER_2013_LOCATION,
        ),
        KaggleDatasetMetadata(
            dataset_name='shawon10/ckplus',
            download_location=CK_PLUS_LOCATION,
        ),
    ]
    
    for metadata in dataset_metadata:
        download_kaggle_dataset(
            dataset_name=metadata.dataset_name,
            download_to=metadata.download_location,
            log=True,
        )

if __name__ == '__main__':
    download_kaggle_datasets()
