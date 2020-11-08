from typing import Any
from abstract_handler import AbstractHandler
from handler import Handler


class CreateDotHandler(AbstractHandler):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: Handler) -> []:
        self.next_handler = handler

    def handle(self, request: Any) -> []:
        dot = JS_to_dot()
        try:
            dot.create_dot(request)
        except AssertionError as e:
            print(e)