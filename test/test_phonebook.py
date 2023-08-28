from src.phonebook import Phonebook
import pytest

@pytest.fixture
def phones():
    return Phonebook()

def test_add(phones):
    phones.add('SAMU', '180')
    assert phones.entries['SAMU'] == '180'

def test_add_hashtag(phones):
    expected_result = 'Nome invalido'
    result = phones.add('#SAMU', '180')
    assert result == expected_result

def test_add_at(phones):
    expected_result = 'Nome invalido'
    result = phones.add('@SAMU', '180')
    assert result == expected_result

def test_add_exclamation(phones):
    expected_result = 'Nome invalido'
    result = phones.add('!SAMU', '180')
    assert result == expected_result

def test_add_dolar(phones):
    expected_result = 'Nome invalido'
    result = phones.add('$AMU', '190')
    assert result == expected_result

def test_add_percent(phones):
    expected_result = 'Nome invalido'
    result = phones.add('%AMU', '190')
    assert result == expected_result

def test_add_Wrong_number(phones):
    expected_result = 'Numero invalido'
    result = phones.add('SAMU', '')
    assert result == expected_result

def test_lookup_success(phones):
    expected_result = '190'
    result = phones.lookup('POLICIA')
    assert result == expected_result

def test_lookup_None(phones):
    expected_result = None
    result = phones.lookup('TESTE_NULL')
    assert result == expected_result

def test_lookup_hashtag(phones):
    expected_result = 'Nome invalido'
    result = phones.lookup('#SAMU')
    assert result == expected_result

def test_lookup_at(phones):
    expected_result = 'Nome invalido'
    result = phones.lookup('@SAMU')
    assert result == expected_result

def test_lookup_exclamation(phones):
    expected_result = 'Nome invalido'
    result = phones.lookup('!SAMU')
    assert result == expected_result

def test_lookup_dolar(phones):
    expected_result = 'Nome invalido'
    result = phones.lookup('$AMU')
    assert result == expected_result

def test_lookup_percent(phones):
    expected_result = 'Nome invalido'
    result = phones.lookup('%AMU')
    assert result == expected_result

def test_get_names(phones):
    expected_list = ['POLICIA','SAMU','BOMBEIROS']
    phones.add('SAMU', '180')
    phones.add('BOMBEIROS', '170')
    names = phones.get_names()
    assert sorted(names) == sorted(expected_list)

def test_get_numbers(phones):
    expected_list = ['170','180','190']
    phones.add('SAMU', '180')
    phones.add('BOMBEIROS', '170')
    names = phones.get_numbers()
    assert sorted(names) == sorted(expected_list)

def test_get_name_by_number(phones):
    expected_name = 'SAMU'
    phones.add('SAMU', '180')
    name = phones.get_name_by_number('180')
    assert name == expected_name

def test_change_number(phones):
    expected_number = '170'
    expected_result = 'Numero alterado'
    phones.add('SAMU', '180')
    result = phones.change_number('SAMU','170')
    assert result == expected_result
    result = phones.lookup('SAMU')
    assert result == expected_number