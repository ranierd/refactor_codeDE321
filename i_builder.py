from abc import ABC, abstractmethod


class IBuilder(ABC):

    def get_classes(self, value):
        """
        Get classes
        """

    def get_functions(self, value):
        """
        Get functions
        """

    def get_attributes(self, attributes):
        """
        Get attributes
        """