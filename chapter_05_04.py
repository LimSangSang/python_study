# 일급 함수
# 클로저 기초
# 데코레이터(Decorator)

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 함수
# 3. 조합해서 사용 용이

# 단점
# 1. 코딩하는 것에 따라 다르지만 가독성이 감소할 수 있다.
# 2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리할 수 있다.
# 3. 디버깅 불편

# 데이터 실습
import time
from functools import wraps

def perf_clock(func):
    '''perf_clock 의 주석입니다.'''
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' %(et, name, arg_str, result))

        return result
    return perf_clocked

def time_func(seconds):
    '''time_func 의 주석입니다.'''
    time.sleep(seconds)

def sum_func(*numbers):
    '''sum_func 의 주석입니다.'''
    return sum(numbers)

# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars) 
# <function perf_clock.<locals>.perf_clocked at 0x7f7fb89b9830> ('func',)
print(none_deco2, none_deco2.__code__.co_freevars)
# <function perf_clock.<locals>.perf_clocked at 0x7f7fb89c7200> ('func',)

# print('-' * 40, 'Called None Decorator -> time_func')
# print()
# none_deco1(1.5) # [1.50468s] time_func(1.5) -> None
# print('-' * 40, 'Called None Decorator -> sum_func')
# print()
# none_deco2(100, 200, 300, 400, 500) # [0.00001s] sum_func(100, 200, 300, 400, 500) -> 1500

# 데코레이터 사용

@perf_clock
def time_func2(seconds):
    '''time_func2 의 주석입니다.'''
    time.sleep(seconds)

@perf_clock
def sum_func2(*numbers):
    '''sum_func2 의 주석입니다.'''
    return sum(numbers)

# print('-' * 40, 'Called Decorator -> time_func')
# print()
# time_func2(1.5) # [1.50255s] time_func2(1.5) -> None
# print('-' * 40, 'Called Decorator -> sum_func')
# print()
# sum_func2(100, 200, 300, 400, 500) # [0.00001s] sum_func2(100, 200, 300, 400, 500) -> 1500

print(time_func2.__name__)
print(time_func.__name__)
print(time_func2.__doc__)
print(time_func.__doc__)