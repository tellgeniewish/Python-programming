# Q1. (33줄)
# score = [90, 85, 55, 70, 100, 92] 
# print("처음부터 세 번째까지 %s" %(score[:4])) 
# %s가 아니라 %d로 적으면 오류 why?
# A1. 여러 개 출력하는데 하나만 연산자 써서

# Q2. 이런 식으로 ,컴마로 이어서 변수 쓰고 출력문 사용 ㄱㄴ?
# plus_list = [1,2,3,4,5,6,7,8,9,10,9]
# print("plus_list=",str(plus_list), "\n")
# A2. 컴마 쓸 때는 전부 문자열로! str()쓰면 됨

# Q3. 평균 구할 때 score = [1,2,3,4,5]라면
# for문 반복해서 더하는거 말고
# sum(score)/len(score) 사용해도 ㄱㅊ?
# A3. ㅇㅇ

'''
문자열& 리스트
덧셈, 곱셈, for문 이용해서 하나씩 출력, len() ㄱㄴ

뺄셈, 리스트끼리는 곱셈 불가 but 숫자는 곱할 수 있다
'''

price=100
for i in range(3):
    print(price, "원", sep='%')
    if i == 2:
        print()
for i in range(5):
    print(price, "원", sep='+', end='//')
    if i == 4:
        print("\n")

score = [90, 85, 55, 70, 100, 92] # 원소를 무한대로 담을 수 있다.
print(score) # 출력 결과도 [대괄호] 안에 원소가 담긴 형태로
print(score[0]) # 하나만 출력하면 [대괄호] 없이 출력됨!!
print(score[0:1]) # 하나만 출력되게 하더라도 : 사용하면 [대괄호] 안에 출력됨

print("index 2부터 끝까지:", score[2:])
print(score[2:5]) # a:b --> a부터 b-1까지
print(score[:]) # == print(score) <<이렇게 쓸 수 있어서 [:]로는 잘 안 쓴다.
print(score[:4]) # 처음부터 세 번째까지
print("처음부터 세 번째까지 %s" %(score[:4])) 
''' %d로 적으면 오류 '''

print("뒤에서 첫 번째 %d" %(score[-1])) # 뒤에서 첫 번째
print(score[-2]) # 뒤에서 두 번째

print(score[1:-1]) # 1번 index부터 뒤에서 첫 번째-1 index까지


print(score[:-1]) # 0번 index부터 뒤에서 첫 번째-1 index까지
print(score[:-2]) # 0번 index부터 뒤에서 두 번째-1 index까지

xx = ["apple", "banana", "cat", "dog"]
for i in xx: # [대괄호] 없이 출력하는 법
    print(i, end=' ')
print()

res = 0
for i in score:
    res += i
print(res)
print("sum = %d"% sum(score))

print(len(xx))

A = [1, 5, 11, -3]
B = ["data", 0, "hi", 0]
print(A + B) # 더하기 ㄱㄴ [1, 5, 11, -3, "data", 0, "hi", 0]
print(A*2) # 곱셈 ㄱㄴ [1, 5, 11, -3, 1, 5, 11, -3]
print(B*3) # ["data", 0, "hi", 0, "data", 0, "hi", 0, "data", 0, "hi", 0]
# 뺄셈 불가능
# 리스트끼리는 곱셈 불가 but 숫자는 곱할 수 있다

# 리스트와 문자열은 상당히 비슷하다
a = "school"
b = "hello"
print(a+b)
print(a*3)
# 덧셈, 곱셈, for문 이용해서 하나씩 출력 ㄱㄴ
for i in b:
    print(i, end=' ')
print()

count = 0
for i in a:
    if i == 'o':
        count += 1
print("문자열a에서 \'o\'가 포함된 개수는", count)

arr = [1,2,3,4,5]
print(arr)

list_arr = []
print(list_arr) # 아무것도 없으면 빈 [대괄호] 출력됨

list_arr.append(0) # append한 순서대로 출력됨
list_arr.append("hi")
print(list_arr)

for i in range(2):
    list_arr.append(input("입력해주세요: "))
print(list_arr)

empty_arr = []
for i in range(1,6): # 리스트에 1부터 5까지 넣고 싶을 때
    empty_arr.append(i)
print(empty_arr)

num_arr = []
for i in range(5,0,-1): # 리스트에 5부터 1까지 넣고 싶을 때
    num_arr.append(i)
print(num_arr)

plus_list = [1,2,3,4,5,6,7,8,9,10,9]
plus_list.insert(2, 100) # insert(인덱스, 값)
print(plus_list)

change = [1,2,3,4,5]
change[3] = 100 # 덮어쓰기로 값을 바꿀 수 있다
print(change)

change.append(7)
print(change)

emt = [] # 빈 리스트에는 append로 무한대로 많은 값을 넣을 수 있다
for i in range(0, 200, 2):
    emt.append(i)
print(emt)

aa = emt
print(aa)
print((type(aa)))
print("len = ", len(aa))

bb = []
#for i in range(100):
    #bb[i] = aa[99 - i] # 오류난 이유: 아직 빈 리스트라서 [0] 칸이 없음!!!

for i in range(len(aa)):
    bb.append(aa[len(aa) - i - 1]) # 빈 리스트일 때는 반드시 append 사용해야 한다
print(bb)

A = [1, 5, 11, -3]
print(A)
print("len = ", len(A))

A[1:2] = [7, -15] # 1:2 --> 1부터 2-1 전까지인 [1]을 의미함 [1]위치에 7, -15 두 개를 넣음
print(A)
print("len = ", len(A))

A[0] = ['a', 'b'] # 리스트 안에 리스트로 들어감(시험X)
print(A)
print("len = ", len(A))

print("plus_list=", plus_list)
print()

del(plus_list[0]) # del(리스트[index])
print("del(plus_list[0])")
print("plus_list=", plus_list)
print()

plus_list[2:4] = [] # 2, 3 인덱스를 빈칸으로 없앰
print("plus_list[2:4] = []")
print("plus_list=", plus_list)
print()

plus_list.remove(9) # remove(값) 값을 삭제함
print("plus_list.remove(9)")
print("plus_list=", plus_list) # 삭제할 값이 여러 개 있는 경우 맨 앞의 값만 삭제됨
print()

#plus_list.remove(99) # 리스트에 없는 값을 삭제하려 해서 오류
#print("plus_list=", plus_list)

plus_list.pop() # 맨 뒷 칸부터 하나씩 사라짐
print("plus_list.pop()")
print("plus_list=", plus_list)
plus_list.pop()
print("plus_list=", plus_list)
plus_list.pop()
print("plus_list=", plus_list)

print("!!!!!HERE!!!!! plus_list=", plus_list, "\n")

del(plus_list) # 리스트 자체를 없앰
#print(plus_list) # 리스트 자체를 없앴기 때문에 출력하려 하면 오류

sort_arr = [7, 5, 3, 1, 8]
print("정렬 전sort_arr=", sort_arr)
sort_arr.sort() # 오름차순 정렬(reverse의 디폴트 값은 False)
print("오름차순 후sort_arr=", sort_arr)
sort_arr.sort(reverse=True) # 내림차순 정렬
print("내림차순 후sort_arr=", sort_arr)

print("len=", len(sort_arr))

gn = "genie"
print("gn len=", len(gn)) # 문자열도 len() ㄱㄴ

#bb = aa.reverse() # 안 된다, 그냥 aa가 리버스된다
aa.reverse() # 여기부터 aa는 리버스됨!
bb = aa.copy() # 복사
print(bb)

exam_score = [88, 90, 95, 100, 85]
exam_cp = exam_score.copy()
print(exam_cp)

print("100점은 몇 개?", exam_cp.count(100)) # count(값) 값의 개수를 찾음

##### 예제 1: greetings 리스트 값 순서대로 출력
greetings = ["안녕","니하오", "하이","곤니찌와","올라","싸와디캅","봉쥬르"]
for i in greetings:
    print(i)

##### 예제 2: a 리스트 값 중에서 길이가 5인 값들만 출력
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school' 'hotel', 'india']
'''
b = a.copy()
b.remove('charlie')
b[3:-1] = []
print(b)
'''

b = []
for i in a:
    if len(i) == 5:
        b.append(i)
print(b)