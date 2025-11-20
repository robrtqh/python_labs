mins = int(input("Минуты: "))
hours = mins // 60
minutes = mins % 60
print(f"{hours}:{minutes:02d}")
