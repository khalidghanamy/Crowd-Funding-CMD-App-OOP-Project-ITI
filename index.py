


import email
from login_registeration.login import login
from login_registeration.registration import registration_system
from crud_menu import crud_minu


main_page_menu = """
====================
HOME PAGE :
====================

1- longin 
2- registeration
3- exit
"""

def main_page():

    authourized = []
    finished_crud = 0
    email = ""
    while True:

        print(main_page_menu)
        form = input("select from list : ")
        if form == "1":
            authourized = login()
        elif form == "2":
            registered = registration_system()
            if registered:
                continue

        if authourized:
            logged_user = authourized[1]
            finished_crud = crud_minu(logged_user)
        if finished_crud:
            print("good bye")
        if form == "3":
            break

main_page()