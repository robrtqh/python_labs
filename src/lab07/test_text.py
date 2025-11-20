import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize( #декоратор для запуска одного теста с разными данными
    "text, expected", #названия параметров которые будут передаваться в тестовую функцию
    [
        ("Hello World", "hello world"),
        ("PYTHON", "python"),
        ("", ""),
        ("   ", ""),  
        ("Text\nwith\tspaces", "text with spaces"),
    ],
)
def test_normalize(text, expected):
    assert normalize(text) == expected #проверка: результат функции должен совпадать с ожиданием

@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", ["hello", "world"]),
        ("python code", ["python", "code"]),
        ("", []),
        ("   ", []),
        ("hello,world!", ["hello", "world"]),
        ("test  spaces", ["test", "spaces"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected

@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c"], {"a": 2, "b": 1, "c": 1}),
        ([], {}),
        (["single"], {"single": 1}),
        (["x", "x", "x"], {"x": 3}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected

@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({}, 5, []),
        ({"x": 1}, 10, [("x", 1)]),
        ({"z": 2, "a": 2, "b": 1}, 3, [("a", 2), ("z", 2), ("b", 1)]),
        ({"cat": 3, "dog": 3, "ant": 2}, 2, [("cat", 3), ("dog", 3)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected

def test_full_pipeline():
    text = "Hello world hello"
    result = top_n(count_freq(tokenize(normalize(text))), 2)
    assert result == [("hello", 2), ("world", 1)]
