from PIL import Image
import argparse

def resize_image(input_file, output_file, size=(32, 32)):
    # Abre a imagem
    with Image.open(input_file) as img:
        # Redimensiona a imagem usando LANCZOS
        resized_img = img.resize(size, Image.LANCZOS)
        # Salva a imagem redimensionada
        resized_img.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Redimensiona uma imagem PNG para 32x32 pixels.")
    parser.add_argument("input_file", help="Caminho para o arquivo de imagem PNG de entrada.")
    parser.add_argument("output_file", help="Caminho para o arquivo de imagem PNG de saída.")
    parser.add_argument("res_x", help="Resolução X")
    parser.add_argument("res_y", help="Resolução Y")

    args = parser.parse_args()
    resize_image(args.input_file, args.output_file, (int(args.res_x), int(args.res_y)))
    print(f"Imagem redimensionada e salva como {args.output_file}")
