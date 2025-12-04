import csv
from pathlib import Path
from typing import List
from datetime import datetime

class Group:
    def __init__(self, storage_path: str): #storage_path - строка с путем к CSV файлу
        self.path = Path(storage_path)
    def _read_csv_rows(self) -> List[dict]: #Объявление приватного метода (начинается с _) для чтения данных из CSV
        rows = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f: #Открытие файла в режиме чтения ('r') с кодировкой UTF-8
                reader = csv.DictReader(f) #Создание объекта DictReader для чтения CSV
                rows = list(reader)
        except FileNotFoundError:
            pass
        return rows
    def _write_csv_rows(self, rows: List[dict]): #Объявление приватного метода для записи данных в CSV, принимает список словарей
        with open(self.path, 'w', encoding='utf-8', newline='') as f: #Открытие файла в режиме записи ('w')
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa']) #Создание объекта DictWriter для записи словарей в CSV
            writer.writeheader()
            writer.writerows(rows)
    def list(self) -> List[dict]: #Объявление публичного метода для получения всех студентов
        return self._read_csv_rows() 
    def add(self, student_data: dict): #Объявление метода для добавления нового студента
        rows = self._read_csv_rows() #Чтение всех текущих строк из файла
        for row in rows:
            if row['fio'] == student_data['fio']:
                return  
        rows.append(student_data)
        self._write_csv_rows(rows)
    def find(self, substr: str) -> List[dict]: #Объявление метода для поиска студентов, принимает подстроку для поиска
        rows = self._read_csv_rows()
        found = []
        for row in rows:
            if substr.lower() in row['fio'].lower(): #Проверка, содержится ли искомая подстрока (в нижнем регистре) в ФИО студента
                found.append(row)
        return found
    def stats(self) -> dict: #Объявление метода для получения статистики, возвращает словарь
        rows = self._read_csv_rows()
        if not rows:
            return {"total": 0, "avg_gpa": 0, "groups": {}} #Если студентов нет, возвращаем словарь с нулевыми значениями
        total_gpa = 0
        groups_count = {}
        for row in rows:
            try:
                total_gpa += float(row['gpa']) #Преобразование GPA из строки в число с плавающей точкой и добавление к общей сумме
                group_name = row['group']
                if group_name in groups_count:
                    groups_count[group_name] += 1
                else:
                    groups_count[group_name] = 1
            except:
                continue
        avg_gpa = total_gpa / len(rows) #Вычисление среднего GPA: сумма GPA / количество студентов
        return {
            "total": len(rows),
            "avg_gpa": avg_gpa,
            "groups": groups_count
        }
    def remove(self, fio: str): #Объявление метода для удаления студента по ФИО
        rows = self._read_csv_rows()
        new_rows = [row for row in rows if row['fio'] != fio] #Создание нового списка строк, исключая студента с указанным ФИО
        if len(new_rows) < len(rows):
            self._write_csv_rows(new_rows)
            return True
        return False
    def update(self, fio: str, **fields): #Объявление метода для обновления данных студента
        rows = self._read_csv_rows()
        updated = False #Флаг, указывающий было ли обновление
        for row in rows:
            if row['fio'] == fio:
                for key, value in fields.items(): #Цикл по всем переданным полям для обновления
                    if key in row:
                        row[key] = value
                updated = True #Установка флага обновления в True
                break
        if updated:
            self._write_csv_rows(rows)
        return updated