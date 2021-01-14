# 시퀀스 형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블(해시테이블 키가 중복될 경우 내부적으로 어떻게 처리하느냐? 면접 질문 많이 나옴)
# Key에 Value를 저장하는 구조
# 파이썬 자체가 강력한 해쉬테이블 엔진으로 만들어졌다고 소개됨
# 파이썬 딕셔너리가 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조(중요) - 1억건의 데이터가 쌓여있어도 주민번호 뒷자리가 2이면 여자인 걸 알 수 있음
# key 값을 해싱 함수를 통해서 해쉬 주소값이 나오고, 이것을 기반으로 key에 대한 value의 위치를 알 수 있다.

# dict 구조
# print(__builtins__.__dic__) # 파이썬 엔진이 해쉬테이블로 소개되어있음

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])


print(hash(t1))  # 465510690262297113
# print(hash(t2)) # TypeError: unhashable type: 'list' -> list는 수정가능한 mutable형. 리스트 값을 언제든지 바꿀 수 있기 때문에 오류남

# Dict Setdefault 예제 : 튜플에서 딕셔너리 만들때  속도향상 됨(레퍼런스 권장)
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5')
)

new_dict1 = {}
new_dict2 = {}

# Not use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)  # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}
from collections import defaultdict
# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v) # k를 기준으로 리스트를 만든다.
print(new_dict2)  # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

new_dict4 = defaultdict(list)
print(new_dict4)

# 주의
new_dict3 = {k: v for k, v in source}  # 덮어써버림
print(new_dict3)  # {'k1': 'val2', 'k2': 'val5'}
