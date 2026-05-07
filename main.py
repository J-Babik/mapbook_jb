# definicja prostej struktury danych obejmującej przykładowego użytkownika
from random import choice

users = [
    {"name": "Artur", "location": "Łomża",
     "posts": ["Sprzedam mercedesa", "Kupię skrzynię biegów", "Ratunku, co robić po wypadku",
               "Kto dzisiaj idzie biegać"]},
    {"name": "Daniel", "location": "Jabłonna",
     "posts": ["Mój kod nie działa, pomocy"]},
    {"name": "Kamil", "location": "Ciechanów",
     "posts": ["Czy ktoś zrobił już sprawozdanie z PPyth", ]}

]

def read_users(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował post {user['posts'][-1]}")

read_users(users)

def add_user(users_data: list) -> None:
    users_data.append({"name": input("Podaj imię użytkownika: "), "location": input("Podaj miejscowość użytkownika: "),
                       "posts": ["Dołączono do znajomych"]})

def delete_user(users_data: list) -> None:
    user_to_remove = input("Podaj imię do usunięcia: ")
    for user in users_data:
        if user["name"] == user_to_remove:
            users_data.remove(user)

def update_user(users_data: list) -> None:
    user_to_update = input("Podaj imię znajomego do update: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowe imię użytkownika: ")
            user["location"] = input("Podaj nową miejscowość użytkownika: ")

def update_user_post(users_data: list) -> None:
    user_to_update = input("Podaj imię znajomego do update: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Co słychać? "))

while True:
    print("==========MENU============")
    print("0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodaj znajomego")
    print("3 - usuń znajomego")
    print("4 - update znajomego")
    print("5 - update posta")
    choice = input("Wybierz opcję menu: ")
    print(f"wybrano opcję {choice}")
    if choice == "0":
        break
    if choice == "1":
        read_users(users)
    if choice == "2":
        add_user(users)
    if choice == "3":
        delete_user(users)
    if choice == "4":
        update_user(users)
    if choice == "5":
        update_user_post(users)



