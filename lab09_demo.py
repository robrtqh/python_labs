from datetime import datetime
from src.lab09.group import Group

def calculate_age(birthdate_str): #Объявление функции calculate_age, которая принимает строку с датой рождения
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d") #Преобразование строки с датой в объект datetime., strptime() - парсит строку в дату, "%Y-%m-%d" - формат строки: ГГГГ-ММ-ДД
        today = datetime.now()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age
    except:
        return 0

def print_student_list(students, title="", indent="    "): #Объявление функции для вывода списка студентов, indent - отступ для каждой строки
    if title:
        print(title)
    for student in students:
        age = calculate_age(student['birthdate'])
        gpa = float(student['gpa']) #Преобразование GPA из строки в число с плавающей точкой
        print(f"{indent}Студент: {student['fio']}, "
              f"Группа: {student['group']}, "
              f"Возраст: {age}, "
              f"GPA: {gpa:.2f}") #GPA с 2 знаками после запятой

def main():
    print()
    group = Group("data/lab09/students.csv")
    print("1. Исходный список студентов:")
    students = group.list()
    print_student_list(students)
    print()
    print("2. Добавляем: Иванов Иван")
    new_student = {
        'fio': 'Иванов Иван',
        'birthdate': '2003-10-10',
        'group': 'БИВТ-21-1',
        'gpa': '4.3'
    }
    group.add(new_student)
    print()
    print("3. Список после добавления:")
    students = group.list()
    print_student_list(students)
    print()
    print('4. Поиск по "ов":')
    found_students = group.find("ов")
    print_student_list(found_students)
    print()
    print("5. Статистика:")
    stats = group.stats()
    print(f"    Всего: {stats['total']}")
    print(f"    Средний GPA: {stats['avg_gpa']:.1f}")
    print("    Группы:")
    for group_name, count in stats['groups'].items():
        print(f"    {group_name}: {count}")
    print()
if __name__ == "__main__":
    main()