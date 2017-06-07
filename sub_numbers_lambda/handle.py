import json
import time

def lambda_handler(event,context):
    number_1 = event['key1']
    number_2 = event['key2']
    return {"number" : abs(number_1 - number_2)}