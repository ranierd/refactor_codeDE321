from extraction_handler import ExtractionHandler
from converter_handler import ConverterHandler
from dot_handler import DotHandler


if __name__ == '__main__':

    extract = ExtractionHandler()
    convert = ConverterHandler()
    dot = DotHandler()

    extract.set_next_handler(convert.set_next_handler(dot))
