from toponym import topodict
from toponym import toponym

topodictionary = {
    "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
    "i": {"nominative": [[""], 0], "genitive": [["o"], 1]},
    "o": {"nominative": [[""], 0], "genitive": [["a"], 1]},
    "ti": {"nominative": [[""], 0], "genitive": [["o"], 1]},
    "esti": {"nominative": [[""], 0], "genitive": [["o", "a"], 1]},
}

td = topodict.Topodict(language="test", file=topodictionary)
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
    assert tn.topo["nominative"] == ["Katzi"]
    assert tn.topo["genitive"] == ["Katzo"]


def test_get_single_word_toponym_from_multi_word_recipe():
    tn = toponym.Toponym("Testi", td)
    tn.build()
    assert tn.topo["nominative"] == ["Testi"]
    assert tn.topo["genitive"] == ["Testo", "Testa"]


def test_get_multi_word_toponym_single_ending():
    tn = toponym.Toponym("Katzi Katzo", td)
    tn.build()
    assert tn.topo["nominative"] == ["Katzi Katzo"]
    assert tn.topo["genitive"] == ["Katzo Katza"]


def test_get_multi_word_toponym_multi_ending():
    tn = toponym.Toponym("Testi Testi", td)
    tn.build()
    assert tn.topo["nominative"] == ["Testi Testi"]
    assert set(tn.topo["genitive"]) == set(
        ["Testo Testo", "Testa Testa", "Testa Testo", "Testo Testa"]
    )


def test_get_multi_word_toponym_multi_ending_single_ending():
    tn = toponym.Toponym("Testi Teto", td)
    tn.build()
    assert tn.topo["nominative"] == ["Testi Teto"]
    assert set(tn.topo["genitive"]) == set(["Testo Teta", "Testa Teta"])


def test_get_multi_word_toponym_multi_ending_single_ending_revers():
    tn = toponym.Toponym("Teto Testi", td)
    tn.build()
    assert tn.topo["nominative"] == ["Teto Testi"]
    assert set(tn.topo["genitive"]) == set(["Teta Testo", "Teta Testa"])


def test_toponym_for_unknown_ending():
    td = topodict.Topodict(language="russian")
    td.load()

    word = ""

    tn = toponym.Toponym(word, td)
    tn.build()
    assert tn.topo["nominative"] == [""]


def test_toponym_multiword_unknown_ending_known_ending():
    word = "Testa Tesi"

    tn = toponym.Toponym(word, td)
    tn.build()
    assert tn.topo["genitive"] == ["Testa Teso"]


def test_toponym_list_toponyms_multiword():
    word = "Testa Tesi"
    tn = toponym.Toponym(word, td)
    tn.build()
    assert isinstance(tn.list_toponyms(), list)


def test_toponym_list_toponyms_singleword():
    word = "Tesi"
    tn = toponym.Toponym(word, td)
    tn.build()
    assert isinstance(tn.list_toponyms(), list)
