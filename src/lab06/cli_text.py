import  argparse # для парсинга аргументов командной строки
from src.lib.text import *

def cat(text, n):
    f = open(text, "r").readlines()  # открываем файл и читаем все строки в список
    if not n:                        # если флаг -n НЕ установлен
        for i in f:                  # проходим по всем строкам
            print(i.replace("\n", ""))  # выводим строку без символа новой строки
    else:                            # если флаг -n установлен
        f = enumerate(f)             # нумеруем строки (индекс, строка)
        for i in f:                  # проходим по пронумерованным строкам
            print(i[0],i[1].replace("\n", ""))  # выводим номер и строку

def stats(txt,n):
    f = open(txt, "r").read()        # читаем весь файл как одну строку
    txt = top_n(count_freq(tokenize(normalize(f))),n)  # цепочка обработки текста
    for a in txt:                    # проходим по результату
        print(a[1],a[0])             # выводим частоту и слово

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6") # создаем главный парсер
subparsers = parser.add_subparsers(dest="command") # добавляем подпарсеры для команд

cat_parser = subparsers.add_parser("cat",help = "Вывести содержимое файла")  # создаем парсер для cat
cat_parser.add_argument("--input",required = True)  # обязательный аргумент --input
cat_parser.add_argument("-n", action="store_true",help = "Нумировать строки")  # флаг -n (нумерация строк)

stats_parser = subparsers.add_parser("stats",help = "Частоты слез")  # создаем парсер для stats
stats_parser.add_argument("--input",required = True) 
stats_parser.add_argument("--top",type = int, default = 5)  # аргумент --top (по умолчанию 5)

args = parser.parse_args()  # парсим аргументы командной строки

if args.command == "cat":  
    cat(args.input,args.n)  # вызываем функцию cat с файлом и флагом -n

if args.command == "stats": 
    stats(args.input,args.top)  # вызываем функцию stats с файлом и числом top