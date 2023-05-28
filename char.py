from dataclasses import dataclass
import random
from dice import ndx
import traits

names = {   "M": ["John", "Jack", "Sam", "Ezekiel"],
            "W": ["Cindy", "Margaret"]
        }


@dataclass
class Character:
    """ A PC or NPC. Most things are optional, default None."""
    id: int     = None
    name: str   = None
    gender: str = None
    race: str   = None
    trait: str  = None
    
    height: int = None
    weight: int = None

    str: int    = None
    dex: int    = None
    con: int    = None
    int: int    = None 
    wis: int    = None
    cha: int    = None

    @property
    def stats(self):
        return [self.str, self.dex, self.con, self.int, self.wis, self.cha]

    @stats.setter
    def stats(self, value):
        self.str = value[0]
        self.dex = value[1]
        self.con = value[2]
        self.int = value[3]
        self.wis = value[4]
        self.cha = value[5]

def char_random(cid) -> Character:
    """Create a completely random character"""
    ch = Character()
    ch.id = cid
    ch.gender = random.choice(["M", "W"])
    ch.name = random.choice(names[ch.gender])
    ch.race = "Human"
    ch.height = (59 if ch.gender == "M" else 53) + ndx(2, 10)
    ch.weight = (140 if ch.gender == "M" else 100) + ndx(6, 10)

    ch.trait = random.choice(traits.table)

    ch.stats = [ndx(3, 6) for _ in range(6)]
    return ch

