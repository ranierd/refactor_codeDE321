from __future__ import annotations
from typing import Optional
from abc import ABC, abstractmethod


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next_handler(self, handler: Handler) -> Handler:
        """Sets next handler"""

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        """Handles the request"""
