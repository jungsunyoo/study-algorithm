class Person:
    def __init__(self, param_name):
        print("I am created!", self)
        self.name = param_name
    def talk(self): # 클래스 내부의 함수는 메소드라고 불린다
        print("안녕하세요, 제 이름은 ", self.name, "입니다")
    # pass

person_1 = Person("유재석")
# 소괄호 = 생성자 (constructor), constructor 위해서는 __init__ 만들어야 한/
# 소괄호 열고 닫고가 init이랑 똑같
print(person_1.name)
person_1.talk()
person_2 = Person("박명수")
print(person_2.name)
person_2.talk()

# 이처럼, 클래스를 이용하면 유사한 데이터 혹은 구조를 쉽게 만들 수 있다