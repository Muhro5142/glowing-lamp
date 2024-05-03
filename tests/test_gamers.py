import pytest
from gamers import Gamer


def test_Задание_1_проверка_имени_и_возраста():
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    assert hasattr(gamer, 'name'), "Задание 1 не выполнено. Класс 'Gamer' не содержит атрибут 'name'"
    assert hasattr(gamer, 'age'), "Задание 1 не выполнено. Класс 'Gamer' не содержит атрибут 'age'"


def test_Задание_2_добавить_nickname():
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    assert hasattr(gamer, 'nickname'), "Задание 2 не выполнено. Класс 'Gamer' не содержит атрибут 'nickname'"


def test_Задание_3_добавить_email():
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    assert hasattr(gamer, 'email'), "Задание 3 не выполнено. Класс 'Gamer' не содержит атрибут 'email'"


def test_Задание_4_изменить_сообщение(capsys):
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    gamer.introduce()
    captured = capsys.readouterr()
    expected_output = "Привет, меня зовут Иван, мне 14 лет. Всегда на связи по john@gmail.com. Ищи меня в игре по нику John"
    assert expected_output in captured.out, f"Задание 4 не выполнено. Ожидаемое сообщение: {expected_output}, Фактическое: {captured.out}"


if __name__ == "__main__":
    pytest.main(["-v"])
