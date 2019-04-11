from flashtext import KeywordProcessor
from entity_model.processing import remove_punct


def create_entity_dict(val, used_punct, unused_punct):
    entity_dict, kp = {}, KeywordProcessor()
    entity_dict_ = val.apply(lambda x: {x['value']+"$%&"+x['name']: x['synonyms']}, axis=1)
    for item in entity_dict_:
        for key, values in item.items():
            new_value = []
            for value in values:
                new_value.append(remove_punct(value, used_punct, unused_punct))
            new_value = list(set(new_value))
            entity_dict[key] = new_value
    kp.add_keywords_from_dict(entity_dict)
    return kp
