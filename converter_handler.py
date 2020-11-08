from typing import Any
from abstract_handler import AbstractHandler
from handler import Handler


class ConverterHandler(AbstractHandler):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: Handler) -> []:
        self.next_handler = handler

    def handle(self, request: Any) -> []:
        conversion = Converter()
        assert (request is not None)
        assert request != ''
        with open(request, 'r') as src_code:
            all_lines = src_code.readlines()
        data = conversion.convert(all_lines)
        if data:
            try:
                self.next_handler(data)
            except AssertionError as e:
                print(e)
