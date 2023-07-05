# coffee_menu =  {
#     '1': {'name': '에스프레소', 'price': 3000},
#     '2': {'name': '아메리카노', 'price': 4000},
#     '3': {'name': '카페라떼', 'price': 5000},
#     '4': {'name': '카푸치노', 'price': 5000},
# }
#
# total_price = 0
#
# def print_menu():
#     print("\n=== 커피 주문 시스템 ===")
#     for id, coffee in coffee_menu.items():
#         print(f"{id}. {coffee['name']} - {coffee['price']}")
#
#
#
# while True:
#     print_menu()
#     choice = input("원하는 메뉴를 선택하세요: ")
#     if choice in coffee_menu:
#         total_price += coffee_menu[choice]['price']
#         print(f"{coffee_menu[choice]['name']}을(를) 주문하셨습니다.\n 현재까지의 총 금액은 {total_price}원 입니다.")
#     elif choice == '5':
#         print(f"\n주문을 종료합니다. 총 주문금액은 {total_price}원 입니다.")
#         break
#     else:
#         print("\n 잘못된 선택입니다. 다시 선택해주세요.")

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    dbname='library',
    user='postgres',
    password='6300',
)

cur = conn.cursor()

# 테이블 생성 코드
# cur.execute('''
# CREATE TABLE test_table (
# id SERIAL PRIMARY KEY,
# name VARCHAR(50))
# ''')
# conn.commit()

# 데이터 삽입 쿼리
# cur.execute("INSERT INTO test_table (name) VALUES (%s)", ("Test Name",))
# conn.commit()

# 데이터 업데이트
cur.execute("UPDATE test_table SET name = 'Change' WHERE id = 1")
conn.commit()

cur.execute('SELECT * FROM test_table')
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()