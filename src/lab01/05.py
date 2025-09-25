full_name = input("ФИО: ")
full_names = ' '.join(full_name.split())
words = full_names.split()
initials = ""
for i in words:
    if i:
        initials += i[0].upper()
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(full_names)}")