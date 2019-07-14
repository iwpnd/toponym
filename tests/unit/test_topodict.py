from toponym import topodict, utils

def test_topodict_load():
    """test load
    """
    tp = topodict.Topodict('russian')
    tp.load()
    assert tp._loaded
