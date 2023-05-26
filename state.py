from dataclasses import dataclass

from char import Character

@dataclass
class State:
    chars:[Character]
