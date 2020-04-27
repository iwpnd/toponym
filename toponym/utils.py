import json
import os
from typing import Tuple

from . import settings


class LanguageNotFoundError(Exception):
    pass


def get_available_language_codes() -> list:
    """Get available/supported language codes

    Return
        ISO_639_1_codes (list): all available/supported languages
    """
    recipes_filespaths = os.listdir(os.path.join(settings.RECIPES_DIR))
    ISO_639_1_codes = [
        filepath.split(".")[0]
        for filepath in recipes_filespaths
        if filepath.endswith(".json")
    ]

    for code in ISO_639_1_codes:
        if not code == "_test":
            assert len(code) == 2
    ISO_639_1_codes.sort()

    return ISO_639_1_codes


def get_language_code(language: str) -> str:
    """Get a single ISO_639_1 language code

    Attributes:
        language (str): language to get a code for

    Return
        ISO_639_1_codes (list): all available/supported languages
    """

    if language not in settings.LANGUAGE_DICT.keys():
        raise LanguageNotFoundError(f"Language '{language}' not found")

    return settings.LANGUAGE_DICT[language]


def print_available_languages() -> None:
    """Prints available languages with their full names
    """

    print("\nYour available languages are:")
    print("\nfull name\t\tiso code")
    for item in settings.LANGUAGE_DICT.items():
        print("  {}\t\t{}".format(item[0], item[1]))
    print()


def get_recipes(language_code: str) -> dict:
    """Get a recipes for a specific ISO_639_1 language code

    Attributes:
        language_code (str): ISO_639_1 language code

    Returns:

    """

    if language_code not in settings.LANGUAGE_DICT.values():
        raise LanguageNotFoundError(f"Language with code {language_code} not found")

    recipes_file_path = os.path.join(
        settings.RECIPES_DIR, "{}.json".format(language_code)
    )

    with open(recipes_file_path, "r", encoding="utf-8") as f:
        recipes = json.loads(f.read())

    return recipes


def get_recipes_from_dict(input_dict: dict) -> Tuple[dict, bool]:
    recipes = input_dict

    return recipes


def get_recipes_from_file(file_input: str):
    try:
        with open(file_input, "r") as file:
            recipes = json.loads(file.read())

    except FileNotFoundError:
        raise FileNotFoundError("File not found or not in os.getcwd()")

    return recipes
