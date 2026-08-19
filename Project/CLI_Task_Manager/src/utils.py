import json
from pathlib import Path



TASKS_FILE = Path(__file__).parent / "tasks.json"



class ValueFormatError(ValueError):
    pass


def is_value_option(user_input):
    """Evaluate if the input is between 1 - 9 [options]"""

    try: 
        input = int(user_input)
    except ValueError :
        return None

    else :
        if input  in range(1,10,1):
            return input
    return None



def filter_task(status):

    return filter(lambda x : x["status"] == status, load_file_content(TASKS_FILE))

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

     current_index = 0

     while current_index < len(file) and id != file[current_index]['id']:
          current_index += 1

     if current_index == len(file):
          return None
     
     return current_index 


         
def save(json_file, tasks):
         with open(json_file, 'w', encoding='utf-8' ) as file :
                json.dump(tasks, file , indent= 4 , ensure_ascii= False )

def handle_user_none_value(input_name, info):
    """Ask to user to enter a value that is not null."""

    print("Current {} : {} \n".format(input_name, info))
    new_input = str(input("New {} :\t".format(input_name)))
    
    while new_input.isspace():
        print("\nTitle must not be empty ! You can copy and paste Current {} if you don't want modify it".format(input_name))
        new_input = str(input("New {} :\t".format(input_name)))
    return new_input



def confirm_msg(reponse):
    """Say Yes (Y) or No (N)"""

    if reponse not in ["y", "n"]:
        return None
    
    return reponse


