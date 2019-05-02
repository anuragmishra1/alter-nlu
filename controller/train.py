from sklearn.model_selection import StratifiedShuffleSplit
from tensorflow.keras.utils import to_categorical
from training_data.parse_data import get_data
from helper_data.data_augmentation import process_data, no_entity_process_data
from processing.prepare import prepare
from intent_model.classifier import model_def
from controller.saving import save_metadata
from intent_model.validation import Metrics
from entity_model.processing import get_used_unused_punct, punctuation
from entity_model.entity_train import train_entity


# start training
def start_train(data):  
    entity_data, intent_data, intent_entity = get_data(data)
    intent_train = intent_data.drop(['entities'], axis=1).drop_duplicates()
    if entity_data.empty:
        intent_train = no_entity_process_data(intent_train)
    else:
        intent_train = process_data(intent_train, entity_data)
    word_max_length, word_vocab_size, word_Xtrain, ytrain, encoder, word_tokenizer, helper_tokens = prepare(intent_train)
    final_model = model_def(word_max_length, word_vocab_size, encoder.classes_)
    if not entity_data.empty:
        used_punct, unused_punct = get_used_unused_punct(entity_data)
    else:
        used_punct, unused_punct = '', punctuation  
    save_metadata((intent_entity, word_tokenizer, encoder, word_max_length, helper_tokens, used_punct, unused_punct))
    if not entity_data.empty:
        print("> Training Entity Model")
        train_entity(intent_data, entity_data, used_punct, unused_punct)
    mcc = Metrics()
    sss = StratifiedShuffleSplit(n_splits = 5, test_size = 0.3)
    print("> Training Intent Model")
    for train_index, test_index in sss.split(word_Xtrain, ytrain):
        X_train, X_test = word_Xtrain[train_index], word_Xtrain[test_index]
        y_train, y_test = to_categorical(ytrain[train_index]), to_categorical(ytrain[test_index])
        final_model.fit(X_train, y_train, epochs = 20, verbose = 2, shuffle = True, validation_data = (X_test, y_test), callbacks = [mcc])
    del final_model

    return
