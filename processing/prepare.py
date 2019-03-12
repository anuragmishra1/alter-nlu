from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences


# prepare data from training
def prepare(val):  
    # create the word tokenizer
    word_tokenizer = Tokenizer(oov_token='<UNK>', filters='', lower=False)
    # fit the word tokenizer on the documents
    word_tokenizer.fit_on_texts(val.text)

    # word sequence encode
    word_encoded_docs = word_tokenizer.texts_to_sequences(val.text)
    
    # pad word sequences
    word_max_length = max([len(s.split()) for s in val.text])
    word_Xtrain = pad_sequences(word_encoded_docs, maxlen=word_max_length, padding='post')

    # encode class values as integers
    encoder = LabelEncoder()
    encoder.fit(val.intent)
    encoded_Y = encoder.transform(val.intent)

    # define word vocabulary size (Adding 1 because of reserved 0 index)
    word_vocab_size = len(word_tokenizer.word_index) + 1
    
    helper_tokens = (word_tokenizer.word_index['<UNK>'], word_tokenizer.word_index['<SOS>'], word_tokenizer.word_index['<EOS>'], 0)
    return word_max_length, word_vocab_size, word_Xtrain, encoded_Y, encoder, word_tokenizer, helper_tokens
