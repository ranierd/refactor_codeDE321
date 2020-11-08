from dot import Converter
from database import Database_connector
from js_to_dot import JS_to_dot
from pickler import Pickler
from uml import Uml


class Controller:
    # static array of all classes for access across the models
    home_dir = JS_to_dot()._home_directory
    classes = None
    db = None

    def js_to_array(self, source_code):
        c = Converter()
        try:
            self.classes = c.convert(source_code)
            print("js contents sucessfully converted")
        except AssertionError as e:
            print("please use a valid javascript file")
        except AttributeError as e:
            print(e)

    def array_to_dot(self, out_path=''):
        j = JS_to_dot()
        try:
            j.create_dot(self.classes, out_path)
        except (AssertionError, FileNotFoundError, PermissionError) as e:
            print(e)

    def make_uml(self, dot_file=''):
        if dot_file == '':
            dot_file = self.home_dir + "\\resources\\JSClasses.dot"
        dot_exe = self.home_dir + \
                  "\\resources\\graphviz-2.38\\release\\bin\\dot.exe"
        image_path = self.home_dir + "\\resources\\uml.png"
        u = Uml()
        u.create_uml_file(dot_exe, dot_file, image_path)

    def make_pickle(self, pickle_location=''):
        p = Pickler()
        p.serialize(self.classes, pickle_location)

    def insert_db(self):
        print("inserting into database")
        # create Database connection
        self.db = Database_connector(self.classes)
        # insert things into database
        self.db.run()

    def get_from_db(self):
        print(self.db.select_from_sql())



