import re
import itertools
import pandas as pd
from flashtext import KeywordProcessor
from processing.preprocessing import create_spacy_clean, create_stem, remove_continuous_duplicates
from helper_data.entity_dictionary import create_entity_dictionary


# get stem, lemma of synonyms
def derive_synonyms(val):
    temp = []
    for word in val:
        temp.append(word.lower())
        temp.append(create_spacy_clean(word).lower())
        temp.append(create_stem(word).lower())

    return(list(set(temp)))


def get_derived_synonyms(val):
    val.synonyms = val.synonyms.apply(derive_synonyms)
    return val


# add to dictionary for replacement
def create_synonym_dictonary(val):
    kp = KeywordProcessor()
    val = get_derived_synonyms(val)
    val.synonyms.apply(kp.add_keywords_from_list)
    return kp


# replace synonyms
def multipleReplace(text, wordDict):
    kp_replace = KeywordProcessor()
    for key in wordDict:
        kp_replace.add_keyword(key, wordDict[key])
        mod_text = kp_replace.replace_keywords(text)
    return mod_text


# create derived training data
def create_derived(kp, val1, val2):
    keywords = kp.extract_keywords(val1[1])
    if len(keywords) != 0:
        derived_queries, synonym_list = [], []
        for keyword in keywords:
            for synonym in val2.synonyms:
                if keyword in synonym:
                    synonym_list.append(synonym)
        all_combo = list(itertools.product(*synonym_list))

        for combo in all_combo:
            derived_query = multipleReplace(val1[1].lower(), dict(zip(keywords, list(combo))))
            derived_queries.append(derived_query)

        return pd.DataFrame({'text' : list(set(derived_queries)), 'intent' : val1[0]})
    else :
        return pd.DataFrame({'text' : [val1[1]], 'intent' : val1[0]})


# add EOS and SOS token
def add_sos_eos(val):
    return '<SOS> ' + val + ' <EOS>'


# Data augmentation
def process_data(val1, val2):
    derived_train = pd.DataFrame()
    kp = create_synonym_dictonary(val2)

    print("> Data Augmentation")
    for val in val1.values.tolist():
        derived_train = pd.concat([derived_train, create_derived(kp, val, val2)], sort=True)
    
    # all training data
    val3 = pd.concat([val1, derived_train])
    
    # drop duplicates
    val3.drop_duplicates(inplace=True)

    # apply preprocessing function
    print("> Preprocessing")
    val3.text = val3.text.apply(create_spacy_clean)
    val3.text = val3.text.apply(remove_continuous_duplicates)
    
    # drop duplicate sentences(if any)
    val3.drop_duplicates(inplace=True)

    # shuffle tranining data
    val3 = val3.sample(frac=1).reset_index(drop=True)

    # create entity dictionary
    print("> Entity Dictionary")
    entity_extractor = create_entity_dictionary(val2)
    
    # add EOS and SOS
    val3['text'] = val3['text'].apply(add_sos_eos)

    return val3, entity_extractor


# no entity process data
def no_entity_process_data(val1):
    # apply preprocessing function
    print("> Preprocessing")
    val1.text = val1.text.apply(create_spacy_clean)

    # drop duplicate sentences(if any)
    val1.drop_duplicates(inplace=True)

    # shuffle training data
    val1 = val1.sample(frac=1).reset_index(drop=True)

    # create empty dictionary
    entity_extractor = KeywordProcessor()
    
    # add EOS and SOS
    val1['text'] = val1['text'].apply(add_sos_eos)

    return val1, entity_extractor
