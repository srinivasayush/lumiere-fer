import os

from lumiere_fer.downloaders.download_fer_2013 import download_fer_2013


def download_datasets():
    """
    Downloads all datasets needed for training and testing
    if they have not already been downloaded
    """
    download_fer_2013()
