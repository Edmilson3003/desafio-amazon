
import boto3
import os

def process_image_with_textract(image_path: str):
    """
    Processa uma imagem com Amazon Textract e retorna o texto detectado.
    """

    textract = boto3.client('textract')

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"O arquivo {image_path} não foi encontrado.")
    
    with open(image_path, 'rb') as document:
        image_bytes = document.read()

  
    response = textract.detect_document_text(Document={'Bytes': image_bytes})
    
  
    text_blocks = response.get('Blocks', [])
    detected_text = []
    for block in text_blocks:
        if block['BlockType'] == 'LINE':  
            detected_text.append(block['Text'])
    
    return '\n'.join(detected_text)



if __name__ == "__main__":
  
    image_path = r"C:\Users\NETO\Pictures\lista-material-escolar.jpeg"  

    try:
        extracted_text = process_image_with_textract(image_path)
        print("Texto Detectado:")
        print(extracted_text)
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

