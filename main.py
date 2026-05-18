from mapbook_lib.model import users
from mapbook_lib.controller import read_data, add_user, delete_user, update_user, get_mapa

while True:
    print("0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodaj użytkownika")
    print("3 - usuń użytkownika")
    print("4 - zmodyfikuj dane użytkownika")
    print("5 - pokaż mapę znajomych")
    choose = input("wybierz opcje: ")
    if choose == "0":
        break
    if choose == "1":
        read_data(users[1:])
    if choose == "2":
        add_user(users)
    if choose == "3":
        delete_user(users)
    if choose == "4":
        update_user(users)
    if choose == "5":
        get_mapa(users)