import requests
import datetime
from decimal import *


def currency_rates(x):
    """Функция принимает от пользователя название валюты и возвращает её курс. Если валюта не найдена - вернет None.
                    Команда all - вернет курсы всех валют доступных на сайте Центробанка.
                    За один раз функция возвращает данные только по одной валюте."""

    # Запрос
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(URL).text
    response = str(response)

    # Сборка даты запроса
    a_date = response.find('Date=')
    b_date = response.find('name=')
    response_data = response[a_date + 6:b_date - 2].split(".")
    date = datetime.date(int(response_data[2]), int(response_data[1]), int(response_data[0]))

    response = response[103:]

    # Cловари с данными
    valute_code_dict = {}
    valute_name_dict = {}
    valute_value_dict = {}

    # Цикл сборки валют
    while len(response) > 10:
        # Строка с данными
        a_string = response.find('<Valute ID')
        b_string = response.find('</Valute>')
        result_str = response[a_string:b_string + 9]

        # Собираем код валюты
        a_valut_code = result_str.find('<CharCode>')
        b_valut_code = result_str.find('</CharCode>')
        valute_code_dict.setdefault(result_str[a_valut_code + 10:b_valut_code].lower(),
                                    result_str[a_valut_code + 10:b_valut_code])

        # Cобираем имя валюты
        a_valut_name = result_str.find('<Name>')
        b_valut_name = result_str.find('</Name>')
        valute_name_dict.setdefault(result_str[a_valut_code + 10:b_valut_code].lower(),
                                    result_str[a_valut_name + 6:b_valut_name])

        # Собираем курс валюты
        a_valut_value = result_str.find('<Value>')
        b_valut_value = result_str.find('</Value>')
        result_valut_value = Decimal(result_str[a_valut_value + 7:b_valut_value].replace(",", ".")).quantize(
            Decimal("1.00"))
        valute_value_dict.setdefault(result_str[a_valut_code + 10:b_valut_code].lower(), result_valut_value)

        # Обновляем строку
        response = response[b_string + 9:]

    def print_all():
        """Выводит на экран курсы всех валют"""
        print(f'\n\nТекущая дата: {date}\n')
        for i in valute_code_dict:
            print(f'Код валюты: {valute_code_dict[i]}\nНазвание валюты: {valute_name_dict[i]}\nТекущий курс: {valute_value_dict[i]}\n\n')

    if x == 'all':
        print_all()
    elif x in valute_code_dict:
        print(f'\n\nТекущая дата: {date}')
        print(
            f'Код валюты: {valute_code_dict[x]}\nНазвание валюты: {valute_name_dict[x]}\nТекущий курс: {valute_value_dict[x]}') 
    else:
        print('None')


print('Если вы хотите получить все текущие котировки - введите команду "all"\n')
currency_rates(x=input('Введите название валюты: ').lower())
