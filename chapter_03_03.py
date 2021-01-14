# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체는 id, type값을 확인 할 수 있음


from math import sqrt  # 루트
# 튜플은 index로 접근하므로 직관적이지 않지만 네임드 튜플은 이름으로 접근 가능
from collections import namedtuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

# 일반적인 튜플
l_length1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_length1)

# 네임드 튜플
# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3)  # Point(x=1.0, y=5.0)
# print(pt3.x)  # 1.0
# print(pt4)  # Point(x=2.5, y=1.5)

# 키로도 접근 가능하다. 데이터 관리나 흐름을 따라가는건 namedtuple이 더 직관적이다.
l_length2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_length2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])  # Point1,2,3 다 같은 선언
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')

# Type names and field names cannot be a keyword: 'class'
# Point4 = namedtuple('Point', 'x y x class')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default = False
print(Point4)  # <class '__main__.Point'>

# <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>
print(Point1, Point2, Point3, Point4)

# Dick to Unpacking
temp_dic = {'x': 75, 'y': 55}

p1 = Point1(x=10, y=35)  # p1, p2, p3 선언 방식 다 똑같음
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
# p4 = Point4(10, 20, 30) # TypeError: __new__() missing 1 required positional argument: '_3'
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dic)

print(p1)  # Point(x=10, y=35)
print(p2)  # Point(x=20, y=40)
print(p3)  # Point(x=45, y=20)

# rename 테스트
print(p4)  # Point(x=10, y=20, _2=30, _3=40)
print(p5)  # Point(x=75, y=55)

# 사용
print(p1[0] + p2[1])  # 50
print(p1.x + p2.y)  # 50 값은 같지만 이 방법을 더 추천. index로 접근하는 거 비추천

# Unpacking
x, y = p2
print(x, y)  # 20, 40

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)  # Point(x=52, y=38)

# _fields : 필드 네임 확인 -> 키 값 조회할 때 쓴다.
print(p1._fields, p2._fields, p3._fields)  # ('x', 'y') ('x', 'y') ('x', 'y')

# _asdict() : OrderedDict 정렬된 딕셔너리 반환(원래 딕셔너리는 정렬되지 않음)
print(p1._asdict())
print(p2._asdict())

# 실 사용 실습
# 한 반에 20명, 4개의 반(A, B, C, D)
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
print(numbers)
print(ranks)  # ['A', 'B', 'C', 'D']

# list Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))  # 80
# [Classes(rank='A', number='1'), Classes(rank='A', number='2'), Classes(rank='A', number='3'), Classes(rank='A', number='4'), Classes(rank='A', number='5'), ...]
print(students)

# 추천
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]
# print(len(students2))  # 80
# print(students2)

for s in students2:
    print(s)
