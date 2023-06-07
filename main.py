a = 5
if a< 6:
    pass
else:
    print("6보다 큼")

for i in range(5):
    print(i)

for i in range(2,7):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(-1,-10,-2):
    print(i)

a = range(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# for in
st = "멋쟁이 사자"
for ch in st:
    print(ch)
else:
    print("Else")

print("코드 종료")

# 첫번째 while 루프
a = 1
while a <= 10:
    print(a)
    a += 1
print("코드 종료")

a = 2
while a <= 20:
    print(a)
    a += 2
print("코드 종료")

a = 1
while a <= 10:
    print(a)
    a += 1
else:
    print("While 조건이 거짓이므로 Else 부분 실행됨")
print("코드 종료")

# 무한 루프
# while True:
#     print("멋쟁이 사자")
# print("코드 종료")

i = 0
while True:
    i += 1
    print(i)
    if i == 5:
        break
print("코드 종료")

# 중첩
i = 1
while i <= 3:
    print("Outer Loop", i)
    i += 1
    j = 1
    while j <= 5:
        print("Inner Loop", j)
        j += 1
print("코드 종료")

# i = 11
# while(i < 10):
#     i+= 1
#     print("i: ",i)
# else:
#     print("else")

# 예제 1: 간단한 if 문
x = 5
if x > 3:
    print("x는 3보다 큽니다.")

# if else
age = 18
if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다.")

# 중첩된 if else
score = 50
if score >= 90:
    print("A 학점")
else:
    if score >= 80:
        print("B 학점")
    else:
        if score >=70:
            print("C 학점")
        else:
            print("D 학점")

# 예제 4: if elif
marks = 75
if marks >= 90:
    print("A 등급")
elif marks >= 80:
    print("B 등급")
elif marks >= 70:
    print("C 등급")
else:
    print("D 등급")

a = int(input("Enter Number Hreater then 2:"))
if a >= 2:
    print("Correct!! You have Entered: ", a)
else:
    print("Wrong!! You have Entered:", a)

day = input("요일을 입력하세요: ")
if day == "Mon":
    print("오늘은 월요일")
elif day == "Tue":
    print("화요일")
elif day == "Wed":
    print("수요일")
else:
    print("휴일")


name = input()

print(name)

name = input("Your Name: ")
mobile = input("Enter Your Mobile Number:")
mb = int(mobile)
print(mb, type(mb))

print(mb, type(mb))

price = int(input("Total Price:"))

print(price)
complex_number = complex(input("Enter Complex Number:"))
print(complex_number)

print("He said, \"Hello World\"")
print('He said, "Hello World"')
print('It\'s beautiful day')
print("It's beautiful day")


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



# 줄바꿈 없이 출력
print("1")
print("2", end='')
print("3")
print("4")

# 명시적 타입 변환
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

# 암시적 타입 변환
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