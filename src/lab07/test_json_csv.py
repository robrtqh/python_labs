import pytest
import json
import csv
from src.lab05.json_csv import json_to_csv, csv_to_json

@pytest.mark.parametrize(
    "data, expected_len", #параметры: тестовые данные и ожидаемое количество строк
    [
        ([{"name": "Alice", "age": 25}], 1),
        ([{"a": 1}, {"a": 2}], 2),
    ],
)
def test_json_to_csv_positive(tmp_path, data, expected_len): #тестируем конвертацию JSON → CSV, фикстура pytest создает временную папку для тестов, получаем параметры из декоратора
    json_file = tmp_path / "test.json" #готовим имена для временных файлов, создаем путь к JSON файлу во временной директории
    csv_file = tmp_path / "output.csv"
    with open(json_file, "w") as f:
        json.dump(data, f) #сериализует Python-объекты в JSON формат
    json_to_csv(str(json_file), str(csv_file)) #преобразуем Path-объект в строку пути
    assert csv_file.exists() #убеждаемся что функция что-то записала
    with open(csv_file, "r") as f:
        rows = list(csv.DictReader(f)) #читаем CSV как список словарей
        assert len(rows) == expected_len #подсчитываем количество строк (записей), cравниваем с ожидаемым количеством

@pytest.mark.parametrize( #CSV → JSON - тестируем обратную конвертацию
    "data, expected_len",
    [
        ([{"name": "Alice", "age": "25"}], 1),
        ([{"x": "1"}, {"x": "2"}], 2),
    ],
)
def test_csv_to_json_positive(tmp_path, data, expected_len):
    csv_file = tmp_path / "test.csv"
    json_file = tmp_path / "output.json"
    with open(csv_file, "w", newline="") as f: #newline="" - важно для корректной работы CSV в Windows
        writer = csv.DictWriter(f, fieldnames=data[0].keys()) #создает writer для записи словарей, fieldnames=data[0].keys() - берем заголовки из первого словаря
        writer.writeheader() #записывает строку с названиями колонок
        writer.writerows(data) #записывает все данные
    csv_to_json(str(csv_file), str(json_file))
    assert json_file.exists() #убеждаемся что JSON создан и содержит правильное количество записей
    with open(json_file, "r") as f:
        result = json.load(f)
        assert len(result) == expected_len

@pytest.mark.parametrize( #проверяем как функции обрабатывают некорректные данные
    "func, file_content, exception", #func - какая функция тестируется, file_content - что записать в файл (или None если файла нет), exception - какое исключение ожидаем
    [
        (json_to_csv, "invalid json", ValueError),
        (json_to_csv, None, FileNotFoundError),
        (csv_to_json, None, FileNotFoundError),
    ],
)
def test_negative_scenarios(tmp_path, func, file_content, exception): #проверяем обработку ошибок
    src_file = tmp_path / "src" #создаем пути для исходного и целевого файлов
    dst_file = tmp_path / "dst"
    if file_content is not None: #либо создаем с некорректным содержимым, либо используем несуществующий путь
        src_file.write_text(file_content) #записывает текст в файл (для некорректных данных)
        src_path = str(src_file)
    else:
        src_path = str(tmp_path / "nonexistent")
    with pytest.raises(exception): #утверждаем что функция ДОЛЖНА выбросить ожидаемую ошибку, контекстный менеджер для проверки исключений
        func(src_path, str(dst_file))

def test_round_trip(tmp_path): #проверяем конвертацию туда и обратно
    data = [{"name": "Test", "value": 123}]
    json1 = tmp_path / "1.json" #создаем пути для всех этапов конвертации
    csv_file = tmp_path / "data.csv"
    json2 = tmp_path / "2.json"
    json1.write_text(json.dumps(data)) #записываем данные в первый JSON файл, json.dumps(data) - преобразует объект в JSON-строку
    json_to_csv(str(json1), str(csv_file))
    csv_to_json(str(csv_file), str(json2))
    with open(json2, "r") as f:
        result = json.load(f) #загружаем финальный JSON файл
    assert len(result) == len(data) #убеждаемся что данные не потерялись и не исказились
    assert result[0]["name"] == data[0]["name"]
