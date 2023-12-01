import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from lemmatizer import Lemmatize

sentences = ["The quick brown fox", "Jumps over the lazy dog", "I saw foxes"]

def test_get_sentences():
    lemmatizer = Lemmatizer(sentences)
    assert lemmatizer.sentences == ["The quick brown fox", "Jumps over the lazy dog", "I saw foxes"]

def test_basic_conversion():
    lemmatizer = Lemmatizer(sentences)
    lemmatizer.to_lemma()
    assert lemmatizer.sentences == ["The quick brown fox", "Jump over the lazy dog", "I see fox"]

