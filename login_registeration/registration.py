from myFunction.my_functions import user_name, user_email, user_password, user_phone, save_to_file

registration_options = """ 

registeration :

1-enter your name :
2-enter your last name :
3-enter your email :
4-enter your password :
5-confirm your pasword :
6-enter your phone number :

"""

def registration_system():
    print(registration_options)

    first_name_data = user_name("first")
    last_name_data = user_name("last")
    user_emaile_data = user_email()
    user_password_data = user_password()
    user_phone_data = user_phone()

    file = open("user_data.txt", "a")
    # file.write(f"{first_name_data}:{last_name_data}:{user_emaile_data}:{user_password_data}:{user_phone_data}\n")
    # file.write(f"""first_name_data:{first_name_data},last_name_data:{last_name_data},user_emaile_data:{user_emaile_data},user_password_data:{user_password_data},user_phone_data:{user_phone_data}\n""")
    # file.close
    user_data = {
        "first_name_data": first_name_data,
        "last_name_data": last_name_data,
        "user_emaile_data": user_emaile_data,
        "user_password_data": user_password_data,
        "user_phone_data": user_phone_data
    }
    filename = "user_data.txt"
    save_to_file(filename, user_data)
    return True
