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
