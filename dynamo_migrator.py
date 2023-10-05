import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=os.getenv('DYNAMODB_LOCAL_ENDPOINT'))

    table = dynamodb.create_table(  # type: ignore
        TableName=os.getenv('DB_TABLE'),
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 2
        }
    )
    return table


if __name__ == '__main__':
    my_table = create_table()
    my_table.meta.client.get_waiter('table_exists').wait(
        TableName=os.getenv('DB_TABLE'))
    print("Table status:", my_table.table_status)
    print(my_table.item_count)
