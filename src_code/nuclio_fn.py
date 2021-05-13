import json
import random

def predict(context, data):
    body = {context.model : f"{data} - {random.random()}"}
    return context.Response(body=body, status_code=200)

def init_context(context):
    context.model = "my_model"

def handler(context, event):
    return predict(context, **json.loads(event.body))