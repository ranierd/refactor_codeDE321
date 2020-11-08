from abc import ABC, abstractmethod


class IBuilder(ABC):

    def set_classes(self, value):
        """
        Set classes
        """

    def set_functions(self, value):
        """
        Set functions
        """

    def set_attributes(self, attributes):
        """
        Set attributes
        """