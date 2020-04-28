import csv
import json
import os
from os import path
from typing import Generator

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
    """Get recipes for a specific ISO_639_1 language code

    Attributes:
        language_code (str): ISO_639_1 language code

    Returns:
        recipes (dict): collection of recipes for input language
    """

    if language_code not in settings.LANGUAGE_DICT.values():
        raise LanguageNotFoundError(f"Language with code {language_code} not found")

    recipes_file_path = os.path.join(
        settings.RECIPES_DIR, "{}.json".format(language_code)
    )

    with open(recipes_file_path, "r", encoding="utf-8") as f:
        recipes = json.loads(f.read())

    return recipes


def get_recipes_from_dict(input_dict: dict) -> dict:
    """Get recipes from dict

    Attributes:
        input_dict (dict): ISO_639_1 language code

    Returns:
        recipes (dict): collection of recipes for input language
    """

    if not isinstance(input_dict, dict):
        raise TypeError("Input is not type dict")

    recipes = input_dict
    return recipes


def get_recipes_from_file(file_input: str) -> dict:
    """Get recipes from file

    Attributes:
        file_input (str): filepath

    Returns:
        recipes (dict): collection of recipes for input language
    """
    try:
        with open(file_input, "r") as file:
            recipes = json.loads(file.read())

    except FileNotFoundError:
        raise FileNotFoundError("File not found or not in os.getcwd()")

    return recipes


def is_consistent_recipes(filepath: str):
    """validate if recipes in /resources/*.json are valid

    Attributes:
        filepath (str): filepath

    Returns:
        bool
    """
    with open(filepath, "r", encoding="utf8") as f:
        recipes_check = json.loads(f.read())

    recipes_consistent = list()

    for word_ending in recipes_check:
        for case in recipes_check[word_ending]:
            if isinstance(recipes_check[word_ending][case][0], list):
                recipes_consistent.append(True)
            else:
                print(filepath, word_ending)
                recipes_consistent.append(False)

    if all([x for x in recipes_consistent]):
        return True


def is_json(myjson: dict):
    """ validate if input is json serializable

    Attributes:
        myjson (dict): input to validate

    Returns:
        bool
    """
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def lazy_load_csv(csvfile: str) -> Generator:
    with open(csvfile, "r") as f:
        r = csv.reader(f)
        for row in r:
            yield row


def file_exists(filename: str) -> bool:
    """Check if filename exists

        Argument:
                filename (str): filename to check
        Returns:
                bool
    """
    return path.exists(filename)
