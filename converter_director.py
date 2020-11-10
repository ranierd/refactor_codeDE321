from i_builder import IBuilder
from js_convert import JSConvert


class ConverterDirector:

    def __init__(self) -> None:
        self.builder = None

    @property
    def builder(self) -> IBuilder:
        return self.builder

    @builder.setter
    def builder(self, builder: IBuilder) -> None:
        self.builder = builder

    def build_classes(self, data: []) -> None:
        return self.builder.get_classes(data)

    def build_functions(self, data: []) -> None:
        return self.builder.get_functions(data)

    def build_attributes(self, data: []) -> None:
        return self.builder.get_attributes(data)

    def build_merged(self, data: []) -> None:
        return self.builder.merge(data)


