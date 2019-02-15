import pandas as pd


# get structured data
def get_data(val):
    botName = val['botName']
    entity = pd.io.json.json_normalize(val['entity_data'], record_path='data', meta='name')
    train = pd.io.json.json_normalize(val['intent_data']).drop(['entities'], axis=1).drop_duplicates()
    intent_entity = list(set(pd.io.json.json_normalize(val['intent_data'], record_path='entities', meta='intent')['intent'].tolist()))

    print('> Training Bot : ' + botName)
    print("\tTotal training examples : {}\n\tIntents : {}".format(train.shape[0], len(train['intent'].unique())))
    if entity.empty:
        print("\tEntities : Not Added.")
    else:
        print("\tEntities : {}".format(len(entity['name'].unique())))
    
    return entity, train, intent_entity
