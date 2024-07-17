score_math = 92
score_science = 87.2
score_english = 95

print("수학, 과학, 영어 점수는 %d점, %f점, %d점입니다." %(score_math, score_science, score_english))

print("%s 점수는 %d입니다." %("수학", score_math))

a = 3
print(a)
a = 5 * 3
print(a)

a = 5/3
print("파이는 %f 입니다." %3.14)
print("5 나누기 3은 %f 입니다." %a)

a = 5%3
print(a)

a = (5%2 == 0)
print(a)

a = (4%2 == 0)
print(a)

b = 3**2
print(b)

n1 = 5
n2 = 3

sum = n1 + n2
mul = n1 * n2
div = n1 / n2 # 나누기(실수값으로 나온다)
quo = n1 // n2 # 몫
rem = n1 % n2 # 나머지
square = n1 ** n2 # 제곱

print("두 수의 합은 %d이지~" %sum)
print("n1을 n2로 나눈 몫은 %d, 나머지는 %d이지~" %(quo, rem))
print("n1의 n2승은 %d이지~" %square)

a = 3
b = 4
c = 5
# a, b, c = 3,4,5 # 오류는 아님 비추!
print(-3*a+(b*c))

x = '100'
y = '100.123'
z = '99.4'

print(int(x), float(y)+1)
# print(int(x), float(y)+1, int(z)+1) # 문자열->숫자: 버림 불가(z는 str인데 float()는 가능하지만 int()는 불가)

a = 100
b = 100.1
print(str(a)+'1')
print(str(b)+'2')

pi = 3.14159265
r = int(input("반지름을 입력하세요: "))

length = 2 * pi * r
area = pi * r**2

print("원의 둘레는 %f, 넓이는 %f 입니다." %(length, area))

a = 5
a = a+3
a += 3
print(a)

num = 20
num += 3
print(num)
num-= 3
print(num)
num *= 3
print(num)
num /= 3
print(num) # / 나누기는 실수값으로 나온다
num //= 3
print(num)
num **= 3
print(num)
num %= 3
print(num)

a = 5
a+=5; print(a)

num = 20
num //= 3
print(num)

a = 5
b = 10
c = (a==b)
print(c)
d = (a!=b)
print(d)

print('가방' < '사랑')
print('가자' > '가차')
print('abc' <= 'abd')

x = 100
print((x==200) and (50<x))
print((x==200) or (50<x))

z = not(x==200)
print(z)