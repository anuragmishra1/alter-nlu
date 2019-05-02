import string
import itertools


flatten = lambda x: [item for sublist in x for item in sublist]
punctuation = string.punctuation


def get_used_punct(val):
    used_punct = []
    items = flatten(val['synonyms'].tolist())
    for item in items:
        for item_ in item:
            if item_ in punctuation:
                used_punct.append(item_)
    used_punct = list(set(used_punct))
    return used_punct


def get_used_unused_punct(val):
    d = punctuation
    used_punct = get_used_punct(val)
    for item in used_punct:
        d = d.replace(item, "")
    return used_punct, d


def remove_punct(val, used_punct, unused_punct):
    test = list(val)
    for item in test:
        if item in unused_punct:
            test[test.index(item)] = ""
        elif item in used_punct:
            #check again
            test[test.index(item)] = " " + item + " "
    return(" ".join("".join(test).split()).lower())


def remove_cont_dupl(val):
    val = val.split()
    new_val = [i for i, j in itertools.zip_longest(val, val[1:]) if i != j]
    return ' '.join(new_val)
