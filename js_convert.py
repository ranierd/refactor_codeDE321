from re import findall, search


class JSConvert:

    def get_classes(self, data: []):
        classes = []
        try:
            for line in data:
                result = search("class .* {", line)
                if result:
                    classes.append(findall(r'class .* {', line))
            print(classes)
        except (AssertionError, FileNotFoundError, PermissionError, AttributeError) as e:
            print(e)

    def get_functions(self, classes: [], data: []):
        bracket_count = 0
        i = 0
        for line in data:
            try:
                if classes[i]:
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
                    elif not in_function:
                        self.functions = search(r'\S(.*).*{', line)
                        if self.functions:
                            current_level = findall(r'(\S+)[(].*[)].*{', line)
                            self.functions.append(current_level[0] + "()")
                            i += 1
                return self.functions
            except (AssertionError, TypeError, AttributeError) as e:
                print(e)

    def get_attributes(self, functions: [], data: []):
        i = 0
        for line in data:
            try:
                if functions[i]:
                    return self.attributes.append(findall(r'this\.(\S+)', line))
            except (AssertionError, TypeError, AttributeError) as e:
                print(e)

    #def formatted(self, classes: [], functions: [], attributes []):


if __name__ == '__main__':
    src_code = open("C:\\Users\\Ranier\\Downloads\\python-assignment-master\\resources\\16_game.js")
    all_lines = src_code.readlines()
    js = JSConvert
    js.get_classes(all_lines, all_lines)
    src_code.close()