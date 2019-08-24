from toponym import utils

def test_get_available_languages():
    """get avalable languages as ISO 639-1
    """

    lg = utils.get_available_language_codes()
    assert lg
