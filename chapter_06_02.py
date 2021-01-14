# 병행성(Concurrency): 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러일을 쉽게 해결
# 병행성(Parallelism): 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')

temp = generator_ex1()

# print(temp) # <generator object generator_ex1 at 0x7fb1311b7250>
# print(next(temp)) 
# # Start 
# # A Point
# print(next(temp))
# # Continue
# # B Point
# print(next(temp))
# # End
# # print(next(temp)) # 호출할 다음 값이 없으면 에러 발생
# # Traceback (most recent call last):
# #  File "chapter_06_02.py", line 18, in <module>
# #     print(next(temp))
# # StopIteration

for v in generator_ex1():
    pass
    # print(v)
    # Start
    # A Point
    # Continue
    # B Point
    # End

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2) # ['A PointA PointA Point', 'B PointB PointB Point']
print(temp3) # <generator object <genexpr> at 0x7f9321ab75d0>

for i in temp2:
    print(i)
    # A PointA PointA Point
    # B PointB PointB Point

for i in temp3:
    print(i)
    # Start
    # A PointA PointA Point
    # Continue
    # B PointB PointB Point
    # End



# Genereator Ex3(중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby ...

import itertools

gen1 = itertools.count(1, 2.5) # count(시작, 증가 단위) -> 무한대로 늘어남

print(next(gen1)) # 1
print(next(gen1)) # 3.5
print(next(gen1)) # 6.0
print(next(gen1)) # 8.5
# ... 무한

# while True: # 무한 루프라 시스템 다운될 수도 있음
#     print(next(gen1))

gen2 = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2.5))

for v in gen2:
    print(v)
    # 1
    # 3.5
    # 6.0
    # 8.5

# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])

for v  in gen3:
    print(v) 
    # 3
    # 4
    # 5

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 11)])

for v in gen4:
    print(v)
    # 1
    # 3
    # 6
    # 10
    # 15
    # 21
    # 28
    # 36
    # 45
    # 55

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5)) # ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6)) # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7)) # [('A',), ('B',), ('C',), ('D',), ('E',)]

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8)) 
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D'), ('D', 'E'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('E', 'E')]

# 그룹화
gen9 = itertools.groupby('AABBBBCCCCDDEEE')
# print(list(gen9))
# [('A', <itertools._grouper object at 0x7fe7452f2790>), ('B', <itertools._grouper object at 0x7fe7452f2550>), ('C', <itertools._grouper object at 0x7fe7452f27d0>), ('D', <itertools._grouper object at 0x7fe7452f2810>), ('E', <itertools._grouper object at 0x7fe7452f2850>)]

for chr, group in gen9:
    print(chr, ' : ', list(group))
    # A  :  ['A', 'A']
    # B  :  ['B', 'B', 'B', 'B']
    # C  :  ['C', 'C', 'C', 'C']
    # D  :  ['D', 'D']
    # E  :  ['E', 'E', 'E']