from typing import Any
from abstract_handler import AbstractHandler
from handler import Handler


class ExtractionHandler(AbstractHandler):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: Handler):
        self.next_handler = handler

    def handle(self, request: Any) -> []:
        extract = Extractor()
        data = extract.get_data(request)
        if data:
            try:
                self.next_handler(data)
            except AssertionError as e:
                print(e)
