from dataclasses import dataclass # Импорт декоратора для автоматического создания методов класса
from datetime import datetime, date # Импорт классов для работы с датами
@dataclass # Декоратор, который автоматически создает конструктор __init__ и другие методы
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    def __post_init__(self): # Метод, который выполняется после конструктора __init__
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d") # Пытаемся преобразовать строку в дату по указанному формату
        except ValueError:
            raise ValueError # Если не получается - выбрасываем ошибку
        if not (0 <= self.gpa <= 5): # Проверка диапазона среднего баллаа
            raise ValueError
    def age(self) -> int: # Метод для вычисления возраста студента
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date() # Преобразуем строку с датой рождения в объект date
        today = date.today() # Получаем текущую дату
        age = today.year - birth_date.year # Вычисляем разницу в годах
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day): # Корректируем возраст, если день рождения в этом году еще не наступил
            age -= 1
        return age
    def to_dict(self) -> dict: # Метод для преобразования объекта в словарь (сериализация)
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    @classmethod # Метод класса для создания объекта из словаря (десериализация)
    def from_dict(cls, data: dict): # Создаем новый объект класса, передавая значения из словаря
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    def __str__(self): # Метод для строкового представления объекта
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()} лет"