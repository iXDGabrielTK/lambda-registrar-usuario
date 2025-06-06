# Função AWS Lambda: Registrar Usuário

Esta função Lambda foi criada como parte do trabalho da disciplina de Arquitetura em Cloud. Seu objetivo é registrar usuários com nome e e-mail, salvando os dados em uma tabela DynamoDB, acessível por meio de uma API pública HTTP via API Gateway.

---

## 📌 Objetivo

Criar uma função serverless que:
- Recebe um `POST` com nome e e-mail
- Salva os dados em uma tabela no DynamoDB (`Usuarios`)
- Retorna uma mensagem de sucesso

---

## 🚀 Endpoint público

🔒 A URL da API foi removida deste repositório por motivos de segurança.  
Ela será disponibilizada apenas para fins de avaliação mediante solicitação.

---

## 📥 Exemplo de entrada (JSON)

```json
{
  "nome": "Lucas",
  "email": "lucas@email.com"
}
```

---

## 📤 Exemplo de saída (JSON)

```json
{
  "mensagem": "Usuário Lucas com e-mail lucas@email.com salvo com sucesso."
}
```

---

## ⚙️ Dependências e ambiente

- AWS Lambda (Python 3.11)
- Amazon DynamoDB
  - Tabela: `Usuarios`
  - Chave primária: `email` (String)
- Amazon API Gateway (HTTP)
- IAM Role com política: `AmazonDynamoDBFullAccess`

---

## 🧪 Como testar (exemplo de uso via curl)

```bash
curl -X POST https://<URL_OCULTADA>/registrarUsuario \
  -H "Content-Type: application/json" \
  -d '{"nome": "Lucas", "email": "lucas@email.com"}'
```

---

## 🛠️ Estrutura do código

```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
tabela = dynamodb.Table('Usuarios')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        nome = body.get('nome')
        email = body.get('email')

        if not nome or not email:
            return {
                'statusCode': 400,
                'body': json.dumps({'erro': 'Nome e e-mail são obrigatórios'}, ensure_ascii=False)
            }

        tabela.put_item(Item={'email': email, 'nome': nome})

        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensagem': f'Usuário {nome} com e-mail {email} salvo com sucesso.'
            }, ensure_ascii=False)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'erro': str(e)}, ensure_ascii=False)
        }
```

---

## 📦 Estrutura do projeto

```
lambda-registrar-usuario/
├── lambda_function.py
└── README.md
```

---

## 📚 Observações finais

- A função foi testada com sucesso via Postman e curl
- O endpoint é público sem autenticação apenas temporariamente para fins acadêmicos
- A URL foi removida deste repositório público para evitar uso indevido
- A solução utiliza serviços 100% serverless e gratuitos no plano AWS Free Tier

---

## 👨‍💻 Autor

Gabriel TK  
Trabalho de Arquitetura em Cloud  
Entregue em: 06/06/2025
