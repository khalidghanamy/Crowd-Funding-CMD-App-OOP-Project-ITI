


from pathlib import Path
import re
import hashlib
from ast import literal_eval
import os
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def user_name(name):
    while True :

        first_name = input(f"please enter your {name} name : ")
        if first_name and first_name.isalpha():
            return first_name
        else :
            print("name is not valid")
            continue

  
def user_email():
    while True :
        email = input("please enter your email : ")
        if re.fullmatch(regex,email):
            return email
        else :
            print("email is not valid")
            continue

def user_password():
     while True :
        password = input("please enter your password : ")
        confirm_password = input("please confirm your password : ")
        if password and len(password) >= 8 and password == confirm_password:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return hashed_password
        else :
            print("password is not valid")
            continue

def user_phone():
    while True :
        user_phone = input("please enter your phone number : ")
        if user_phone and user_phone.isnumeric():
            return user_phone
        else :
            print("user_phone is not valid")
            continue


def save_to_file(file_name,data):
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\{file_name}"
 
    file = open(file_path,"a")
    file.write(f"{str(data)}\n")
    file.close

def read_user_file(email,password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\user_data.txt"

    file = open(file_path,"r")
    lines = file.readlines()
    flag =True
    for line in lines:
        # data = line.split(":")
        data = literal_eval(line)
        if data["user_emaile_data"]== email and data["user_password_data"] == hashed_password:
            print("logged successfully")
            flag = False

    file.close()
    return flag
    
    

def ask_user_to_continue():
    ask_user = input("try again (y) : ")

    if ask_user == "y":
        return True
    else:
        return False



def clear_file():
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\projects.txt"

    with open(file_path,"r+") as file:
        lines= file.readlines()
        
        file.seek(0)
        for line in lines:
            if "\x00" in line:
                pass
            else:
                file.write(line)
        file.truncate()
    
   
   

