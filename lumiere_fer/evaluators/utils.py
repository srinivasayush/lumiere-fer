from lumiere_fer.constants.generic import DARK_SUFFIX
from pathlib import Path
from typing import List, Optional, Union

from deepface import DeepFace
from lumiere_fer.models.emotion_counter import EmotionCounter


def _get_emotion_name_by_alias(emotion_alias: str) -> Optional[str]:
    emotion_to_aliases = {
        'angry': ['angry', 'anger'],
        'disgust': ['disgust'],
        'fear': ['fear'],
        'happy': ['happy'],
        'sad': ['sad', 'sadness'],
        'surprise': ['surprise'],
    }

    for emotion_name in emotion_to_aliases.keys():
        if emotion_alias in emotion_to_aliases[emotion_name]:
            if DARK_SUFFIX in emotion_alias:
                return emotion_name + DARK_SUFFIX
            return emotion_name


def evaluate_on_images(image_filepaths: List[str]) -> EmotionCounter:
    result = EmotionCounter.zero()
    result_dict = result.dict()


    emotion_counter = EmotionCounter.zero().dict()

    for image_path in image_filepaths:
        parent_folder_path = str(Path(image_path).absolute().parent)
        emotion_alias = parent_folder_path.split('\\')[-1]
        emotion_name = _get_emotion_name_by_alias(emotion_alias)

        if emotion_name not in list(emotion_counter.keys()):
            continue
        
        if DARK_SUFFIX in image_path:
            emotion_counter[emotion_name + DARK_SUFFIX] += 1
        else:
            emotion_counter[emotion_name] += 1

        deepface_result = DeepFace.analyze(
            img_path=image_path,
            actions=['emotion'],
            enforce_detection=False,
        )

        if deepface_result['dominant_emotion'] == emotion_name:
            
            if DARK_SUFFIX in image_path:
                result_dict[emotion_name + DARK_SUFFIX] += 1
            else:
                result_dict[emotion_name] += 1
    


    print('log: the value of emotion counter is: ')
    print(emotion_counter)
        
    for key in result_dict.keys():
        result_dict[key] = result_dict[key] / emotion_counter[key]

        
    return EmotionCounter(**result_dict)
