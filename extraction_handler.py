from typing import Any, List
from abstract_handler import AbstractHandler
from handler import Handler


class ExtractionHandler(AbstractHandler):

    def handle(self, request: Any) -> List[str]:
        src_code = open(request)
        all_lines = src_code.readlines()
        if all_lines:
            try:
                super().handle(all_lines)
            except (AssertionError, FileNotFoundError, FileExistsError) as e:
                raise e
