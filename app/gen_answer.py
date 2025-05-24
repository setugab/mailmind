from openai import OpenAI
from aws_utils import get_secret
import json

# Pegando a secret key do OpenAI
# A função get_secret é responsável por buscar a chave secreta do OpenAI no AWS Secrets Manager
secrets = get_secret("openai/api_key")

# Inicializando o cliente OpenAI com a chave secreta
client = OpenAI(api_key=secrets["OPENAI_API_KEY"])

# Função para gerar a resposta do e-mail esperando o texto limpo como parâmetro
def generate_answer(clean_text):
    prompt = f"""
    Você é um assistente de IA que ajuda a avaliar e-mails, trazendo duas classificações: Produtivo e Improdutivo.
    Sua missão é analisar o conteúdo do e-mail e classificá-lo de acordo com essas categorias além de gerar uma resposta sugerida.
    O e-mail a ser analisado é o seguinte: {clean_text}
    
    As saídas devem ser apresentadas em formato JSON, com as seguintes chaves:
    - "classificacao": a classificação do e-mail (Produtivo ou Improdutivo)
    - "resposta_sugerida": uma resposta sugerida para o e-mail, de forma agradável e sucinta.

    Caso o email esteja em outra língua, traduza-o para o português antes de gerar a resposta.
    """

    try:
        # Enviando o prompt para o modelo OpenAI e recebendo a resposta
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente de IA especializado em avaliação de e-mails."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400,
        )
        # Extraindo a resposta do modelo
        answer = response.choices[0].message.content

        try: 
            # Tentando converter a resposta para JSON
            answer = json.loads(answer)
        except json.JSONDecodeError:
            # Se a conversão falhar, retorna a resposta original
            print("Não foi possível converter a resposta para JSON. Retornando a resposta original.")

        return answer
    except Exception as e:
        print(f"Error generating answer: {e}")
        raise
