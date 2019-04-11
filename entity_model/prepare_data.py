import pandas as pd
from spacy.gold import biluo_tags_from_offsets
from processing.preprocessing import create_stem, nlp


def get_spacy_data(val, entities):
    LEMMA = []
    POS = []
    DEP = []
    for token in val:
        if token.lemma_ == "-PRON-":
            LEMMA.append(token.text)
        else:
            LEMMA.append(token.lemma_)
        POS.append(token.pos_)
        DEP.append(token.dep_)
    tags = biluo_tags_from_offsets(val, entities)
    tags = 'Ω'.join(list(map(lambda x: x[2:] if x != 'O' else 'other', tags)))
    return create_stem(' '.join(LEMMA)), ' '.join(POS), ' '.join(DEP), tags

def data_feature(val):
    spacy_data = []
    for doc, span in zip(nlp.pipe(val['text'].tolist(), n_threads=-1, batch_size=10000), val['span_info'].tolist()):
        spacy_data.append(list(get_spacy_data(doc, span)))
    new_frame = pd.DataFrame(spacy_data, columns = ['lemma', 'pos', 'dep', 'ref_values'])
    new_frame.drop_duplicates(inplace=True)
    new_frame.reset_index(drop=True, inplace=True)
    return new_frame
