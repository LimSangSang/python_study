# Chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2019.08.22
    Description: Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self: 객체의 고유한 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))  # print(id(car1))과 값 같음
        print('Car Detail Info : {}{}'.format(
            self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before car price -> Company: {}, price: {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After car price -> Company: {}, price: {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please enter 1 or more')
            return
        cls.price_per_raise = per
        print('Successed! price increased.')

    # Static Method
    # 파라미터를 아무것도 받지 않음
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! this car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'


# Self 의미
car1 = Car("Ferrai", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "black", "horsepower": 270, "price": 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
# 인스턴스 함수에 직접 접근해서 가격을 얻어올 수 있음
# 그러나, 안 좋은 방법. 그래서 private로 막아놓음
# 변수 값이 변경됨으로서 크게 변경될 가능성이 있음
# 보통은 메서드를 만들어서 내가 필요로한 정보를 리턴하게 함
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메소드 사용)
# 위처럼 클래스 변수를 수정하는 것보다 메소드로 사용하는 걸 더 추천
# if문처럼 로직도 추가 가능
# 클래스 변수를 핸들링할 때는 클래스 메소드를 사용하는 걸 추천
Car.raise_price(1)
Car.raise_price(1.6)

# 인스턴스 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
