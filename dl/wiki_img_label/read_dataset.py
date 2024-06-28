from zipfile import ZipFile
from io import BytesIO
import pandas

DATASET_ARCHIVE_PATH = r'C:\data\2024_ml_cohert_dl_proj\wikipedia-image-caption.zip'
CAPTION_RELPATH = 'test_caption_list.csv'
TSV_RELPATH = 'train-00000-of-00005.tsv'

def read_from_zip(zip_path, file_relpath):
    with ZipFile(zip_path, 'r') as z:
        with z.open(file_relpath) as f:
            for line in f:
                print(line)

d = read_from_zip(DATASET_ARCHIVE_PATH, TSV_RELPATH)
print('done')