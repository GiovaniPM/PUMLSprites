import argparse
from PIL import Image

# Função para converter uma imagem em texto
def image_to_text(image_path, output_path):
    image = Image.open(image_path)
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

    # Escrever a representação em texto no arquivo de saída
    with open(output_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text_representation)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converte uma imagem em texto.")
    parser.add_argument("input_file", help="Caminho para o arquivo de imagem de entrada.")
    parser.add_argument("output_file", help="Caminho para o arquivo de imagem de saída.")
    
    args = parser.parse_args()
    image_to_text(args.input_file, args.output_file)
    print(f"Conversão concluída. Verifique o arquivo {args.output_file} para o resultado.")
