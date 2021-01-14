# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제2(벡터)
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max((5, 10)) = 10

class Vector(object):
    def __init__(self, *args):
        '''
            Create a vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:  # Vector()으로 넘겼을 때
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        ''' Return the vector information '''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return the vector addtion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


print(Vector.__init__.__doc__)  # Create a vector, example : v = Vector(5, 10)

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()  # 0,0

print(v1, v2, v3)  # Vector(5, 7) Vector(23, 35) Vector(0, 0)
print(v1 + v2)  # Vector(28, 42)
print(v1 * 3)  # Vector(15, 21)
print(v2 * 10)  # Vector(230, 350)
print(bool(v1), bool(v2))  # True True
print(bool(v3))  # False
