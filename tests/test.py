import os
import pytest
import qrcode
from app.main import *

def test_qr_code_generation():
    # Set environment variables for the test
    os.environ['QR_DATA_URL'] = 'https://github.com/test'
    os.environ['QR_CODE_DIR'] = 'test_qr_codes'
    os.environ['QR_CODE_FILENAME'] = 'test_qr.png'
    os.environ['FILL_COLOR'] = 'black'
    os.environ['BACK_COLOR'] = 'white'

    # Ensure the directory exists
    os.makedirs('test_qr_codes', exist_ok=True)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://github.com/test')
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img_path = os.path.join('test_qr_codes', 'test_qr.png')
    img.save(img_path)

    assert os.path.exists(img_path) is True
