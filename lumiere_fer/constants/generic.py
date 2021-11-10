from glob import glob


FER_2013_LOCATION = 'datasets/fer2013'
FERG_DB_LOCATION = 'datasets/FERG_DB_256'
DARK_SUFFIX = '_dark'

DATASETS_TO_PATHS = {
    'fer2013': glob(f'{FER_2013_LOCATION}/test/**/**.jpg') + glob(f'{FER_2013_LOCATION}/train/**/**.jpg'),
    'ferg_aia': glob(f'{FERG_DB_LOCATION}/aia/**/**'),
    'ferg_bonnie': glob(f'{FERG_DB_LOCATION}/bonnie/**/**'),
    'ferg_jules': glob(f'{FERG_DB_LOCATION}/jules/**/**'),
    'ferg_malcolm': glob(f'{FERG_DB_LOCATION}/malcolm/**/**'),
    'ferg_mery': glob(f'{FERG_DB_LOCATION}/mery/**/**'),
    'ferg_ray': glob(f'{FERG_DB_LOCATION}/ray/**/**'),
}
