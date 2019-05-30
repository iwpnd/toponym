import os
import json

from . import settings
from .utils import (get_available_language_codes, print_available_languages, get_language_code, load_topodict)


class Topodict:
    """
    """

    def __init__(self, language, fp=False):
        self.language = language
        self.fp = fp
        self._loaded = False

    def __repr__(self):
        if self._loaded:
            return "Topodict(language='{language}', filepath='{fp}', loaded={i}, word_endings={we})".format(
                language=self.language,
                fp=self.fp,
                i=self._loaded,
                we=list(self._dict.keys())
            )
        else:
            return "Topodict(language='{language}', filepath='{fp}', loaded={i})".format(
                language=self.language,
                fp=self.fp,
                i=self._loaded
            )

    def __getitem__(self, word_ending):
        if not self._loaded:
            raise NameError("load topodict first")
        elif word_ending in self._dict.keys():
            return self._dict[word_ending]
        else:
            raise KeyError("{we} not in {language} topodict".format(
                we=word_ending,
                language=self.language
            )
            )

    def load(self):
        if not self.fp:
            _language_code = get_language_code(self.language)
            self._dict = load_topodict(_language_code)

            self._loaded = True
        
        else:
            with open(self.fp, 'r') as f:
                self._dict = json.loads(f.read())

            self._loaded = True
