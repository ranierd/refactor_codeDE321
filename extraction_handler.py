from typing import Any, List
from abstract_handler import AbstractHandler
from handler import Handler


class ExtractionHandler(AbstractHandler):

    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler: Handler):
        self.next_handler = handler

    def handle(self, request: Any) -> List[str]:
        src_code = open(request)
        all_lines = src_code.readlines()
        src_code.close()
        if all_lines:
            try:
                self.next_handler(all_lines)
            except AssertionError as e:
                print(e)
