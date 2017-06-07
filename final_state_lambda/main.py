import json
import boto3
import inflect

def lambda_handler(event,context):
    inflect_engine = inflect.engine()
    number = inflect_engine.number_to_words(event['final_number'])
    message = {"DelMeMessage": "The StepFunctions Result is %r" %number}
    client = boto3.client('sns')
    response = client.publish(
        TargetArn="SNS-TOPIC-ARN",
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
