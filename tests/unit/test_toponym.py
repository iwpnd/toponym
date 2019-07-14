from toponym import toponym, topodict

td = {
    "i": {
        "nominative": ["", 0],
        "genitive": ["o", 1]
    },
    "o": {
        "nominative": ["", 0],
        "genitive": ["a", 1]
    },
    "ti": {
        "nominative": ["", 0],
        "genitive": ["o", 1]
    },
    "esti": {
        "nominative": ["", 0],
        "genitive": [["o", "a"], 1]
    }
}

td = topodict.Topodict(language='test', file=td)
td.load()

def test_get_longest_word_ending():
    word = "Testi"
    tn = toponym.Toponym(word, td)
    assert tn._get_longest_word_ending(word) == "esti"


def test_all_cases_created():
    tn = toponym.Toponym("Testi", td)
    tn.build()
    assert tn.recipe.keys() == tn.topo.keys()


def test_get_single_word_toponym():
    tn = toponym.Toponym("Katzi", td)
    tn.build()
    assert tn.topo['nominative'] == 'Katzi'
    assert tn.topo['genitive'] == 'Katzo'


def test_get_single_word_toponym_from_multi_word_recipe():
    tn = toponym.Toponym("Testi", td)
    tn.build()
    assert tn.topo['nominative'] == 'Testi'
    assert tn.topo['genitive'] == ['Testo', 'Testa']


def test_get_multi_word_toponym_single_ending():
    tn = toponym.Toponym("Katzi Katzo", td)
    tn.build()
    assert tn.topo['nominative'] == 'Katzi Katzo'
    assert tn.topo['genitive'] == 'Katzo Katza'


