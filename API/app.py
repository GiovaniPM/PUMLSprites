from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app)

@app.route('/resize', methods=['POST'])
def resize_image():
    if 'image' not in request.json or 'width' not in request.json or 'height' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400

    image_base64 = request.json['image']
    width = int(request.json['width'])
    height = int(request.json['height'])

    try:
        # Decode the base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))

        # Resize the image
        image = image.resize((width, height))

        # Save the resized image to a bytes buffer
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        # Encode the resized image to base64
        resized_image_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({'resized_image': resized_image_base64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
