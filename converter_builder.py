from i_builder import IBuilder
from js_convert import JSConvert


class ConverterBuilder(IBuilder):

    def __init__(self):
        self.converter = JSConvert()

    def set_classes(self, data: []):
        self.converter.set_classes = data

    def set_functions(self, data: [], classes: []):
        self.converter.set_functions = data

    def set_attributes(self, data: [], functions: []):
        self.converter.set_attributes = data
