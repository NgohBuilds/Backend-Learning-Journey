import utils
import uuid
import tasks

def handle_option(user_input):
    """Call the function matching the num option."""

    
    value = utils.is_value_option(user_input)

    while value is None : 
        print("Your input is not Valid . Please Try Again ! (1 - 9 expected)\n")
        user_input = input("Choose an option :\t")
        value = utils.is_value_option(user_input)

    match (value):
            case 1 : option_1()
            case 2 : option_2()
            case 3 : option_3()
            case 4 : option_4()
            case 5 : option_5()
            case 6 : option_6()
            case 7 : option_7()
            case 8 : option_8()
            case 9 : print("This is option 9")

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
     tasks.display_task()

def option_3():
    """Display Completed tasks."""

    print("============== COMPLETED TASKS ==============\n")
    tasks.display_task("Completed")

def option_4():
    """Display Pending tasks."""
    print("============== PENDING TASKS ==============\n")

    tasks.display_task("Pending")


def option_6():

    print("------- Complete Task -------\n")
    print(tasks.mark_task("Completed"))

def option_7():
    print("------- Pending Task -------\n")
    print(tasks.mark_task("Pending"))

def option_5():
    
    print("----------- Update Task -----------\n")

    id_task = str(input("Task ID :\t"))
    position_task = utils.search_task_by_id(id_task, utils.TASKS_FILE) # return position of 

    while position_task is None :

        print("ID not found !\n")
        id_task = str(input("Task ID :\t"))
        position_task = utils.search_task_by_id(id_task, utils.TASKS_FILE)

    msg = tasks.update(position_task, utils.TASKS_FILE)
    print(msg)
        
def option_8():
    """Delete Tasks option."""    

    print("---------- Delete Task ----------\n") 

    task_id = str(input("Task ID :\t"))

    pos_task = utils.search_task_by_id(task_id, utils.TASKS_FILE)

    while pos_task is None :
        print("Id not Found ! Please , try again .\n")
        task_id = str(input("Task ID :\t"))
        pos_task = utils.search_task_by_id(task_id, utils.TASKS_FILE)

    

    reponse = utils.confirm_msg(str(input("\nAre you sure ? (y/n)\t")))

    while reponse is None :
        print("y or n expected !")
        reponse = utils.confirm_msg(str(input("\nAre you sure ? (y/n)\t")))

    if reponse.lower() == "y":
        print(tasks.remove_task(pos_task, utils.TASKS_FILE))
            
    else:
        print("\nDeleting task canceled")

