import unittest
from dot import Dot
from js_convert import JSConvert


class TestCases(unittest.TestCase):

    def setup(self):
        return "C:\\Users\\Ranier\\Downloads\\python-assignment-master\\resources\\16_game.js"

    def test_classes(self):
        js_converter = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = [['Level'], ['State'], ['Vec'], ['Player'], ['Lava'], ['Coin'], ['DOMDisplay']]
        actual = js_converter.get_classes(all_lines)
        src_code.close()
        self.assertEquals(expected, actual)

    def test_no_classes(self):
        js_converter = JSConvert()
        expected = []
        actual = js_converter.get_classes([])
        self.assertEquals(expected, actual)

    def test_error_classes(self):
        js_converter = JSConvert()
        expected = None
        actual = js_converter.get_classes([['']])
        self.assertEquals(expected, actual)

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
        self.assertEquals(expected, actual)

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
        self.assertEquals(expected, actual)

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
        self.assertEquals(expected, actual)

    def test_dot_file(self):
        dot = Dot()
        js_convert = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = 'digraph "classes"{\ncharset="utf-8"\nrankdir=BT\n' \
                   '"0"[label="{Level|height\lwidth\lstartActors\lrows\lstartActors.push(\l|constructor()\l}", ' \
                   'shape="record"];\n"1"[label="{State|level\lactors\lstatus\lactors.find(a\l|constructor()\lstart(' \
                   ')\lplayer()\l}", shape="record"];\n"2"[label="{Vec|x\lx\lx\l|constructor()\lplus()\ltimes()\l}", ' \
                   'shape="record"];\n"3"[label="{Player|pos\lspeed\l|constructor()\ltype()\l}", ' \
                   'shape="record"];\n"4"[label="{Lava|pos\lspeed\lreset\l|constructor()\ltype()\l}", ' \
                   'shape="record"];\n"5"[label="{Coin|pos\lbasePos\lwobble\l|constructor()\ltype()\l}", ' \
                   'shape="record"];\n"6"[label="{DOMDisplay|actorLayer\ldom);\l|constructor()\l}", shape="record"];\n}'
        actual = dot.create_dot(js_convert.merge(all_lines))
        src_code.close()
        self.assertEquals(expected, actual)

    def test_converter_with_no_parameters(self):
        js_converter = JSConvert()
        expected = "TypeError"
        try:
            actual = js_converter.merge()
        except TypeError as error:
            actual = "TypeError"
        print(str(actual))
        self.assertEquals(expected, actual)

    def test_converter_with_file(self):
        js_converter = JSConvert()
        src_code = open(self.setup())
        all_lines = src_code.readlines()
        expected = [('Level', ('constructor()',), ('height', 'width', '\
startActors', 'rows', 'startActors.push(')), ('State', ('co\
nstructor()', 'start()', 'player()'), ('level', 'actors\
', 'status', 'actors.find(a')), ('Vec', ('construct\
or()', 'plus()', 'times()'), ('x', 'x', 'x')), ('\
Player', ('constructor()', 'type()'), ('pos', '\
speed')), ('Lava', ('constructor()', 'type()\
'), ('pos', 'speed', 'reset')), ('Coin\
', ('constructor()', 'type()'), ('pos', 'basePos', 'wobble')), ('DOMDis\
play', ('constructor()',), ('actorLayer', 'dom);'))]
        self.assertEquals(expected,  js_converter.merge(all_lines))

    def test_converter_with_bad_input(self):
        js_converter = JSConvert()
        expected = "Error"
        try:
            actual = js_converter.merge(None)
        except TypeError:
            actual = "Error"
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
