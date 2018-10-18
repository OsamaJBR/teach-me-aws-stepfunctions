import json

def lambda_handler(event, context):
    number_1 = int(event['key1'])
    number_2 = int(event['key2'])
    return {"number" : abs(number_1 - number_2)}
