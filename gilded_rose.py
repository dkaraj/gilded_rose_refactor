from items import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS, CONJURED
from categories import DefaultCategory, AgedBrieCategory, BackstagePassesCategory, SulfurasCategory, ConjuredCategory


CATEGORIES = {
    AGED_BRIE: AgedBrieCategory(),
    BACKSTAGE_PASSES: BackstagePassesCategory(),
    SULFURAS: SulfurasCategory(),
    CONJURED: ConjuredCategory()
}


class GildedRose:

    def __init__(self, items):
        self.items = items

    def find_category(self, item):
        for special_item, strategy in CATEGORIES.items():
            if special_item.matches(item):
                return strategy
        return DefaultCategory()

    def update_quality(self):
        for item in self.items:
            strategy = self.find_category(item)
            strategy.update_quality(item)
            strategy.update_sell_in(item)
