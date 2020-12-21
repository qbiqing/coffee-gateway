# Coffee-gateway

Test app using AWS API Gateway, AWS Lambda, DynamoDB, serverless framework.\
Lambda written in Python.

## References

Build Python REST API with Flask & serverless: https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb<br/>
AWS Dynamodb & serverless: https://www.serverless.com/dynamodb<br/>
Build Node.js REST API with AWS API Gateway & serverless: https://www.serverless.com/blog/node-rest-api-with-serverless-lambda-and-dynamodb<br/>
Python API with AWS API Gateway & Lambda: https://medium.com/accenture-the-dock/serverless-api-with-aws-and-python-tutorial-3dff032628a7<br/>
Handle Python packaging in serverless: https://www.serverless.com/blog/serverless-python-packaging<br/>

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

After making changes, deploy with serverless directly:

```bash
sls deploy
```

Monitor via the serverless [dashboard](https://app.serverless.com/).
