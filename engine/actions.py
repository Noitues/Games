"""Decision objects passed between the engine and the policies (Part 3.3)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional, Sequence, Tuple

from .hexmap import Node


@dataclass(frozen=True)
class Activation:
    """A complete legal plan for one champion's activation (Rules 5.2)."""
    champ: Optional[str]                 # None == Pass
    dest: Optional[Node] = None          # node after the Speed movement
    recall: bool = False
    flip_entry: Optional[int] = None     # tile bumped into (Rules 3.3)
    intent: Optional[Node] = None        # where to push on after that flip
    ability: Optional[str] = None        # "L0" | "Q" | "W" | "E" | "R"
    when: str = "after"                  # ability before or after the movement
    plan: Tuple = ()                     # one choice per icon step
    tonic: bool = False                  # Swift Tonic played with this ability

    @property
    def is_pass(self) -> bool:
        return self.champ is None


PASS = Activation(champ=None)


@dataclass(frozen=True)
class CardPlay:
    card: str
    target: Any = None


@dataclass(frozen=True)
class Placement:
    """One complete assignment of champions to hexes on a flip (Rules 3.3)."""
    mapping: Tuple[Tuple[str, Tuple[int, int]], ...]

    def as_dict(self):
        return {uid: h for uid, h in self.mapping}


@dataclass(frozen=True)
class Purchase:
    item: str
    champ: Optional[str] = None      # stat boosts apply to one champion
