class JSConvert:
    """Used by the builder so that when a director uses a builder it has"""
    def __init__(self):
        self.classes = []

    def add(self, data: []):
        return self.classes.append(data)


