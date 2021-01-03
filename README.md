# Coffee-gateway

Test app using AWS API Gateway, AWS Lambda, DynamoDB, serverless framework.\
Lambda written in Python.

## References

[Build Python REST Api with Flask and serverless framework](https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb)

[Serverless framework guide on AWS Dynamodb](https://www.serverless.com/dynamodb)

[Build NodeJS REST Api with AWS API Gateway and serverless framework](https://www.serverless.com/blog/node-rest-api-with-serverless-lambda-and-dynamodb)

[Python API with AWS API Gateway and Lambda](https://medium.com/accenture-the-dock/serverless-api-with-aws-and-python-tutorial-3dff032628a7)

[Handle Python packaging in serverless](https://www.serverless.com/blog/serverless-python-packaging)

[Using Lambda layers in serverless framework](https://www.serverless.com/framework/docs/providers/aws/guide/layers/)

[AWS Lambda layer guide: sample python application](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-python)

## Development

You need to [install](https://www.serverless.com/framework/docs/providers/aws/guide/installation/) serverless and set up AWS credentials.

Use a virtual environment. Install packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Also install the necessary NPM packages:

```bash
npm install
```

## Deployment

To build the python requirements layer, run:

```bash
./build_layers.sh
```

After making changes, deploy with serverless directly:

```bash
sls deploy
```

Monitor via the serverless [dashboard](https://app.serverless.com/).
