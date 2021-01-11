import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("jack-workshop-contacts")


def lambda_get_contact(event, context):
    try: 
        item_name = event["pathParameters"]["proxy"]
        response = table.get_item(Key={"name": item_name})
        
        if "Item" not in response:
            return {
                "statusCode": 404,
                "body": "Contact not found"
            }
        
        return {
            "statusCode": 200,
            "body": json.dumps(response["Item"])
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": "error retrieving item: " + str(e) 
        }



def lambda_patch_handler(event, context):
    try: 
        item_name = event["pathParameters"]["proxy"]
        data = json.loads(event["body"])
        
        response = table.update_item(
            Key={"name": item_name},
            UpdateExpression="set favourite_colour=:c",
            ExpressionAttributeValues={
                ":c": data["favourite_colour"],
            },
            ReturnValues="ALL_NEW"
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps(response["Attributes"])
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": "error updating item: " + str(e) 
        }


def lambda_delete_handler(event, context):
    try: 
        item_name = event["pathParameters"]["proxy"]
        table.delete_item(Key={"name": item_name})
        return {
            "statusCode": 204,
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": "error retrieving item: " + str(e) 
        }
