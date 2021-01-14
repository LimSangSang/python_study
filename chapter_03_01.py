# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print(int(10))  # 10
print(int)  # <class 'int'>
print(float)  # <class 'float'>

# 모든 속성 및 메소드 출력
# dir : dir()내장함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 매소드를 가지고 있는지 나열해준다.
print(dir(int))  # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
print(dir(float))  # ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

n = 10
print(type(n))  # <class 'int'>
print(n+100)  # 110
print(n.__add__(100))  # 110
print(n.__doc__)  # int의 의미, 주석
print(n.__bool__(), bool(n))  # True, True (0이면 False)
print(n * 100, n.__mul__(100))  # 1000, 1000

# 클래스 예제1


class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit class info: {}, {}'.format(self._name, self._price)

    def __add__(self, x):
        print('Called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called __sub__')
        return self._price - x._price

    def __le__(self, x):  # 작거나 같다.
        print('Called __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):  # 크거나 같다.
        print('Called __ge__')
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 이렇게 접근하는 것은 좋지 않음
# 코드 양도 늘어나고 가독성도 좋지 않음
print(s1._price + s2._price)  # 10500

print(s1 + s2)  # 10500
print(s1 - s2)  # 4500

# 매직 매소드
print(s1 >= s2)  # True __ge__
print(s1 <= s2)  # False __le__
print(s1 - s2)  # 4500 __sub__
print(s2 - s1)  # -4500 __sub__
print(s1)  # Fruit class info: Orange, 7500
print(s2)  # Fruit class info: Banana, 3000
