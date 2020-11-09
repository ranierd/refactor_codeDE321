from extraction_handler import ExtractionHandler
from converter_handler import ConverterHandler
from create_dot_handler import CreateDotHandler


class CreationChain:
    """
    Chain where it starts with extraction and finishes with conversion
    """

    def __init__(self):
        self.extract = ExtractionHandler()
        self.convert = ConverterHandler()

        self.extract.set_next_handler(self.convert)
