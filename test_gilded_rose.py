import pytest

from gilded_rose import GildedRose
from items import Item


@pytest.fixture()
def gilded_rose():
    def _initializer(days=1, items=[]):
        gilded_rose = GildedRose(items)
        for i in range(days):
            gilded_rose.update_quality()
        return gilded_rose
    return _initializer


def validate_sell_in_and_quality(item, sell_in, quality):
    assert item.sell_in == sell_in
    assert item.quality == quality


def test_sell_in_and_quality_decreases_each_day(gilded_rose):
    days = 1
    item = Item("Item", 1, 1)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, 0, 0)


def test_quality_decreases_twice_after_sell_in(gilded_rose):
    days = 1
    item = Item("Item", 0, 2)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, -1, 0)


def test_quality_is_never_negative(gilded_rose):
    days = 1
    item1 = Item("Item 1", 0, 0)
    item2 = Item("Item 2", -1, 0)
    item3 = Item("Item 3", -1, 1)
    gilded_rose(days, [item1, item2, item3])
    validate_sell_in_and_quality(item1, -1, 0)
    validate_sell_in_and_quality(item2, -2, 0)
    validate_sell_in_and_quality(item3, -2, 0)


def test_aged_brie_increases_in_quality_when_older(gilded_rose):
    days = 1
    item = Item("Aged Brie", 1, 0)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, 0, 1)


def test_aged_brie_increases_in_quality_twice_after_sell_in(gilded_rose):
    days = 1
    item = Item("Aged Brie", 0, 0)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, -1, 2)


def test_quality_of_an_item_is_never_more_than_50(gilded_rose):
    days = 1
    item1 = Item("Aged Brie", 1, 50)
    item2 = Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)
    gilded_rose(days, [item1, item2])
    validate_sell_in_and_quality(item1, 0, 50)
    validate_sell_in_and_quality(item2, 9, 50)


def test_sulfuras_never_has_to_be_sold_and_never_degrades_in_quality(gilded_rose):
    days = 1
    item = Item("Sulfuras, Hand of Ragnaros", 1, 10)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, 1, 10)


def test_backstage_pass_increases_in_quality_when_older(gilded_rose):
    days = 1
    item = Item("Backstage passes to a TAFKAL80ETC concert", 20, 0)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, 19, 1)


def test_backstage_pass_increases_in_quality_by_2_when_sell_in_10_or_less(gilded_rose):
    days = 1
    item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, 9, 2)


def test_backstage_pass_increases_in_quality_by_3_when_sell_in_5_or_less(gilded_rose):
    days = 1
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, 4, 3)


def test_backstage_pass_quality_is_0_after_concert(gilded_rose):
    days = 1
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
    gilded_rose(days, [item])
    validate_sell_in_and_quality(item, -1, 0)


def test_conjured_item_quality_decrease_twice_as_fast(gilded_rose):
    days = 1
    item1 = Item("Conjured mooncake", 1, 10)
    item2 = Item("Conjured spork", 0, 10)
    gilded_rose(days, [item1, item2])
    validate_sell_in_and_quality(item1, 0, 8)
    validate_sell_in_and_quality(item2, -1, 6)
