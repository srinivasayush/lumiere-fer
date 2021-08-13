import os
from io import TextIOWrapper
from pathlib import Path
from typing import Optional


def write_file(
    filepath: str,
    content: str,
    overwrite: Optional[bool] = None,
    append: Optional[bool] = None,
) -> None:
    """Writes `lines` to a file located at `filepath`
    Parameters
    ----------
    filepath : str
        Filepath of file you want to write to
    content : str
        String you want to write into file
    overwrite : Optional[bool]
        Whether the file should be used if it already exists
    append: Optional[bool]
        Whether you would like to append to the existing file or overwrite it from scratch
    """

    if overwrite is None:
        overwrite = False
    if append is None:
        append = False


    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    main_file: Optional[TextIOWrapper] = None
    try:
        if os.path.exists(filepath):
            if not overwrite:
                raise Exception(
                    f'file `{filepath}` already exists'
                )
            if append:
                main_file = open(filepath, mode='a', encoding='utf-8')
            else:
                main_file = open(filepath, mode='w+', encoding='utf-8')
        else:
            main_file = open(filepath, mode='x', encoding='utf-8')
    except FileNotFoundError as error:
        raise Exception(
            f'folder `{Path(error.filename).parent}` not found'
        )

    main_file.write(content)
    main_file.close()
    main_file = None
