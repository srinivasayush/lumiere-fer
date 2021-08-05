from pydantic import BaseModel

class KaggleDatasetMetadata(BaseModel):
    dataset_name: str
    download_location: str
    