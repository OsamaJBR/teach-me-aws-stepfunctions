import json
import random

def lambda_handler(event,context):
    final_number = random.randint(0,100)
    return {"final_number" : final_number} 