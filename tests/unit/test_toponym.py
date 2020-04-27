from toponym.recipes import Recipes
from toponym.toponym import concat_case_dictionaries
from toponym.toponym import get_longest_word_ending
from toponym.toponym import get_recipes_for_input_word
from toponym.toponym import merge_list_of_case_dictionaries
from toponym.toponym import Toponym


def test_get_longest_word_ending(test_recipes):
    word = "Testi"
    assert get_longest_word_ending(word, test_recipes) == "esti"


def test_get_recipe_for_input_word(test_recipes):
    input_word = "Testi"
    recipe = get_recipes_for_input_word(input_word=input_word, recipes=test_recipes)

    assert recipe


def test_merge_list_of_case_dictionaries():
    test_list_of_dict = [
        {"nominative": ["Beograd"], "genitive": ["Beograda"]},
        {"nominative": ["Beograf"], "genitive": ["Beografa"]},
    ]

    merged_dict = merge_list_of_case_dictionaries(
        list_of_case_dictionaries=test_list_of_dict
    )

    assert isinstance(merged_dict, dict)
    assert test_list_of_dict[0].keys() == merged_dict.keys()


def test_concat_case_dictionaries():
    merged_dict = {
        "nominative": [["Beograd"], ["Beograf"]],
        "genitive": [["Beograda"], ["Beografa"]],
    }

    concated_dict = concat_case_dictionaries(merged_dict)

    assert merged_dict.keys() == concated_dict.keys()
    assert all([isinstance(concated_dict.get(x)[0], str) for x in concated_dict])


def test_get_single_word_toponym(test_recipes):
    t = Toponym("Katzi", test_recipes)
    t.build()
    assert t.toponyms["nominative"] == ["Katzi"]
    assert t.toponyms["genitive"] == ["Katzo"]


def test_get_single_word_toponym_from_multi_word_recipe(test_recipes):
    t = Toponym("Testi", test_recipes)
    t.build()
    assert t.toponyms["nominative"] == ["Testi"]
    assert t.toponyms["genitive"] == ["Testo", "Testa"]


def test_get_multi_word_toponym_single_ending(test_recipes):
    t = Toponym("Katzi Katzo", test_recipes)
    t.build()
    assert t.toponyms["nominative"] == ["Katzi Katzo"]
    assert t.toponyms["genitive"] == ["Katzo Katza"]


def test_get_multi_word_toponym_multi_ending(test_recipes):
    t = Toponym("Testi Testi", test_recipes)
    t.build()
    assert t.toponyms["nominative"] == ["Testi Testi"]
    assert set(t.toponyms["genitive"]) == set(
        ["Testo Testo", "Testa Testa", "Testa Testo", "Testo Testa"]
    )


def test_get_multi_word_toponym_multi_ending_single_ending(test_recipes):
    t = Toponym("Testi Teto", test_recipes)
    t.build()
    assert t.toponyms["nominative"] == ["Testi Teto"]
    assert set(t.toponyms["genitive"]) == set(["Testo Teta", "Testa Teta"])


def test_get_multi_word_toponym_multi_ending_single_ending_revers(test_recipes):
    t = Toponym("Teto Testi", test_recipes)
    t.build()
    assert t.toponyms["nominative"] == ["Teto Testi"]
    assert set(t.toponyms["genitive"]) == set(["Teta Testo", "Teta Testa"])


def test_toponym_for_unknown_ending():
    recipes_russian = Recipes()
    recipes_russian.load_from_language(language="russian")

    input_word = ""

    t = Toponym(input_word, recipes_russian)
    t.build()
    assert t.toponyms["nominative"] == [""]


def test_toponym_multiword_unknown_ending_known_ending(test_recipes):
    input_word = "Testa Tesi"

    t = Toponym(input_word, test_recipes)
    t.build()
    assert t.toponyms["genitive"] == ["Testa Teso"]


def test_toponym_list_toponyms_multiword(test_recipes):
    input_word = "Testa Tesi"
    t = Toponym(input_word, test_recipes)
    t.build()
    assert isinstance(t.list_toponyms(), list)


def test_toponym_list_toponyms_singleword(test_recipes):
    input_word = "Tesi"
    t = Toponym(input_word, test_recipes)
    t.build()
    assert isinstance(t.list_toponyms(), list)
