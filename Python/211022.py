f=(1,[1,2,3],2)
print(f) # (1, [1, 2, 3], 2)
print(f[0]) # 1
print(f[1]) # [1, 2, 3]
print(f[2]) # 2
print(f[1][2]) # 3

# f[2] = 5 - 튜플은 값을 바꿀 수 없으므로 에러가 뜬다
f[1][1] = 5;
print(f) # (1, [1, 5, 3], 2) - [1]은 리스트이므로 값이 변경된다.

x = 9000
y = 9000
z = 1
print(x, ", ", y) # 9000 ,  9000
print(type(x), ", ", type(y)) # <class 'int'> ,  <class 'int'>
print(id(x), ", ", id(y)) # 2635380671568 ,  2635380671568 - id() : 객체의 주소
print(x is y) # True
print(id(x) == id(y)) # True 
print(x == y) # True

'''
[문제] 아래와 같이 출력하시오 (다중 for)

1     54321
12     4321
123     321
1234     21
12345     1
'''

for i in range(1, 6): # 1<= i < 6
    for j in range(1, i+1): # i=1이라면 1, 2
        print(j, end=" ")
    print()
print('-' * 30)
    
for i in list(range(1, 6)[::-1]): # index를 잡아주기 위해 list형태로 잡아 역순을 시켜준다
    for j in range(1, i+1)[::-1]:
        print(j, end=" ")
    print()
print('-' * 30)

a = []
a = [1, 2, "Great"]
print(a[0], a[-1]) # 1 Great
print(a[1:3], a[:]) # [2, 'Great'] [1, 2, 'Great'] - a[:] 전체값
print(type(a[0])) # <class 'int'>
print(type(a[1:3])) # <class 'list'>

lt = [('one', 1), ('two', 2), ('three', 3)]
for t in lt:
    print(t)
    print(t[0], ", ", t[1])
    print()
print('-' * 30)

str = "i love you"
print(str.title()) # I Love You - 단어의 첫글자를 대문자
print(str.capitalize()) # I love you - 문장의 첫글자를 대문자
print('-' * 30)

s = [10, 20, 30, 40, 50]
s.remove(10) # 요소 중에서 10의 값을 제거
print(s) # [20, 30, 40, 50]

del s[0] # [30, 40, 50] - 인덱스 0번째 값 제거
print(s)

s = [10, 20, 30, 20, 40, 50]
s.remove(20)
print(s) # [10, 30, 20, 40, 50] - 똑같은 값이 여러 개일 경우 맨 앞에 있는 값이 제거됨

s.extend([60, 70]) # 값으로 추가되어 하나의 list가 됨
print(s) # [10, 30, 20, 40, 50, 60, 70]
s.append([60, 70]) # 리스트 형태 그대로 추가
print(s) # [10, 30, 20, 40, 50, 60, 70, [60, 70]]

s = [10, 20, 30, 40 ,50]
s.append(60)
print(s) # [10, 20, 30, 40, 50, 60] - 60 추가

print(s.pop()) # 60 - 맨 뒤의 값을 꺼내오면서 꺼내진 값은 지워진다
print(s) # [10, 20, 30, 40, 50] - 60이 지워졌음을 알 수 있다
print(s. pop(0)) # 10 
print(s) # [20, 30, 40, 50]
print('-' * 30)

#sort() - 원본 변경
L = [('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]
L.sort() # reverse=False(기본이 오름차순. 생략해주면 오름차순으로)
print(L) # [('jung', 10, 36), ('kim', 3, 28), ('lee', 5, 38)]
L.sort(reverse=True)
print(L) # [('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]

L.sort(key=lambda x: x[1]) # 중간값으로 sort
print(L) # [('kim', 3, 28), ('lee', 5, 38), ('jung', 10, 36)]

# sorted() - 원본 변경 X
num = [87, 30, 36, 78, 45]
print(sorted(num)) # [30, 36, 45, 78, 87]
print(num) # [87, 30, 36, 78, 45]
print('-' * 30)

#람다(lambda)식
L = []
for k in range(10): 
    L.append(k)
print(L) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

# 위 구문을 람다식으로 표현
print([k for k in range(10)]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('-' * 30)

L = []
for k in range(10): 
    L.append(k*k)
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()

# 위 구문을 람다식으로 표현
print([k*k for k in range(10)])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print('-' * 30)

L = []
for k in range(10): 
    if k%2:
        L.append(k*k)
print(L) # [1, 9, 25, 49, 81] 
print()

# 위 구문을 람다식으로 표현
print([k*k for k in range(10) if k%2]) # [1, 9, 25, 49, 81]
print('-' * 30)

seq1 = 'abc'
seq2 = (1, 2, 3)
L = []
for x in seq1:
    for y in seq2:
        L.append((x,y))
print(L) # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
print()

# 위 구문을 람다식으로 표현
print([(x,y) for x in seq1 for y in seq2]) 
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]

'''
함수
- 명령어들의 집합

[형식]
* 구현
def 함수명([매개변수, 매개변수])
    명령어
    [return 리턴값]
    [return 리턴값, 리턴값,...] - 여러 개의 리턴값이 생길 경우 튜플로 리턴된다
    
* 호출
함수명([값1, 값2, ...])
'''
# 자바스크립트 문법과 비슷하다.
# - 자료형이 없다

def square(x):
    return x**2

print(square(5)) # 호출

#람다함수
square2 = lambda x : x**2 # 5의 제곱
print(square2(5)) # 25 - 호출

square3 = (lambda x : x**2)(5)
print(square3) # 25

print((lambda x : x**2)(5)) # 25 - 함수명 없이도 결과값이 나온다
print('-' * 30)



'''
[문제] 람다함수를 이용하여 1~5까지의 제곱을 구하시오
'''
lst = [(lambda x : x**2)(i) for i in range(1, 6)]
print(lst)



'''
[문제] 함수(f)와 람다함수(f2)를 만드시오
x + 2*y + 5*z 의 연산결과를 리턴하도록 작성
'''
def f(x, y, z):
    return x+(2*y)+(5*z)

print(f(1,2,3));

#람다함수
f2= (lambda x,y,z : x+(2*y)+(5*z))
print(f2(1,2,3))

f3= (lambda x, y, z : x+(2*y)+(5*z))(1,2,3)
print(f3)


def test() :
    print('test')
    return # return은 생략가능

test() # 호출

#람다함수
test2 = lambda : print('test') # 매개변수 없으니 그냥 lambda : 
test2() # 호출


'''
람다(Lambda) 함수
- 한 줄로 표현된 함수
- 람다 함수는 구성이 단순해서 간단한 연산을 하는데 종종 사용된다.
- 기본 구조

lambda 인자 : 인자 활용 수행 코드

  => 람다함수에 “인자”를 전달하면, “인자 활용 수행 코드”를 수행한 후에 결과를 바로 반환한다.
'''