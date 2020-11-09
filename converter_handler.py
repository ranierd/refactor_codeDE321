from typing import Any
from abstract_handler import AbstractHandler
from handler import Handler
from js_convert import JSConvert


class ConverterHandler(AbstractHandler):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: Handler) -> []:
        self.next_handler = handler

    def handle(self, request: Any) -> []:
        js_convert = JSConvert
        classes = js_convert.get_class(request)
        functions = js_convert.get_function(classes, request)
        attributes = js_convert.get_attributes(functions, request)
        formatted = classes, functions, attributes
        if formatted:
            try:
                self.next_handler(formatted)
            except AssertionError as e:
                print(e)
