from flask import Flask, render_template, request, redirect, url_for
import qrcode
import cv2
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    img.save('static/qr_code.png')

    return render_template('index.html', url=url, generated=True)

@app.route('/scan_qr')
def scan_qr():
    # Read QR code image
    img = cv2.imread('static/qr_code.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use a QR code detector
    detector = cv2.QRCodeDetector()
    val, pts, qr_code = detector.detectAndDecode(gray)

    if val:
        return render_template('index.html', scanned_url=val, scanned=True)
    else:
        return render_template('index.html', scanned=False)

if __name__ == '__main__':
    app.run(debug=True)
