# 클로져 심화

def closure_ex1():
    # Free variable 자유 영역
    # 클로져 영역
    series=[]
    def averager(v):
        series.append(v)
        print(len(series))
        print('inner >>> {}/{}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager # first class 특징: 함수를 결과로 반환 가능

avg_closure1 = closure_ex1()

print(avg_closure1(10))
# inner >>> [10]/1
# 10.0
print(avg_closure1(30))
# inner >>> [10, 30]/2
# 20.0
print(avg_closure1(50))
# inner >>> [10, 30, 50]/3
# 30.0

# function inspection
print(dir(avg_closure1))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
print(dir(avg_closure1.__code__))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']
print(avg_closure1.__code__.co_freevars) # ('series',)
print(dir(avg_closure1.__closure__[0]))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'cell_contents']
print(avg_closure1.__closure__[0].cell_contents) # [10, 30, 50]
# print(avg_closure1.__closure__[1].cell_contents) # # IndexError: tuple index out of range

# # 잘못된 클로져 사용
def closure_ex2():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1 # cnt = cnt + 1 도 같은 에러
        total += v # total = total + 1 같은 에러
        return total / cnt
    return averager
avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # UnboundLocalError: local variable 'cnt' referenced before assignment

def closure_ex3():
    # free variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # cnt, total은 free 변수가 됨
        cnt += 1 # cnt = cnt + 1 도 같은 에러
        total += v # total = total + 1 같은 에러
        return total / cnt
    return averager
avg_closure3 = closure_ex3()
print(avg_closure3(15)) # 15.0
print(avg_closure3(35)) # 25.0
print(avg_closure3(40)) # 30.0