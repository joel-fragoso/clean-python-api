from dataclasses import dataclass
from typing import Any


@dataclass
class HttpResponse:
    code: int
    body: Any
