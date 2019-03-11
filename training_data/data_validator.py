from jsonschema import validate
from training_data.schema import *


# check number of intents
def check_intent_count(val):
    intent_count = len(set(map(lambda datum: datum['intent'], val['intent_data'])))
    if intent_count >= 2:
        return False
    else:
        return True


# validate training data with schema
def validate_json(val):    
    try:
        for item in val['intent_data']:
            validate(item, intent_data_schema)
        for item in val['entity_data']:
            validate(item, entity_data_schema)
        validate(val['botName'], botName)
        return False
    except Exception:
        return True
