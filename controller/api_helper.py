from training_data.data_validator import validate_json, check_intent_count
from controller.loading import loader
from controller.train import start_train
from extractors.extract_intent import get_intent
from extractors.extract_entity import extract_entity


# load bot models
def load_all():
    global metadata, model
    metadata, model = loader()


# train and load continuously
def train_n_load(data):
    if validate_json(data):
        return {"error": "Invalid training data format!", "statusCode": 400}
    if check_intent_count(data):
        return {"error": "At least 2 intents required!", "statusCode": 400}
    global metadata, model
    start_train(data)
    metadata, model = loader()
    return {"message": "Training Complete & Model Deployed Successfully!", "statusCode": 200}


# convert input query to structured data
def extract_info(data):
    try:
        intent, confidence = get_intent(data['text'], metadata, model)
    except TypeError:
        return {"error": "No Bot Trained!", "statusCode": 400}
    if intent in metadata[0]:
        entities = extract_entity(data['text'], metadata[1])
    else:
        entities = []
    return {"intent": intent, "confidence": round(float(confidence), 4), "entities": entities}
