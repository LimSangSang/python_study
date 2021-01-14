# 병행성(Concurrency)
# 이터레이너, 제너레이터
# iterator, generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args ...: iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 반복 가능한 이유는 내부적으로 iter(x) 함수가 호출되었다.
for c in t:
    print(c) # A B C D ...

# while문
w = iter(t)
while True:
    try:
        print(next(w)) # 위와 출력값이 같음
    except StopIteration:
        break
# c와 출력값이 똑같은데 while문이 더 길다. 실제로는 for문 사용하면 되는데 어떻게 동작하는지 메커니즘만 확인한 것.

from collections import abc # abc(Abstract Base Class)
# 반복형 확인
# print(dir(t)) # 이러한 방식으로 하면 내가 원하는 값을 찾기 힘듦
print(hasattr(t, '__iter__')) # True
# hasattr(has attribute) : iter속성을 가지고있니?
print(isinstance(t, abc.Iterable)) # true
# isinstance: 인스턴스가 특정 클래스/데이터 타입인지 검사하는 함수.

# next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('ABC DEF GHI JKL')

print(wi) # WordSplit(['ABC', 'DEF', 'GHI', 'JKL'])
print(next(wi)) 
# Called __next__
# ABC
print(next(wi)) 
# Called __next__
# DEF
print(next(wi)) 
# Called __next__
# GHI
print(next(wi)) 
# Called __next__
# JKL

# generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 등을 만들 때 데이터 양 증가하고 메소리 사용량도 증가한다. -> generator 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동 
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # yield가 다음에 나올 위치값 기억
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('ABC DEF GHI JKL')