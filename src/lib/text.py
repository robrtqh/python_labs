import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
         text = text.casefold()
    else: text
    if yo2e:
        text = text.replace('ё','е').replace('Ё','Е') 
    else: text
    text = text.strip()
    text = re.sub(r'[\t\r\x00-\x1f\x7F]', ' ', text) 
    text = ' '.join(text.split())
    return text

def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    tokens  = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    unique_words = list(set(tokens))
    list_count = [tokens.count(i) for i in unique_words]
    dict_count = {key: word for key, word in list(zip(unique_words, list_count))}
    return dict_count

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    list_dict = list(freq.items())
    top = sorted(list_dict, key=lambda x:  x[0])
    top_plus = sorted(top, key=lambda x: x[1], reverse=True)[:n]
    return top_plus

if __name__ == "__main__":
    print('___________normalize___________')
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(normalize("  двойные   пробелы  "))
    print('___________tokenize___________')
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))
    print('___________count_freq + top_n___________')
    print(count_freq(["a","b","a","c","b","a"]))
    print(count_freq(["bb","aa","bb","aa","cc"]))
    print(top_n({"a":3,"b":2,"c":1}, n=2))
    print(top_n({"aa":2,"bb":2,"cc":1}, n=2))