"""Class for Luck"""

from dataclasses import dataclass


@dataclass
class LuckChances:
    CustomerSpawn: float = 0.05
    ActiveRestLuck: int = 2
