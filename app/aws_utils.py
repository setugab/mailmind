import boto3
import json
from botocore.exceptions import ClientError

# Função para obter o segredo do AWS Secrets Manager
# Esta função é responsável por buscar a chave secreta do OpenAI no AWS Secrets Manager
def get_secret(secret_name, region_name="sa-east-1"):
    client = boto3.client('secretsmanager', region_name=region_name)
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        return json.loads(secret)
    except ClientError as e:
        raise RuntimeError(f"Unable to retrieve secret: {e}")
