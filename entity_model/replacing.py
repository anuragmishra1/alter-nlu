import itertools
import pandas as pd
from entity_model.slicing import get_sliced_data
from entity_model.processing import remove_punct, remove_cont_dupl, flatten
from entity_model.entity_dictionary import create_entity_dict

def reverse_span(val):
    new_val = []
    for item in val:
        new_item = item[1:] + item[:-2]
        new_val.append(new_item)
    return new_val

def get_replace_dict(val):
    replace_dict = val.groupby('name')['synonyms'].apply(flatten).to_dict()
    return replace_dict

def get_replaced_data(val1, val2, used_punct, unused_punct):
    all_examples = []
    sliced_frame = get_sliced_data(val1)
    replace_dict = get_replace_dict(val2)
    entity_dict = create_entity_dict(val2, used_punct, unused_punct)
    for i in sliced_frame['combined']:
        replaced_synonym = []
        for item in i:
            if item[1] == ["other"]:
                replaced_synonym.append(item[0])
            if item[1] != ["other"]:
                replaced_synonym.append(replace_dict[item[1][0]])

        all_combo = list(itertools.product(*replaced_synonym))
        all_ex = list(map(lambda x: remove_punct(remove_cont_dupl(" ".join(x)), used_punct, unused_punct), all_combo))
        all_examples.extend(all_ex)

    all_examples = pd.DataFrame(all_examples, columns=['text'])
    all_examples.drop_duplicates(inplace=True)
    all_examples.reset_index(drop=True, inplace=True)
    all_examples['span_info'] = all_examples['text'].apply(lambda x: reverse_span(entity_dict.extract_keywords(x, span_info=True)))
    return all_examples
