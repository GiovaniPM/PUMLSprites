import argparse
from PIL import Image

def convert_to_grayscale(input_file, output_file):
    # Abra a imagem
    image = Image.open(input_file)
    
    # Converta a imagem para escala de cinza
    grayscale_image = image.convert("L")
    
    # Salve a imagem convertida
    grayscale_image.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converte imagem em tons de cinza.")
    parser.add_argument("input_file", help="Caminho para o arquivo de imagem de entrada.")
    parser.add_argument("output_file", help="Caminho para o arquivo de imagem de saída.")
    
    args = parser.parse_args()
    convert_to_grayscale(args.input_file, args.output_file)
    print(f"A imagem foi convertida para escala de cinza e salva como {args.output_file}")
