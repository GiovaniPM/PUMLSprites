import argparse
from PIL import Image

def replace_transparency_with_white(input_file, output_file):
    # Abra a imagem
    image = Image.open(input_file)
    
    # Verifica se a imagem tem um canal alfa (transparência)
    if image.mode in ('RGBA', 'LA'):
        # Cria uma imagem de fundo branco
        background = Image.new('RGB', image.size, (255, 255, 255))
        # Compoem a imagem no fundo branco, eliminando a transparência
        background.paste(image, (0, 0), image if image.mode == 'RGBA' else image.convert('RGBA'))
        # Salva a nova imagem
        background.save(output_file)
    else:
        # Se não tiver canal alfa, apenas salva a imagem original
        image.save(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Substitui a transparência de uma imagem PNG pela cor branca.")
    parser.add_argument("input_file", help="Caminho para o arquivo de imagem de entrada.")
    parser.add_argument("output_file", help="Caminho para o arquivo de imagem de saída.")
    
    args = parser.parse_args()
    replace_transparency_with_white(args.input_file, args.output_file)
    print(f"A transparência foi substituída por branco e a imagem foi salva como {args.output_file}")
