#slicing & Indexing
a = "Hello Python"
print(a[6:] + ' ' + a[0:5]) # [6:]6번부터 시작해서 끝까지 / 

b="Hello"
print(b[::-1]) # 거꾸로
print('-' * 30)

# 리스트(list), 튜플(tuple), 사전(dict)
# 1. 리스트
# - 배열로 생각
# - 변경 가능, 순서형
print(type([])) #리스트
print(type(())) #튜플
print(type({})) #사전(dict)
print('-' * 30)

L = [1,2,3]
print(type(L))
print() #다음줄로 내려가라
print('크기=',len(L)) #개수
print(L[1]) #0번부터 시작하므로 1번방인 '2'가 나온다
print(L[-1]) #거꾸로 시작해 -3, -2, -1 순이므로 결과값은 '3'이 나온다
print(L[1:3]) #리스트 형태로 가져온다. [2, 3]
print()
print(L + L) #결합
print(L * 3) #반복
print(L)
print('-' * 30)

d={'one':[1,2,3], 'two':(1,2,3), 'three':'set'}
print(d['two'])  
print(d['one'])
print(d['three'])
print('-' * 30)

k=[1,2,3]
k[1]=10
print(k)
print('-' * 30)

#range(n) : 0부터 (n-1)까지
p = range(10)
print(p)
print(list(p))
print(list(p)[::-1])
print(list(p)[::2]) # [0, 2, 4, 6, 8]
print('-' * 30)

# 2. 튜플
# - 변경 불가능, 순서형
# - 요소가 1개일 경우에는 반드시 , 를 써야한다
t = (1,2,3)
print(t)
print('크기=', len(t))
print(t[-1]) # 뒤에서 첫번째 값
print(t+t+t) #반복
print(t*3) # 위와 같은 결과
print(4 in t) #False - t안에 4가 있는가
print()

s = (4)
print(s)
print(type(s))

s2 = (5,)
print(s2)
print(type(s2))
print('-' * 30)

# 3. 사전
# - 변경 가능, 순서형X
d = {'one': 'apple', 'two': 'orange', 'three': 'banana'}
print(d['one']) # apple
print(d) # {'one': 'apple', 'two': 'orange', 'three': 'banana'}

d['four']='melon'
print('추가=', d)

d['one']='strawberry' # 기존 one의 값이었던 apple이 strawberry로 바뀐다
print('변경=', d) # 변경= {'one': 'strawberry', 'two': 'orange', 'three': 'banana', 'four': 'melon'}

print('two' in d) # True

print('키=', d.keys())
print('값=', d.values())
print(d.items()) # dict을 list형태로 결과값을 냄
print('-' * 30)

list1 = []
list2 = [1,2,3,4,5]

tup1 = () # 초기화
tup2 = (1,2,3,4,5)
tup3 = 1,2,3,4,5

set = {1,2,3,4,5}

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print(list1, type(list1))
print(list2, type(list2))
print(tup1, type(tup1))
print(tup2, type(tup2))
print(tup3, type(tup3))
print(set, type(set))
print(dic, type(dic))
print('-' * 30)

#format() 함수
# - {}괄호를 이용한 문자열 포맷팅을 한다.
# - %와 동일한 기능들을 지원하며, 변수의 타입과 상관없이 괄호와 숫자만 이용한다.

s = "{} {} {}".format(100, "Hello", 1.1)
print(s) # 100 Hello 1.1

print(5/3) # 1.6666666666666667
print("{:10.2f}".format(5/3)) #       1.67 - 총 10자리, 5에서 3을 나눈 값의 소수점 둘째자리까지, 나머지는 공백으로 채우기
print('Hello, {0}'.format('world!'))
print('Hello, {1} {0}'.format(100, 200))
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.8))
print('{0} {0} {1} {1}'.format('Python', 'Script')) # Python Python Script Script
print('Hello, {language} {version}'.format(language='Python', version=3.6)) # Hello, Python 3.6
print()

print('%03d' %1) #001 - 백의 자리까지 나옴. 빈자리는 0으로 채우기
print('{0:03d}'.format(2)) #002 - 빈자리는 0으로 채우면서 전체 3자리 중 0번째 값만 꺼내와라
print('{2:05d}'.format(1, 2, 3)) #00003 - 빈자리는 0으로 채우면서 전체 5자리 중 2번째 값만 꺼내와라
print()

s="123"
print(s.zfill(5)) # 00123 - 5자리를 잡고 나머지는 0(zero)로 채워라
print(s.rjust(5, '#')) # ##123 - 나머지는 #으로 채워라
print('goofy'.zfill(6)) # 0goofy

print("{:10.6f}".format(5/3))
