# 코루틴: 단일(싱글) 스레드, 스텍을 기반으로 동작하는 비동기 작업
# thread:os에서 관리, cpu코어에서 실시간/시분할 비동기 작업->멀티스레드
# yield, send: 메인과 서브루틴이 상호작용
# 코루틴을 제어, 상태, 양방향 전송할 때 yield 키워드를 사용 
# def -> async, yield -> wait으로 사용할 수 있다.

# 서브루틴: 메인루틴에서 호출하면 서브루틴에서 수행(흐름제어)
# 코루틴: 루틴 실행 중 중지한 후 다시 실행할 수 있음 -> 동시성 프로그래밍
# 코루틴 장점: 스레드에 비해 오버헤드 감소(싱글 스레드이기 때문)
# 멀티 스레드는 메모리를 공유할 수도 있기 때문에 복잡하다. 그리고 공유되는 자원이 많아서 교착상태 발생 => 컨텍스트 스위칭 비용 큼, 자원 소비 가능성 증가.
# 컨텍스트 스위칭 비용 클 때는 싱글 스레드가 더 빠를 수 있음

# 코루틴 ex1
# 서브루틴
def coroutine1():
    print('>>> coroutine stated.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언
# 메인 루틴
cr1 = coroutine1()
print(cr1, type(cr1)) # <generator object coroutine1 at 0x7fc9a5ab74d0> <class 'generator'>

next(cr1) # >>> coroutine stated.
# yield 지점가지 서브루틴 수행
# next(cr1) 
# >>> coroutine received : None
# Traceback (most recent call last):
#   File "chapter_06_03.py", line 25, in <module>
#     next(cr1)
# StopIteration

# # send()를 통해 메인루틴과 서브루틴 데이터를 공유할 수 있음. 기본 전달값 None
# cr1.send(100)
# # >>> coroutine received : 100
# # Traceback (most recent call last):
# #   File "chapter_06_03.py", line 33, in <module>
# #     cr1.send(100)
# # StopIteration

# 잘못된 사용
# cr2 = coroutine1()
# cr2.send(100)
# # Traceback (most recent call last):
# #   File "chapter_06_03.py", line 34, in <module>
# #     cr1.send(100)
# # TypeError: can't send non-None value to a just-started generator
# # next()없이 바로 send보낼 수 없음. 코루틴 컨텍스트 안에 yield에서 멈춘다음 실행해야 함

# 코루틴 ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태(중요. send로 받고 보낼 수 있음)
# GEN_CLOSED : 실행 완료 상태

from inspect import getgeneratorstate

def coroutine2(x):
    print('>>> coroutine stated : {}'.format(x))
    y = yield x
    print('>>> coroutine received1: {}'.format(y))
    z = yield x + y
    print('>>> coroutine received2: {}'.format(z))

cr3 = coroutine2(10) # >>> coroutine stated.
print(getgeneratorstate(cr3)) # GEN_CREATED
print(next(cr3))
# >>> coroutine stated : 10
# 10
print(getgeneratorstate(cr3)) # GEN_SUSPENDED
cr3.send(100)
# >>> coroutine received : 100
# 100
# print(cr3.send(100)) 
# >>> coroutine received : 100
# 110
print(getgeneratorstate(cr3)) # GEN_SUSPENDED
# cr3.send(50)

# 코루틴 ex3
# StopIteration는 3.5 이상에서 await으로 자동 처리할 수 있다.
# 중첩 코루틴 처리

def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y

t1 = generator1()
print(next(t1)) # A
print(next(t1)) # B
print(next(t1)) # 1
print(next(t1)) # 2
print(next(t1)) # 3

t2 = generator1()
print(list(t2)) # ['A', 'B', 1, 2, 3] 알아서 next호출해서 리스트 생성

def generator2():
    yield from 'AB'
    yield from range(1, 4)

t3 = generator2()
print(next(t3)) # A
print(next(t3)) # B
print(next(t3)) # 1
print(next(t3)) # 2
print(next(t3)) # 3