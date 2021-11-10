from __future__ import annotations

import json
from typing import Dict

from pydantic import BaseModel


class EmotionCounter(BaseModel):
    angry: float
    angry_dark: float

    disgust: float
    disgust_dark: float

    fear: float
    fear_dark: float

    happy: float
    happy_dark: float

    neutral: float
    neutral_dark: float

    sad: float
    sad_dark: float

    surprise: float
    surprise_dark: float


    @staticmethod
    def zero():
        return EmotionCounter(
            angry=0,
            angry_dark=0,
            disgust=0,
            disgust_dark=0,
            fear=0,
            fear_dark=0,
            happy=0,
            happy_dark=0,
            neutral=0,
            neutral_dark=0,
            sad=0,
            sad_dark=0,
            surprise=0,
            surprise_dark=0,
        )

    def __str__(self):
        return json.dumps(
            self.dict(), indent=4,
        )
