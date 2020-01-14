from toponym import topodict, settings
import pytest
import json
import os


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


def test_topodict_load_success_russian():
    """test load
    """

    tp = topodict.Topodict("russian")
    tp.load()

    assert tp._loaded


def test_topodict_load_success_croatian():
    """test load
    """

    tp = topodict.Topodict("croatian")
    tp.load()

    assert tp._loaded


def test_topodict_load_success_ukrainian():
    """test load
    """

    tp = topodict.Topodict("ukrainian")
    tp.load()

    assert tp._loaded


def test_topodict_load_success_romanian():
    """test load
    """

    tp = topodict.Topodict("romanian")
    tp.load()

    assert tp._loaded


def test_topodict_load_success_latvian():
    """test load
    """

    tp = topodict.Topodict("latvian")
    tp.load()

    assert tp._loaded


def test_topodict_load_success_hungarian():
    """test load
    """

    tp = topodict.Topodict("hungarian")
    tp.load()

    assert tp._loaded


def test_topodict_load_success_greek():
    """test load
    """

    tp = topodict.Topodict("greek")
    tp.load()

    assert tp._loaded


def test_topodict_load_failed_language_not_supported():
    """test load
    """

    with pytest.raises(KeyError):
        tp = topodict.Topodict("german")
        tp.load()


def test_topodict_load_with_input_dictionary():

    td = {
        "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
        "i": {"nominative": ["", 0], "genitive": ["o", 1]},
    }

    t = topodict.Topodict(language="test", file=td)
    t.load()

    assert t._dict


def test_topodict_load_with_input_filepath_fails():
    with pytest.raises(TypeError):
        t = topodict.Topodict(language="test", file=123)
        t.load()

    with pytest.raises(FileNotFoundError):
        t = topodict.Topodict(language="test", file="test")
        t.load()

    with pytest.raises(TypeError):
        t = topodict.Topodict(language="test", file=[1, 2, 3])
        t.load()


def test_topodict_load_file():
    t = topodict.Topodict(language="test", file="./toponym/resources/_test.json")
    t.load()

    assert t._loaded


def test_topodict_consistency():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

    def _is_consistent_topodict(filepath):
        with open(filepath, "r", encoding="utf8") as f:
            topodict_check = json.loads(f.read())

        topodict_consistent = list()

        for ending in topodict_check:
            for case in topodict_check[ending]:
                if isinstance(topodict_check[ending][case][0], list):
                    topodict_consistent.append(True)
                else:
                    print(filepath, ending)
                    topodict_consistent.append(False)

        if all([x for x in topodict_consistent]):
            return True
        else:
            return False

    assert all([_is_consistent_topodict(tdict) for tdict in filepaths])


def test_topodict_valid_json():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

    for filepath in filepaths:
        with open(filepath, "r", encoding="utf8") as f:
            assert is_json(f.read())


def test_topodict_default_in_json():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

    for filepath in filepaths:
        with open(filepath, "r", encoding="utf8") as f:
            topodict_check = json.loads(f.read())
            assert isinstance(topodict_check, dict)
            assert "_default" in topodict_check
