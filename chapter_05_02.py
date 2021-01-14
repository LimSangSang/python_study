# 일급 함수
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능
# 파이썬 변수 범위(scope)

# ex1
def func_v1(a):
    print(a)
    print(b)
# func_v1(10) # NameError: name 'b' is not defined


# ex2
b = 20
def func_v2(a):
    print(a) # 10 지역 변수
    print(b) # 20 글로별 변수


func_v2(10)

# ex3
# c = 30
# def func_v3(a):
#     global c # 함수 내에 global을 사용하는 건 좋지 않음
#     #c = 40
#     print(a)
#     print(c)
#     # c = 40 # UnboundLocalError: local variable 'c' referenced before assignment
#     # 함수 안에 같은 변수가 있을 때는 로컬 변수로 인식. 그래서 위에 선언해줘야 함
#     c = 40


# print('>>', c)  # 30
# func_v3(10)
# print('>>>', c)  # 40

# closure 사용 이유
# 서버 프로그래밍에서 중요한건 동시성(Concurrency) 제어 
# -> 한정된 메모리 공간에 여러 자원이 접근하기 때문에 교착상태(Dead Lock)이 일어남
# -> 파이썬에서는 이러한 문제를 회피하기 위해서 메모리를 공유하지 않고 메세지 전달로 처리하기 위한 여러 언어들이 나옴 -> erlang , python ..
# 파이썬에서 클로저는 공유하되 변경되지 않는다(immutable, read only). 클로저를 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM을 통해 멀티스레드 프로그래밍에 강점 제공
# 하지만 우리는 멀티스레드를 사용하지 않고 코루틴을 사용하여 단일 스레드 환경에서도 멀티스레드가 처리하는 것처럼 사용

a = 100

print(a + 100) # 200
print(a + 1000) # 1100

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

# 누적
print(averager_cls(10)) 
# inner >> [10] / 1
#10.0
print(averager_cls(30))
# inner >> [10, 30] / 2
# 20.0
print(averager_cls(50))
# inner >> [10, 30, 50] / 3
# 30.0