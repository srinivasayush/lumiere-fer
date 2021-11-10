import enum
import os
from typing import Optional

from PIL import Image, ImageEnhance

from lumiere_fer.constants.generic import DATASETS_TO_PATHS
from lumiere_fer.utils.progress import show_current_progress


class RelightType(enum.Enum):
    bright = 'bright'
    dark = 'dark'


def relight_image_and_save_simple(
    image_path: str,
    relight_type: RelightType,
    verbose: Optional[bool] = False,
) -> Optional[Image.Image]:

    image_name, image_file_extension = os.path.splitext(image_path)
    relit_image_path = f'{image_name}_bright{image_file_extension}' if relight_type == RelightType.bright else f'{image_name}_dark{image_file_extension}'

    if os.path.exists(relit_image_path):
        return

    try:
        image = Image.open(image_path)
        image_enhancer = ImageEnhance.Brightness(image)

        enhance_factor = 1.5 if relight_type == RelightType.bright else 0.4 # If not bright, then assume dark
        relit_image = image_enhancer.enhance(enhance_factor)

        relit_image.save(relit_image_path)

        image.close()

        return relit_image
    except Exception as exception:
        if verbose:
            print(f'Got an Exception when relighting: {exception}')


def relight_datasets():
    print('Relighting started!')
    image_filepaths = []
    
    for dataset_image_filepaths in DATASETS_TO_PATHS.values():
        image_filepaths += dataset_image_filepaths

    for i in range(0, len(image_filepaths)):
        show_current_progress(
            current=i,
            total=len(image_filepaths)
        )

        relight_image_and_save_simple(
            image_path=image_filepaths[i],
            relight_type=RelightType.dark,
            verbose=True,
        )
    
    print('Relighting finished!')

if __name__ ==  '__main__':
    relight_datasets()
