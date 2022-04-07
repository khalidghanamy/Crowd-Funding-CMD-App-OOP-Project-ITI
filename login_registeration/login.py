
from myFunction.my_functions import user_email,read_user_file
def login():
    result = ""
    while True:
        user_email_data = user_email()
        uesr_passowrd = input("Enter your passowrd : ")

        result = read_user_file(user_email_data,uesr_passowrd)
        if result:
            ask_user = input("try again (y) : ")
            if ask_user == "y":
                continue
            else:
                result = "not authorized"
                return result
        else:
            result = "logged"
            return [result,user_email_data]
    







