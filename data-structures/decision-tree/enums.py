from enum import Enum


class Answer(Enum):
    YES = 's'
    NO = 'n'


class Direction(Enum):
    CORRECT_ANSWER = 'CORRECT_ANSWER'
    WRONG_ANSWER = 'WRONG_ANSWER'
