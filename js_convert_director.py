from i_builder import IBuilder


class JSConvertDirector:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: IBuilder) -> None:
        self._builder = builder

    def build_classes(self, data: []) -> None:
        return self.builder.get_classes(data)

    def build_functions(self, data: []) -> None:
        return self.builder.get_functions(data)

    def build_attributes(self, data: []) -> None:
        return self.builder.get_attributes(data)

    def build_merged(self, data: []) -> None:
        return self.builder.merge(data)


