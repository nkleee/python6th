data = [10, 20, -50, 21.3, 'LikeLion']
print(data)

print("Like", "Share", "Subscribe", sep='')
print("Like", "Share", "Subscribe", sep='***')

print("Like", "Share", "Subscribe", sep='***', end='\t')
print("Like", "Share", "Subscribe", sep='***', end='\n')

m = 40
print("value: ", m)

name = "배정만"
age = 42
print("My name is", name, "and My age is", age, sep=' ')



#줄바꿈 없이 출력
print("1")
print("2", end='')
print("3")
print("4")

#명시적 타입 변환
n5 = ("Kim", "Bae", "Park", "Lee")
vn5 = list(n5)

print(n5, type(n5))
print(vn5, type(vn5))

n5 = "멋쟁이 사자"
vn5 = tuple(n5)

print(vn5, type(vn5))

a = 5
b = 2
value = a / b
print(type(value))
int_value = int(value)
print(int_value, type(int_value))

q = 20
u = '10'
print(type(u))
r = q + int(u)
s = str(q) + u
print(r, type(r))
print(s, type(s))

n1 = 10.36
vn1 = int(n1)

print(vn1, type(vn1))

n1 = 10
vn1 = complex(n1)

print(vn1, type(vn1))

#암시적 타입 변환
a = 5
b = 2
print(b, type(b))
value = a / b
print(value)
print(type(value))

x = 10
y = 5.5
total = x + y
print(total)
print(type(total))

j = "Hello"
k = "like lion"
p = j + k
print(p)
print(type(p))

# q = 20
# u = '10'
# r = q + u
# print(r)

# is 연산자
a = 10
b = 10
print(a is not b)

a = 10
b = '10'
print(a is not b)

#멤버 in 연산자

st1 = "Welcome to 멋사"
print("to" in st1)

st2 = "Welcome 멋사"
print("to" in st2)

st3 = "Welcome todo 멋사"
print("to" in st3)

# 비트 연산자
a = 10
b = 15

print('a: ', bin(a))
print('b: ', bin(b))
print('a & b: ', a & b)
print('a << 2: ', a << 2)
print('a >> 2: ', a >> 2)

# 할당 연산자
a = 10
b = 20
m = 15

y = a + b
print(y)

m += 10
print(m)

m **= 2
print(m)

m //= 10
print(m)

# 논리 연산자 (4교시)
a = 5
b = 2
c = 3
d = 200

print('AND 연산자')
print('a > b and a > c:', a > b and a < c)

print('OR 연산자')
print('a > b and a > c:', a > b or a < c)

print('NOT 연산자')
print('not(a < b):', not(a < b))


# 덧셈 (3교시)
a = 4
b = 2.0
total = a + b
print('total = a + b:', total)

# 뺄셈
total = a - b
print('total = a - b:', total)

# 곱셈
total = a * b
print('total = a * b:', total)

# 나눗셈
print('a / b:', a / b)

# 나머지
a = 5.5
b = 2.0
print('a%b: ', a % b)

# 거듭제곱
print('a ** b: ', a ** b)

# 몫 (양수)
print('a // b: ', a // b)

# 몫 (음수)
a = -5
print('a // b(음수) :', a // b)

# 비교 연산자
a = 5
b = 2
print('a < b: ', a < b)

print('a <= b: ', a <= b)

print('a == b: ', a == b)

print('a != b: ', a != b)


# 변수 선언 (2교시)
a = 10
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (4, 5, 6)
f = {7, 8, 9}
g = {"apple": 1, "banana": 2, "orange": 3}

# 데이터 타입 출력
print("a: ", type(a))
print("b: ", type(b))
print("c: ", type(c))
print("d: ", type(d))
print("e: ", type(e))
print("f: ", type(f))
print("g: ", type(g))