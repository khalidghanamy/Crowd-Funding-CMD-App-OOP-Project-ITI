from myFunction.crud_functions import create_project, view_all_projects,delete_projects,search_project,edite,edite_menu,clear_file

crud_minu_list = """ 
====================
CRUD MENU
====================

1-view all projects : 
2-create a project : 
3-edit project : 
4-delete project : 
5-search for a project : 
6-close menu : 


"""


def crud_minu(logged_user,project_id):
    
    minu = ["1", "2", "3", "4", "5", "6"]
    while True:
        print(crud_minu_list)

        res = input("select from list : ")

        if res in minu:
            if res == "1":
                view_all_projects(logged_user)
            if res == "2":
                create_project(logged_user)
            if res == "3":
                clear_file()
                data = edite_menu()                
                edite(logged_user,project_id,data[0],data[1],data[2],data[3],data[4])
                clear_file()
            if res == "4":
                
                view_all_projects(logged_user)
                project_id = input("enter project id to delete it : ")
                delete_projects(logged_user,project_id)

            if res == "5":
                title = input(" Enter title : ")
                search_project(logged_user,title)

            if res == "6":
                break
        else:
            continue
    return 1


crud_minu("kh@kh.cc","1")