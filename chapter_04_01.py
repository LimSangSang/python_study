# 시퀀스 형
# 시퀀스는 정렬된 셋(ordered set)의 일반적인 용어다.  순서를 가지고 나열되어 있는 객체
# 컨테이너(Container: 서로 다른 자료형을 담을 수 있음[list, tuple, collections.deque])
# ex) a = [3, 3.0, 'a']
# 플랫(Flat: 한개의 자료형만 담을 수 있음[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) - 한 번 선언하면 변경 가능
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)

import array
chars = '+_)(*&^%$#@!'  # str: 플랫&불변
# chars[2] = 'h' # TypeError: 'str' object does not support item assignment -> str은 불변형이기 때문에 바꿀 수 없음
code_list1 = []

for s in chars:
    code_list1.append(ord(s))  # ord() : 문자의 아스키 코드 값을 돌려주는 함수
print(code_list1)  # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]

code_list2 = [ord(s) for s in chars]
print(code_list2)  # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

print(code_list3)  # [43, 95, 41, 42, 94, 64]
print(code_list4)  # [43, 95, 41, 42, 94, 64]
# ['+', '_', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!']
print([chr(s) for s in code_list1])
# ['+', '_', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!']
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])  # ['+', '_', ')', '*', '^', '@']
print([chr(s) for s in code_list4])  # ['+', '_', ')', '*', '^', '@']

# Generator 생성
# generator 는 간단하게 설명하면 iterator 를 생성해 주는 function이고, iterator 는 next() 메소드를 이용해 데이터에 순차적으로 접근이 가능한 object이다. 파이썬에서 성능 및 효율적으로 코드를 작성하기 위해 제네레이터 패턴을 많이 사용한다. 제네레이터는 간단하게 설명하면 배열이나 리스트와 같은 반복가능한 연속적인 값들을 생성해내는 패턴이고 가장 중요한 점은 모든 값을 포함하여 반환하는 대신 호출할 때마다 한 개의 값을 리턴한다. 때문에 아주 작은 메모리로 효율적 대용량 반복가능한 구조를 순회할 수 있음.
# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x), 다음에 내가 반환해야 할 값만 가지고 있음
# https://docs.python.org/ko/3/library/array.html
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(tuple_g)  # <generator object <genexpr> at 0x7ffa59270970>
print(array_g)  # array('I', [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33])
print(type(tuple_g))  # <class 'generator'>
print(next(tuple_g))  # 43
print(type(array_g))  # <class 'array.array'>
print(array_g.tolist())  # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]

# Generator 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
# <generator object <genexpr> at 0x10b968970>
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

# 리스트 주의(꼭 알아두어야함)
# deep copy vs shallow copy
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4
# [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks1)
# [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks2)

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

# [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks1)
# [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]
print(marks2)
# 각각 결과 값이 다름. marks1은 정확하게 복사가 됐기 때문에 모두 주소값이 다름. marks2는 하나의 주소값이 계속 복사가 됐기 때문에 변경된 값이 똑같다.

# 증명
# [4515663616, 4515663424, 4515663360, 4515663168]
print([id(i) for i in marks1])
# [4515663104, 4515663104, 4515663104, 4515663104]
print([id(i) for i in marks2])
