# 시험 X
# 예외 처리하는 법
import os # os에 있는 다양한 기능을 가져다 쓸 수 있다

name = 'tony.txt'

if os.path.exists(name):
    f = open(name, 'r')
    
    lines = f.readlines()
    print(lines)

    f.close()
else: print("파일이 없는데 다시 찾아봐")

# 예외 처리 없이 그냥 open할 때 폴더에 파일이 없으면 오류
# 다른 폴더에 있으면 경로를 쓰면 된다(경로 복붙 시 \를 /으로 바꾸어야 한다)
f = open("score.txt", 'r') # 읽기 r

print("while문 시작")
while True:
    line = f.readline() # 한 줄 읽을 때는 readline(): 한 줄에 ,로 다 있으면
    print(line.strip())

    if not line: # if line == '': 써도 됨
        break # ctrl + C 강제종료
print("while문 끝")

lin = f.read() # read() 하나의 문자열로 읽어온다
print(lin)

lines = f.readlines() # 여러 줄 읽기(리스트로 읽어온다)
print(lines)

with open("score.txt", 'r') as f: # close() 안 해도 자동으로 닫힌다
    lines = f.readlines()

    for line in lines:
        print(line.strip())

print("\n.strip() 했어요")
for line in lines:
    print(line.strip()) # .strip() 앞뒤 공백을 없애줌

a = []
print("\nappend 했어요")
for line in lines:
    a.append(line.strip())
print(a)

a = []
print("\nint 후에 append 했어요")
for line in lines:
    a.append(int(line.strip()))
print(a)

amount = 0
for line in lines:
    amount += int(line.strip())
print("\nsum=", amount)

avg = 0.0
avg = sum(a)/len(a)
print(avg)

f.close()

f = open("midterm.txt", 'r')
lines = f.readlines()[4:] # 5번 줄부터 가져온다

print("\nmidterm.txt를 출력할게요")
for line in lines:
    print(line.strip())

f.close()

# 폴더에 파일이 없으면 새로 생성된다
f = open("write.txt", 'w') # 같은 파일이 있으면 덮어쓰기 됨

a = 10
print(a)

f.write(str(a))

f.close()

f = open("mid4.txt", 'w') # 같은 파일이 있으면 덮어쓰기 됨

for i in range(1,7):
    f.write(str(i)*i + "\n") # write는 수동으로 "\n" 넣어줘야 함

f.close()

f = open("result.txt", 'w')

for i in range(1,11):
    x = "%d 줄입니다." %i
    f.write(x + "\n")

f.close()

f = open("result.txt", 'a') # w는 덮어쓰기 되지만 a는 이어쓰기 됨

for i in range(1,11):
    x = "%d 줄입니다." %i
    f.write(x + "\n")

f.close()


##### 예제 1: 폴더에 ‘star.txt' 파일을 생성한 후 다음과 같이 써보세요.
f = open('star.txt', 'w')

i = 7
while 0 < i: # == for i in range(7, 0, -2):
    #print('*'*i)
    f.write('*'*i + "\n")
    i -= 2

f.close()

##### 예제 2: “capital.txt”를 열었을 때 아래와 같이 보이게 코드를 구현해 보자.
capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이", "덴마크":"코펜하겐"}

### coding here ###
f = open('capital.txt', 'w')

for i in capital:
    if len(i) == 3:
        f.write("%s의 수도는 %s 입니다\n" %(i, capital[i]))

f.close()

##### 예제 3: 50명의 학생의 시험 점수 (100점 만점)가 기록되어 있는 score.txt 파일을 읽어 n명의 평균 점수를 구해보자.
f = open('score.txt', 'r')
sum = 0
average = 0.0

## coding here ##
lines = f.readlines()
for line in lines:
    sum += int(line.strip())

average = sum / 50
average = sum / len(lines)

print(average)

f.close()

##### 예제 4: 우리 반 학생의 이름이 적힌 ‘name.txt’ 파일을 읽어 이름이 4글자인 학생들만 아래와 같이 출력해보자.
f = open('name.txt', 'r')

## coding here ##
lines = f.readlines()

res = []
for line in lines:
    index = line.strip().find(' ')
    if len(line.strip()[index + 1:]) == 4:
        res.append(line.strip()[index + 1:])    
    '''
    name = line.strip().split()[1]
    if len(name) == 4:
        res.append(name)
    '''
print(res)

f.close()

##### 예제 5: 우리 반 학생의 중간고사 점수가 입력된 ‘midterm.txt’파일을 읽어 국어 점수의 평균을 구해보자.
f = open('midterm.txt','r')

## coding here ##
lines = f.readlines()[1:]

sum = 0
for line in lines:
    sum += int(line.strip().split(',')[0])

avg = 0.0

avg = sum / len(lines)

print(avg)

#print('%.2f' %avg) # 다른 처리법 없음 이 방법 써야 함

f.close()