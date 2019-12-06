from toponym import topodict
import pytest

def test_topodict_load_success_russian():
    """test load
    """

    tp = topodict.Topodict('russian')
    tp.load()

    assert tp._loaded


def test_topodict_load_success_croatian():
    """test load
    """

    tp = topodict.Topodict('croatian')
    tp.load()

    assert tp._loaded


def test_topodict_load_success_ukrainian():
    """test load
    """

    tp = topodict.Topodict('ukrainian')
    tp.load()

    assert tp._loaded


def test_topodict_load_success_romanian():
    """test load
    """

    tp = topodict.Topodict('romanian')
    tp.load()

    assert tp._loaded


def test_topodict_load_success_latvian():
    """test load
    """

    tp = topodict.Topodict('latvian')
    tp.load()

    assert tp._loaded


def test_topodict_load_failed_language_not_supported():
    """test load
    """

    with pytest.raises(KeyError):
        tp = topodict.Topodict('german')
        tp.load()


def test_topodict_load_with_input_dictionary():
    
    td = {
        "_default": {
            "nominative": [[""], 0],
            "genitive": [[""], 0]
        },
        "i": {
            "nominative": ["", 0],
            "genitive": ["o", 1]
        }
    }

    t = topodict.Topodict(language='test', file=td)
    t.load()

    assert t._dict


def test_topodict_load_with_input_filepath_fails():
    with pytest.raises(TypeError):
        t = topodict.Topodict(language='test', file=123)
        t.load()


    with pytest.raises(FileNotFoundError):
        t = topodict.Topodict(language='test', file="test")
        t.load()


    with pytest.raises(TypeError):
        t = topodict.Topodict(language='test', file=[1,2,3])
        t.load()


def test_topodict_load_file():
    t = topodict.Topodict(language='test', file='./toponym/resources/_test.json')
    t.load()

    assert t._loaded