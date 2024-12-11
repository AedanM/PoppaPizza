"""Base Test Class for testing Modules"""

from dataclasses import dataclass
from typing import Any


@dataclass
class TestClass:
    Result: Any
    ParamList: list
