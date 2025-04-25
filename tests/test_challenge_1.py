from activity.challenge_1 import uncommon_from_sentences
from .contains_all import contains_all
import pytest

# tests
# @pytest.maßrk.skip("comment this skip out for challenge 1")
def test_gets_unique_words():
    expected = ["sweet", "sour"]
    sentences = [
        "this apple is sweet",
        "this apple is sour",
    ]
    result = uncommon_from_sentences(sentences)
    assert len(expected) == len(result)
    assert contains_all(expected, result)

# @pytest.mark.skip("comment this skip out for challenge 1")
def test_disallow_repeat_in_same_sentence():
    expected = ["banana"]
    sentences = [
        "apple apple",
        "banana",
    ]
    result = uncommon_from_sentences(sentences)
    assert len(expected) == len(result)
    assert contains_all(expected, result)
    
# @pytest.mark.skip("comment this skip out for challenge 1")
def test_gets_unique_words_from_three_sentences():
    expected = ["tulips", "have", "thorns"]
    sentences = [
        "tiptoe through the tulips",
        "tiptoe through the roses",
        "roses have thorns",
    ]
    result = uncommon_from_sentences(sentences)
    assert len(expected) == len(result)
    assert contains_all(expected, result)
    