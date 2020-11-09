from itertools import cycle
from re import findall, search
from i_builder import IBuilder


class JSConvert(IBuilder):

    def get_classes(self, data: []):
        classes = []
        try:
            for line in data:
                result = search("class .* {", line)
                if result:
                    classes.append(findall(r'class (\S+).*{', line))
            return classes
        except (AssertionError, FileNotFoundError, PermissionError, AttributeError) as e:
            print(e)

    def get_functions(self, data: []):
        functions = []
        try:
            for line in data:
                current_level = findall(r'(\S+)[(].*[)].*{', line)
                if current_level:
                    functions.append(current_level[0] + "()")
            return functions
        except (AssertionError, TypeError, AttributeError, IndexError) as e:
            print(e)

    def get_attributes(self, data: []):
        attributes = []
        try:
            for line in data:
                attribute = findall(r'this\.(\S+)', line)
                if attribute:
                    attributes.append(attribute)
            return attributes
        except (AssertionError, TypeError, AttributeError) as e:
            print(e)

    def merge(self, data: []):
        classes = []
        functions = []
        attributes = []
        in_class = False
        in_function = False
        bracket_count = 0
        current_class = ""
        for line in data:
            if (not in_class) & (current_class == ""):
                result = search("class .* {", line)
                if result is not None:
                    current_class = findall(r'class (\S+).*{', line)
                    in_class = True
            elif in_class:
                if in_function:
                    r = findall('{', line)
                    if len(r) > 0:
                        bracket_count += len(r)
                    r = findall('}', line)
                    if r:
                        if bracket_count > 0:
                            bracket_count -= len(r)
                        if bracket_count == 0:
                            in_function = False
                            continue
                elif not in_function:
                    result = search(r'\S(.*).*{', line)
                    if result is not None:
                        current_level = findall(r'(\S+)[(].*[)].*{', line)
                        functions.append(current_level[0] + "()")
                        in_function = True
                        continue
                    elif findall('}', line):
                        in_class = False
                        classes.append(tuple([current_class[0], tuple(functions), tuple(attributes)]))
                        attributes.clear()
                        functions.clear()
                        current_class = ""
                attribute = findall(r'this\.(\S+)', line)
                if attribute:
                    attributes.append(attribute[0])
        return classes

