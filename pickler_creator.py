from creator_factory import CreatorFactory
from pickler import Pickler


class PicklerCreator(CreatorFactory):

    def create_items(self):
        return Pickler()
