# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩

# 차량1
car_company_1 = "Ferrari"
car_detail_1 = [
    {"color": "white"},
    {"horsepower": 400},
    {"price": 8000}
]

# 차량2
car_company_1 = "BMW"
car_detail_1 = [
    {"color": "black"},
    {"horsepower": 270},
    {"price": 5000}
]

# 차량3
car_company_1 = "Audi"
car_detail_1 = [
    {"color": "silver"},
    {"horsepower": 300},
    {"price": 6000}
]

# 리스트 구조
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "white", "horsepower": 400, "price": 8000},
    {"color": "black", "horsepower": 270, "price": 5000},
    {"color": "black", "horsepower": 300, "price": 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {"car_company": "Ferrai", "car_detail": {
        "color": "white", "horsepower": 400, "price": 8000}},
    {"car_company": "BMW", "car_detail": {
        "color": "black", "horsepower": 270, "price": 5000}},
    {"car_company": "Audi", "car_detail": {
        "color": "black", "horsepower": 300, "price": 6000}}
]

del car_dicts[1]
print(car_dicts)

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용


class Car():
    # 매직 메소드, 스페셜 매소드라고도 함
    def __init__(self, company, details):
        self._company = company
        self._details = details
        # 출력하면 <__main__.Car object at 0x101709f70> => Car의 object라고 표현한 것

    # 파이썬에서 미리 만들어놓은 메소드를 활용하면 이 클래스 정보를 디테일하게 출력 가능
    def __str__(self):
        # 비 공식적인, 레퍼런스에 의하면 프린트 문으로 문자열을 확인하고 싶을 때. 사용자 입장에서 출력을 원할 때.
        # 사용자 레벨에서 프린트 문으로 정보를 확인할 때.
        # 기본값__str__이 있으면 먼저 실행
        # __str__, __repr__ 둘 다 없을 때 상위 정보 __init__ 실행
        # str : Ferrai - {'color': 'white', 'horsepower': 400, 'price': 8000}
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        # 자료형에 타입에 따른 객체를 그대로 표시하고 싶을 때(__str__보다 더 엄격)
        # 개발자, 엔지니어 레벨에서 객체의 엄격한 타입, 정보를 알 수 있는 공식적인 문자열로 표현할 때 사용
        # __str__이 없을 때 사용
        return 'repr: {} - {}'.format(self._company, self._details)


car1 = Car("Ferrai", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("Ferrai", {"color": "black", "horsepower": 300, "price": 6000})

# str: Ferrai - {'color': 'white', 'horsepower': 400, 'price': 8000}
print(car1)
print(car2)  # str: Bmw - {'color': 'black', 'horsepower': 270, 'price': 5000}
# str: Ferrai - {'color': 'black', 'horsepower': 300, 'price': 6000}
print(car3)

# __dic__으로 접근하면 안의 속성을 다 볼 수 있음
# {'_company': 'Ferrai', '_details': {'color': 'white', 'horsepower': 400, 'price': 8000}}
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# [repr: Ferrai - {'color': 'white', 'horsepower': 400, 'price': 8000}, repr: Bmw - {'color': 'black', 'horsepower': 270, 'price': 5000}, repr: Ferrai - {'color': 'black', 'horsepower': 300, 'price': 6000}]
print(car_list)
# 여기에서는 __str__출력이 아님. 왜냐하면 리스트 안에서 객체에 대한 정보를 보여주기 때문에.


for x in car_list:
    # print(x)
    # str: Ferrai - {'color': 'white', 'horsepower': 400, 'price': 8000}
    #str: Bmw - {'color': 'black', 'horsepower': 270, 'price': 5000}
    #str: Ferrai - {'color': 'black', 'horsepower': 300, 'price': 6000}
    print(repr(x))  # 별로 안 중요. 파이썬이 알아서 구별해줌
    #repr: Ferrai - {'color': 'white', 'horsepower': 400, 'price': 8000}
#repr: Bmw - {'color': 'black', 'horsepower': 270, 'price': 5000}
#repr: Ferrai - {'color': 'black', 'horsepower': 300, 'price': 6000}
