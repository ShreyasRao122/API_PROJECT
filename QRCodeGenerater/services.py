import pyqrcode
from random import randrange
from datetime import datetime
from settings import FILE_NAME_DATE_FORMAT, FILE_NAME_RANDOM_END, FILE_NAME_RANDON_START

def generate_qr(url):
    file_name = (
        f"qr_{randrange(FILE_NAME_RANDON_START,FILE_NAME_RANDOM_END)}_"
        f"{datetime.now().strftime(FILE_NAME_DATE_FORMAT)}.png"
    )
    qr_code = pyqrcode.create(url)
    qr_code.png(file_name, scale=6)


