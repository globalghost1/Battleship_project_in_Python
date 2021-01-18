from enum import Enum


class Players(Enum):
    Player1 = 1
    Player2 = 2
    AI = 3


class Modes(Enum):
    HUMAN_HUMAN = 1
    HUMAN_AI = 2
