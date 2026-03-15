import json


def handler(event, context):
    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Deploy with CDK"},
        {"id": 3, "title": "Become unstoppable"},
    ]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(tasks[0]),
    }


if __name__ == "__main__":
    # Local test harness for debugging
    test_event = {"test": "value"}
    result = handler(test_event, None)
    print(json.dumps(result, indent=2))
