def lambda_handler(event, context):
    name = "User"
    if event and "queryStringParameters" in event:
        params = event["queryStringParameters"]
        if params and "name" in params:
            name = params["name"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": f"Hello {name}, Welcome to Lambda via CodePipeline 🚀"
    }
