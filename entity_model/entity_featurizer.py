from entity_model.prepare_data import data_feature
from entity_model.replacing import get_replaced_data

def get_sentences(val):
    sentences = val.apply(lambda x: list(zip(x['lemma'].split(), x['pos'].split(),
                x['dep'].split(), x['ref_values'].split('Ω'))), axis=1).tolist()
    return sentences

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    dep = sent[i][2]

    features = {
        'bias': 1.0,
        'word': word,
        'postag': postag,
        'dep': dep,
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        dep1 = sent[i-1][2]
        features.update({
            '-1:word': word1,
            '-1:postag': postag1,
            '-1:dep': dep1,
        })
    else:
        features['BOS'] = True
    
    if i > 1:
        word2 = sent[i-2][0]
        postag2 = sent[i-2][1]
        dep2 = sent[i-2][2]
        features.update({
            '-2:word': word2,
            '-2:postag': postag2,
            '-2:dep': dep2,
        })

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        dep1 = sent[i+1][2]
        features.update({
            '+1:word': word1,
            '+1:postag': postag1,
            '+1:dep': dep1,
        })
    else:
        features['EOS'] = True
    
    if i < len(sent)-2:
        word2 = sent[i+2][0]
        postag2 = sent[i+2][1]
        dep2 = sent[i+2][2]
        features.update({
            '+2:word': word2,
            '+2:postag': postag2,
            '+2:dep': dep2,
        })

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return list(map(lambda x: x[3], sent))


def get_trainable_features(intent_data, entity_data, used_punct, unused_punct):
    sentences = get_sentences(data_feature(get_replaced_data(intent_data, entity_data, used_punct, unused_punct)))
    X = [sent2features(s) for s in sentences]
    y = [sent2labels(s) for s in sentences]
    return X, y
