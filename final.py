##### 2024-1학기 파이썬프로그래밍 (A0019 기말고사) #####
# ----------------------------------------------------------------------------------------------------------
# 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# (1) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# (2) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# (3) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# ----------------------------------------------------------------------------------------------------------

# 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

##### 대답 : 동의합니다
##### 학번 : 20211689
##### 이름 : 김현진


##### 1번 문제 #####

name = ['Keith', 'Jessie', 'Charlie', 'Aidan', 'Ivan', 'Peter']
score = [90, 66, 82, 93, 71, 88]
n = int(input('몇 등의 학생 자료를 알고 싶습니까?'))

xx = score.copy()
xx.sort(reverse=True)
# print('xx=', xx)
# print(xx[n-1])

remember = 0
for i in score:
    if xx[n-1] == i:
        break
    remember += 1

# print(remem)

print('%d등 학생은 %d점이고 이름은 %s입니다.' %(n, xx[n-1], name[remember]))




##### 2번 문제 #####

def count_space(a):
    count = a.count(' ')
    # count = 0
    # for i in a:
    #     if i == ' ':
    #         count += 1
    return count

sentence = 'Python is powerful and interesting for me.'
num = count_space(sentence)
print(sentence)
print('빈칸의 개수 : ', num)



##### 3번 문제 #####

number = int(input("게임 최대 숫자를 입력해 주세요: "))
count = 0 # 박수 수

# coding here ##
for i in range(1, number+1):
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            count += 1

print(count)



##### 4번 문제 #####

def sasp(n):
    res = ''
    for i in range(1, n+1):
        if i % 2 == 0:
            res += '덕'
        else: res += '동'
    return res


print(sasp(4)) #동덕동덕
print(sasp(5)) #동덕동덕동



##### 5번 문제 #####

## coding here ##
f = open('1.txt', 'r')

lines = f.readlines()

amount = 0
count = 0
for line in lines:
    if len(line.strip().split(':')[0]) == 4:
        amount += int(line.strip().split(':')[1])
        count += 1

avg = 0.0
avg = amount / count

print(avg)

f.close()



##### 6번 문제 #####

class Vehicle:
    make = ''
    model = ''
    year = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print("제조사: %s, Model: %s, Year: %d"%(self.make, self.model, self.year))


# ## coding here ##
class Car(Vehicle):
    cc = 0

    def __init__(self, make, model, year, cc):
        self.make = make
        self.model = model
        self.year = year
        self.cc = cc

    def info_car(self):
        print("cc: %d 입니다."%(self.cc))

car = Car("Toyota", "Camry", 2020, 1700)
car.info()
car.info_car()



##### 7번 문제 #####

def filter_long_words(word_list, min_length):
    res = []
    for i in word_list:
        if min_length <= len(i):
            res.append(i)
    return res


words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "hot", "cozy"]
print(filter_long_words(words, 5))


##### 8번 문제 #####

with open('phone.txt','r') as f:
    lines = f.readlines()[1:]
    
    for line in lines:
        if len(line.strip().split(' ')[0]) == 4:
            numbers = line.strip().split(' ')[1]
            numbers = numbers.replace('-', '')
            print(numbers)



##### 9번 문제 #####

class Dog:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, n):
        print('Woof!'*n)


dog1 = Dog("Buddy", 3)
dog1.bark(5)



##### 10번 문제 #####

eat = ['미역국','김치','햄버거','피자','떡','순대','떡볶이']
wish = ['햄버거', '떡볶이', '라면', '김밥']

result=[]

## coding here ##
for i in wish:
    if i in eat:
    # for j in eat:
    #     if j == i:
        result.append(i)

print(result)