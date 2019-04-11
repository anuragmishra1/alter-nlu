import itertools
import operator
from processing.preprocessing import nlp, create_stem
from entity_model.processing import remove_punct
from entity_model.entity_featurizer import sent2features


def get_org_lemma_pos_dep(val, used_punct, unused_punct):
    ORG, LEMMA, POS, DEP = [], [], [], []
    doc = nlp(remove_punct(val, used_punct, unused_punct))
    for token in doc:
        if token.lemma_ == "-PRON-":
            LEMMA.append(token.text)
        else:
            LEMMA.append(create_stem(token.lemma_))
        POS.append(token.pos_)
        DEP.append(token.dep_)
        ORG.append(token.text)
    return ORG, (LEMMA, POS, DEP)

def query_feature(val, used_punct, unused_punct):
    org, spacy_feature = get_org_lemma_pos_dep(val, used_punct, unused_punct)
    lemma = spacy_feature[0]
    return org, list(zip(lemma, spacy_feature[1], spacy_feature[2]))

def extract_entity(val, crfmodel, used_punct, unused_punct, score=0.5,):
    entities = []
    features = query_feature(val, used_punct, unused_punct)
    out = crfmodel.predict_marginals_single(sent2features(features[1]))
    out = list(zip(out, features[0]))
    out = list(map(lambda x : ((x[1],)+max(x[0].items(), key=operator.itemgetter(1))), out))
    out = [list(group) for key, group in itertools.groupby(out, lambda x: x[1])]
    for item in out:
        entity = list(set(map(lambda x: x[1], item)))[0].split("$%&")
        if entity != ['other']:
            avg_score = sum(list(map(lambda x: x[2], item)))/len(list(map(lambda x: x[2], item)))
            if avg_score > score:
                selection = ' '.join(list(map(lambda x: x[0], item)))
                entities.append(({"name": str(entity[1]), "value": str(entity[0]), "parsed_value": str(selection)}))
    return entities
