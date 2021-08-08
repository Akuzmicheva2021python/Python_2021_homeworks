import requests
from bs4 import BeautifulSoup

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from models import Index, Information, MyException


def get_keyrate_info(url, dt_from, dt_to):
    informs = []
    # http://www.cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&
    # UniDbQuery.From=20.07.2021&UniDbQuery.To=20.07.2021
    response = requests.get(url, params={"UniDbQuery.Posted": "True",
                                         "UniDbQuery.From": dt_from,
                                         "UniDbQuery.To": dt_to})
    rez1 = response.status_code
    if rez1 == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_title = soup.find_all('td')
        for j in range(0, len(div_title) - 1, 2):
            dt0 = div_title[j].text
            information = Information(dt0)
            information.name = 'KeyRate'
            val0 = div_title[j + 1].text
            information.value = val0

            informs.append(information)

    return informs


def get_usd_info(url, dt_from, dt_to):
    informs = []
    # http://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&
    # UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01235&
    # UniDbQuery.From=31.07.2021&UniDbQuery.To=07.08.2021
    response = requests.get(url, params={"UniDbQuery.Posted": "True",
                                         "UniDbQuery.so": 1,
                                         "UniDbQuery.mode": 1,
                                         "UniDbQuery.date_req1": "",
                                         "UniDbQuery.date_req2": "",
                                         "UniDbQuery.VAL_NM_RQ": "R01235",
                                         "UniDbQuery.From": dt_from,
                                         "UniDbQuery.To": dt_to})
    rez1 = response.status_code
    if rez1 == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_title = soup.find_all('td')
        for j in range(1, len(div_title), 3):
            dt0 = div_title[j].text
            information = Information(dt0)
            information.name = 'USD Rate'
            val0 = div_title[j + 2].text
            information.value = val0

            informs.append(information)

    return informs


def get_euro_info(url, dt_from, dt_to):
    informs = []
    # http://www.cbr.ru/eng/currency_base/dynamics/?
    # UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&
    # UniDbQuery.date_req1=&UniDbQuery.date_req2=&
    # UniDbQuery.VAL_NM_RQ=R01239&UniDbQuery.From=31%2F07%2F2021&UniDbQuery.To=07%2F08%2F2021
    response = requests.get(url, params={"UniDbQuery.Posted": "True",
                                         "UniDbQuery.so": 1,
                                         "UniDbQuery.mode": 1,
                                         "UniDbQuery.date_req1": "",
                                         "UniDbQuery.date_req2": "",
                                         "UniDbQuery.VAL_NM_RQ": "R01239",
                                         "UniDbQuery.From": dt_from,
                                         "UniDbQuery.To": dt_to})
    rez1 = response.status_code
    if rez1 == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_title = soup.find_all('td')
        for j in range(1, len(div_title), 3):
            dt0 = div_title[j].text
            information = Information(dt0)
            information.name = 'EURO Rate'
            val0 = div_title[j + 2].text
            information.value = val0

            informs.append(information)

    return informs

# 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002'


def get_rate_info(url, dt_from, dt_to):
    informs = []
    dt0 = dt_from.replace('.', '/')
    response = requests.get(url, params={"date_req": dt0})
    res = response.content.decode('cp1251')
    root = ET.fromstring(res)
    for elm in root.iter('Valute'):
        information = Information(dt_from)
        information.name = elm.find('Name').text
        tkol = int(elm.find('Nominal').text)
        sval = elm.find('Value').text.replace(',', '.')
        tval = float(sval)
        tval1 = str(tval/tkol)
        information.value = tval1
        informs.append(information)
    return informs


async def run(config, dt_start, dt_finish):
    informs_map = {
        Index.KeyRate: get_keyrate_info,
        Index.USD: get_usd_info,
        Index.EURO: get_euro_info,
        Index.CurrencyRate: get_rate_info
    }
    url = config.get_url()
    func_to_get_data = informs_map.get(config.index, None)

    if func_to_get_data is None:
        raise MyException(f"{config.index} не определен")

    informs = func_to_get_data(url, dt_start, dt_finish)

    return informs


if __name__ == '__main__':
    url1 = 'http://www.cbr.ru/scripts/XML_daily.asp'
    dt1 = '26.07.2021'
    dt2 = '26.07.2021'
    r1 = get_rate_info(url1, dt1, dt2)
    for el1 in r1:
        print([el1.name])
        print([el1.value])
