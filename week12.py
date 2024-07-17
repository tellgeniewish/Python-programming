class Car: # 첫 글자를 대문자로
    # 필드: 클래스 객체에서 생성되는 변수 -> 초기값을 지정
    company = '' # 문자열은 ''로 초기화
    color = ''
    speed = 0 # 숫자는 0으로 초기화

    # 메소드: 클래스 내의 함수
    def up_speed(self, a): # 맨 앞에 self를 꼭 써야 한다
        self.speed += a

    def down_speed(self, a):
        self.speed -= a
    
    def stop(self):
        self.speed = 0

    def no_param(self): # self는 꼭 써야 한다
        res = 10
        return res

class Truck(Car): # Car를 상속받는다
    cc = 0

    def joke(self): # Truck에만 있는 메소드이기 때문에 트럭 객체만 사용 ㄱㄴ
        print("메롱~ㅋㅋ")
    
    # 메소드 오버라이딩: 부모에게서 상속받은 메소드를 재정의
    def up_speed(self, a):
        self.speed *= a
        #return super().up_speed(a)

car1 = Car()
car1.company = 'benz'
car1.color = 'red'
car1.speed = 0
car1.up_speed(70)

print("생성된 차의 제조사는 %s이고, 색상은 %s입니다" %(car1.company, car1.color))
print("속력은 %d" %car1.speed)

car1.down_speed(20)
print("속력은 %d" %car1.speed)

x = car1.no_param()
print(x)

tr1 = Truck()
tr1.company = 'benz'
tr1.color = 'blue'
tr1.speed = 0
tr1.cc = 2000
print("내 트럭 회사는 %s이고, 색상은 %s이고, 속력은 %d입니다" %(tr1.company, tr1.color, tr1.speed))


class Student:
    name = ''
    mbti = ''
    age = 0
    count = 0

    # 생성자: 반드시 존재 X
    def __init__(self, a, b, c):
        self.name = a
        self.mbti = b
        self.age = c
        Student.count += 1 # 클래스 변수

    # 소멸자: 객체 소멸할 때 자동으로 호출됨
    def __del__(self): # self 꼭 써야 한다
        print("이제 나 죽습니다")

    def introduce(self):
        print("안녕하세요, 제 이름은 %s이고, 나이는 %d입니다" %(self.name, self.age))

# st1 = Student()
# st1.name = "suzy"
# st1.mbti = "enfp"
# st1.age = 20

st1 = Student("suzy", "enfp", 20)

st1.introduce()

st2 = Student("alex", "infp", 23)

print("현재 학생 수는? %d명 입니다" %st1.count) # st1.count 또는 st2.count 사용해도 ㄱㅊ
# Student.count 잘 안 씀

del(st1) # 수동으로 호출 가능함

##### 예제 1:
class Human:
    name = ''
    age = 0
    gender = '남자'

    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g

    def __del__(self):
        print("나의 죽음을 알리지 마라")

    def who(self):
        print("이름은 %s이고, 나이는 %d이고, 성별은 %s입니다" %(self.name, self.age, self.gender))

areum = Human("아름", 25, "여자")
print(areum.name)
print(areum.age)
print(areum.gender)

##### 예제 2:
areum = Human("아름", 25, "여자")
areum.who()
del areum

##### 예제 3:
class 차:
    바퀴 = 0
    가격 = 0

    def __init__(self, 바, 가):
        self.바퀴 = 바
        self.가격 = 가

car = 차(2, 1000)
print(car.바퀴)
print(car.가격)

##### 예제 4:
class 자동차(차):
    def 정보(self):
        print("바퀴 수 %d" %self.바퀴)
        print("가격 %d" %self.가격)

car = 자동차(4, 1000)
car.정보()