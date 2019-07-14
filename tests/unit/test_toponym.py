from toponym import toponym, topodict

td = {
    "i": {
        "nominative": ["", 0],
        "genitive": ["o", 1]
    },
    "ti": {
        "nominative": ["", 0],
        "genitive": ["o", 1]
    },
    "esti": {
        "nominative": ["", 0],
        "genitive": ["o", 1]
    }
}

td = topodict.Topodict(language='test', file=td)
td.load()

def test_get_longest_word_ending():
    tn = toponym.Toponym("Testi", td)
    assert tn._get_longest_word_ending() == "esti"
