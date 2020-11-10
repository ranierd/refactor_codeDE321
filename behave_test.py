from unittest import TestCase
from extraction_handler import ExtractionHandler
from converter_handler import ConverterHandler
from dot_handler import DotHandler
from dot import Dot
from js_convert import JSConvert
from converter_director import Director


class TestCases(TestCase):

    def setup(self):
        return "C:\\Users\\Ranier\\Downloads\\python-assignment-master\\resources\\16_game.js"

    @staticmethod
    def tear_down():
        print('Closing Tests')

    def test_handlers(self):
        extract = ExtractionHandler()
        convert = ConverterHandler()
        dot = DotHandler()
        expected = extract.set_next_handler(convert).set_next_handler(dot)
        try:
            actual = extract.set_next_handler(convert).set_next_handler(dot)
        except (TypeError, AttributeError) as e:
            print(str(actual))
        self.assertEqual(expected, actual)

    def test_director_classes(self):
        director = Director()
        builder = JSConvert()
        director.builder = builder
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = director.builder.get_classes(all_lines)
        actual = builder.get_classes(all_lines)
        src_code.close()
        self.assertEqual(expected, actual)

    def test_classes(self):
        js_converter = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = [['Level'], ['State'], ['Vec'], ['Player'], ['Lava'], ['Coin'], ['DOMDisplay']]
        actual = js_converter.get_classes(all_lines)
        src_code.close()
        self.assertEqual(expected, actual)
    
    def test_no_classes(self):
        js_converter = JSConvert()
        expected = []
        actual = js_converter.get_classes([])
        self.assertEqual(expected, actual)

    def test_error_classes(self):
        js_converter = JSConvert()
        expected = None
        actual = js_converter.get_classes([])
        self.assertEqual(expected, actual)

    def test_functions(self):
        js_converter = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = ['constructor()', 'rows.map(()', 'row.map(()', 'constructor()', 'start()', 'player()',
                    'constructor()', 'plus()', 'times()', 'constructor()', 'type()', 'create()', 'constructor()',
                    'type()', 'create()', 'constructor()', 'type()', 'create()', 'elt()', 'Object.keys()',
                    'constructor()', 'clear()', 'drawGrid()', 'drawActors()', 'function()', 'function()',
                    'function()', 'function()', '(this.level.touches()', 'overlap()', 'overlap()', 'function()',
                    'function()', 'function()', '(!state.level.touches()', 'function()', 'function()',
                    '(!state.level.touches()', '(!state.level.touches()', 'trackKeys()', 'track()', '(keys.includes()',
                    'runAnimation()', 'frame()', 'runLevel()', 'runGame()']
        actual = js_converter.get_functions(all_lines)
        src_code.close()
        self.assertEqual(expected, actual)

    def test_attributes(self):
        js_converter = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = [['height'], ['width'], ['startActors'], ['rows'], ['startActors.push('], ['level'], ['actors'],
                    ['status'], ['actors.find(a'], ['x', 'y'], ['x', 'y'], ['x', 'y'], ['pos'], ['speed'], ['pos'],
                    ['speed'], ['reset'], ['pos'], ['basePos'], ['wobble'], ['dom'], ['actorLayer'], ['dom);'],
                    ['dom.remove();'], ['actorLayer)', 'actorLayer.remove();'], ['actorLayer'],
                    ['dom.appendChild(this.actorLayer);'], ['dom.className'], ['scrollPlayerIntoView(state);'],
                    ['dom.clientWidth;'], ['dom.clientHeight;'], ['dom.scrollLeft,'], ['dom.scrollTop,'],
                    ['dom.scrollLeft'], ['dom.scrollLeft'], ['dom.scrollTop'], ['dom.scrollTop'], ['width'],
                    ['height;'], ['rows[y][x];'], ['actors'], ['level,', 'status);'], ['level.touches(player.pos,'],
                    ['level,'], ['pos.plus(this.speed.times(time));'], ['size,'], ['speed,', 'reset);'], ['reset)'],
                    ['reset,', 'speed,', 'reset);'], ['pos,', 'speed.times(-1));'], ['wobble'], ['basePos.plus(new'],
                    ['basePos,'], ['pos;'], ['size,'], ['speed.y'], ['size,']]
        actual = js_converter.get_attributes(all_lines)
        src_code.close()
        self.assertEqual(expected, actual)

    def test_merge(self):
        js_converter = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = [('Level', ('constructor()',), ('height', 'width', 'startActors', 'rows', 'startActors.push(')),
                    ('State', ('constructor()', 'start()', 'player()'), ('level', 'actors', 'status', 'actors.find(a')),
                    ('Vec', ('constructor()', 'plus()', 'times()'), ('x', 'x', 'x')),
                    ('Player', ('constructor()', 'type()'), ('pos', 'speed')),
                    ('Lava', ('constructor()', 'type()'), ('pos', 'speed', 'reset')),
                    ('Coin', ('constructor()', 'type()'), ('pos', 'basePos', 'wobble')),
                    ('DOMDisplay', ('constructor()',), ('actorLayer', 'dom);'))]
        actual = js_converter.merge(all_lines)
        src_code.close()
        self.assertEqual(expected, actual)

    def test_dot_file(self):
        dot = Dot()
        js_convert = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = dot.create_dot(js_convert.merge(all_lines))
        actual = dot.create_dot(js_convert.merge(all_lines))
        src_code.close()
        self.assertEqual(expected, actual)
