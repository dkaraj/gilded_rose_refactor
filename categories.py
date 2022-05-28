class DefaultCategory:
    def update_quality(self, item):
        self._depreciate_quality(item)
        self._ceil_quality(item)
        self._floor_quality(item)

    def update_sell_in(self, item):
        item.sell_in -= 1

    def _quality_change_when_sell_in(self, item):
        if item.sell_in <= 0:
            return 2
        else:
            return 1

    def _depreciate_quality(self, item):
        item.quality -= self._quality_change_when_sell_in(item)

    def _inflate_quality(self, item):
        item.quality += self._quality_change_when_sell_in(item)

    def _make_worthless_after_sell_in_0(self, item):
        if item.sell_in <= 0:
            item.quality = 0

    def _ceil_quality(self, item):
        item.quality = min(50, item.quality)

    def _floor_quality(self, item):
        item.quality = max(0, item.quality)


class AgedBrieCategory(DefaultCategory):
    """
     Increases in quality the older it gets
    """
    def update_quality(self, item):
        self._inflate_quality(item)
        self._ceil_quality(item)
        self._floor_quality(item)


class BackstagePassesCategory(DefaultCategory):
    def update_quality(self, item):
        self._inflate_quality(item)
        self._ceil_quality(item)
        self._floor_quality(item)
        self._make_worthless_after_sell_in_0(item)

    def _quality_change_when_sell_in(self, item):
        if item.sell_in <= 5:
            return 3
        elif item.sell_in <= 10:
            return 2
        else:
            return 1


class SulfurasCategory(DefaultCategory):
    def update_quality(self, item):
        pass

    def update_sell_in(self, item):
        pass


class ConjuredCategory(DefaultCategory):
    def _quality_change_when_sell_in(self, item):
        return super()._quality_change_when_sell_in(item) * 2
