import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from depparser import DependencyParser

sentence = "The quick brown fox jumps over the lazy dog."

def test_get_sentences():
    parser = DependencyParser([sentence])
    assert parser.sentences == ["The quick brown fox jumps over the lazy dog."]

def test_keep_heads():
    parser = DependencyParser([sentence])
    parser.keep_heads()
    assert parser.sentences == ["fox jumps dog"]
