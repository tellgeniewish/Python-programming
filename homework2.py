##### 2024-1학기 파이썬프로그래밍 (2차 과제) #####
##### 학번 : 20211689
##### 이름 : 김현진

##### 1. 함수 만들기
# • 자연수를 입력 받아 약수를 출력하는 함수를 만들어 보자.
# • 함수 이름 : divisor
# • 약수를 리스트 형태로 출력함

def divisor(x):
    div = []
    for i in range(1, x + 1):
        if x % i == 0:
            div.append(i)
    print(div)

divisor(10)
divisor(7)

##### 2. 함수 만들기
# • 리스트 안에 특정 숫자보다 큰 숫자가 몇 개 포함되어 있는지 찾는 함수를 만들어 보자.

def bigger_than(a,b):
    count = 0
    for i in a:
        if b < i:
            count += 1
    return count

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(bigger_than(x,4))
print(bigger_than(x,5))

##### 3. 파일 읽기
# • 파이썬프로그래밍 수업을 듣는 50명의 학생 중간고사 점수가 기록되어 있는 ‘mid_test.txt’ 파일을 이용하여
# 평균 점수(score_avg) 와 100점을 맞은 학생 수 (n_student)를 출력하는 함수 analyze_mid 를 구현해보자.
# 함수의 매개변수 부분에 네모 박스를 친 부분은 자유롭게 설정하라고 함을 의미. 즉, 빈칸은 아님을 주의!

def analyze_mid(lines):
    ## coding here ##
    count_100 = 0
    amount = 0
    avg = 0.0
    for line in lines:
        if int(line.strip()) == 100:
            count_100 += 1
        amount += int(line.strip())
    avg = amount / len(lines)
    return avg, count_100

f = open('mid_test.txt','r')
score_avg, n_student = analyze_mid(f.readlines())

print(score_avg, n_student)
f.close()

##### 4. 클래스 만들기
# • Student 클래스 생성해보자.
# • 클래스 내 필수 사항
# • 필드 : 이름, 전공, 학년, 전화번호
# • 메서드 : 자기소개
# • 출력 결과
# • “안녕하세요. 저의 이름은 정영희, 데사 전공 1학년이며, 연락처는 010-1234-5678입니다.”

class Student_DD:
    ##coding here
    name = ''
    major = ''
    grade = 0
    phone = ''

    def __init__(self, n, m, g, p):
        self.name = n
        self.major = m
        self.grade = g
        self.phone = p

    def introduce(self):
        print("안녕하세요. 저의 이름은 %s, %s 전공 %d학년이며, 연락처는 %s입니다." %(self.name, self.major, self.grade, self.phone))

student1 = Student_DD("정영희", "데사", 1, "010-1234-5678")
student1.introduce()

##### 5. 문자열
# • 영어로 구성된 문자열을 입력 받아 처음과 마지막 알파벳으로 약자 만들기
# • 예시 : tiger → tr , school → sl, advertisement → at, biology → by, …

sentence = input("영문자열을 입력하세요: ")
res = sentence[0] + sentence[len(sentence)-1]
#res = sentence[0] + sentence[-1]
print(res)