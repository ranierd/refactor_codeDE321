from i_creator import ICreator
from pathlib import Path


class UML(ICreator):

    def create(self):
        home_directory = str(Path(__file__).parent.absolute().parent) + "\\resources\\"
        from subprocess import call as sub_call
        call = [home_directory + "graphviz-2.44.1\\bin\\dot.exe"] + \
               [home_directory + "JSClasses.dot"] +\
               ['-Tpng'] + ['-o' + home_directory + "\\uml.png"]
        sub_call(call)
