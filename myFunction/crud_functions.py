


from ast import literal_eval
from functools import total_ordering
from turtle import title
from myFunction.project_validation import project_title,project_details,project_total_target,project_date
from myFunction.my_functions import save_to_file





def create_project(logged_user):
        project_tittle_data = project_title()
        project_details_data = project_details()
        project_total_target_data = project_total_target()
        project_start_date = project_date("start")
        project_end_date = project_date("end")
        project_id = project_id_generator()
        project_id +=1


        project_data = {
            "project_id":project_id,
            "owner_email":logged_user,
            "title":project_tittle_data,
            "details":project_details_data,
            "total_target":project_total_target_data,
            "start_time":project_start_date,
            "end_time":project_end_date
        }

        file_name = f"projects.txt"
        save_to_file(file_name,project_data)


def view_all_projects(logged_user):
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\projects.txt"
    counter = 0
    header = """"

============>>> YOUR PROJECTS <<<============

"""
    print(header)
    with open(file_path,"r") as file:
        my_project = file.readlines()
        
        file.seek(0)
        for line in my_project:
        
            data = literal_eval(line)
    
            if data["owner_email"] == logged_user:
                counter+=1
                title = data["title"]
                project_id = data["project_id"]
                print(f"{counter}- title is {title} and id = {project_id} .")
            
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
    

def delete_projects(owner,project_id):
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\projects.txt"

    with open(file_path,"r+") as file:
        my_project = file.readlines()
       
        file.seek(0)
        for line in my_project:
           
            data = literal_eval(line)
            
            if data["owner_email"] == owner and data["project_id"] == int(project_id):
                pass
            else:
                file.write(line)
        file.truncate()
    print("=========> Deleted <==========")


def search_project(logged_user,title):
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\projects.txt"
    counter = 0
    

    header = """"
============
============>>> YOUR SEARCH <<<============
============
"""
    print(header)
    with open(file_path,"r") as file:
        my_project = file.readlines()
        file.seek(0)
        for line in my_project:
        
            data = literal_eval(line)
          
            if data["owner_email"] == logged_user and data["title"] == title:
               
                counter +=1
                title = data["title"]
                project_id = data["project_id"]
                print(f"{counter}- title is {title} and id = {project_id} .")
            
        if counter == 0:
            print("not found")
    
def project_id_generator():
    my_project = view_all_projects()
    
    projects_number= my_project.split("owner_email")
    if len(projects_number):
        return len(projects_number)-1
    else:
        return 0

def edite(logged_user,id,title="",details="",total_target="",start_time="",end_time=""):
    file_path = f"D:\\41\\day02\\day02_lab\\my_database\\projects.txt"

    with open(file_path,"r+") as file:
    
        my_project = file.readlines()
        
        str1 = ''.join(my_project)
        fixed_data=str1.split("\n")
        for index,line in enumerate(my_project) :
            data = literal_eval(line)
            
            if data["owner_email"] == logged_user and data["project_id"] == int(id):

                if title:
                    data['title'] = title
                    fixed_data[index]=str(data)
                    
                if details:
                    data['details'] = details
                    fixed_data[index]=data
                    
                if total_target:
                    data['total_ordering'] = total_target
                    fixed_data[index]=data
                    
                if start_time:
                    data['start_time'] = start_time
                    fixed_data[index]=data
                    
                if end_time:
                    data['end_time'] = end_time
                    fixed_data[index]=data
        
        for index,line in enumerate(fixed_data):
            if index==0:
                file.truncate(0)
                clear_file()
            
            file.write(f"{str(line)}\n")


def edite_menu():
    title = ""
    details=""
    total_target=""
    start_time=""
    end_time=""

    menu_to_edite = """"

============
============>>>  UPDATE <<<============
============

1-title
2-details
3-total_target
4-start_time
5-end_time
6-close
    """
    print(menu_to_edite)
    while True:
        
        res = input(' select to edite : ')
        if res == "1" :
            title = input(' new title : ')
        elif res == "2" :
            details = input(' new details : ')
        elif res == "3" :
            total_target = input(' new total_target : ')
        elif res == "4" :
            start_time = input(' new start_time : ')
        elif res == "5" :
            end_time = input(' new end_time : ')
        elif res == "6" :
            break
    
    data = [title,details,total_target,start_time,end_time]
    return data

