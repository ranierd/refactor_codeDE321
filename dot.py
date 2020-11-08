from pathlib import Path


class Dot():

    def __init__(self):
        self.result = ""
        self._home_directory = str(Path(__file__).parent.absolute().parent)
        self.default_path = self._home_directory + "\\resources\\JSclasses.dot"
        self.classes = None

    def create_dot(self, classes, out_path):
        assert classes is not None, "There must be an object to \
work with, please use \"convert_js_file\" to create one"
        obj_number = 0
        all_Lines = []
        all_Lines.append("digraph \"classes\"{\n")
        all_Lines.append("charset=\"utf-8\"\n")
        all_Lines.append("rankdir=BT\n")
        for i in range(len(classes)):
            line = "\"" + str(obj_number) + "\"" + "[label=\"{\
" + classes[obj_number][0] + "|"
            for att in classes[obj_number][2]:
                line += att + "\\l"
            line += "|"
            for function in classes[obj_number][1]:
                line += function + "\\l"
            line += "}\", shape=\"record\"];\n"
            all_Lines.append(line)
            obj_number += 1
        all_Lines.append("}")
        # for line in all_Lines:
        #     print(line)
        with open(out_path, 'w') as dot_file:
            for li in all_Lines:
                dot_file.write(li)
                self.result += li
