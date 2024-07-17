x = (1,2,3,4) # 튜플은 (소괄호)
print(x)

# 튜플 시험X

# 튜플은 수정, 삽입이 안 된다. -> 바꾸면 안 될 때 사용
# 리스트는 append, remove 등 ㄱㄴ

a = [10] # 리스트는 하나만 넣어도 [대괄호] 출력됨
print(a)
a = (10) # 튜플은 하나만 넣으면 그대로만 나온다.
print(a)
a = (10,) # 튜플에서 하나만 넣을 때는 뒤에 ,컴마 찍기
print(a)

# 튜플은 순서가 정해져 있음 -> 튜플 안에서 순서가 다르면 서로 다른 튜플

y = list(x)
print(y)

y[0] = 0
x = tuple(y)
print(x)

#####

info = {'이름':'지니', '전공':'ds', '나이':40} # 딕셔너리는 늘 쌍(key & value)으로 존재해야 한다
print(info)
print(len(info)) # 쌍의 개수

name_info = {'이름':'지니', '이름':'홍길동'} # key는 중복되어서는 안 된다
print(name_info) # 덮어쓰기 됨

same_info = {'이름':'ds', '전공':'ds'} # value는 중복 ㄱㄴ
print(same_info)

print(info['이름'])
print(info['전공'])
print(info['나이'])

print("\ninfo")
for i in info:
    print(i, info[i]) # key, value

print("\ninfo.keys()")
for i in info.keys(): # info == info.keys()
    print(i, info[i])

print("\ninfo.items()") # info == info.keys() == info.items()
for k,v in info.items():
    print(k,v)

print("\n<value값만>")
print("info")
for i in info:
    print(info[i])

print("\ninfo.keys()")
for i in info.keys():
    print(info[i])

print("\ninfo.items()")
for k,v in info.items():
    print(v)

print("\ninfo.values()")
for i in info.values():
    print(i)

info['나이'] = 24 # 원래 있던 key값 덮어쓰기로 바꾸기 ㄱㄴ
info['전번'] = '010-1234-5678' # 새로 추가 ㄱㄴ
print(info)

# 딕셔너리는 순서가 없다

del(info['전번'])
print(info)

print(info.keys())
print(list(info.keys())) # dict_keys가 없어짐

list_key_info = list(info.keys())
print((list_key_info[0]))

print(info.values())
print(list(info.values())) # dict_values가 없어짐

list_value_info = list(info.values())
print((list_value_info[0]))

print(info.items())
print(list(info.items())) # dict_items가 없어짐

print(info['이름'])
print(info.get('이름'))

##### 예제 3: 끝 입력 전까지 무한 반복문 생성
foods = {"떡볶이":"김밥", "자장면":"단무지", "라면":"파김치", "치킨":"맥주", "삼겹살":"소주"}

print(foods['떡볶이'])

print(foods)
print(list(foods))
print(list(foods.keys()))

answer = input("%s중 좋아하는 음식은?" %(list(foods.keys()))) # 이렇게 써도 되나? ㅇㅇ
print(str(answer) + " 궁합 음식은" + str(foods[answer]) + " 입니다") # 출력문 내에서 +로 바로 출력해도 ㄱㅊ? str()로 감싸야 함
print(str(answer), "궁합 음식은" + str(foods[answer]), "입니다") # 출력문에서 ,컴마랑 + 혼합 사용 ㄱㄴ? 정석적인 방법은 아님

print("\n질문 시작!")
while True:
    answer = input(str(list(foods.keys())) + "중 좋아하는 음식은?")

    if answer == '끝':
        break

    print("%s 궁합 음식은 %s 입니다." %(answer, foods[answer]))

##### 예제 4: 딕셔너리로 성적 합계/평균 구하기
scores = {"김예진": 90, "박영진": 95, "김소희": 84}

sum = 0
for key in scores:
    sum += scores[key]
    print('%s : %d' % (key , scores[key]))

avg = 0.0 # 초기값 넣어주면 오류 방지 ㄱㄴ
avg = sum/len(scores)

print('합계 : %d, 평균 : %.2f' % (sum, avg))