from abc import ABC, abstractmethod
from pathlib import Path

class ICreator(ABC):



    @abstractmethod
    def create(self):
        """Default implementation"""
