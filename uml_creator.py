from creator_factory import CreatorFactory
from uml import UML


class UMLCreator(CreatorFactory):

    def create_items(self):
        return UML()
