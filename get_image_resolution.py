from PIL import Image
import argparse

def get_image_resolution(image_path):
    # Abre a imagem
    with Image.open(image_path) as img:
        # Obtém a largura e a altura da imagem
        width, height = img.size
    return width, height

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obtém a resolução de uma imagem PNG e salva em um arquivo.")
    parser.add_argument("image_path", help="Caminho para o arquivo de imagem PNG.")
    parser.add_argument("output_file", help="Caminho para o arquivo de saída com as variáveis de ambiente.")

    args = parser.parse_args()
    width, height = get_image_resolution(args.image_path)

    # Escreve as variáveis de ambiente no arquivo de saída
    with open(args.output_file, "w") as f:
        f.write(f"set IMG_WIDTH={width}\n")
        f.write(f"set IMG_HEIGHT={height}\n")

    print(f"A resolução da imagem é {width}x{height} pixels. Variáveis de ambiente salvas em {args.output_file}.")
