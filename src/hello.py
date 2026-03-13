import json

# Lambda function handler
def handler(event, context):
    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Deploy with CDK"},
        {"id": 3, "title": "Become unstoppable"}
    ]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(tasks)
    }
