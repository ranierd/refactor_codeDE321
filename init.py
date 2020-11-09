from extraction_handler import ExtractionHandler
from converter_handler import ConverterHandler
from dot_handler import DotHandler
from handler import Handler


def client_code(handler: Handler) -> None:
    data = "C:\\Users\\Ranier\\Downloads\\python-assignment-master\\resources\\16_game.js"
    result = handler.handle(data)
    print(result)


if __name__ == '__main__':

    extract = ExtractionHandler()
    convert = ConverterHandler()
    dot = DotHandler()

    extract.set_next_handler(convert)

    client_code(extract)


