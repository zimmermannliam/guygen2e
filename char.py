from dataclasses import dataclass, asdict
import random
from dice import ndx
import traits

names = {   "M": ["John", "Jack", "Sam", "Ezekiel"],
            "W": ["Cindy", "Margaret"]
        }


cid = 0
def get_cid() -> int:
    ''' Character id generator'''
    global cid
    cid += 1
    return cid

@dataclass
class Character:
    """ A PC or NPC. Most things are optional, default None."""
    id: int     = None
    name: str   = None
    gender: str = None
    race: str   = None
    trait: str  = None

    str: int    = None
    dex: int    = None
    con: int    = None
    int: int    = None 
    wis: int    = None
    cha: int    = None

    @property
    def stat(self):
        return [self.str, self.dex, self.con, self.int, self.wis, self.cha]

    @stat.setter
    def stat(self, value):
        self.str = value[0]
        self.dex = value[1]
        self.con = value[2]
        self.int = value[3]
        self.wis = value[4]
        self.cha = value[5]

    @property
    def dict(self):
        return asdict(self)

def character_random() -> Character:
    """Create a completely random character"""
    ch = Character()
    ch.id = get_cid()
    ch.gender = random.choice(["M", "W"])
    ch.name = random.choice(names[ch.gender])
    ch.race = "Human"

    ch.trait = random.choice(traits.table)

    ch.stat = [ndx(3, 6) for _ in range(6)]
    return ch

