import sys
import os
#sys.path.append("c:\Users\enser\github\GitHub\python_labs\src\lib") 
from ..lib import text




def main():
    print("Введите текст (Ctrl+D/Ctrl+Z для завершения):")
    text = sys.stdin.read()
    
    if not text.strip():
        print("Ошибка: введен пустой текст")
        return
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, 5)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()