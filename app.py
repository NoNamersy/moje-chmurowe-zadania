import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    path = event.get('resource', '')
    http_method = event.get('httpMethod', '')

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET,POST'
    }

    try:
        user_id = "test_user_001" 

        if path == '/tasks' and http_method == 'GET':
            response = table.scan(
                FilterExpression="begins_with(userId, :prefix)",
                ExpressionAttributeValues={":prefix": "task_"}
            )
            tasks = response.get('Items', [])
            tasks = sorted(tasks, key=lambda x: x.get('task_number', 0))
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'total_tasks': len(tasks), 'tasks': tasks}, cls=DecimalEncoder)
            }

        elif path == '/level' and http_method == 'POST':
            response = table.update_item(
                Key={'userId': user_id},
                UpdateExpression='ADD current_level :inc',
                ExpressionAttributeValues={':inc': 1},
                ReturnValues='UPDATED_NEW'
            )
            new_level = int(response['Attributes']['current_level'])
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({
                    'message': 'Awans na nowy poziom zakończony sukcesem!',
                    'new_level': new_level
                })
            }

        return {
            'statusCode': 404,
            'headers': headers,
            'body': json.dumps({'error': 'Endpoint not found'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }