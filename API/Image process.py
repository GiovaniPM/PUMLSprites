from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import base64
import io
import os

app = Flask(__name__)
CORS(app)

def decode_base64_image(image_base64):
    image_data = base64.b64decode(image_base64)
    return Image.open(io.BytesIO(image_data))

def encode_image_to_base64(image):
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return base64.b64encode(img_io.getvalue()).decode('utf-8')

def encode_image_to_base64_format(image, format):
    img_io = io.BytesIO()
    
    # Verificar se o formato é JPEG e a imagem tem um canal alfa (transparência)
    if format.upper() == 'JPEG' and image.mode == 'RGBA':
        image = image.convert('RGB')
    
    image.save(img_io, format)
    img_io.seek(0)
    return base64.b64encode(img_io.getvalue()).decode('utf-8')

def handle_image_processing(image_base64, process_function):
    try:
        image = decode_base64_image(image_base64)
        image = process_function(image)
        processed_image_base64 = encode_image_to_base64(image)
        return jsonify({'processed_image': processed_image_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return render_template('help.html')

@app.route('/resize', methods=['POST'])
def resize_image():
    if 'image' not in request.json or 'width' not in request.json or 'height' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    width = int(request.json['width'])
    height = int(request.json['height'])
    
    return handle_image_processing(request.json['image'], lambda img: img.resize((width, height)))

@app.route('/grayscale', methods=['POST'])
def grayscale_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    return handle_image_processing(request.json['image'], lambda img: img.convert("L"))

@app.route('/no_transparency', methods=['POST'])
def no_transparency_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, (0, 0), img if img.mode == 'RGBA' else img.convert('RGBA'))
            return background
        return img
    
    return handle_image_processing(request.json['image'], process)

@app.route('/sprite_txt', methods=['POST'])
def sprite_txt_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        img = img.convert('P', palette=Image.ADAPTIVE, colors=16)
        pixel_data = img.getdata()
        char_map = '0123456789ABCDEF'
        text_representation = "".join([char_map[pixel] + ('\n' if (index + 1) % img.width == 0 else '') for index, pixel in enumerate(pixel_data)])
        return text_representation
    
    try:
        image_base64 = request.json['image']
        image = decode_base64_image(image_base64)
        text_representation = process(image)
        return jsonify({'sprite': text_representation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/negative', methods=['POST'])
def negative_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, (0, 0), img if img.mode == 'RGBA' else img.convert('RGBA'))
            img = background
        return ImageOps.invert(img.convert('RGB'))
    
    return handle_image_processing(request.json['image'], process)

@app.route('/black_white', methods=['POST'])
def black_white_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    return handle_image_processing(request.json['image'], lambda img: img.convert("1"))

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.json or 'format' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    image_base64 = request.json['image']
    output_format = request.json['format'].upper()
    
    if output_format not in ['JPG', 'PNG', 'BMP', 'GIF']:
        return jsonify({'error': 'Invalid format'}), 400
    
    try:
        image = decode_base64_image(image_base64)
        
        if output_format == 'JPG':
            output_format = 'JPEG'
        
        converted_image_base64 = encode_image_to_base64_format(image, output_format)
        
        return jsonify({'converted_image': converted_image_base64})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dimensions', methods=['POST'])
def get_image_dimensions():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    try:
        image_base64 = request.json['image']
        image = decode_base64_image(image_base64)
        width, height = image.size
        image_format = image.format
        
        return jsonify({
            'width': width,
            'height': height,
            'format': image_format
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/enhance', methods=['POST'])
def enhance_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        enhancer = ImageEnhance.Sharpness(img)
        return enhancer.enhance(2)
    
    return handle_image_processing(request.json['image'], process)

@app.route('/emboss', methods=['POST'])
def emboss_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    def process(img):
        return img.filter(ImageFilter.EMBOSS)
    
    return handle_image_processing(request.json['image'], process)

@app.route('/reduce_colors', methods=['POST'])
def reduce_colors_image():
    if 'image' not in request.json or 'num_colors' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400
    
    num_colors = int(request.json['num_colors'])
    
    def process(img):
        return img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    
    return handle_image_processing(request.json['image'], process)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))