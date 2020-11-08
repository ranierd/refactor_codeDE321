from cmd import Cmd
import sys


class CommandLineView(Cmd):

    def __init__(self, controller):
        Cmd.__init__(self)
        self.say('Type ? or help to see command list')
        self.prompt = '>>> '
        self.runner = controller
        self.cmdloop()

    def default(self, arg):
        """Default response if incorrect input has been entered"""
        self.say(arg)
        self.say(' is an incorrect command. Type ? or help to see \
command list')

    def do_convert_js_file(self, arg):
        """
        Converts the JS contents to an array of class data and returns it
        Syntax: convert_js_file [file path]
        """
        try:
            if (arg == ''):
                self.runner.js_to_array(input("Please type the path of the javascript file you wish to convert"))
            else:
                self.runner.js_to_array(arg)
        except (FileNotFoundError, PermissionError, FileExistsError) as e:
            self.say(e)

    def do_create_dot_file(self, arg):
        """
        Creates a dot file and saves it in your resources folder
        Syntax: create_dot_file
        """
        try:
            self.runner.array_to_dot()
        except FileNotFoundError as e:
            self.say(e)

    def do_create_uml(self, arg):
        """
        Creates an UML PNG of the selected dot file and saves it in your resources folder
        Syntax: create_uml [filepath]
        """
        try:
            if (arg == ''):
                self.runner.make_uml(input("Please type the path of the dot file you wish to create into a UML class diagram"))
                self.say('Uml.png successfully created')
            else:
                self.runner.make_uml(arg)
        except (FileNotFoundError, PermissionError) as e:
            self.say(e)

    def do_create_pickle(self, arg):
        """
        Creates a pickle file
        Syntax: create_pickle
        """
        self.runner.make_pickle()
        self.say('Pickle successfully created')

    def do_save_to_database(self, arg):
        """
        Saves data to database
        Syntax: load_from_data_base
        """
        try:
            self.runner.insert_db()
        except ConnectionError as e:
            self.say(e)

    def do_load_from_database(self, arg):
        """
        Loads data from database
        Syntax: load_from_data_base
        """
        try:
            self.runner.get_from_db()
        except ConnectionError as e:
            self.say(e)
        except AttributeError as e:
            self.say(e)

    def do_quit(self, arg):
        """
        Stop the program
        Syntax: quit
        """
        self.say('Program is stopping')
        sys.exit(1)

    @staticmethod
    def say(message):
        print(message)
