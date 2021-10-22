import sys
import keyword

print (3+2)
print ("Hello World") # '문자열' 또는 "문자열"
print('-' * 30) # '-' 30번 반복
 
print(4 + 5)
print(12 - 32)
print((4 + 5) * 6)
print(4 + 5 * 6)
print(9 / 5) 
print(9.0 / 5.0)
print(9 / 5.0)
print('-' * 30)

print(sys.version)
print()
print(sys.version_info)
print('-' * 30)

print(keyword.kwlist)
print('-' * 30)

# 기본 운영
a="123"
print(a, type(a))

b = int(a)
print(b, type(b))
print('-' * 30)

#입력
name = input("이름 입력 : ") 
age = int(input("나이 입력 : "))
#print(name, age)
print(name, end=",")
print(age)

print(name, end="\t")
print(age)
print('-' * 30)

#이름, 국어, 영어, 수학 점수를 입력받아서 총점과 평균울 구하시오
name = input("이름 입력 : ")
kor = int(input("국어 입력 : "))
eng = int(input("영어 입력 : "))
math = int(input("수학 입력 : "))
tot = kor+eng+math
avg = tot / 3

print('%10s %7s %7s %7s %8s %7s' %('이름','국어','영어', '수학' ,'총점' ,'평균'))
print('%10s %9d %9d %9d %9d %9f' %(name, kor, eng, math, tot, avg))
print('%10s %9d %9d %9d %9d %9d' %(name, kor, eng, math, tot, avg))
print('%10s %9d %9d %9d %9d %9s' %(name, kor, eng, math, tot, avg))
print('-' * 30)
print('이름','\t','국어','\t','영어','\t','수학','\t','총점','\t','평균')
print(name,'\t',kor,'\t',eng,'\t',math,'\t',tot,'\t',(tot/3))

# 서식 출력
# 서식 문자 : %d %f %s
# 정수형 : %d, %자릿수d
# 실수형 : %f, %전체자릿수.소수이하.자릿수f
# 문자열 : %s, %자릿수s

#주석
'''
여러 줄 주석
'''

"""
여러 줄 주석
"""

#주석 또는 여러 줄의 문자열 처리
str = '''
안녕하세요
반갑습니다
'''
print(str)


