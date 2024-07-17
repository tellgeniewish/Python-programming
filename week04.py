# Q1. 교수님 실행 단축키?
# A1. 그냥 실행 버튼 누름

# Q2. break point(F9)의 의미 뭐지? (찍으면 여기부터 시작?) 어차피 다 실행되는데 왜 쓰지?
# A2. 예를 들어 77번 줄에 break point 찍으면 76번 줄까지는 한 번에 실행된 후 77번 줄에서 대기한다.

# Q3. F10과 F11 차이?
# A3. 

# Q4. pass뒤에 출력 why?
# A4. 이런 식으로 사용X 보통 잠시 코드 안 쓸 때 사용(continue와 다름!)
# num = int(input("숫자를 입력해 주세요: "))
# if num < 0:
#     pass
#     print("과연 출력될까?")
#     print("0보다 큰 숫자를 입력해주세요.")
# elif num % 2 == 0:
#     print("입력하신 숫자는 짝수입니다.")
# else:
#     print("입력하신 숫자는 홀수입니다.")

# Q4. str을 int()으로 감쌌을 때 아스키코드 출력 왜 안 되는가?
# A4. 파이썬에는 이런거 없음
# a='a' # 97
# print(int(a))

print(1, 2)
print(1+2)

print("lo", "ve")
print("lo"+"ve")

a = 0
print(1<a)

'''
F9 break point
F5 디버그 실행 시작
F10 한줄씩 진행
'''

if 1<a : # 조건이 많을 때는 () 사용
    print(a,"는 1보다 큽니다.")
    print("hi")
print("끝")

##### 예제 1: “password” 라는 변수에 “data”를 저장하고,
##### 비밀번호를 입력 받아 “data”를 정확히 입력 시 “correct”를 출력해 보자.
answer = "data"
question = input("답을 입력: ")

if answer==question:
    print("옳아요")

password = "data"
answer = input("비밀번호를 입력해주세요: ")
if password==answer:
    print("correct")

if password==answer:
    pass # 안 쓰면 다음 줄에서 오류
a = 3

##### 예제 2: 숫자를 입력 받아 홀/짝을 출력해 보자.
##### 만약 음수를 입력 시, 0보다 큰 숫자를 입력하라는 메시지도 출력해 보자.
num = int(input("숫자를 입력해 주세요: "))
if num < 0:
    print("0보다 큰 숫자를 입력해주세요.")
elif num % 2 == 0:
    print("입력하신 숫자는 짝수입니다.")
else:
    print("입력하신 숫자는 홀수입니다.")

r = 'r'
print(r)
# print(int(r))

a = 10
message = "짝수"
message2 = "홀수"

if a % 2 == 0:
    print(message)
else:
    print(message2)

message = "짝수" if a%2==0 else "홀수" # 시험X
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
print(message)

score = int(input("점수 입력: "))
if 90<=score:
    grade='A'
else:
    if 80<=score:
        grade='B'
    else:
        if 70 <= score:
            grade='C'
        else:
            grade='D'
print(grade)

score=87
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("F")
print("학점입니다.")

##### 예제 4: 사용하는 통신사 종류를 입력 받아 출력해보자.
answer = input("고객님께서 사용 중인 통신사는? ")
if answer == "SK":
    tele = "SK"
elif answer == "KT":
    tele = "KT"
elif answer == "LG":
    tele = "LG U+"
else:
    tele=None
    print("제대로 입력해주세요")

if tele!=None:
    print("고객님께서 사용 중이신 통신사는", tele, "입니다.")

##### 예제 5: 나이를 입력 받아 10대 이하, 10대, 20대, 30대, 40대, 50대, 60대 이상 중 하나를 출력해보자.
age = int(input("고객님의 나이를 입력해 주세요: "))
if 60<=age:
    age_range = 60
elif 50 <= age:
    age_range = 50
elif 40 <= age:
    age_range = 40
elif 30 <= age:
    age_range = 30
elif 20 <= age:
    age_range = 20
elif 10 <= age:
    age_range = 10
else:
    age_range = "미취학"
print("고객님의 연령대는", age_range, "입니다.")

##### 예제 6: 짝홀 판별
num = int(input("자연수를 입력해 주세요: "))
if num<0:
    print("자연수가 아닙니다.")
elif num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

##### 예제 7: A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다.
##### 회원 등급에 따른 할인율은 다음과 같습니다.
##### (S = 실버, G = 골드, V = VIP)
##### S 할인율: 5%, G 할인율: 10%, V 할인율: 15%
##### 회원 등급과 구매 금액을 입력 받아 할인이 적용된 가격을 구하세요.

#level = input("회원 등급을 입력해 주세요: ")
#price = int(input("구매 금액은? "))

level='G'
price=10000

if level == 'S':
    dc = 5
elif level == 'G':
    dc = 10
else:
    dc = 15

cal = 1-(dc/100)

print("당신의 회원 등급은 %s이고, 할인율은 %d %%입니다.\n따라서 최종 구매 금액은 %d원입니다." %(level, dc, int(price*cal)))

##### 예제 8: 다음 프로그램의 실행 결과는?
a = 2
z = a * 5 # 10
w = (z - 3) * (a - 2) / 7 + 10 # 10
if a > z or w > a:
    y = 2 * a
else:
    y = 4 * a
print("y는", y)

##### 예제 9: 영어와 수학이 모두 80점 이상이면 '합격',
##### 영어와 수학이 모두 80점 미만이면 '불합격',
##### 두 사람 중 한 과목이 80점 이상이면 '재시험 기회제공'의
##### 메시지를 출력하는 프로그램을 작성해보자.
english = int(input("영어시험 점수를 입력하세요: "))
math = int(input("수학시험 점수를 입력하세요: "))
if (80<=english and 80<=math):
    print("합격")
elif (80<=english or 80<=math):
    print("재시험 기회제공")
else:
    print("불합격")

##### 예제 10: 나이를 입력 받아 입장료를 계산하는 프로그램을 작성해보자.
##### 10세 이하의 입장료는 1000원, 65세 이상의 입장료는 0원, 기본 입장료는 2000원이다.
age = int(input("나이를 입력하세요: "))
if age <= 10:
    fee = 1000
elif 65 <= age:
    fee = 0
else:
    fee = 2000
print("입장료는 %d입니다."%fee)