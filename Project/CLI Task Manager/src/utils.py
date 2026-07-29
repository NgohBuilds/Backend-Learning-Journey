import json
import uuid
import tasks
import utils
from pathlib import Path




class valueOutOfRangeOption(Exception):
    pass 

class ValueFormatError(ValueError):
    pass


def is_value_option(input):
    """Evaluate if the input is between 1 - 9 [options]"""

    if input not in range(0,10,1):
        raise valueOutOfRangeOption("Your value is {}. Choose a value between 1 - 9".format(input))
    return input 


def option_1 ():


    task ={"id" : uuid.uuid1().hex, "status" : "Pending"} # Gerer la generation de ID
    informations = ["title", "description"]

    print("------------ Add Task ------------")

    for task_info in informations:

        info = input("{} :\t".format(task_info))

        while info.isspace():
                print("{} must not be empty ! Try Again !")
                info = input("{} :\t".format(task_info))

        task[task_info] = info

    
    msg = "Task successfully created." if tasks.add_task(task) else "There's already a task with this id {}".format(task["id"])

    print("\n\t {}".format(msg))


    return msg
        
def option_2():
     """Display all Tasks."""

     print("============== TASKS ==============\n")


     for task in utils.load_file_content(tasks.TASKS_FILE):

          print(""" 
id : {} ,
title : {} , 
Status : {}
________________________________________________________""".format(task["id"], task["title"], task["status"]))


def option_5():
     print("----------- Update Task -----------\n")

     id_task = str(input("Task ID :\t"))

     try:

        position_task = search_task_by_id(id_task, tasks.TASKS_FILE) # return position of task

     except ValueError as e:
        print("\n{}\n".format(e))
        # Revenir au menu ou permettre de faire encore la saisie
        option_5()

     else:
        msg = update(position_task, tasks.TASKS_FILE)
        print(msg)
        
def option_8():
    """Delete Tsks option."""    

    print("---------- Delete Task ----------\n") 

    task_id = str(input("Task ID :\t"))

    try :
        pos_task = search_task_by_id(task_id, tasks.TASKS_FILE)

    except ValueError as e:
        print(e)

    else:
        try:

            reponse = confirm_msg(str(input("\nAre you sure ? (y/n)")))

            if reponse == "y":
                print(remove_task(pos_task, tasks.TASKS_FILE))
            
            else:
                print("Task is not deleted.")
        except ValueFormatError as e:
            print(e)

        
def handle_option(input):
    """Call the function matching the num option."""
    try:
        value = is_value_option(int(input))
    except ValueError:
        print("Invalid Value ! Must Be digit")
    except valueOutOfRangeOption as e:
        print(e)
    else:
        match (value):
            case 1 : option_1()
            case 2 : option_2()
            case 3 : print("This is Option 3")
            case 4 : print("This is option 4")
            case 5 : option_5()
            case 6 : print("This is option 6")
            case 7 : print("This is option 7")
            case 8 : option_8()
            case 9 : print("This is option 9")

def load_file_content(json_file):
        # Open the json file that contains tasks
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            tasks = json.load(file)

    except (FileNotFoundError , json.decoder.JSONDecodeError):
        tasks = []
    return tasks

def search_task_by_id(id, json_file):
     file = load_file_content(json_file)

     current = 0

     while current < len(file) and id != file[current]['id']:
          current+= 1

     if current == len(file):
          raise ValueError("Your Id doesn't exists here ! Try Again !")
     
     return current 

def update(pos_task, json_file):

     file = load_file_content(json_file)

     print("Current title : {} \n".format(file[pos_task]['title']))
     new_title = str(input("New title :\t"))

     while new_title.isspace():
        print("\nTitle must not be empty ! You can copy and paste Current Title if you don't want modify it")
        new_title = str(input("New title :\t"))


     print("\nCurrent description {} :\n".format(file[pos_task]['description']))
     new_description = str(input("New description : \t"))

     while new_description.isspace():
        print("Description must not be empty ! You can copy and paste Current description if you don't want modify it")
        new_description = str(input("New description :\t"))

     file[pos_task]['title'], file[pos_task]['description'] = new_title, new_description

     save(json_file, file)

     return "Task successfully updated."
         
def save(json_file, tasks):
         with open(json_file, 'w', encoding='utf-8' ) as file :
                json.dump(tasks, file , indent= 4 , ensure_ascii= False )

def handle_user_none_value(msg, *inputs):
    """Ask to user to enter a value that is not null."""
    results = []
    for inp in inputs:
        while inp.isspace():
            print("\n{}".format(msg))
            new_input = str(input("New title :\t"))
        results.append(new_input)

    return results # First Approach

def remove_task(task_pos, json_file):
    """Remove Task (use the task_id)"""

    file = load_file_content(json_file)
    file.pop(task_pos)
    save(tasks.TASKS_FILE, file)
    return "Task deleted."

def confirm_msg(reponse):
    """Say Yes (Y) or No (N)"""

    if reponse not in ["y", "n"]:
        raise ValueFormatError("y or n  expected !")
    
    return reponse


