##### 2024-1학기 파이썬프로그래밍 (A0019 1차 과제) #####
##### 학번 : 20211689
##### 이름 : 김현진


## 1. 완전한 파일이름 출력 ##
#### coding here ####

drive = input("드라이브 이름: ")
directory = input("디렉토리 이름: ")
file_name = input("파일 이름: ")
extension = input("확장자: ")

answer = drive + directory + file_name + extension
print("완전한 파일이름: " + answer)
'''
# 교수님 풀이 코드
print("완전한 파일이름: ", drive, directory, file_name, extension, sep='')
'''

## 2. 숫자 맞추기 게임 ##
answer = 25
### coding here ####

num = int(input("숫자를 입력하세요 : "))
if num < answer:
        print("UP !")
if answer < num:
        print("DOWN !")

while num != answer:
    num = int(input("숫자를 입력하세요 : "))
    if num < answer:
        print("UP !")
    if answer < num:
        print("DOWN !")
print("정답 !")

## 3. 자동 판매기 시뮬레이션 프로그램 ##
#### coding here ####

price = int(input("물건 값을 입력 : "))
income = int(input("받은 금액 : "))

change = income - price
print("거스름돈은 아래와 같습니다.")
ch_500 = change // 500
change %= 500
ch_100 = change // 100
change %= 100
ch_10 = change // 10
change %= 10
ch_1 = change
print("500원 = %d개, 100원 = %d개, 10원 = %d개, 1원 = %d개" %(ch_500, ch_100, ch_10, ch_1))

## 4. while문 출력 ## 
#### coding here ####
star = 7
while 0 < star:
    for i in range(star):
        print("*", end='')
    print()
    star -= 2
'''
# 교수님 풀이 코드
star = 7
while 0 < star:
    print('*' * star)
    star -= 2
'''

## 5. 리스트 데이터 확인 ##
answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

A = ['hello', 62, 'umbrella', 145]
B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

#### coding here ####

arr = input("리스트를 입력하세요 : ")

if (arr != "A") and (arr != "B") and (arr != "C"):
    print("리스트에 없습니다.")
else:
    if arr == "A":
        target = A
    elif arr == "B":
        target = B
    else:        
        target = C

    for i in target:
        flag = False
        for j in answer:
            if i == j:
                print('O', end='')
                flag = True
        if flag == False:
            print('X', end='')
    '''
    # 교수님 풀이 코드
    for i in target:
        if i in answer:
            print('O', end='')
        else: print('X', end='')
    '''