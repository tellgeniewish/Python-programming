print("Hello, World")
print("hello")
print("안녕")

# 주석
'''여러 줄 주석'''
# ctrl + k + c 통째로 주석 처리
# ctrl + k + u 통째로 주석 취소

# 터미널에 clear를 치면 깔끔해진다.

print("3+2")
print("%d" %(3+2))
print("%d+%d=%d" %(3,2,3+2))

print("hello")
print("%s" %("hello"))

print("%d/%d=%d입니다." %(100,20,100/20))

print("파이는 %f 입니다." %3.14)

x = 10
y = 2
print("%d * %d = %d 입니다." %(x, y, x*y))

z = "data"
print(x, y, z)
print("%d %d %s" %(x, y, z))

print("hello\nworld")

print("\"")
print("\"hi")
print("\\") # \뒤에 원하는 문자

price = 100
print(price)
print(price, "원") # 콤마 , 쓰면 자동으로 띄어쓰기 됨
print(price, "원", sep='')
print(price, "원", sep=' ') # sep는 ,와 , 사이에

print("010", "1234", "5678")
print("010", "1234", "5678", sep='')
print("010", "1234", "5678", sep='-')

a = 2
b = 0.33
c = "hi"
d = True
e = False

print(a)
print(d)

print(type(a))
print(type(d))

a = 20
b = 4
c = a / b
print(c) # /는 무조건 float가 나온다
print(type(c))

a = 20
b = 4.0
c = a*b
print(c)
print(type(c))

x = "datascience"
print(x)
print(type(x))

a = 2
b = 3
c = a + b
print(c)

a = "data"
b = 3
# c = a + b # error
# print(c)

a = "data"
b = '3'
c = a + b # str끼리 더하기 가능
print(c)

c = a * 5 # str끼리 곱하기 가능
print(c)

x = 100<3
print(x)

x = '동덕'
y = '동덕'
z = (x==y)
print(z)

_a = 3
print(_a)

age = input("당신의 나이는 몇 살입니까?") # input 함수는 무조건 string으로 받는다
print(age)

# man_age = age - 1 # error
# print(man_age)

man_age = int(age) - 1
print("만 나이는",man_age)

age = int(input("당신의 나이는 몇 살입니까?")) # int()로 입력문을 감싸기
man_age = age - 1
print(man_age)

a = int(input("숫자 하나 입력하세요: "))
b = int(input("숫자 하나 입력하세요: "))
c = a * b
print(c)

number1 = input("숫자1 ==> ")
number2 = input("숫자2 ==> ")
print(number1 + number2)
print(number1,number2)

name = input("이름 ? :")
univ_id = input("학번 ?:")
print("제 이름은 ", name, "이고, 제 학번은", univ_id, " 입니다.")