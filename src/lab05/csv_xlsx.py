from openpyxl import Workbook # импорт класса для создания Excel файлов
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    if not csv_file.is_file():
        raise FileNotFoundError("FileNotFoundError")
    wb = Workbook()      # создаем новую Excel книгу
    ws = wb.active       # получаем активный лист
    ws.title = "Sheet1"  # переименовываем лист
    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)  # создаем CSV reader
        rows = list(reader)  # читаем все строки в список списков
    if not rows:
        raise ValueError("ValueError")
    for row in rows:
        ws.append(row) # добавляем строку в Excel лист
    for col_idx, col_cells in enumerate(ws.columns, start=1): # ws.columns - генератор всех колонок листа, enumerate(..., start=1) - получаем индекс колонки
        max_length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in col_cells) # для каждой колонки находим максимальную длину текста, находим максимальную длину среди всех ячеек колонки
        adjusted_width = max(max_length, 8) # устанавливаем ширину как максимум
        col_letter = ws.cell(row=1, column=col_idx).column_letter # получаем букву колонки из первой ячейки колонки
        ws.column_dimensions[col_letter].width = adjusted_width # устанавливаем вычисленную ширину для колонки
    wb.save(xlsx_file)

csv_to_xlsx('data/lab05/samples/example2.csv', 'data/lab05/out/example3_csv.xlsx')
