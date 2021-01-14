# 시퀀스 형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# Tuple Advanced
# Unpacking

# b, a = a, b (다른 언어는 임시 변수를 만들어서 a, b를 각각 할당했다가 그 다음 교차해주는게 필요한데 python은 바로 할당 가능)

print(divmod(100, 9))  # divmod는 100을 9로 나눈 몫과 나머지를 반환해주는 함수(11, 1)
# print(divmod((100, 9))) TypeError: divmod expected 2 arguments, got 1
print(divmod(*(100, 9)))  # 튜플을 풀어서 넣어줘야함 (11, 1)
print(*(divmod(100, 9)))  # 11 1 결과값 튜플이 풀림

# x, y, rest = range(10) # ValueError: too many values to unpack (expected 3)
x, y, *rest = range(10)
print(x, y, rest)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest)  # 0 1 []
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)  # 1 2 [3, 4, 5]

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)  # tuple 불변
m = [15, 20, 25]  # list 가변

# 새로운 변수를 재할당 했기 때문에 id값이 전부 다름
print(l, id(l))  # (15, 20, 25) 140361051709568
print(m, id(m))  # [15, 20, 25] 140361052258432

l = l * 2
m = m * 2

print(l, id(l))  # (15, 20, 25, 15, 20, 25) 140361051798496
print(m, id(m))  # [15, 20, 25, 15, 20, 25] 140361052258368

l *= 2
m *= 2

print(l, id(l))
# (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 140361015516176
# 불변형은 한 번 id값을 할당하면 수정을 할 수 없기 때문에 id가 재할당 이루어짐
print(m, id(m))
# [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 140361052258368
# 가변형은 자기 id값에 추가를 한다

# sort vs sorted
# reverse, key=len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체 반환(원본 수정x)
f_list = ['orange', 'apple', 'mango',
          'papaya', 'lemon', 'strawberry', 'coconut']
# sorted -  ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']
print('sorted - ', sorted(f_list))
# sorted -  ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
print('sorted - ', sorted(f_list, reverse=True))
# sorted -  ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry']
print('sorted - ', sorted(f_list, key=len))  # 길이순
# sorted -  ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry']
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))  # 단어 끝 글자부터 정렬
# print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))
# print(f_list)

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인(None) - 반환값이 없음
# sort -  None ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry'] -> 원본이 수정됨
print('sort - ', f_list.sort(), f_list)
# sort -  None ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple'] 
print('sort - ', f_list.sort(reverse=True), f_list)
# sort -  None ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry']
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list)
# sort -  None ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya']
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
