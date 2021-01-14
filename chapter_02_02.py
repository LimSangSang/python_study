# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2019.11.08
    """

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))  # print(id(car1))과 값 같음
        print('Car Detail Info : {}{}'.format(
            self._company, self._details.get('price')))


# Self 의미
car1 = Car("Ferrai", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("Ferrai", {"color": "black", "horsepower": 300, "price": 6000})

# ID 확인
print(id(car1))  # 4499774912
print(id(car2))  # 4499967952
print(id(car3))  # 4500201968

print(car1._company == car2._company)  # False
print(car1 is car2)  # False

print(dir(car1))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details']
print(dir(car2))  # 위와 같음

# {'_company': 'Ferrai', '_details': {'color': 'white', 'horsepower': 400, 'price': 8000}}
print(car1.__dict__)
# {'_company': 'Bmw', '_details': {'color': 'black', 'horsepower': 270, 'price': 5000}}
print(car2.__dict__)

# Doctring
print(Car.__doc__)  # Car class
# Author : Kim
# Date : 2019.11.08

car1.detail_info()  # Current ID : 4499774912 # Car Detail Info : Ferrai8000 -> 자동으로 매개변수 전달
# Car.detail_info()  # Error : TypeError: detail_info() missing 1 required positional argument: 'self'
# Current ID : 4394155456 Car Detail Info : Ferrai8000 -> 클래스 이름으로 접근했을 때는 매개변수가 자동으로 접근되지 않기 때문에 명시적으로 전달해줘야 함
Car.detail_info(car1)

# <class '__main__.Car'> <class '__main__.Car'>
print(car1.__class__, car2.__class__)
# 140555443029472 140555443029472
print(id(car1.__class__), id(car2.__class__))
# 우리는 인스턴스(car1, car2, car3)을 출력한 게 아니라 클래스 자체를 id 값으로 본 것이기 때문에 id가 똑같다.
print(id(car1.__class__) == id(car2.__class__))  # True

# 공유확인
# {'_company': 'Ferrai', '_details': {'color': 'white', 'horsepower': 400, 'price': 8000}} -> 클래스에서 선언한 car_count가 없음
print(car1.__dict__)
# {'_company': 'Bmw', '_details': {'color': 'black', 'horsepower': 270, 'price': 5000}} -> 클래스에서 선언한 car_count가 없음
print(car2.__dict__)
print(car1.car_count)  # 3 -> 네임스페이스는 없는데 car_count는 나옴
print(dir(car1))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details', 'car_count', 'detail_info'] -> car_count 있음 -> 클래스 변수까지 접근할 때는 __dict__보다 dir로 접근하는게 더 좋음

print(car1.car_count)  # 3
print(Car.car_count)  # 3

del car2
# 삭제 확인
print(car1.car_count)  # 2
print(Car.car_count)  # 2

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 없으면 상위(클래스 변수, 부모 클래스 변수)를 찾음)
