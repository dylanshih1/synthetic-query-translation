import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from postagger import POSTagger

def remove_types_test():
    Tagger = POSTagger(["The quick brown fox.", "Jumps over the lazy dog."])
    Tagger.remove_types(["PUNCT"])
    assert Tagger.sentences == ["The quick brown fox", "Jumps over the lazy dog"]


