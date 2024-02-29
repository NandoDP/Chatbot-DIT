import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("french")


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    # stem chaque mot
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialiser le sac avec 0 pour chaque mot
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag