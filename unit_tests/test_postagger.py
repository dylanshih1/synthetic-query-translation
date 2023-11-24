import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from postagger import POSTagger

sentence = "The quick brown fox jumps over the lazy dog."

def test_get_sentences():
    tagger = POSTagger([sentence])
    assert tagger.sentences == ["The quick brown fox jumps over the lazy dog."]

def test_remove_types_punct():
    tagger = POSTagger([sentence])
    tagger.remove_types(["PUNCT"])
    assert tagger.sentences == ["The quick brown fox jumps over the lazy dog"]

def test_remove_types_det():
    tagger = POSTagger([sentence])
    tagger.remove_types(["DET"])
    # note that punctuation has space before it
    assert tagger.sentences == ["quick brown fox jumps over lazy dog ."]

def test_remove_types_mult():
    tagger = POSTagger([sentence])
    tagger.remove_types(["DET", "PUNCT"])
    assert tagger.sentences == ["quick brown fox jumps over lazy dog"]

def test_keep_types_adj():
    tagger = POSTagger([sentence])
    tagger.keep_types(["ADJ"])
    assert tagger.sentences == ["quick brown lazy"]

def test_keep_types_noun():
    tagger = POSTagger([sentence])
    tagger.keep_types(["NOUN"])
    assert tagger.sentences == ["fox dog"]

def test_keep_types_mult():
    tagger = POSTagger([sentence])
    tagger.keep_types(["NOUN", "ADJ"])
    assert tagger.sentences == ["quick brown fox lazy dog"]