from toponym.recipes import Recipes
from toponym.toponym import get_longest_word_ending
from toponym.toponym import Toponym


def test_get_longest_word_ending(test_recipes):
    word = "Testi"
    assert get_longest_word_ending(word, test_recipes) == "esti"


def test_all_cases_created(test_recipes):
    toponym = Toponym("Testi", test_recipes)
    toponym.build()
    assert toponym.recipe.keys() == toponym.topo.keys()


def test_get_single_word_toponym(test_recipes):
    toponym = Toponym("Katzi", test_recipes)
    toponym.build()
    assert toponym.topo["nominative"] == ["Katzi"]
    assert toponym.topo["genitive"] == ["Katzo"]


def test_get_single_word_toponym_from_multi_word_recipe(test_recipes):
    toponym = Toponym("Testi", test_recipes)
    toponym.build()
    assert toponym.topo["nominative"] == ["Testi"]
    assert toponym.topo["genitive"] == ["Testo", "Testa"]


def test_get_multi_word_toponym_single_ending(test_recipes):
    toponym = Toponym("Katzi Katzo", test_recipes)
    toponym.build()
    assert toponym.topo["nominative"] == ["Katzi Katzo"]
    assert toponym.topo["genitive"] == ["Katzo Katza"]


def test_get_multi_word_toponym_multi_ending(test_recipes):
    toponym = Toponym("Testi Testi", test_recipes)
    toponym.build()
    assert toponym.topo["nominative"] == ["Testi Testi"]
    assert set(toponym.topo["genitive"]) == set(
        ["Testo Testo", "Testa Testa", "Testa Testo", "Testo Testa"]
    )


def test_get_multi_word_toponym_multi_ending_single_ending(test_recipes):
    toponym = Toponym("Testi Teto", test_recipes)
    toponym.build()
    assert toponym.topo["nominative"] == ["Testi Teto"]
    assert set(toponym.topo["genitive"]) == set(["Testo Teta", "Testa Teta"])


def test_get_multi_word_toponym_multi_ending_single_ending_revers(test_recipes):
    toponym = Toponym("Teto Testi", test_recipes)
    toponym.build()
    assert toponym.topo["nominative"] == ["Teto Testi"]
    assert set(toponym.topo["genitive"]) == set(["Teta Testo", "Teta Testa"])


def test_toponym_for_unknown_ending():
    recipes_russian = Recipes(language="russian")
    recipes_russian.load()

    input_word = ""

    toponym = Toponym(input_word, recipes_russian)
    toponym.build()
    assert toponym.topo["nominative"] == [""]


def test_toponym_multiword_unknown_ending_known_ending(test_recipes):
    input_word = "Testa Tesi"

    toponym = Toponym(input_word, test_recipes)
    toponym.build()
    assert toponym.topo["genitive"] == ["Testa Teso"]


def test_toponym_list_toponyms_multiword(test_recipes):
    input_word = "Testa Tesi"
    toponym = Toponym(input_word, test_recipes)
    toponym.build()
    assert isinstance(toponym.list_toponyms(), list)


def test_toponym_list_toponyms_singleword(test_recipes):
    input_word = "Tesi"
    toponym = Toponym(input_word, test_recipes)
    toponym.build()
    assert isinstance(toponym.list_toponyms(), list)
