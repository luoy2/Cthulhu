from enum import Enum
import random


class OldOne(object):
    def __init__(self, name):
        self.name = name
        # TODO: Add more

    def __repr__(self):
        return self.name


class OldOnes(Enum):
    DAGON = OldOne('DAGON')
    YOG_SOTHOTH = OldOne('YOG_SOTHOTH')
    YIG = OldOne('YIG')
    AZATHOTH = OldOne('AZATHOTH')
    TSATHOGGUA = OldOne('TSATHOGGUA')
    NYARLATHOTEP = OldOne('NYARLATHOTEP')
    SHUB_NIGGURATH = OldOne('SHUB_NIGGURATH')
    ITHAQUA = OldOne('ITHAQUA')
    ATLACH_NACHA = OldOne('ATLACH_NACHA')
    HASTUR = OldOne('HASTUR')
    SHUDDE_MELL = OldOne('SHUDDE_MELL')
    CTHULHU = OldOne('CTHULHU')


def get_initial_old_ones():
    old_ones = random.sample(list(OldOnes)[:-1], 6)
    old_ones.append(OldOnes.CTHULHU)
    return old_ones

