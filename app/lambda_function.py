import json
import base64
import os
from io import BytesIO
from extractor import extractor_pdf, extractor_text
from gen_answer import generate_answer
import cgi

# Classe para representar o arquivo
class FileObj:
    def __init__(self, content, filename):
        self.file = content
        self.filename = filename

# Função para gerar a resposta da Lambda
# Esta função é responsável por formatar a resposta da Lambda
def make_response(status_code, body):
    return {
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*'
        },
        'statusCode': status_code,
        'body': json.dumps(body, ensure_ascii=False)
    }

# Função principal da Lambda
def lambda_handler(event, context):
    try:
        content_type = event['headers'].get('Content-Type') or event['headers'].get('content-type')

        # Tratativa para caso o Content-Type venha como application/json
        # OBS: Exclusivo para o raw_text! 
        if 'application/json' in content_type:
            body = event.get('body', '{}')
            body = json.loads(body) if isinstance(body, str) else body

            if 'raw_text' not in body:
                return make_response(400, {'error': 'No raw_text provided.'})

            result = extractor_text(body['raw_text'])

        # Caso multipart/form-data
        # Aqui o arquivo é enviado como um campo de formulário
        elif 'multipart/form-data' in content_type:
            # Parse multipart
            body = event['body']

            # Decodifica o corpo se necessário
            decoded_body = base64.b64decode(body) if event.get('isBase64Encoded', False) else body
            fp = BytesIO(decoded_body)

            # Cria um ambiente para o cgi.FieldStorage
            env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': content_type}

            form = cgi.FieldStorage(fp=fp, environ=env, keep_blank_values=True)
            
            # Verifica se o arquivo foi enviado
            # e se o campo 'file' está presente
            if 'file' not in form:
                return make_response(400, {'error': 'No file provided.'})
            
            # Obtém o campo do arquivo
            file_field = form['file']
            
            # Verifica se o arquivo é válido
            # e se o nome do arquivo está presente
            if not file_field.file or not getattr(file_field, 'filename', None):
                return make_response(400, {'error': 'Invalid file upload.'})
            
            # Lê o conteúdo do arquivo
            file_content = file_field.file.read()

            file = FileObj(file_content, file_field.filename)

            # Chamada para o extractor_pdf
            result = extractor_pdf(file)

        else:
            return make_response(415, {'error': f'Unsupported Content-Type: {content_type}'})

        # Geração da resposta após extração
        response = generate_answer(result)
        return make_response(200, response)

    # Tratativas de erro
    except ValueError as e:
        return make_response(400, {'error': str(e)})
    except UnicodeDecodeError as e:
        return make_response(422, {'error': str(e)})
    except Exception as e:
        return make_response(500, {'error': str(e)})
