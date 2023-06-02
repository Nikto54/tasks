import requests
from config import values
class APIException(Exception):
    pass

class ValuesConverter:
    @staticmethod
    def get_price(qoute,base,amount):

        if qoute == base:
            raise APIException('Вы указали одинаковые валюты')

        try:
            main_qoute = values[qoute]
        except KeyError:
            raise APIException(f'Неверно введена первая валюта')

        try:
            main_base = values[base]
        except KeyError:
            raise APIException(f'Неверно введена 2 валюта')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неверно введено количество переводимой валюты')
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        total_base=int(amount) * data['Valute'][main_qoute]['Value'] / data['Valute'][main_base]['Value']
        return total_base