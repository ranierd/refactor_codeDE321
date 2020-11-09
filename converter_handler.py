from typing import Any
from abstract_handler import AbstractHandler
from js_convert import JSConvert



class ConverterHandler(AbstractHandler):

    def handle(self, request: Any) -> []:
        js_builder = JSConvert()
        if request:
            print(js_builder.merge(request))
        else:
            try:
                super().handle(js_builder.merge(request))
            except (AssertionError, TypeError, AttributeError) as e:
                print(e)
