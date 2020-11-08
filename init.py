from command_line import CommandLineView
from controller import Controller

if __name__ == "__main__":
    c = Controller()
    console = CommandLineView(c)
