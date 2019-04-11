from processing.preprocessing import create_spacy_clean
from tensorflow.keras.preprocessing.sequence import pad_sequences


# get intent of input query
def get_intent(text, metadata, model):
    text_query = ['<SOS> ' + create_spacy_clean(text) + ' <EOS>']
    word_encoded_docs = metadata[1].texts_to_sequences(text_query)
    word_Xtest = pad_sequences(word_encoded_docs, maxlen=metadata[3], padding='post')

    if len(set(word_Xtest[0])-set(metadata[4])) != 0:
        prediction = model.predict([word_Xtest])[0]
        if max(prediction) > 0.3:
            output = [metadata[2].classes_[list(prediction).index(max(prediction))], max(prediction)]
            return output[0], output[1]
        else:
            return 'fallback', 0
    else:
        return 'fallback', 0