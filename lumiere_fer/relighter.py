import enum
import os
from glob import glob
from typing import Optional

from PIL import Image, ImageEnhance

from lumiere_fer.constants.generic import CK_PLUS_LOCATION, FER_2013_LOCATION


class RelightType(enum.Enum):
    bright = 'bright'
    dark = 'dark'


def relight_image_and_save_simple(
    image_path: str,
    relight_type: RelightType,
) -> Optional[Image.Image]:

    image_name, image_file_extension = os.path.splitext(image_path)
    relit_image_path = f'{image_name}_bright{image_file_extension}' if relight_type == RelightType.bright else f'{image_name}_dark{image_file_extension}'

    if os.path.exists(relit_image_path):
        return

    image = Image.open(image_path)
    image_enhancer = ImageEnhance.Brightness(image)

    enhance_factor = 1.5 if relight_type == RelightType.bright else 0.4 # If not bright, then assume dark
    relit_image = image_enhancer.enhance(enhance_factor)

    relit_image.save(relit_image_path)

    image.close()

    return relit_image


def relight_datasets():
    fer_2013_image_filepaths = glob(f'{FER_2013_LOCATION}/test/**/**.jpg') + glob(f'{FER_2013_LOCATION}/train/**/**.jpg')
    ck_plus_filepaths = glob(f'{CK_PLUS_LOCATION}/CK+48/**/**.png')

    image_filepaths = fer_2013_image_filepaths + ck_plus_filepaths
    for filepath in image_filepaths:
        relight_image_and_save_simple(image_path=filepath, relight_type=RelightType.dark)
    
    print('Relighting Finished!')

if __name__ ==  '__main__':
    relight_datasets()
