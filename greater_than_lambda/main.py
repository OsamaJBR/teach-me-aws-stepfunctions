import json
import random

def lambda_handler(event,context):
    final_number = random.randint(100,1000)
    return {"final_number" : final_number} 