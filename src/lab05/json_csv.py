import json
import csv
from pathlib import Path  # для работы с путями файлов


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not json_file.is_file():
        raise FileNotFoundError("FileNotFoundError")
    with json_file.open("r", encoding="utf-8") as f:  # открытие файла в UTF-8
        try:
            data = json.load(f)  # парсинг JSON в Python объект
        except json.JSONDecodeError as e:
            raise ValueError("ValueError")
    if not data or not isinstance(data, list):  # проверка: не пустой ли список
        raise ValueError("ValueError")
    if not all(isinstance(item, dict) for item in data):  # все элементы - словари
        raise ValueError("ValueError")
    first_keys = list(data[0].keys())  # ключи из первого объекта
    all_keys = set(first_keys)  # множество всех уникальных ключей
    for item in data[1:]:  # проходим по остальным объектам
        all_keys.update(item.keys())  # добавляем новые ключи в множество
    additional_keys = sorted(all_keys - set(first_keys))  # новые ключи по алфавиту
    fieldnames = first_keys + additional_keys  # итоговый порядок колонок
    with csv_file.open("w", encoding="utf-8", newline="") as f:  # открытие на запись
        writer = csv.DictWriter(f, fieldnames=fieldnames)  # создание writer с колонками
        writer.writeheader()  # записываем заголовоки
        for item in data:
            row = {
                key: item.get(key, "") for key in fieldnames
            }  # создаем строку, заполняя пустые поля
            writer.writerow(row)  # записываем строку в CSV


json_to_csv(f"data/lab05/samples/example1.json", f"data/lab05/out/example1_json.csv")


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    if not csv_file.is_file():
        raise FileNotFoundError("FileNotFoundError")
    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)  # создаем reader, который вернет словари
        if reader.fieldnames is None:  # проверяем, есть ли заголовок
            raise ValueError("ValueError")
        data = list(reader)  # все строки в список словарей
    if not data:
        raise ValueError("ValueError")
    with json_file.open("w", encoding="utf-8") as f:  # открытие на запись
        json.dump(
            data, f, ensure_ascii=False, indent=2
        )  # ensure_ascii=False - сохраняет кириллицу, indent=2 - форматирование с отступами


csv_to_json(f"data/lab05/samples/example2.csv", f"data/lab05/out/example2_csv.json")
