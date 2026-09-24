import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from engine.config import make_config
from engine.game import new_game
from engine.hexmap import Board
from engine.kits import load_roster

ROSTER = os.environ.get("HEXNEXUS_ROSTER") or os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "roster", "roster_v1.7.0.json")


@pytest.fixture(scope="session")
def board():
    return Board.load()


@pytest.fixture(scope="session")
def kits():
    return load_roster(ROSTER)


@pytest.fixture
def cfg():
    return make_config()


PICKS = {"north": ["bastion", "thornjaw", "ashwyn", "kestrel", "lumen"],
         "south": ["vurmak", "mossgrove", "vellum", "dax", "grivven"]}


@pytest.fixture
def state(board, kits, cfg):
    return new_game(board, kits, PICKS, cfg, first="north")


class DummyGame:
    def placer(self, state, tile, champs, free):
        out, avail = {}, list(free)
        for c in champs:
            if c.hexpos in avail:
                avail.remove(c.hexpos)
                out[c.uid] = c.hexpos
            elif avail:
                out[c.uid] = avail.pop(0)
        return out


@pytest.fixture
def game():
    return DummyGame()
