'''
Flower, Bouquet models description.
'''
from django.db.models import (
    CharField,
    DecimalField,
    Model
)

FLOWER_NAME_MAX_LENGTH = 120
FLOWER_PRICE_DECIMAL_PLACES = 2


class Flower(Model):
    '''
    Flower model description.
    '''
    name = CharField(
        max_length=FLOWER_NAME_MAX_LENGTH,
        verbose_name='Цветок'
    )
    buy_price = DecimalField(
        decimal_places=FLOWER_PRICE_DECIMAL_PLACES,
        verbose_name='Закупочная цена'
    )
    sell_price = DecimalField(
        decimal_places=FLOWER_PRICE_DECIMAL_PLACES,
        verbose_name='Цена'
    )

    def __str__(self) -> str:
        return f'{self.name}, цена: {self.sell_price}'
