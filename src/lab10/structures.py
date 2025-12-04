from collections import deque #deque нужен для эффективной реализации очереди

class Stack: #Стек — структура данных LIFO
    def __init__(self):
        self._data = [] #_data — приватный атрибут
    def push(self, item): #push — добавляет элемент на вершину стека
        self._data.append(item) #добавляет элемент в конец списка
    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._data.pop() #удаляет последний элемент списка и возвращает его
    def peek(self): #смотрит верхний элемент без удаления
        if self.is_empty():
            return None
        return self._data[-1] #обращение к последнему элементу списка
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self): #вызывается при использовании len(obj)
        return len(self._data)
    def __str__(self): #при преобразовании объекта в строку
        return f"Stack({self._data})" #Возвращает строку вида Stack([элементы])

class Queue: #Очередь — структура данных FIFO
    def __init__(self):
        self._data = deque() #создаёт пустую двустороннюю очередь
    def enqueue(self, item): #добавляет элемент в конец очереди
        self._data.append(item) #добавляет элемент в правый конец deque
    def dequeue(self): #удаляет и возвращает элемент из начала очереди
        if self.is_empty():
            raise IndexError
        return self._data.popleft() # удаляет элемент с левого конца deque
    def peek(self): 
        if self.is_empty():
            return None
        return self._data[0] #обращение к первому элементу deque
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)
    def __str__(self): #Преобразует deque в список для красивого отображения
        return f"Queue({list(self._data)})"

if __name__ == "__main__":
    s = Stack() #Демонстрация стека
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(f"peek: {s.peek()}")
    print(f"pop: {s.pop()}")
    print(s)
    print() 
    q = Queue() #Демонстрация очереди
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)
    print(f"peek: {q.peek()}")
    print(f"dequeue: {q.dequeue()}")
    print(q)