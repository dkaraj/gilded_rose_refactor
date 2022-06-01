from enum import Enum
import environ

env = environ.Env()

environ.Env.read_env()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

import os
class SpecialItems(Enum):
    AGED_BRIE = os.getenv('AGED_BRIE')
    BACKSTAGE_PASSES = os.getenv("BACKSTAGE_PASSES")
    SULFURAS = os.getenv("SULFURAS")
    CONJURED = os.getenv("CONJURED")

    def matches(self, item):
        return item.name.startswith(self.value)

    def __str__(self):
        return self.value


globals().update(SpecialItems.__members__)
