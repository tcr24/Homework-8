import qrcode
import os

# Get environment variables
url = os.getenv('QR_DATA_URL', 'https://github.com/tcr24')
qr_code_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
qr_code_filename = os.getenv('QR_CODE_FILENAME', 'my_github_qr.png')
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')

# Ensure the directory exists
os.makedirs(qr_code_dir, exist_ok=True)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)
img_path = os.path.join(qr_code_dir, qr_code_filename)
img.save(img_path)

print(f"QR code saved to {img_path}")
