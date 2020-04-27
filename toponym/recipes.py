from typing import Union

from loguru import logger

from .utils import get_language_code
from .utils import get_recipes
from .utils import get_recipes_from_dict
from .utils import get_recipes_from_file


class Recipes:
    """Loads and provides access to recipes

    Load Recipes from either file, dictionary or from stored default Recipes

    Attributes:
        language (str): language the recipe is for
        file (Union[bool, str, dict]): if str load from file, if dict load from dict, defaults to bool
    """

    def __init__(self, language: str, file: Union[bool, dict, str] = False) -> None:
        self.language = language
        self.file = file
        self.is_loaded = False

    def __getitem__(self, word_ending: str) -> dict:
        if not self.is_loaded:
            raise NameError("load recipes first")
        elif word_ending in self._dict.keys():
            return self._dict[word_ending]
        elif not word_ending:
            logger.warning("No word_ending found. Using _default")
            return self._dict["_default"]

    def __repr__(self) -> str:
        if self.is_loaded:
            return f"Recipes(language='{self.language}', filepath='{self.file}', is_loaded={self.is_loaded}, word_endings={list(self._dict.keys())})"

    def load(self) -> None:
        if not self.file:
            self._language_code = get_language_code(language=self.language)
            self._dict = get_recipes(language_code=self._language_code)
            logger.info(f"Recipes loaded for {self.language}")

        else:
            if isinstance(self.file, dict):
                self._dict = get_recipes_from_dict(input_dict=self.file)

                logger.info(
                    f"Recipes loaded from dictionary for language {self.language}"
                )

            elif isinstance(self.file, str):
                self._dict = get_recipes_from_file(file_input=self.file)
                logger.info(
                    f"Recipes loaded from file ({self.file}) for language {self.language}"
                )

            else:
                raise TypeError("Input file can either be filepath or dictionary")

        self.is_loaded = True
