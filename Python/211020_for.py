'''
for
for 변수 in range(반복횟수) :
    명령문
    
for 변수 in range(시작, 종료, 증감) :
    명령문

순환 가능 객체 : 문자열, 리스트, 튜플, 사전, range()
- for 변수 in 문자열 :
    명령문
- for 변수 in 리스트 :
    명령문
- for 변수 in 사전 :
    명령문

** while
while '조건식' :
    명령문

파이썬에는 do-while문이 없다.    

'''

for i in range(10):
    print(i, end=" ")
print()
# 0 1 2 3 4 5 6 7 8 9 

for i in range(1, 10, 1):
    print(i, end=" ")
print()
# 1 2 3 4 5 6 7 8 9 

for i in list(range(10)[::-1]):
    print(i, end=",")
print()
# 9,8,7,6,5,4,3,2,1,0,

'''
[문제1] 단은 입력하여 구구단을 출력하시오

원하는 단을 입력 : 7
7*1=7
7*2=14
...
7*9=63
'''
dan = int(input('원하는 단을 입력 : '))
for i in range(1, 10, 1):
    print(dan, " * ", i, " = ", dan*i)
print()


  
'''    
[문제2] 2~9단까지 출력하시오 (다중FOR)

2*1=2   3*1=3   4*1=4           9*1=9
'''
for i in range(1, 10):
    for dan in range(2, 10):
        print(dan, "*", i, "=", dan*i, end="\t")
print()
print()


'''
[문제3] 1~100 사이 5의 배수의 합에서 7의 배수의 합을 빼시오
5의 배수 합 = XXXX
7의 배수 합 = XXXXXXX

XXXX - XXXXXXX = ~~~    
'''
sum_5 = 0
sum_7 = 0
for i in range(1, 101):
    if i % 5 == 0: sum_5 += i
    if i % 7 == 0: sum_7 += i

print('5의 배수 합 = ', sum_5)
print('7의 배수 합 = ', sum_7)
print(sum_5, "-", sum_7, "=", sum_5-sum_7)
print("%d - %d = %d" %(sum_5, sum_7, sum_5-sum_7))
print("{0} - {1} = {2}".format(sum_5, sum_7, sum_5-sum_7))