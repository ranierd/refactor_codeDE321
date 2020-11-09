from typing import Any
from abstract_handler import AbstractHandler
from js_convert import JSConvert


class ConverterHandler(AbstractHandler):

    def handle(self, request: Any) -> []:
        if request:
            js_builder = JSConvert()
            classes = js_builder.get_classes(request)
            functions = js_builder.get_functions(request)
            attributes = js_builder.get_attributes(request)
            if classes and functions and attributes:
                try:
                    super().handle(js_builder.merge(request))
                except (AssertionError, TypeError, AttributeError) as e:
                    print(e)
