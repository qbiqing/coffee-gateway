import json
import boto3

TABLE_NAME = "to_do_list"
ddb = boto3.resource("dynamodb")
ddb_table = ddb.Table(TABLE_NAME)

def lambda_handler_post(event, context):
    try: 
        response = ddb_table.put_item(Item=event)
        return {
            "statusCode": 201,
            "body": {
                "message": "successfully inserted",
                "response": response,
                "input": event
            }
        }
    except Exception as e:
        return {
           "statusCode": 400,
            "body": {
                "message": f"error inserting: {e}",
                "input": event
            }
        }


def lambda_handler_get(event, context):
    try:
        response = ddb_table.scan()
        return {
            "statusCode": 200,
            "body": response["Items"]
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"message": f"error retrieving: {e}"},
        }


def lambda_handler_patch(event, context):
    try:
        response = ddb_table.get_item(Key={"item": event["item"]})
        if "Item" not in response:
            raise Exception("Item not found.")

        response = ddb_table.put_item(Item=event)
        return {
            "statusCode": 200,
            "body": {
                "message": "successfully updated",
                "response": response,
                "input": event
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": {"message": f"error updating: {e}"},
        }


def lambda_handler_delete(event, context):
    try:
        response = ddb_table.get_item(Key={"item": event["item"]})
        if "Item" not in response:
            raise Exception("Item not found.")

        response = ddb_table.delete_item(Key={"item": event["item"]})
        return {
            "statusCode": 204,
            "body": {
                "message": "successfully deleted",
                "response": response,
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": {"message": f"error deleting: {e}"},
        }
