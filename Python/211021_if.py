# 제어문 if
'''
[형식]
1. if 조건:
    참
    
2. if 조건:
    참
    else:
    거짓 
    
3. if 조건:
    참
    elif 조건:
    참
    else:
    거짓
    
파이썬에는 switch가 없다.
'''

x = 11
if x>10:
    print("참")
print('-' * 30)

x = 30
if x>10 and x<20:
    print("참")
else:
    print("거짓")
print('-' * 30)

x = 65
if x>=65 and x<=90:
    print(x, '는 대문자')
elif x>=90 and x<=120:
    print(x, '는 대문자')
else:
    print('숫자이거나 특수문자')

'''
[문제] 문자열을 입력받아서 회문인지 아닌지 출력하시오

[실행결과]
문자열 입력 : aba
aba 회문이다

문자열 입력 : abc
abc 회문 아니다
'''
str = input('문자열 입력 : ')
if str == str[::-1] :
    print(str,"은 회문입니다.")
else :
    print(str,"은 회문이 아닙니다.")


'''
[문제2] 2개의 값을 입력하여 순서대로 출력하시오

[실행결과]
a의 값을 입력 : 36
a의 값을 입력 : 25
25   36
'''

'''
a = int(input('a의 값을 입력: '))
b = int(input('b의 값을 입력: '))

if a < b :
    print(a, "\t", b)
else :
    print(b, "\t", a)
'''

a = int(input('a의 값을 입력: '))
b = int(input('b의 값을 입력: '))

if a > b :
    a, b = b, a
    
print(a, "\t", b)

