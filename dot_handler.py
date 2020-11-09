from typing import Any
from abstract_handler import AbstractHandler
from dot import Dot


class DotHandler(AbstractHandler):

    def handle(self, request: Any) -> []:
        if request:
            try:
                dot = Dot()
                dot.create_dot(request)
            except (AssertionError, FileExistsError, FileNotFoundError, PermissionError) as e:
                print(e)