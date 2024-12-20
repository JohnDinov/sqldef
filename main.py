import sqlite3

connection = sqlite3.connect("user.db") # Подключаемся к базе данных
cursor = connection.cursor() # Создаём курсор управления

def create_user(name: str, surname: str, user_id: int, balance: int, role: str):
    """ Создание пользователя
    Входные данные:
        name(str): Имя пользователя
        surname(str): Второе имя пользователя
        user_id(int): Идентификатор
        balance(int): Баланс пользователя
        role(str): Роль пользователя

    Данная функция добавляет в базу данных нового пользователя по указанным параметрам

    """
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (name, surname, user_id, balance, role))
    connection.commit()

# Запрашиваем данные
name: str = input("Name: ")
surname = input("Surname: ")
user_id = input("UserID: ")
balance = input("Balance: ")
role = input("Role: ")

# Создаём пользователя
create_user(name, surname, user_id, balance, role)
print("User created!")

# Закрываем базу данных
connection.close()
