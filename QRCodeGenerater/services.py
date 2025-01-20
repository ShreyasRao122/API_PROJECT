import pyqrcode
import re
from settings import FILE_NAME_PATTERN

def generate_qr(urls):
    if not isinstance(urls, list):
        raise ValueError("Input must be a list of dictionaries")

    qr_file_names = []
    for entry in urls:
        if "url" not in entry:
            raise ValueError("Each entry must contain a 'url' key")

        url = entry["url"]
        cleaned_url = re.sub(FILE_NAME_PATTERN, "_", url)
        file_name = cleaned_url + ".png"
        qr_code = pyqrcode.create(url)
        qr_code.png(file_name, scale=6)
        qr_file_names.append(file_name)

    return qr_file_names
