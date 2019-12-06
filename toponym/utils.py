import os
import json
import logging

from . import settings
import logging

logger = logging.getLogger(__name__)


def get_available_language_codes():
    """Returns a list of available languages and their 2 char input codes
    """
    topodict_files = os.listdir(os.path.join(settings.TOPODICT_DIR))
    two_dig_codes = [f.split('.')[0] for f in topodict_files if f.endswith(".json")]
    for d in two_dig_codes:
        if not d == "_test":
            assert len(d) == 2
    two_dig_codes.sort()
    return two_dig_codes


def get_language_code(language):
    
    try:
        return settings.LANGUAGE_DICT[language]
    except KeyError:
        raise KeyError("{} not supported - check print_available_languages()".format(
            language
        ))


def print_available_languages():
    """Prints available languages with their full names
    """

    print("\nYour available languages are:")
    print("\nfull name\t\tiso code")
    for item in settings.LANGUAGE_DICT.items():
        print("  {}\t\t{}".format(item[0],item[1]))
    print()


def load_topodict(language_code):
    """ 
    Loads language-specific stopwords for keyword selection
    """

    topodictFile = os.path.join(settings.TOPODICT_DIR,
                                  '{}.json'.format(language_code))

    with open(topodictFile, 'r', encoding='utf-8') as f:
        tdict = json.loads(f.read())
        return tdict
