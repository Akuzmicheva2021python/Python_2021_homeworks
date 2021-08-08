from enum import Enum
from pydantic import BaseModel

class MyException(Exception):
    pass


class Index(str, Enum):
    KeyRate = "Ключевая ставка"
    USD = "Курс USD"
    EURO = "Курс EURO"
    CurrencyRate = "Курс обмена"


class Information:
    def __init__(self, dt):
        self.name = None
        self.date = dt
        self.value = None


class Config(BaseModel):
    index: str = None

    index_map = {
        Index.KeyRate: 'http://www.cbr.ru/hd_base/KeyRate/',
        Index.USD: 'http://www.cbr.ru/currency_base/dynamics/',
        Index.EURO: 'http://www.cbr.ru/currency_base/dynamics/',
        Index.CurrencyRate: 'http://www.cbr.ru/scripts/XML_daily.asp',
    }

    def get_url(self):
        return self.index_map[self.index]

# 'http://www.cbr.ru/eng/currency_base/daily/'
# http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002