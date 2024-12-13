import argparse
import base64
import sys

def image_to_base64(image_path):
    """
    Converte uma imagem em Base64.
    
    :param image_path: Caminho para o arquivo da imagem.
    :return: String Base64 representando a imagem.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def save_base64_to_file(base64_string, output_txt_path):
    """
    Salva a string Base64 em um arquivo de texto.
    
    :param base64_string: String Base64 representando a imagem.
    :param output_txt_path: Caminho para salvar o arquivo de texto.
    """
    with open(output_txt_path, "w") as text_file:
        text_file.write(base64_string)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Converte uma imagem na base 64.")
    parser.add_argument("image_file", help="Caminho para o arquivo de imagem.")
    parser.add_argument("text_file", help="Caminho para o arquivo txt.")
    
    args = parser.parse_args()
    
    # Receba os parâmetros da linha de comando
    image_path = args.image_file
    txt_path = args.text_file
    operator = args.operator
    
    # Converter imagem para Base64
    base64_string = image_to_base64(image_path)
    
    # Salvar a string Base64 no arquivo de texto
    save_base64_to_file(base64_string, txt_path)