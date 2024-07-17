# sep
# end

# 나누기 -> 실수

# while문 i += 1

# 조건문에서 continue 사용 시 그 전에 i += 1
# sum = 0
# i = 0
# while i<11:
#     if i % 3 == 0:
#         print("지금", i)
#         i += 1
#         continue # 3의 배수에서 if문에 걸렸을 때 증가가 안 되어서 무한 반복됨! 위에서 i += 1 증가시켜줘야 함
#     sum += i
#     i += 1
# print(sum)

# score = [90, 85, 55, 70, 100, 92]
# # print("뒤에서 첫 번째 %d" %(score[-1]))

# print(score[0]) # 하나만 출력하면 [대괄호] 없이 출력됨!!
# print(score[0:1]) # 하나만 출력되게 하더라도 : 사용하면 [대괄호] 안에 출력됨

# score.append('G')
# print(score)
# score.insert(1, 'A')
# del(score[1])
# # score.remove(55)
# score.pop()
# score.count(100)
# len(score)
# score.sort(reverse=True)
#print(score)

# bb = []
#for i in range(100):
    #bb[i] = aa[99 - i] # 오류난 이유: 아직 빈 리스트라서 [0] 칸이 없음!!!

# for i in range(len(aa)):
#     bb.append(aa[len(aa) - i - 1]) # 빈 리스트일 때는 반드시 append 사용해야 한다
# print(bb)

# scores = {"김예진": 90, "박영진": 95, "김소희": 84}
# print(sum(scores.values()))

# admin_info = ['admin', '12345', 'data@dongduk.ac.kr']
# id = input("id: ")
# pw = input("pw: ")
# if id == admin_info[0] and pw == admin_info[1]:
#     print("관리자")
# elif id == admin_info[0] or pw == admin_info[1]:
#     print("id or pw 오류")
# else:
#     print("오류")

# price = int(input("물건 값을 입력 : "))
# income = int(input("받은 금액 : "))

# change = income - price
# print("거스름돈은 아래와 같습니다.")
# ch_500 = change // 500
# change %= 500
# ch_100 = change // 100
# change %= 100
# ch_10 = change // 10
# change %= 10
# ch_1 = change
# print("500원 = %d개, 100원 = %d개, 10원 = %d개, 1원 = %d개" %(ch_500, ch_100, ch_10, ch_1))

# answer = {"fruit":'apple', "age":39, "bgm":'music', "hz":568.2, "univ":'Dongduk', "height":145, "hi":'hello'}

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# arr = input("리스트를 입력하세요:")

# if (arr != 'A') and (arr != 'B') and (arr != 'C'):
#     print("리스트에 없습니다.")
# else:
#     if (arr == 'A'):
#         target = A
#     elif (arr != 'B'):
#         target=B
#     else:
#         target=C

#     for i in target:
#         flag=False
#         for j in answer:
#             if i == answer[j]:
#                 print('O', end='')
#                 flag=True
#         if flag==False:
#             print('X', end='')

# if 100 in score:
#     print("YES")

# star=7
# while 0<star:
#     for i in range(star):
#         print('*', end='')
#     star -= 2
#     if 0<star:
#         print()
# print('\n끝', star)     
# for i in range(1,4):
#     print('*'*(i*2+1))

#     rice = int(input("물건 값을 입력 : "))
# income = int(input("받은 금액 : "))

# price = int(input("물건 값을 입력 : "))
# income = int(input("받은 금액 : "))

# change = income - price
# print("거스름돈은 아래와 같습니다.")
# ch_500 = change // 500
# change %= 500
# ch_100 = change // 100
# change %= 100
# ch_10 = change // 10
# change %= 10
# ch_1 = change
# print("500원 = %d개, 100원 = %d개, 10원 = %d개, 1원 = %d개" %(ch_500, ch_100, ch_10, ch_1))

# game369
# number = int(input("숫자 몇 까지?"))
# clap = 0

# for i in range(1, number+1):
#     for j in str(i):
#         print("i type=", type(i))
#         print("j type=", type(j))
#         if j == '3' or j == '6' or j == '9':
#             clap += 1
# print("clap =", clap)

# print('출력 시작')
# star = 7
# while 0 < star:
#     print('*' * star)
#     star -= 2
# print('출력 끝')

## 5. 리스트 데이터 확인 ##
# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# #### coding here ####

# arr = input("리스트를 입력하세요 : ")

# if (arr != "A") and (arr != "B") and (arr != "C"):
#     print("리스트에 없습니다.")
# else:
#     if arr == "A":
#         target = A
#     elif arr == "B":
#         target = B
#     else:        
#         target = C

#     for i in target:
#         if i in answer:
#             print('O', end='')
#         else: print('X', end='')

# game369
# number = input("숫자 몇 까지?")
# clap = 0

# for i in range(1, int(number)+1):
#     for j in str(i): # j의 타입은 str / i의 타입은 int
#         if j == '3' or j == '6' or j == '9':
#             clap += 1
# print("clap =", clap)

# id = '900101-2214567'
# print("7번째 자리는", id[7])
# if id[7] == '2' or id[7] == '4':
#     print("여자")
# else: print("남자")

# id_num = ['12347-41888', '11115-12777']
# for i in id_num:
    # print('-의 인덱스는?',i.find('-'))
    # print(i[i.find('-')])
    # print(i[5])
    # print(i[i.find('-')+1])
    
    # if i[i.find('-')+1] == '2' or i[i.find('-')+1] == '4':
    #     print("여자")
    # else: print("남자")
# 만약 - 다음 자리 숫자로 남/녀 판별해야 한다면?
#if i[4] == '-':
#        print(i)

# 매개변수로 이상한걸 넣으면? 초기값 사용!
# def prevent(a, b):
#     res=0
#     res = a + b

#     return res

# hap = 0
# hap = prevent(100, 200)
# print(hap)

# hap = 0
# hap = prevent('a', 200)
# print(hap)

# def no_input():
#     n1 = 100
#     n2 = 200

#     return n1, n2

# hap1, hap2 = 0, 0
# hap1, hap2 = no_input()
# print("func3()에서 돌려준 값 ==> ", hap1, hap2)

# def hap(a,b,c=0): # 매개변수를 3개까지 받을 수 있는 함수! 만약 2개만 들어오면 c=0이 됨
#     res = 0 # 초기값
#     res = a+b+c
#     return res
# res1 = hap(3,5)
# res2 = hap(3,5,1)
# print(res1, res2)

# def hap_all(*a): # 변수 앞에 *을 붙이면 리스트가 된다
#     res = 0
#     for i in a:
#         res += i

#     return res

# x = hap_all(1,2,3)
# print(x)

# f = open('score.txt', 'r')

# lines = f.readlines()
# print(lines)

# ##### 예제 4: 우리 반 학생의 이름이 적힌 ‘name.txt’ 파일을 읽어 이름이 4글자인 학생들만 아래와 같이 출력해보자.
# f = open('name.txt', 'r')

# ## coding here ##
# lines = f.readlines()

# res = []
# for line in lines:
#     index = line.strip().find(' ')
#     print("index", line.strip()[index + 1])
#     if len(line.strip()[index + 1:]) == 4:
#         res.append(line.strip()[index + 1:])    
#     '''
#     name = line.strip().split()[1]
#     if len(name) == 4:
#         res.append(name)
#     '''
# print(res)

# f.close()

# # game369
# number = int(input("숫자 몇 까지?"))
# clap = 0

# for i in range(1, number+1):
#     for j in str(i): # j의 타입은 str / i의 타입은 int
#         if j == '3' or j == '6' or j == '9':
#             clap += 1
# print("clap =", clap)

# hate = '재미없어 노잼'
# print(hate.find('싫어', 5))

# print(hate.rfind('재미')) # 오른쪽부터 찾은 단어가 몇 번째 index인지 반환
# print("len =", len(hate))

# score = '90,80,70'
# print(score.split(','))
# print("score =", score)

# score = [90, 85, 55, 70, 100, 92] # 원소를 무한대로 담을 수 있다.
# print(score[1:-1]) # 1번 index부터 뒤에서 첫 번째-1 index까지

# emt = [] # 빈 리스트에는 append로 무한대로 많은 값을 넣을 수 있다
# for i in range(0, 200, 2):
#     emt.append(i)
# print(emt)

# aa = emt
# print(aa)
# print((type(aa)))
# print("len = ", len(aa))

# bb = []
# #for i in range(100):
#     #bb[i] = aa[99 - i] # 오류난 이유: 아직 빈 리스트라서 [0] 칸이 없음!!!

# for i in range(len(aa)):
#     bb.append(aa[len(aa) - i - 1]) # 빈 리스트일 때는 반드시 append 사용해야 한다
# print(bb)

# bb = aa.reverse() # 안 된다, 그냥 aa가 리버스된다
# print("확인>>>", bb)
# print(bb)

# aa.reverse() # 여기부터 aa는 리버스됨!
# bb = aa.copy() # 복사
# print(bb)

# f = open('score.txt', 'r')

# lines = f.readlines()

# for line in lines:
#     print(line.strip())
# print(len(lines))

# f.close()

# def smile():
#     print("Hahaha")
#     return

# smile()

# def analyze_mid(lines):
#     ## coding here ##
#     count_100 = 0
#     amount = 0
#     avg = 0.0
#     for line in lines:
#         if int(line.strip()) == 100:
#             count_100 += 1
#         amount += int(line.strip())
#     avg = amount / len(lines)
#     return avg, count_100

# f = open('mid_test.txt','r')
# score_avg, n_student = analyze_mid(f.readlines())

# print(score_avg, n_student)
# f.close()

# answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# A = ['hello', 62, 'umbrella', 145]
# B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# def check(arr):
#     if (arr != "A") and (arr != "B") and (arr != "C"):
#         print("리스트에 없습니다.")
#     else:
#         if arr == "A":
#             target = A
#         elif arr == "B":
#             target = B
#         else:        
#             target = C
#     for i in target:
#         if i in answer:
#             print('O', end='')
#         else: print('X', end='')

# arr = input("리스트를 입력하세요 : ")
# check(arr)

# class Student_DD:
#     ##coding here
#     name = ''
#     major = ''
#     grade = ''
#     phone = ''

#     def __init__(self, n, m, g, p):
#         self.name = n
#         self.major = m
#         self.grade = g
#         self.phone = p

#     def introduce(self):
#         print('안녕 난 %s' %self.name)
#     pass

# student1 = Student_DD("정영희", "데사", 1, "010-1234-5678")
# student1.introduce()

# class 자동차():
#    wheel = 0
#    price = 0
   
#    def __init__(self, w, p):
#     self.wheel = w
#     self.price = p

#    def 정보(self):
#     print(self.wheel, self.price)

# car = 자동차(4, 1000)
# car.정보()

# f = open('midterm.txt','r')

# lines = f.readlines()[1:]

# for line in lines:
#     print(line.strip().split(',')[0])

# f.close()

# x = ['apple', 'banana', 'hi', 'car']

# for i in x:
#     if len(i) < 4:
#         print(i, end=' ')

# print()

# # game369
# number = int(input("숫자 몇 까지?"))
# clap = 0

# for i in range(1, number+1):
#     for j in str(i):
#         if j == '3' or j == '6' or j == '9':
#             clap += 1
# print("clap =", clap)

# class Student:
#     name = ''
#     mbti = ''
#     age = 0
#     count = 0

#     # 생성자: 반드시 존재 X
#     def __init__(self, a, b, c):
#         self.name = a
#         self.mbti = b
#         self.age = c
#         Student.count += 1 # 클래스 변수

#     # 소멸자: 객체 소멸할 때 자동으로 호출됨
#     def __del__(self): # self 꼭 써야 한다
#         print("이제 나 죽습니다")

#     def introduce(self):
#         print("안녕하세요, 제 이름은 %s이고, 나이는 %d입니다" %(self.name, self.age))

# # st1 = Student()
# # st1.name = "suzy"
# # st1.mbti = "enfp"
# # st1.age = 20

# st1 = Student("suzy", "enfp", 20)

# st1.introduce()

# st2 = Student("alex", "infp", 23)

# print("현재 학생 수는? %d명 입니다" %st1.count) # st1.count 또는 st2.count 사용해도 ㄱㅊ
# # Student.count 잘 안 씀
# print("현재 학생 수는? %d명 입니다" %st2.count)

# del(st1)

# print(2**3)

# ##### 6번 문제 #####
# #### coding here ####
# for i in range(1,7):
#     for j in range(i):
#         print(i, end='')
#     print()

# i = 1
# while i<=30:
#     if i%3==0:
#         i+=1
#         continue    
#     else:
#         print(i, ',', sep='', end='')
#     i+=1

i = 1
while i<=30:
    if i%3==0:
        i+=1
        continue    
    else:
        print(i, end=',')
        print(i, ',', sep='', end='')
    i+=1