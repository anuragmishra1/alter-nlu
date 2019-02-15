import itertools
from flashtext import KeywordProcessor


# Create entity dictionary
def create_dictionary_items(row, dictionary):
    z = list(itertools.product(*[[row['value_name']], row['synonyms']]))
    for item in z:
        new_item = item[0] + (item[1], )
        dictionary.add_keyword(item[1], new_item)


def create_entity_dictionary(val):
    val['value_name'] = list(zip(val.value, val.name))
    entity_dictionary = KeywordProcessor()
    val.apply(create_dictionary_items, args=(entity_dictionary,), axis=1)
    return entity_dictionary
