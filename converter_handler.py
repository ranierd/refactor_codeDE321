from typing import Any
from abstract_handler import AbstractHandler
from converter import Converter
from handler import Handler


class ConverterHandler(AbstractHandler):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: Handler) -> []:
        self.next_handler = handler

    def handle(self, request: Any) -> []:
        classes = get_class(request)
        functions = get_function(classes)
        attributes = get_attributes(functions)
        formatted =  classes, functions, attributes
        if data:
            try:
                self.next_handler(data)
            except AssertionError as e:
                print(e)
