import json
import os

from . import settings


def get_available_language_codes() -> str:
    """Returns a list of available languages and their 2 char input codes
    """
    recipes_filespaths = os.listdir(os.path.join(settings.RECIPES_DIR))
    ISO_639_1_code = [
        filepath.split(".")[0]
        for filepath in recipes_filespaths
        if filepath.endswith(".json")
    ]

    for code in ISO_639_1_code:
        if not code == "_test":
            assert len(code) == 2
    ISO_639_1_code.sort()
    return ISO_639_1_code


def get_language_code(language: str) -> str:

    try:
        return settings.LANGUAGE_DICT[language]
    except KeyError:
        raise KeyError(
            "{} not supported - check print_available_languages()".format(language)
        )


def print_available_languages() -> None:
    """Prints available languages with their full names
    """

    print("\nYour available languages are:")
    print("\nfull name\t\tiso code")
    for item in settings.LANGUAGE_DICT.items():
        print("  {}\t\t{}".format(item[0], item[1]))
    print()


def load_recipes(language_code: str) -> dict:
    """
    Loads language-specific stopwords for keyword selection
    """

    recipes_file_path = os.path.join(
        settings.RECIPES_DIR, "{}.json".format(language_code)
    )

    with open(recipes_file_path, "r", encoding="utf-8") as f:
        recipes_file = json.loads(f.read())
        return recipes_file
