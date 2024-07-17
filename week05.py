# Q1. i++ 오류나던데 파이썬에 없는지?
# A1. 없음

# Q2. 파이썬에서 do while 어떻게 사용하는지
# A2. 없음 

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

for i in range(5):
    print(i, "Hello")

for i in range(1, 11):
    print(i, end=" ")

print()
for i in range(5, 2, -1):
    print(i, end=" ")

print()
for i in range(1, 11, 1):
    if i != 10:
        print(i, end='-')
    else:
        print(i)

print("중첩 반복문")
for i in range(5):
    for j in range(10):
        print("*", end='')
    print()

print("반복문 하나로")
for i in range(5):
    print("*" * 10)

print("삼각형")
for i in range(5):
    print("*" * i)

print("역삼각형")
for i in range(5):
    print("*" * (5-i))

print("짝수줄에는 10개, 홀수줄에는 5개")
for i in range(10):
    if i % 2 == 0:
        print("*" * 10)
    else:
        print("*" * 5)

print()
##### 예제 1: 1부터 30까지의 숫자 중 3의 배수만 출력하세요.
for i in range(1, 31): # 30까지면 31을 적어야 한다!
    if i % 3 == 0:
        print(i)

##### 예제 2: 팩토리얼 (!) 값 구하기
num = int(input("2 이상의 숫자를 입력해 주세요: "))

if 2 <= num:
    fac = 1
    for i in range(1, num+1):
        fac *= i
    print(fac)

while num < 2:
    num = int(input("2 이상의 숫자를 입력해 주세요: "))

    if 2 <= num:
        fac = 1
        for i in range(1, num+1):
            fac *= i
        print(fac)

print("1부터 10까지의 합은 55")
sum = 0
for i in range(11):
    sum += i
print(sum)

print("1000부터 2000까지 홀수의 합은 750000")
sum = 0
for i in range(1000, 2001):
    if i % 2 != 0:
        sum += i
print(sum)

res = 0
for i in range(1001, 2001, 1):
    if i % 2 == 1 : 
        res = res + i
print("1000에서 2000까지의 홀수의 합 =", res)

##### 예제 3: 구구단 구하기
num = int(input("구구단 몇 단을 계산할까요?: "))
for i in range(1, 10):
    print(num, "x", i, "=", num*i)
    
num = int(input("구구단 몇 단을 계산할까요?: "))
for i in range(1, 10):
    print("%d x %d = %d" %(num, i, num*i))

for i in range(3):
    for j in range(2):
        print(i, j, "안녕하세요. 어서 오세요. QR 체크 부탁드립니다.")

for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d" %(i, j, i*j))

for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %d" %(j, i, i*j), end="   ")
    print()

print("1부터 10까지의 합은 55")
sum = 0
i = 1
while i<=10:
    sum += i
    i += 1 # while문 사용할 때는 반드시 i += 1 증감식을 써야 한다! 안 쓰면 무한반복
print(sum)

##### 예제 4: while문을 이용하여 실행 결과와 같은 형태로 출력해보자.
i=0
while i<5:
    print('*'*10)
    i += 1

print("삼각형")
i = 0
while i<5:
    print("*" * i)
    i += 1

print("역삼각형")
i = 0
while i < 5:
    print("*" * (5-i))
    i += 1

while True:
    print('ㅋㅋ') # 무한반복 시 ctrl+c 누르면 강제 종료
    break

i=0
while i<=10:
    if i == 5:
        break
    print(i)
    i += 1

res = 0
for i in range(1, 11, 1) :
    res = res + i
    if res > 40:
        print("1에서 10까지의 합에서 최초로 40을 넘는 숫자는 =", i)
        break

for i in range(1, 11):
    if i % 3 == 0:
        print("^^")
        continue # 반복문으로 돌아간다
    print(i)

sum = 0
i = 0
while i<11:
    if i % 3 == 0:
        i += 1
        continue # 3의 배수에서 if문에 걸렸을 때 증가가 안 되어서 무한 반복됨! 위에서 i += 1 증가시켜줘야 함
    sum += i
    i += 1
print(sum)

##### 예제 5: 1부터 100까지 숫자를 모두 더한 값을 출력하세요.
sum = 0
for i in range(1, 101):
    sum += i
print("1부터 100까지 합=", sum)

sum = 0
i = 0
while i <= 100:
    sum += i
    i += 1
print("1부터 100까지 합=", sum)

##### 예제 6: 30과 75의 최대 공약수를 출력해보세요.
print("30과 75의 최대공약수는", end=' ')
common = 1
for i in range(1, 31):
    if (30 % i == 0 and 75 % i == 0):
        common = i
print(common)

print("30과 75의 최대공약수는", end=' ')
common = 1
i = 1
while i<=30:
    if (30 % i == 0 and 75 % i == 0):
        common = i
    i += 1
print(common)

print("최대공약수 구하기")
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
common = 1
i = 1
while i<=30:
    if (num1 % i == 0 and num2 % i == 0):
        common = i
    i += 1
print(common)