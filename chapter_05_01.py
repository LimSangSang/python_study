# 일급 함수(first class, 일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화 - 실행 시점에 초기화
# 2. 함수를 변수 할당 가능
# 3. 함수의 인자에 다른 함수를 인수로 전달 가능
# 4. 함수의 반환값(return)으로 함수를 전달 가능

# 파이썬과 first-class 함수
# - 사실 파이썬에서는 모든 것이 객체 취급
# - 파이썬 함수도 객체로 되어있어서, 기본 함수 기능 이외 객체와 같은 활용이 가능
#  -> 즉 파이썬 함수들은 first-class 함수로 사용 가능
# * 지금까지 배운 언어의 맥락과는 다른 사고 -> 함수형 프로그래밍에서 부터 고안된 기법

# 언어별 first-class 지원 여부
# - python, Go, javascript, Kotlin은 first-class 지원
# - C 언어 등은 미지원 


# 함수 객체

from functools import partial
from operator import mul
from operator import add
from functools import reduce

# 수학 factorial : 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    '''Factorial Function -> n:int'''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass


print(factorial(5))  # 120 -> 5*4*3*2*1
print(factorial.__doc__)  # Factorial Function -> n:int
print(type(factorial), type(A))  # <class 'function'> <class 'type'>
print(dir(factorial))  
# 클래스가 아니고 함수이지만 객체 취급
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


print(set(sorted(dir(factorial))) - set(sorted(dir(A))))  # 함수 - 클래스 -> 클래스가 가진 속성은 전부 뺐음 (함수만 남음)
# {'__qualname__', '__closure__', '__call__', '__name__', '__annotations__', '__get__', '__defaults__', '__code__', '__kwdefaults__', '__globals__'}
print(factorial.__name__)  # factorial
print(factorial.__code__) # 함수가 정의된 위치
# <code object factorial at 0x7fc9e61702f0, file "/Users/seula/Desktop/test/python_study/chapter_05_01.py", line 10>

# 변수 할당
var_func = factorial
print(var_func)  # <function factorial at 0x7fc4d615f1f0> factorial 할당 됨
print(var_func(10))  # 3628800
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce

print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))  # [1, 6, 120]
print([var_func(i) for i in range(1, 6) if i % 2])  # [1, 6, 120]

# reduce

print(reduce(add, range(1, 11)))  # 55
print(sum(range(1, 11)))  # 55

# 익명함수(Lambda)
# 가급적 주석 작성, 복잡한 함수일 때는 다른 사람이 알아보기 어려움
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x+t, range(1, 11)))  # 55

# Callable: 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(list), callable(
    var_func), callable(factorial), callable(3.14), callable('3.14'))  # True True True True False False
# 3.14(334) # 'float' object is not callable

# partial 사용법 : 인수 고정 -> 콜백 함수 사용

print(mul(10, 10))  # 100

# 인수 고정
five = partial(mul, 5) # 5 * ?

# 고정 추가
six = partial(five, 6)
print(five(10))  # 50
print(six())  # 30
# print(six(3)) # mul expected 2 arguments, got 3
print([five(i) for i in range(1, 10)])  # [5, 10, 15, 20, 25, 30, 35, 40, 45]
print(list(map(five, range(1, 10))))  # [5, 10, 15, 20, 25, 30, 35, 40, 45]
