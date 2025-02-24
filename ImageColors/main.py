from flask import Flask, request, render_template, jsonify, url_for
import os
from PIL import Image
import numpy as np
from collections import Counter

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Function to check if the file has allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to extract colors from the image
def extract_colors(image_path, num_colors=10):
    # Open the image using Pillow
    image = Image.open(image_path)
    image = image.convert("RGB")  # Ensure it's in RGB mode

    # Resize image to reduce computation time
    image = image.resize((image.width // 10, image.height // 10))

    # Convert image to numpy array
    pixels = np.array(image)
    pixels = pixels.reshape(-1, 3)

    # Count the most frequent colors
    color_counts = Counter(map(tuple, pixels.tolist()))
    top_colors = color_counts.most_common(num_colors)

    return top_colors


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Extract top 10 colors
        top_colors = extract_colors(filename)

        # Return the file path and the top 10 colors
        return render_template('index.html', filename=file.filename, top_colors=top_colors)

    return jsonify({"error": "Invalid file type"}), 400


if __name__ == '__main__':
    app.run(debug=True)
