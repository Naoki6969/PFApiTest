from api import PetFriends
from data import valid_email, valid_password
from invalid_data import invalid_email, invalid_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем что при валидном email и password запрос api ключа возвращает статус 200
     и в результате содержится слово key"""

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result



def test_get_api_key_for_invalid_email_user(email=invalid_email, password=valid_password):
    """Проверяем что при невалидном значении email запрос api ключа возвращает статус 403
     и в результате не содержится слово key(ключ не получен)"""

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result



def test_get_api_key_for_invalid_password_user(email=valid_email, password=invalid_password):
    """Проверяем что при невалидном значении password запрос api ключа возвращает статус 403
     и в результате не содержится слово key(ключ не получен)"""

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result



def test_get_api_key_for_full_invalid_setting(email=invalid_email, password=invalid_password):
    """Проверяем что при невалидных значениях и email и password запрос api ключа возвращает статус 403
     и в результате не содержится слово key(ключ не получен)"""

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result
