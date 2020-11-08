def test_converter_with_bad_input(self):
    c = Converter()
    expected = "Error"
    try:
        actual = c.convert('badfilepath')
    except AssertionError:
        actual = "Error"
    self.assertEqual(expected, actual)


def test_extraction_no_input(self):
    e = Extractor()
    expected = "Error"
    try:
        actual = e.getData()
    except AssertionError:
        actual = "Error"
    self.assertEqual(expected, actual)


def test_extraction_blank_input(self):
    e = Extractor()
    expected = "Error"
    try:
        actual = e.getData('')
    except AssertionError:
        actual = "Error"
    self.assertEqual(expected, actual)


def test_extraction(self):
    from pathlib import Path
    e = Extractor()
    expected = ['\
from i_pretty_print import IPretty_print\n', '\
\n', '\
\n', '\
class Uml(IPretty_print):\n', '\
\n', '\
    def __init__(self):\n', '\
        pass\n', '\
\n', '\
    def create_uml_file(self, dot_exe, source_file_path, image_path):\n', '\
        from subprocess import call as sub_call\n', "\
        call = [dot_exe] + [source_file_path] + ['-Tpng'] +\
 ['-o' + image_path]\n", '\
        sub_call(call)\n']
    actual = e.getData(str(Path(__file__).parent.absolute()) + "\\uml.py")
    print(actual)
    self.assertEqual(expected, actual)