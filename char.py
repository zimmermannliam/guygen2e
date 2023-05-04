from dataclasses import dataclass
import random
from dice import ndx

names = {   "M": ["John", "Jack", "Sam", "Ezekiel"],
            "W": ["Cindy", "Margaret"]
        }

@dataclass
class Character:
    name: str   = None
    gender: str = None
    race: str   = None

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
    def stat_dict(self):
        return {"str" : self.str,
                "dex" : self.dex,
                "con" : self.con,
                "int" : self.int,
                "wis" : self.wis,
                "cha" : self.cha}

def character_random() -> Character:
    ch = Character()
    ch.gender = random.choice(["M", "W"])
    ch.name = random.choice(names[ch.gender])
    ch.race = "Human"
    ch.stat = [ndx(3, 6) for _ in range(6)]
    return ch
