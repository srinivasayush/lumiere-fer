
from typing import Optional
from lumiere_fer.constants.generic import DARK_SUFFIX

def get_emotion_name_by_alias(emotion_alias: str) -> Optional[str]:
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
