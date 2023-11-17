import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from postagger import POSTagger

def test_get_sentences():
    tagger = POSTagger(["The quick brown fox.", "Jumps over the lazy dog."])
    assert tagger.sentences == ["The quick brown fox.", "Jumps over the lazy dog."]

def test_remove_types():
    tagger = POSTagger(["The quick brown fox.", "Jumps over the lazy dog."])
    tagger.remove_types(["PUNCT"])
    assert tagger.sentences == ["The quick brown fox", "Jumps over the lazy dog"]

def test_keep_types():
    tagger = POSTagger(["The quick brown fox.", "Jumps over the lazy dog."])
    tagger.keep_types(["NOUN", "ADJ"])
    assert tagger.sentences == ["quick brown fox", "lazy dog"]