from loguru import logger


class Topodict:
    """Loads and provides access to recipes
    """

    def __init__(self, language: str, file=False) -> None:
        self.language = language
        self.file = file
        self._loaded = False
        logger.warning("Topodict is deprecated. Use Recipes instead.")
