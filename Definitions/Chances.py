"""Class for Luck"""

from dataclasses import dataclass


@dataclass
class LuckChances:
    """Chances of Random Events"""

    CustomerSpawn: float = 0.05
    ActiveRestLuck: int = 2
