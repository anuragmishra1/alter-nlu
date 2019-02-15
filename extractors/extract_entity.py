from fuzzywuzzy import process, fuzz
from processing.preprocessing import create_spacy_clean


# Get entity from input query
def extract_entity(text, dictionary):
    entity_output = []
    text = create_spacy_clean(text)
    for user_entity in dictionary.extract_keywords(text):
        output = {"value":str(user_entity[0]), "category":str(user_entity[1])}
        if output not in entity_output:
            entity_output.append({"value":str(user_entity[0]), "category":str(user_entity[1])})

    synonyms = list(dictionary.get_all_keywords().keys())
    for synonym in process.extractBests(text, synonyms, score_cutoff=90, scorer=fuzz.token_set_ratio):
        entities = dictionary.extract_keywords(synonym[0])
        output = {"value":str(entities[0][0]), "category":str(entities[0][1])}
        if output not in entity_output:
            entity_output.append({"value":str(entities[0][0]), "category":str(entities[0][1])})
    
    return entity_output
