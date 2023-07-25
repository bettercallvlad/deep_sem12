# Создайте класс-функцию, который считает факториал
# числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.

# Доработаем задачу 1.
# Создайте менеджер контекста,
# который при выходе сохраняет значения в JSON файл.
import json


class Factorial:
    def __init__(self, k) -> None:
        self.k = k
        self.history = []

    def __call__(self, fact: int) -> int:
        res = 1
        for i in range(1, fact+1):
            res *= i
        if len(self.history) >= self.k:
            self.history.pop(0)

        self.history.append({fact: res})

        return self.history[-1]

    def show_history(self) -> list[dict[int, int]]:
        return self.history

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open('results_facotial.json', 'w') as log:
            json.dump(self.history, log, indent=2)


get_fact = Factorial(3)
# for i in range(1, 4):
#     get_fact(i)
# print(get_fact.show_history())
# for i in range(4, 5):
#     get_fact(i)
# print(get_fact.show_history())

with get_fact as fact:
    for i in range(1, 5):
        fact(i)
    print(fact.show_history())
