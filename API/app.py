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

@app.route('/grayscale', methods=['POST'])
def grayscale_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400

    image_base64 = request.json['image']

    try:
        # Decode the base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))

        # Convert image to grayscale
        image = image.convert("L")

        # Save the image to a bytes buffer
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        # Encode the image to base64
        grayscale_image_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({'grayscaled_image': grayscale_image_base64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transparency', methods=['POST'])
def transparency_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400

    image_base64 = request.json['image']

    try:
        # Decode the base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))

        # Verifica se a imagem tem um canal alfa (transparência)
        if image.mode in ('RGBA', 'LA'):
            # Cria uma imagem de fundo branco
            background = Image.new('RGB', image.size, (255, 255, 255))
            # Compoem a imagem no fundo branco, eliminando a transparência
            background.paste(image, (0, 0), image if image.mode == 'RGBA' else image.convert('RGBA'))
            # Save the image to a bytes buffer
            img_io = io.BytesIO()
            background.save(img_io, 'PNG')
            img_io.seek(0)
        else:
            # Se não tiver canal alfa, apenas salva a imagem original
            img_io = io.BytesIO()
            image.save(img_io, 'PNG')
            img_io.seek(0)

        # Encode the image to base64
        image_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({'no_transparency_image': image_base64})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sprite_txt', methods=['POST'])
def sprite_txt_image():
    if 'image' not in request.json:
        return jsonify({'error': 'Missing parameters'}), 400

    image_base64 = request.json['image']

    try:
        # Decode the base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))
        
        # Converter imagem para modo P (paleta) para garantir 16 cores
        image = image.convert('P', palette=Image.ADAPTIVE, colors=16)

        # Obter as cores da paleta
        palette = image.getpalette()

        # Obter dados dos pixels
        pixel_data = image.getdata()

        # Mapear índices de paleta para caracteres
        char_map = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }

        # Criar uma string para representar a imagem em texto
        text_representation = ""
        for index, pixel in enumerate(pixel_data):
            text_representation += char_map[pixel]
            if (index + 1) % image.width == 0:
                text_representation += '\n'

        return jsonify({'sprite': text_representation})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
