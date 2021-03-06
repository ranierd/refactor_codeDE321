from pathlib import Path


class Dot:

    def __init__(self):
        self.home_directory = str(Path(__file__).parent.absolute().parent)

    def create_dot(self, data: []) -> object:
        try:
            assert data is not None
        except (AssertionError, TypeError) as e:
            print(e)
            return
        obj_number = 0
        all_lines = ["digraph \"classes\"{\n", "charset=\"utf-8\"\n", "rankdir=BT\n"]
        for i in range(len(data)):
            line = "\"" + str(obj_number) + "\"" + "[label=\"{" + data[obj_number][0] + "|"
            for att in data[obj_number][2]:
                line += att + "\\l"
            line += "|"
            for function in data[obj_number][1]:
                line += function + "\\l"
            line += "}\", shape=\"record\"];\n"
            all_lines.append(line)
            obj_number += 1
        all_lines.append("}")
        dot_file = open(self.home_directory + "\\resources\\JSClasses.dot", "w")
        if dot_file:
            result = ""
            for attributes in all_lines:
                dot_file.write(attributes)
                result += attributes
        dot_file.close()
        return result
