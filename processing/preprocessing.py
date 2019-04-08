import re
import string
import spacy
from itertools import zip_longest

from nltk.stem.snowball import SnowballStemmer

# Load pretrained model
# nlp = spacy.load('en')
nlp = spacy.load('en', disable=['ner', 'parser'])
nlp.add_pipe(nlp.create_pipe('sentencizer'))

# Punctuation
tr = str.maketrans(string.punctuation, ' '*len(string.punctuation))
# Stemmer Language
stemmer = SnowballStemmer("english")

# remove punctuation
def remove_punct(val):
    return(re.sub(' +', ' ',val.translate(tr)).strip())


# snowball stemming
def create_stem(val):
    stemmed = ' '.join([stemmer.stem(word) for word in val.split()])
    return(stemmed)


# remove pronouns
def remove_pron(val):
    return ' '.join([word for word in val.split() if word != 'pron'])


# spacy lemmatizer
def create_spacy_lemma(val):
    doc = nlp(val)
    lemma_sentence = ' '.join([token.lemma_ for token in doc])
    return(remove_pron(lemma_sentence))


# clean function
def create_spacy_clean(val):
    clean_sentence = remove_pron(remove_punct(create_stem(create_spacy_lemma(val))).lower())
    return(clean_sentence)


# remove adjacent duplicate tokens
def remove_continuous_duplicates(val):
    check_list = val.split()
    return " ".join([i for i, j in zip_longest(check_list, check_list[1:]) if i != j])