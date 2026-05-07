from mapbook_lib.model import users
from mapbook_lib.controler import read_users, add_user, delete_user, update_user, update_user_post, get_user_map

def main():

    while True:
        print("==========MENU============")
        print("0 - zakończ program")
        print("1 - wyświetl znajomych")
        print("2 - dodaj znajomego")
        print("3 - usuń znajomego")
        print("4 - update znajomego")
        print("5 - update posta")
        print("6 - pokaż mapę")
        choice = input("Wybierz opcję menu: ")
        print(f"Wybrano opcję {choice}")
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
        if choice == "6":
            get_user_map(users)

if __name__ == "__main__":
    main()