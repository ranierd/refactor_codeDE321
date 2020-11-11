from abc import ABC


class CreatorFactory(ABC):

    def create_items(self):
        """Create different requirements from extracted content"""
