from loguru import logger

from .utils import get_language_code
from .utils import get_recipes
from .utils import get_recipes_from_dict
from .utils import get_recipes_from_file


class Recipes:
    """Loads and provides access to recipes

    Load Recipes from either file, dictionary or from stored
     default Recipes

    Attributes:
        language (str): language the recipe is for
        file (Union[bool, str, dict]): if str load from
             file, if dict load from dict, defaults to bool
    """

    def __init__(self) -> None:
        self.is_loaded = False

    def __getitem__(self, word_ending: str) -> dict:
        if not self.is_loaded:
            raise NameError("load recipes first")
        elif word_ending in self._dict.keys():
            return self._dict[word_ending]
        elif not word_ending:
            logger.warning("No word_ending found. Using _default")
            return self._dict["_default"]

    def load_from_file(self, language: str, filepath: str) -> None:
        if isinstance(filepath, str):
            self._dict = get_recipes_from_file(file_input=filepath)
            logger.info(
                f"Recipes loaded from file ({filepath}) for language {language}"
            )

            self.is_loaded = True

        else:
            raise TypeError("Input file can either be filepath or dictionary")

    def load_from_dict(self, language: str, input_dict: str) -> None:
        self._dict = get_recipes_from_dict(input_dict=input_dict)

        logger.info(f"Recipes loaded from dictionary for language {language}")

        self.is_loaded = True

    def load_from_language(self, language: str) -> None:
        self._language_code = get_language_code(language=language)
        self._dict = get_recipes(language_code=self._language_code)
        logger.info(f"Recipes loaded for {language}")
        self.is_loaded = True
