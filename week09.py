a = '파이썬'
b = "python"

print(a)

for i in a:
    print(i)

c = []
for i in a:
    c.append(i)
print(c)

print(len(b))

pp = "파이썬프로그래밍"
print(pp[2:])

id_num = ['1234-1111', '1111-2222']
for i in id_num:
    if i[5] == '3' or i[5] == '2':
        print("여자")
    else: print("남자")
# 만약 - 다음 자리 숫자로 남/녀 판별해야 한다면?
# for i in id_num:
#     if i[i.find('-')+1] == '2' or i[i.find('-')+1] == '4':
#         print("여자")
#     else: print("남자")

hi = 'hello'
# for문 2개 똑같은 결과
for i in range(len(hi)):
    print(hi[i], end='')
print()
for i in hi:
    print(i, end='')
print()

# game369
number = int(input("숫자 몇 까지?"))
clap = 0

for i in range(1, number+1):
    for j in str(i): # j의 타입은 str / i의 타입은 int
        if j == '3' or j == '6' or j == '9':
            clap += 1
print("clap =", clap)

# 대소문자 변환(시험X)

# 대소문자 확인(시험X): 싹 다 소문자이거나 대문자여야만 True 반환함

word = '공부가 너무 재미있어서 공부도 너무 공부만 하고 싶어요'
print(word.count("공부")) # 원하는 문자열이 몇 개 있는지

print(word.find("너무")) # index 값 반환!
print(word.find("너무", 5)) # 5번 인덱스부터 찾음
print(word.find("너무", 5, 12)) # (시작 인덱스, 끝 인덱스) / -1 반환 = 없다는 의미

hate = '파이썬 싫어 파이썬 정말 싫어 파이썬 재미없어 노잼'
print(hate.find('싫어', 5))

print(hate.rfind('재미')) # 오른쪽부터 찾은 단어가 몇 번째 index인지 반환
print("len =", len(hate))

funny = ['나는', '파이썬', '재미', '없어']
print(funny.index('재미')) # list의 몇 번째 원소인지

# list에서는 .index('찾고 싶은 단어')
# String에서는 .find('찾고 싶은 단어')

w = ' 안녕 하세요 '
print(w)
print(w.strip()) # 앞뒤 공백을 없애줌
print(len(w.strip()))
print(w)

phone = '010-1234-5678'
print(phone.replace('-', '')) # replace('교체하고 싶은 원래 문자', '교체할 문자')
print(phone)

pic = 'pic.jpg'
print(pic.replace('jpg', 'txt'))

road = 'genie/com'
print(road.replace('/', '\\')) # \를 출력하려면 이스케이프 문자 \\ 사용

intro = '나는 공부가 너무 재미있어서 공부 공부 공부'
print(intro.split()) # 괄호 안에 아무것도 안 쓰면 띄어쓰기 기준으로 리스트를 만든다
print("낱말 개수 =", len(intro.split()))

intro_check = intro.split() # 리스트로 생성되었기 때문에
print("첫번째 단어는?", intro_check[0]) # 대괄호[] 사용 ㄱㄴ

sentence = '하나:둘:셋'
print(sentence.split(':'))

score = '90,80,70'
print(score.split(','))
print("score =", score)
hap = 0
for i in score.split(','):
    hap += int(i)
print(hap)
#print("sum =", sum(score))

res = ['a', 'b', 'c']
print(''.join(res)) # join은 리스트를 문자열로 만들 때 사용한다
print(type(res))
print('@'.join(res))

phone_num = ['010', '1234', '5678']
print('-'.join(phone_num)) # '리스트 요소 사이에 넣고 싶은 문자열'.join(사용하고 싶은 리스트)

# list --> 문자열: '요소 사이 넣고 싶은 문자'.join('사용하고 싶은 리스트')
# String --> list: 바꿀 문자열.split('나눌 기준 문자')