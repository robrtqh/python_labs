import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src')) 
from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json
def main():
    students = [
        Student("Иванов Иван", "2000-05-15", "SE-01", 4.5),
        Student("Петрова Анна", "2001-08-22", "SE-02", 3.8),
    ]
    print("Созданные студенты:")
    for student in students:
        print(f"  {student}")
    students_to_json(students, "data/lab08/students_output.json")
    loaded_students = students_from_json("data/lab08/students_input.json")
    print("Загруженные студенты:")
    for student in loaded_students:
        print(f"  {student}")
    student = Student("Тестовый", "2000-01-01", "TEST-01", 3.0)
    student_dict = student.to_dict() # Преобразуем студента в словарь
    new_student = Student.from_dict(student_dict) # Создаем нового студента из словаря
if __name__ == "__main__":
    main()