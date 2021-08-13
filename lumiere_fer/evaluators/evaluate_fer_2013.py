from glob import glob
from pathlib import Path

from lumiere_fer.constants.generic import FER_2013_LOCATION
from lumiere_fer.models.emotion_counter import EmotionCounter
from lumiere_fer.evaluators.utils import evaluate_on_images


def evaluate_on_fer_2013(detector: str) -> EmotionCounter:
    image_filepaths = glob(f'{FER_2013_LOCATION}/test/**/**.jpg') + glob(f'{FER_2013_LOCATION}/train/**/**.jpg')
    image_filepaths = [str(Path(filepath).absolute()) for filepath in image_filepaths]

    evaluation_result = evaluate_on_images(
        detector=detector,
        image_filepaths=image_filepaths,
        verbose=True,
    )
    return evaluation_result
