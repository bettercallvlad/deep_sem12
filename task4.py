# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину
# и ширину на дескриптор с валидацией размера.

class Range:
    def __set_name__(self, own, name):
        self.p_name = '_' + name

    def __get__(self, inst, own):
        return getattr(inst, self.p_name)

    def __set__(self, inst, val):
        self.is_valid(val)
        setattr(inst, self.p_name, val)

    def is_valid(self, val):
        if val <= 0:
            raise ValueError


class Rectangle:
    __slots__ = ('_width', '_length')

    width = Range()
    length = Range()

    def __init__(self, width, length):
        self.width = width
        self.length = length

    # @property
    # def width(self):
    #     return self._width

    # @width.setter
    # def width(self, value):
    #     self._width = value

    # @property
    # def length(self):
    #     return self._length

    # @length.setter
    # def length(self, length):
    #     self._length = length

    def area(self):
        return self.width * self.length

    def perimetr(self):
        return 2 * (self.width + self.length)

    def __add__(self, other):
        summary_perimetr = self.perimetr() + other.perimetr()
        width_rectangle_c = self.width
        length_rectangle_c = summary_perimetr / 2 - width_rectangle_c

        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __sub__(self, other):
        sub_perimetr = abs(self.perimetr() - other.perimetr())
        width_rectangle_c = min(self.width, other.width,
                                self.length, other.length)
        length_rectangle_c = sub_perimetr / 2 - width_rectangle_c

        return Rectangle(width_rectangle_c, length_rectangle_c)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()


rect = Rectangle(1, 2)
rect.width = -1
print(rect.width)
