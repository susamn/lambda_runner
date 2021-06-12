import json

import lambda_function


class Context:
    def __init__(self, arn: str):
        self.invoked_function_arn = arn


if __name__ == "__main__":
    event = {}
    with open("events/s3-put.json", 'r') as f:
        event = json.load(f)
        lambda_function.lambda_handler(event, Context("Sample ARN"))
