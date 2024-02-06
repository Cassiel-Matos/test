import requests
import json
import base64

# Substitua com seu token de acesso pessoal do GitHub
token = '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'

# URL da API do GitHub para criar um ambiente
url_create_environment = 'https://api.github.com/repos/Cassiel-Matos/Game-TFORCE/environments'

# Cabeçalhos para incluir o token de acesso
headers = {
    'Authorization':'token {token}',    
    'Accept': 'application/vnd.github.antiope-preview+json', # Necessário para usar a API de ambientes
    'Content-Type': 'application/json'
}

# Corpo da requisição para criar o ambiente
data_create_environment = {
    'name': 'prod'
}

# Realiza a requisição POST para criar o ambiente
response = requests.post(url_create_environment, headers=headers, data=json.dumps(data_create_environment))

# Verifica se a criação do ambiente foi bem-sucedida
if response.status_code == 201:
    print('Ambiente "prod" criado com sucesso.')
else:
    print(f'Erro ao criar ambiente: {response.text}')

# URL da API do GitHub para adicionar uma variável de ambiente ao ambiente "prod"
url_add_secret = 'https://api.github.com/repos/Cassiel-Matos/Game-TFORCE/actions/secrets/prod'

# Valor a ser criptografado (no caso, "teste1")
value = 'teste1'

# Codifica o valor em base64
encoded_value = base64.b64encode(value.encode()).decode()

# Corpo da requisição para adicionar a variável "teste" com o valor "teste1"
data_add_secret = {
    'secret_name': 'teste',
    'encrypted_value': encoded_value, # O valor precisa ser criptografado antes de ser enviado (use base64)
    'visibility': 'all' # Define a visibilidade da variável
}

# Realiza a requisição PUT para adicionar a variável
response = requests.put(url_add_secret, headers=headers, data=json.dumps(data_add_secret))

# Verifica se a adição da variável foi bem-sucedida
if response.status_code == 204:
    print('Variável "teste" adicionada com sucesso.')
else:
    print(f'Erro ao adicionar variável: {response.text}')
