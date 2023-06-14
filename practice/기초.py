# 생성
menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

#추가
menu["냉면"] = 6000

#가격 출력
print(menu["짬뽕"])

#가격 수정
menu["탕수육"] = 8500

#메뉴 삭제
del menu["짜장"]

#메뉴 전체 출력
print(menu)

myGrade = int(input("학번을 입력하세요 : "))
yourGrade = int(input("학번을 입력하세요 : "))

if myGrade == yourGrade :
    print("안녕하세요 동기님!")
elif myGrade > yourGrade :
    print("안녕하세요 선배님!")
elif myGrade < yourGrade :
    print("안녕하세요 후배님!")
else :
    print("누구세요?")

orders = ["짜장", "짬뽕", "탕수육"]

food = input("먹고싶은 메뉴를 입력해주세요 : ")

if food in orders :
    print("주문할 수 있습니다.")
else :
    print("주문할 수 없습니다.")

menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}

food = input("먹고싶은 메뉴를 입력해주세요 : ")

if food in menu :
    print(menu[food], "원 입니다.")
else :
    print("주문 불가")

#100번 안녕하세요
for x in range(0,100):
	print("안녕하세요")

#2부터 31까지 2의 배수
for x in range(2, 31, 2) :
    print(x)

# 1부터 10까지 곱
result =1
for x in range(1,10,1):
	result *= x

#별 1개 찍기
print("*")

# 별 5개 찍기
for i in range(0,5):
	print("*")

# 별 5개 가로로 찍기
for i in range(0,5):
	print("*", end ="")

# 별 5개 가로 5줄 찍기
for x in range(0,5):
		print("*"*5)

# 별 삼각형 5줄 찍기
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print("*"*i)

# 입력받아 1씩 증가하며 출력
x= int(input("입력:"))
for i in range(1,x+1):
    print(i)

# 입력받아 거꾸로 감소하며 출력
x= int(input("입력:"))
for i in range(x,0,-1):
    print(i)

# 입력받아 10 넘어가면 줄바꿈 출력
for i in range(1,x+1):
    if not (i % 10): #10의 배수일때 줄바꿈
        print(i)
    else: #10의 배수 아닐때 줄바꿈 X
        print(i,end="")

# 로또 뽑아 정렬
n =int(input("로또 몇개?"))
x = []
for i in range(0,n):
    x.extend(random.sample(range(1, 45), 6))
x.sort()