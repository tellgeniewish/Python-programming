id_num_1 = '030901-4075102'

print(id_num_1.split('-')) # '-' 기준으로 나뉘어 리스트 생성
print(id_num_1.split('-')[1])
print(id_num_1.split('-')[1][0])

print("id_num_1의 결과는?", end=' ')
if id_num_1.split('-')[1][0] == '3':
    print("male")
elif id_num_1.split('-')[1][0] == '4': # 이상한 주민번호가 왔을 때를 대비해서 elif를 사용
    print("female")

id_num_2 = '040102-3112345'
print("id_num_2의 결과는?", end=' ')
if id_num_2.split('-')[1][0] == '3':
    print("male")
elif id_num_2.split('-')[1][0] == '4':
    print("female")

# 반드시 함수 정의 후에 함수 호출!
# 코드를 쭉 읽어내려오면서 함수 정의를 살펴보지 않음! 함수 호출이 되어있으면 그때 함수를 본다
# 함수 정의
def check_sex(id):
    if id.split('-')[1][0] == '3':
        print("male")
    elif id.split('-')[1][0] == '4':
        print("female")
    # 반환값이 없으면 return만 써도 되고 아무것도 안 써도 된다

# 함수 호출
print("함수 호출의 결과는?", end=' ')
check_sex('030123-4321789')

def plus(a, b):
    return a + b # 반환 값이 있는 함수

result = plus(1, 2)
print(result) # 만약 함수에서 return하고 끝나는데(반환값이 없음!) 호출해서 출력하면 None이라고 뜬다

def smile():
    print("Hahaha")

smile()

def printf(a):
    print(a)

printf('a')

def basic_4op(a, b):
    mul = a*b
    diff = a-b

    return mul, diff # 순서 조심!

m, d = basic_4op(3,2) # 반환 순서에 맞게 변수로 받아야 한다
print(m, d)

x = ['apple', 'banana', 'hi', 'car']

for i in x:
    if len(i) < 4:
        print(i, end=' ')

print()

def len_under_4(a):
    for i in a:
        if len(i) < 4:
            print(i, end=' ')

len_under_4(x)

print()

def no_return_print_index(a, b): # 리스트와 인덱스를 매개변수로 받아 인덱스 번째를 출력하는 함수
    print(a[b-1])

no_return_print_index(x,2)

def print_index(a, b):
    res = a[b-1]

    return res

res = print_index(x,2)
print(res)
print(print_index(x,2))

# 매개변수로 이상한걸 넣으면? 초기값 사용!
def prevent(a, b):
    res=0
    res = a + b

    return res

hap = 0

hap = prevent(100, 200)
print(hap)

def no_input():
    n1 = 100
    n2 = 200

    return n1, n2

hap1, hap2 = 0, 0
hap1, hap2 = no_input()
print("func3()에서 돌려준 값 ==> ", hap1, hap2)

# 함수 매개변수 초기값은 뒤쪽부터!
def hap(a,b,c=0): # 매개변수를 3개까지 받을 수 있는 함수! 만약 2개만 들어오면 c=0이 됨
    res = 0 # 초기값
    res = a+b+c
    return res
res1 = hap(3,5)
res2 = hap(3,5,1)
print(res1, res2)

# 매개변수로 몇 개가 올 지 상상이 안 될 때
def hap_all(*a): # 변수 앞에 *을 붙이면 리스트가 된다
    res = 0
    for i in a: # 리스트 형태로 푼다!
        res += i

    return res

x = hap_all(1,2,3)
print(x)

# 전역변수
a = 1
b = 2

def hap(x, y):
    res = 0
    res = x + y # res, x, y는 지역변수
    return res

res = hap(1,2) # 여기 res는 전역변수

# 지역변수와 전역변수의 이름이 같은 경우 --> 지역변수가 우선
a = 10
print(a)

def same_val(x):
    a = x + 1
    print(a)

same_val(a)

## 함수 정의 부분
def func1() :
    a = 10 # 지역변수
    print("func1()에서 a의 값 ", a)
def func2() :
    print("func2()에서 a의 값 ", a)
## 전역변수 선언 부분
a = 20
## 메인 코드 부분
func1()
func2()

##### 예제 3: 나라 이름을 함수에 입력하면 수도를 출력해주는 함수
def find_capitalcity(capital, country):
    #### coding here ####
    #for i in capital:
        #if i == country:
    return capital[country]

capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이", "덴마크":"코펜하겐"}

print(find_capitalcity(capital, "대한민국"))
print(find_capitalcity(capital, "덴마크"))
#print(find_capitalcity(capital, "일본"))

def return_capitalcity(capital, country):
    return country + '->' +  capital[country]

capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이", "덴마크":"코펜하겐"}

print(return_capitalcity(capital, "대한민국"))

print("모든 수도를 알아보자!!!")
def all_capitalcity(capital):
    res = ''
    for i in capital:
        res += i + ' : ' +  capital[i] + '\n'
    return res

capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이", "덴마크":"코펜하겐"}

print(all_capitalcity(capital))

##### 예제 4: 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의해보자
def make_list(string):
    ### coding here ###
    res = []
    for i in string:
        res.append(i)
    print(res)

make_list("naver")
make_list("facebook")

##### 예제 5: 숫자로 구성된 하나의 리스트를 입력 받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 정의
def pickup_even(items):
    ### coding here ###
    num = []
    for i in items:
        if i % 2 == 0:
            num.append(i)
    print(num)

pickup_even([3, 4, 5, 6, 7, 8])

##### 예제 6: 문자열과 index k 값을 입력 받아 문자열 string의 k 번째 문자를 출력하는 함수를 만들어보자.
def find_character(string,k):
    print(string[k-1])

find_character("computer",2) # o 출력
find_character("happy",1) # h 출력
find_character("data",3) # t 출력