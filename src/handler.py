import json
import numpy as np


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def goodbye(event, context):
    response = {
        "statusCode": 200,
        "body": "Goodbye, world!"
    }

    return response

def calculate_dot_product(event, context):
    data = json.loads(event["body"], parse_float=Decimal)
    v1 = data["v1"]
    v2 = data["v2"]
    dot_pdt = np.dot(v1, v2)

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "result": dot_pdt
        })
    }
