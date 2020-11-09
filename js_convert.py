from re import findall, search


class JSConvert:

    def get_classes(self, data: []):
        classes = []
        try:
            for line in data:
                result = search("class .* {", line)
                if result:
                    classes.append(findall(r'class .* {', line))
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
            print(attributes)
        except (AssertionError, TypeError, AttributeError) as e:
            print(e)



if __name__ == '__main__':
    src_code = open("H:\\Ranier and Daniels python-assignment-2\\resources\\16_game.js")
    all_lines = src_code.readlines()
    js = JSConvert
    js.get_classes(all_lines, all_lines)
    js.get_functions(all_lines, all_lines)
    js.get_attributes(all_lines,all_lines)
    src_code.close()
