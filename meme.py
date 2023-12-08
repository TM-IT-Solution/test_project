from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Set the path to your fonts directory
font_path = "path/to/your/fonts"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']

    if image.filename == '':
        return redirect(request.url)

    # Save the uploaded image
    image_path = os.path.join("static", "uploads", image.filename)
    image.save(image_path)

    # Open the image using Pillow
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Get user input text
    top_text = request.form.get('top_text', '')
    bottom_text = request.form.get('bottom_text', '')

    # Set the font
    font = ImageFont.truetype(os.path.join(font_path, "arial.ttf"), 40)

    # Add text to the image
    draw.text((10, 10), top_text, font=font, fill='white')
    draw.text((10, img.size[1] - 50), bottom_text, font=font, fill='white')

    # Save the modified image
    modified_image_path = os.path.join("static", "uploads", "modified_" + image.filename)
    img.save(modified_image_path)

    return render_template('index.html', original_image=image_path, modified_image=modified_image_path)

if __name__ == '__main__':
    app.run(debug=True)
