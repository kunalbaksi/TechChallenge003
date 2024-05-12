import pytest
from get_nested_obj_value import get_nested_obj_value

@pytest.fixture
def test_object():
    return {"x": {"y": {"z": "a"}}}

def test_valid_object_and_key(test_object):
    test_key = "x/y/z"
    value = get_nested_obj_value(test_object, test_key)
    assert value == "a"

def test_invalid_object_and_valid_test_key():
    object = "not a dictionary"
    test_key = "x/y/z"
    with pytest.raises(ValueError):
        get_nested_obj_value(object, test_key)

def test_invalid_test_key(test_object):
    test_key = 123
    with pytest.raises(ValueError):
        get_nested_obj_value(test_object, test_key)

def test_empty_test_key(test_object):
    test_key = ""
    with pytest.raises(ValueError):
        get_nested_obj_value(test_object, test_key)