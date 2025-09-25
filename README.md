# Лабораторная работа №1

### Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![Картинка 1](./images/lab01/01.png)

### Задание 2
```python
a = float(input("a: ").replace(',', '.'))
b = float(input("b: ").replace(',', '.'))
sum = a + b
ave = sum / 2
print(f"sum={sum:.2f}; avg={ave:.2f}")
```
![Картинка 1](./images/lab01/02.png)

### Задание 3
```python
price = float(input("price (₽): "))
discount = float(input("discount (%): "))
vat = float(input("vat (%): "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
![Картинка 1](./images/lab01/03.png)

### Задание 4
```python
mins = int(input("Минуты: "))
hours = mins // 60
minutes = mins % 60
print(f"{hours}:{minutes:02d}")
```
![Картинка 1](./images/lab01/04.png)

### Задание 5
```python
full_name = input("ФИО: ")
full_names = ' '.join(full_name.split())
words = full_names.split()
initials = ""
for i in words:
    if i:
        initials += i[0].upper()
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(full_names)}")
```
![Картинка 1](./images/lab01/05.png)