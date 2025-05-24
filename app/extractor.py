import re
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pypdf import PdfReader
from io import BytesIO

# Setando as palavras de parada para o português, fazendo o download do NLTK
# e adicionando o diretório de download ao caminho do NLTK
nltk_data = "/tmp/nltk_data"
nltk.download('stopwords', download_dir=nltk_data)
nltk.download('punkt_tab', download_dir=nltk_data)
nltk.data.path.append(nltk_data)

stop_words = set(stopwords.words('portuguese'))

# Função para extrair texto de arquivos PDF e TXT
def extractor_pdf(file):
    try: 

        # Salva o nome do arquivo
        # e inicializa uma string vazia para armazenar o texto
        filename = file.filename
        text = ""

        # Garante que file.file é BytesIO
        if isinstance(file.file, bytes):
            file.file = BytesIO(file.file)
        
        # Reseta o ponteiro do arquivo para o início
        # para garantir que o conteúdo seja lido corretamente
        file.file.seek(0)  

        # Verifica a extensão do arquivo
        # e processa o conteúdo de acordo
        if filename.endswith(".pdf"):
            reader = PdfReader(file.file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        elif filename.endswith(".txt"):
            contents = file.file.read()
            try:
                # Tenta decodificar o conteúdo como UTF-8
                text = contents.decode("utf-8").strip()

            # Se falhar, tenta decodificar como Latin-1
            except UnicodeDecodeError:
                text = contents.decode("latin1").strip()

        else: 
            raise ValueError("Unsupported file type. Please upload a PDF or TXT file.")

        # Chama a função extractor_text para processar o texto extraído
        # e retorna os tokens filtrados
        tokens = extractor_text(text)
        return tokens

    except Exception as e:
        raise RuntimeError(f"Error processing file: {e}")


# Função para extrair texto de strings
def extractor_text(text):
    try:
        # Regex que remove caracteres especiais e números
        text = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ\s]', '', text)
        text = re.sub(r'\d+', '', text)

        # Tokenização do texto
        tokens = word_tokenize(text, language='portuguese')

        # Remove stopwords
        filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]

        # Junta os tokens filtrados em um texto limpo que será enviado para o modelo
        # no arquivo gen_answer.py
        clean_text = ' '.join(filtered_tokens)
        return clean_text
    
    except Exception as e:
        print(f"Error processing text: {e}")
        raise
