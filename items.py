from enum import Enum

import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class SpecialItems(Enum):
    AGED_BRIE = env("AGED_BRIE")
    BACKSTAGE_PASSES = env("BACKSTAGE_PASSES")
    SULFURAS = env("SULFURAS")
    CONJURED = env("CONJURED")

    def matches(self, item):
        return item.name.startswith(self.value)

    def __str__(self):
        return self.value


globals().update(SpecialItems.__members__)
