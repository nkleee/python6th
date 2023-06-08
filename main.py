def pw(x, y):
    z = x ** y
    print(z)

pw(2, 5)
# pw(5, 2, 3) 2개의 값을 입력 받아야하는데 3개를 받아서 error

def show(name, age=27):
    print(f"Name: {name} Age:{age}")

show(name="멋쟁이사자", age=42)

show(name="멋쟁이사자")

