from tasks import add_task

class valueOutOfRangeOption(Exception):
    pass 



def is_value_option(input):
    """Evaluate if the input is between 1 - 9 [options]"""

    if input not in range(0,10,1):
        raise valueOutOfRangeOption("Your value is {}. Choose a value between 1 - 9".format(input))
    return input 


def option_1 ():


    task ={"Id" : "Blumberg", "status" : "Pending"} # Gerer la generation de ID
    print("------------ Add Task ------------")

    for task_info in ["Title", "Description"]:

        info = input("{} :\t".format(task_info))

        while(info.isspace()):
                print("{} must not be empty ! Try Again !")
                info = input("{} :\t".format(task_info))

        task[task_info] = info

    
    msg = "Task successfully created." if add_task(task) else "There's already a task with this id {}".format(task["Id"])

    print("\n\t {}".format(msg))


    return msg
        

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
            case 2 : print("This is option 2")
            case 3 : print("This is  option 3")
            case 4 : print("This is option 4")
            case 5 : print("This is option 5")
            case 6 : print("This is option 6")
            case 7 : print("This is option 7")
            case 8 : print("This is option 8")
            case 9 : print("This is option 9")

  
        

