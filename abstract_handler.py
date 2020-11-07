from abc import abstractmethod
from typing import Any
from handler import Handler


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    next_handler: Handler = None

    def set_next_handler(self, handler: Handler) -> str:
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self.next_handler:
            return self.next_handler.handle(request)
        return None
