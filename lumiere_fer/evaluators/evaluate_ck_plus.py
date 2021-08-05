from glob import glob
from pathlib import Path

from lumiere_fer.constants.generic import CK_PLUS_LOCATION
from lumiere_fer.models.emotion_counter import EmotionCounter
from lumiere_fer.evaluators.utils import evaluate_on_images


def evaluate_on_ck_plus() -> EmotionCounter:
    print('Evaluating model on CK Plus...')

    image_filepaths = glob(f'{CK_PLUS_LOCATION}/CK+48/**/**.png')
    image_filepaths = [str(Path(filepath).absolute()) for filepath in image_filepaths]

    evaluation_result = evaluate_on_images(image_filepaths=image_filepaths)
    return evaluation_result