import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="project1",
    user="postgres",
    password="qwErt1928",
    port="5432"
)
cursor = connection.cursor()


def create_account(account_number, account_owner: str, balance: int):
    values = (account_number, account_owner, balance)
    cursor.execute('''INSERT INTO pycard(card_number, card_user, balance) VALUES (%s, %s, %s)''', values)
    connection.commit()
    print("Account muvaffaqiyatli yaratildi")


def pul_kirgizish(amount, card_number):
    insert_query = f"UPDATE pycard SET balance = balance + {amount} WHERE card_number = {card_number} ;"
    cursor.execute(insert_query)
    connection.commit()
    print("Pul muvofaqiyatli kiritildi !")


def pul_chiqarish(amount, card_number):
    insert_query = f"UPDATE pycard SET balance = balance - {amount} WHERE card_number = {card_number} ;"
    cursor.execute(insert_query)
    connection.commit()
    print("Pul muvofiqqiyatli chiqarildi !")


def starter():
    print("Assalomu alekum xizmatlardan birini tanlang!\n"
          "1. Akkount ochish\n"
          "2. Pul kiritish\n"
          "3. Pul chiqarish")
    choice = input("Raqam bilan tanlang: ")
    if choice == "1":
        acc_num = input("Akkountni raqamini kiriting: ")
        acc_ownr = input("Ism familyanini kiriting: ")
        create_account(acc_num, acc_ownr, 0)
    elif choice == "2":
        price = input("Qancha pul tashlamoqchisiz: ")
        crd_nmbr = input("Karta nomeringizni ayting: ")
        pul_kirgizish(price, crd_nmbr)
    elif choice == "3":
        prc = input("Qancha pul chiqarmoqchisiz: ")
        krd_number = input("Karta raqamingizni kiriting: ")
        pul_chiqarish(prc, krd_number)
    else:
        print("Bunday raqam ko'rsatib o'tilmagan")


if __name__ == "__main__":
    starter()
