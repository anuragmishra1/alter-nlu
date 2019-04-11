import pandas as pd


# get structured data
def get_data(val):
    botName = val['botName']
    entity_data = pd.io.json.json_normalize(val['entity_data'], record_path='data', meta='name')
    intent_data = pd.io.json.json_normalize(val['intent_data'])
    intent_entity = list(set(pd.io.json.json_normalize(val['intent_data'], record_path='entities', meta='intent')['intent'].tolist()))

    print('> Training Bot : ' + botName)
    print("\tTotal training examples : {}\n\tIntents : {}".format(intent_data.shape[0], len(intent_data['intent'].unique())))
    if entity_data.empty:
        print("\tEntities : Not Added.")
    else:
        print("\tEntities : {}".format(len(entity_data['name'].unique())))
    
    return entity_data, intent_data, intent_entity
