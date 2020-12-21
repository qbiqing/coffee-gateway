import simplejson as json
import boto3
import os
from decimal import Decimal

COFFEE_TABLE = os.environ["COFFEE_TABLE"]

dynamodb = boto3.resource("dynamodb")
client = boto3.client("dynamodb")
coffee_table = dynamodb.Table(COFFEE_TABLE)

def create(event, context):
    data = json.loads(event["body"], parse_float=Decimal)
    try:
        response = coffee_table.put_item(Item=data)

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "successfully inserted",
                "response": response,
                "input": data
            }),
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"error inserting: {e}",
                "input": data
            }),
        }

def retrieve(event, context):
    try:
        response = coffee_table.scan()
        return {
            "statusCode": 200,
            "body": json.dumps(response["Items"])
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"error retrieving: {e}"
            }),
        }
