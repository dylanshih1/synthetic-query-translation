import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from delstop import delete_stopwords

def test_delete_stop():
    my_sentences = ["The quick brown fox", "Jumps over the lazy dog", "I saw the fox"]
    updated_sentences = delete_stopwords(my_sentences)
    assert updated_sentences == ["quick brown fox", "Jumps lazy dog", "saw fox"]
