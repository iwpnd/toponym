import json

from loguru import logger

from .utils import get_language_code
from .utils import get_recipes
from .utils import get_recipes_from_dict


class Recipes:
    """Loads and provides access to recipes
    """

    def __init__(self, language: str, file: bool = False) -> None:
        self.language = language
        self.file = file
        self.is_loaded = False

    def __getitem__(self, word_ending: str) -> str:
        if not self.is_loaded:
            raise NameError("load recipes first")
        elif word_ending in self._dict.keys():
            return self._dict[word_ending]
        elif not word_ending:
            logger.warning("No word_ending found. Using _default")
            return self._dict["_default"]

    def load(self) -> None:
        if not self.file:
            self._language_code = get_language_code(self.language)
            self._dict = get_recipes(self._language_code)
            self.is_loaded = True
            logger.info(f"Recipes loaded for {self.language}")

        else:
            if isinstance(self.file, dict):
                self._dict, self.is_loaded = get_recipes_from_dict(input_dict=self.file)

                logger.info(
                    f"Recipes loaded from dictionary for language {self.language}"
                )

            elif isinstance(self.file, str):
                try:
                    with open(self.file, "r") as f:
                        self._dict = json.loads(f.read())
                        self.is_loaded = True
                        logger.info(
                            f"Recipes loaded from file ({self.file}) for language {self.language}"
                        )

                except FileNotFoundError:
                    raise FileNotFoundError("File not found or not in os.getcwd()")

            else:
                raise TypeError("Input file can either be filepath or dictionary")
