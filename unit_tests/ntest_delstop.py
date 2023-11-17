import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
import delstop

def test_delete_stop():
    my_sentences = ["The quick brown fox", "Jumps over the lazy dog", "I saw the fox"]
    updated_sentences = delstop(my_sentences)
    assert updated_sentences == ["quick brown fox", "Jumps lazy dog", "saw fox"]
