from i_creator import ICreator
from pathlib import Path
import pickle


class Pickler(ICreator):

    def create(self, data: []):
        home_directory = str(Path(__file__).parent.absolute().parent) + "\\resources\\"
        with open(home_directory + 'pickle.txt', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)
