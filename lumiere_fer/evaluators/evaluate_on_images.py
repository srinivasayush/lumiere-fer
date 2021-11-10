from pathlib import Path
from typing import List, Optional

import cv2
import imutils
from deepface import DeepFace
from lumiere_fer.constants.generic import DARK_SUFFIX
from lumiere_fer.models.emotion_counter import EmotionCounter
from lumiere_fer.utils.emotion import get_emotion_name_by_alias
from lumiere_fer.utils.progress import show_current_progress

emotion_model = DeepFace.build_model('Emotion')


def evaluate_on_images(
    detector: str,
    image_filepaths: List[str],
    verbose: Optional[bool] = False,
) -> EmotionCounter:
    image_filepaths = [str(Path(filepath).absolute()) for filepath in image_filepaths]
    image_filepaths = list(set(image_filepaths))
    result_dict = EmotionCounter.zero().dict()
    emotion_counter = EmotionCounter.zero().dict()

    for image_path in image_filepaths:
        if verbose:
            show_current_progress(
                current=image_filepaths.index(image_path),
                total=len(image_filepaths),
            )

        parent_folder_path = str(Path(image_path).absolute().parent)
        emotion_alias = parent_folder_path.split('\\')[-1]
        emotion_name = get_emotion_name_by_alias(emotion_alias)

        if emotion_name is None or emotion_name not in list(emotion_counter.keys()):
            continue


        image = cv2.imread(image_path)
        try:
            image = imutils.resize(image, width=300, height=300)
        except Exception as exception:
            if verbose:
                print(f'There was something wrong with the image at {image_path}')
                print(image)

        try:
            deepface_result = DeepFace.analyze(
                img_path=image,
                actions=['emotion'],
                models={
                    'emotion': emotion_model,
                },
                detector_backend=detector,
                enforce_detection=False,
            )

            if DARK_SUFFIX in image_path:
                emotion_counter[emotion_name + DARK_SUFFIX] += 1
            else:
                emotion_counter[emotion_name] += 1


            if deepface_result['dominant_emotion'] == emotion_name:
                if DARK_SUFFIX in image_path:
                    result_dict[emotion_name + DARK_SUFFIX] += 1
                else:
                    result_dict[emotion_name] += 1
        except Exception as exception:
            if verbose:
                print('log: DeepFace.analyze threw an exception:')
                print(exception)
                print(f'log: the image path is {image_path}')



    for emotion_data in result_dict.keys():
        result_dict[emotion_data] = result_dict[emotion_data] / emotion_counter[emotion_data]

  
    return EmotionCounter(**result_dict)
