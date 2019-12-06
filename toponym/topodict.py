import os
import json
from . import settings
from .utils import (
    get_available_language_codes,
    print_available_languages,
    get_language_code,
    load_topodict
)

import logging

logger = logging.getLogger(__name__)


class Topodict:
    """Loads and provides access to recipes
    """

    def __init__(self, language, file=False):
        self.language = language
        self.file = file
        self._loaded = False


    def __repr__(self):
        if self._loaded:
            return "Topodict(language='{language}', filepath='{file}', loaded={i}, word_endings={we})".format(
                language=self.language,
                file=self.file,
                i=self._loaded,
                we=list(self._dict.keys())
            )
        else:
            return "Topodict(language='{language}', filepath='{file}', loaded={i})".format(
                language=self.language,
                file=self.file,
                i=self._loaded
            )


    def __getitem__(self, word_ending):
        if not self._loaded:
            raise NameError("load topodict first")
        elif word_ending in self._dict.keys():
            return self._dict[word_ending]
        elif not word_ending:
            logger.warning("No word_ending found. Using _default")
            return self._dict["_default"]


    def load(self):
        if not self.file:
            self._language_code = get_language_code(self.language)
            self._dict = load_topodict(self._language_code)
            self._loaded = True
            logger.info("Topodictionary loaded for {}".format(self.language))

        else:
            if isinstance(self.file, dict):
                self._dict = self.file
                self._loaded = True
                logger.info("Topodictionary loaded from dictionary for language {}".format(
                    self.language))

            elif isinstance(self.file, str):
                try:
                    with open(self.file, 'r') as f:
                        self._dict = json.loads(f.read())
                        self._loaded = True
                        logger.info("Topodictionary loaded from file ({}) for language {}".format(
                            self.file,
                            self.language))
                except FileNotFoundError:
                    raise FileNotFoundError(
                        "File not found or not in os.getcwd()")

            else:
                raise TypeError(
                    "Input file can either be filepath or dictionary")
