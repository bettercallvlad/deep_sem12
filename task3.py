# Создайте класс-генератор. Экземпляр класса должен генерировать
# факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class FactorialGenerator:
    def __init__(self, stop: int,
                 start: int = 1,
                 step: int = 1) -> None:
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.stop:
            raise StopIteration
        return self.calc_fact(self.current)

    @staticmethod
    def calc_fact(fact):
        res = 1
        for i in range(1, fact+1):
            res *= i
        return res


factorial = FactorialGenerator(5)
for i in factorial:
    print(i)
