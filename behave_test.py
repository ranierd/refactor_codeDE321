import unittest
from pickler import Pickler
from dot import Dot
from extract import Extract
from js_convert_builder import JSConvertBuilder
from uml import UML
from js_convert_director import JSConvertDirector
from pathlib import Path




class TestCases(unittest.TestCase):

    def setup(self):
        """Initializes the extracted contents"""
        extract = Extract()
        default_path = str(Path(__file__).parent.absolute().parent) + "\\resources\\16_game.js"
        lines = extract.get_data(default_path)
        return lines

    def builder(self):
        """Initializes my builder class"""
        js_convert_builder = JSConvertBuilder()
        return js_convert_builder

    def director(self):
        """Initializes my director class"""
        director = JSConvertDirector()
        return director

    def test_director_classes(self):
        """Checking if the concrete builder and director can do the produce the same products"""
        director = self.director()
        director.builder = self.builder()
        actual = self.builder().get_classes(self.setup())
        self.assertEquals(director.build_classes(self.setup()), actual)

    def test_director_functions(self):
        """Checking if the concrete builder and director can do the produce the same products"""
        director = self.director()
        director.builder = self.builder()
        actual = self.builder().get_functions(self.setup())
        self.assertEquals(director.build_functions(self.setup()), actual)

    def test_director_attributes(self):
        """Checking if the concrete builder and director can do the produce the same products"""
        director = self.director()
        director.builder = self.builder()
        actual = self.builder().get_attributes(self.setup())
        self.assertEquals(director.build_attributes(self.setup()), actual)

    def test_director_merged(self):
        """Checking if the concrete builder and director can do the produce the same products"""
        director = self.director()
        director.builder = self.builder()
        actual = self.builder().merge(self.setup())
        self.assertEquals(director.build_merged(self.setup()), actual)

    def test_director_properties(self):
        """Director property testing"""
        director = self.director()
        with self.assertRaises(Exception):
            director.builder.builder = None

    def test_classes(self):
        """One of my original tests from Assignment 2"""
        expected = [['Level'], ['State'], ['Vec'], ['Player'], ['Lava'], ['Coin'], ['DOMDisplay']]
        actual = self.builder().get_classes(self.setup())
        self.assertEquals(expected, actual)

    def test_no_classes(self):
        """One of my original tests from Assignment 2"""
        expected = []
        actual = self.builder().get_classes([])
        self.assertEquals(expected, actual)

    def test_error_classes(self):
        """One of my original tests from Assignment 2"""
        expected = None
        actual = self.builder().get_classes([['']])
        self.assertEquals(expected, actual)

    def test_functions(self):
        """One of my original tests from Assignment 2"""
        expected = ['constructor()', 'rows.map(()', 'row.map(()', 'constructor()', 'start()', 'player()',
                    'constructor()', 'plus()', 'times()', 'constructor()', 'type()', 'create()', 'constructor()',
                    'type()', 'create()', 'constructor()', 'type()', 'create()', 'elt()', 'Object.keys()',
                    'constructor()', 'clear()', 'drawGrid()', 'drawActors()', 'function()', 'function()',
                    'function()', 'function()', '(this.level.touches()', 'overlap()', 'overlap()', 'function()',
                    'function()', 'function()', '(!state.level.touches()', 'function()', 'function()',
                    '(!state.level.touches()', '(!state.level.touches()', 'trackKeys()', 'track()', '(keys.includes()',
                    'runAnimation()', 'frame()', 'runLevel()', 'runGame()']
        actual = self.builder().get_functions(self.setup())
        self.assertEquals(expected, actual)

    def test_error_functions(self):
        """One of my original tests from Assignment 2"""
        expected = None
        actual = self.builder().get_functions([['']])
        self.assertEquals(expected, actual)

    def test_attributes(self):
        """One of my original tests from Assignment 2"""
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
        actual = self.builder().get_attributes(self.setup())
        self.assertEquals(expected, actual)

    def test_error_attributes(self):
        """One of my original tests from Assignment 2"""
        expected = None
        actual = self.builder().get_attributes([['']])
        self.assertEquals(expected, actual)

    def test_merge(self):
        """One of my original tests from Assignment 2"""
        expected = [('Level', ('constructor()',), ('height', 'width', 'startActors', 'rows', 'startActors.push(')),
                    ('State', ('constructor()', 'start()', 'player()'), ('level', 'actors', 'status', 'actors.find(a')),
                    ('Vec', ('constructor()', 'plus()', 'times()'), ('x', 'x', 'x')),
                    ('Player', ('constructor()', 'type()'), ('pos', 'speed')),
                    ('Lava', ('constructor()', 'type()'), ('pos', 'speed', 'reset')),
                    ('Coin', ('constructor()', 'type()'), ('pos', 'basePos', 'wobble')),
                    ('DOMDisplay', ('constructor()',), ('actorLayer', 'dom);'))]
        actual = self.builder().merge(self.setup())
        self.assertEquals(expected, actual)

    def test_dot_file(self):
        """One of my original tests from Assignment 2"""
        dot = Dot()
        js_convert_builder = JSConvertBuilder()
        expected = dot.create_dot(js_convert_builder.merge(self.setup()))
        actual = dot.create_dot(self.builder().merge(self.setup()))
        self.assertEquals(expected, actual)

    def test_no_input_dot_file(self):
        """One of my original tests from Assignment 2"""
        dot = Dot()
        expected = 'digraph "classes"{\ncharset="utf-8"\nrankdir=BT\n}'
        actual = dot.create_dot(self.builder().merge(''))
        self.assertEquals(expected, actual)

    def test_error_dot_file(self):
        """One of my original tests from Assignment 2"""
        dot = Dot()
        expected = None
        actual = dot.create_dot(None)
        self.assertEquals(expected, actual)

    def test_converter_with_no_parameters(self):
        """One of my original tests from Assignment 2"""
        expected = "TypeError"
        try:
            actual = self.builder().merge()
        except TypeError as error:
            actual = "TypeError"
        self.assertEquals(expected, actual)

    def test_converter_with_file(self):
        """One of my original tests from Assignment 2"""
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
        self.assertEquals(expected, self.builder().merge(self.setup()))

    def test_converter_with_bad_input(self):
        """One of my original tests from Assignment 2"""
        expected = "Error"
        try:
            actual = self.builder().merge()
        except TypeError:
            actual = "Error"
        self.assertEquals(expected, actual)

    def test_builder_properties(self):
        """Test builder properties"""
        builder = self.builder()
        with self.assertRaises(Exception):
            builder.js_array()

    def test_js_convert_classes(self):
        """Test to make sure that this cannot be used directly without builder"""
        builder = self.builder()
        actual = None
        self.assertEquals(builder.convert.add("classes"), actual)

    def test_pickler(self):
        """Test to make sure that this cannot be used directly without builder"""
        dot = Dot()
        data = dot.create_dot(self.builder().merge(self.setup()))
        pickler = Pickler()
        self.assertEquals(pickler.create(data), None)

    def test_UML(self):
        """Test the UML file"""
        dot = Dot()
        dot.create_dot(self.builder().merge(self.setup()))
        uml = UML()
        self.assertEquals(uml.create(), None)


if __name__ == '__main__':
    unittest.main()
