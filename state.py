from dataclasses import dataclass

from char import Character

@dataclass
class State:
    chars:[Character]
    cid: int = 0


def get_cid(state: State) -> int:
    """ get character id from state and update it """
    cid = state.cid
    state.cid += 1
    return cid
