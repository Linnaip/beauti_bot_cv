import re
from typing import List

PATTERN = r'^{|}$'


def validate_text(test_text: str, list_keys: List[str]) -> str:
    """
    Функция проверки текста на наличие скобок в ключе
    и наличие ключа в тексте.
    """
    for key in list_keys:
        if re.search(PATTERN, key):
            raise ValueError(f'Присутствуют скобки в {key}')
        else:
            if not re.findall(key, test_text):
                raise KeyError(f"{key} нет в тексте!")
    return test_text
            

def test_validate_text():
    '''
    Тест на наличие ключа в тексте.
    '''
    test_text = '''{name}, ваша запись изменена:
    ⌚️ {day_month} в {start_time}   
    👩 {master}
    Услуги:
    {services}
    управление записью {record_link}'''
    
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']
    error = 'day_of_week нет в тексте!'
    assert validate_text(test_text, list_keys) == error


def test_validate_staples():
    '''
    Тест на проверку наличия скобок в ключах.
    '''
    test_text = '''{name}, ваша запись изменена:
    ⌚️ {day_month} в {start_time}   
    👩 {master}
    Услуги:
    {services}
    управление записью {record_link}'''
    
    list_keys = ['{name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']
    error = 'Присутствуют скобки в {name'
    assert validate_text(test_text, list_keys) == error
