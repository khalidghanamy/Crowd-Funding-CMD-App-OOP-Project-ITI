
from datetime import datetime














def project_title():
    while True :
        title = input("please enter project title : ")
        if title and title.isalpha():
            return title
        else :
            print("title is not valid")
            continue

def project_details():
    while True :
        details = input("please enter project details : ")
        if details and details.isalpha():
            return details
        else :
            print("details is not valid")
            continue

def project_total_target():
    while True :
        total_target = input("please enter project total_target : ")
        if total_target and total_target.isnumeric():
            return total_target
        else :
            print("total target is not valid")
            continue

def project_date(data):
    format = "%H:%M:%S"
    while True :
        project_date = input(f"please enter project {data} : ")
        if bool(datetime.strptime(project_date, format)):
            return project_date
        else :
            print("time is not valid")
            continue

