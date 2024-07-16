import os
import sys
import pytest
import qrcode

# Add the parent directory of 'app' to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import generate_qr_code

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
    generate_qr_code()

    img_path = os.path.join('test_qr_codes', 'test_qr.png')
    assert os.path.exists(img_path) is True
