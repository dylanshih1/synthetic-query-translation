import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from lemmatizer import Lemmatizer

sentence = ["the quick brown fox jumps over the lazy dogs"]

def test_get_sentences():
    lemmatizer = Lemmatizer(sentence)
    assert lemmatizer.sentences == ["the quick brown fox jumps over the lazy dogs"]

def test_basic_conversion():
    lemmatizer = Lemmatizer(sentence)
    lemmatizer.to_lemma()
    assert lemmatizer.sentences == ["the quick brown fox jump over the lazy dog"]

def test_convert_nouns():
    lemmatizer = Lemmatizer(sentence)
    lemmatizer.to_lemma(["NOUN"])
    assert lemmatizer.sentences == ["the quick brown fox jumps over the lazy dog"]

def test_convert_verbs():
    lemmatizer = Lemmatizer(sentence)
    lemmatizer.to_lemma(["VERB"])
    assert lemmatizer.sentences == ["the quick brown fox jump over the lazy dogs"]

def test_convert_multiple():
    lemmatizer = Lemmatizer(sentence)
    lemmatizer.to_lemma(["NOUN", "VERB"])
    assert lemmatizer.sentences == ["the quick brown fox jump over the lazy dog"]


