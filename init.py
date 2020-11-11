from js_convert_director import JSConvertDirector
from js_convert_builder import JSConvertBuilder
from pathlib import Path

if __name__ == '__main__':
    director = JSConvertDirector()
    builder = JSConvertBuilder()
    director.builder = builder
    src_code = open((str(Path(__file__).parent.absolute().parent)+"\\resources\\16_game.js"))
    all_lines = src_code.readlines()

    director.build_classes(all_lines)
