# ##### 2024-1학기 파이썬프로그래밍 (A0019 퀴즈) #####
# # ----------------------------------------------------------------------------------------------------------
# # 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# # (1) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# # (2) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# # (3) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# # ----------------------------------------------------------------------------------------------------------

# # 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# # 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

# ##### 대답 : 동의합니다
# ##### 학번 : 20211689
# ##### 이름 : 김현진


##### 1번 문제 #####

in_str = input('영어 문자열을 입력해주세요:')

## coding here ##
result=''
for i in in_str:
    if not i in result: # if i not in result: 보통 not in으로 사용함!
        result += i
print(result)


##### 2번 문제 #####

def find_max(x):
   ## coding here ##
   m = 0
   j = ''
   for i in x:
       if m < x[i]:
           m = x[i]
           j = i
   return j

scores = {'Tony': 92, 'Alice': 88, 'Suzy':91, 'Joshua':79, 'Antonio':97}

res = find_max(scores)
print(res)


##### 3번 문제 #####

## coding here ##
f = open("quiz.txt", 'r')

lines = f.readlines()

amount = 0
for line in lines:
    amount += int(line.strip().split(':')[1]) # split하면 list가 됨

avg = 0.0
avg = amount / len(lines)
print(avg)

f.close()

# 이름의 길이가 3인 애들의 평균은?
f = open("quiz.txt", 'r')

lines = f.readlines()

amount = 0
count = 0
for line in lines:
    if (len(line.strip().split(':')[0])) == 3:
        amount += int(line.strip().split(':')[1])
        count += 1

avg = 0.0
avg = amount / count
print(avg)

f.close()