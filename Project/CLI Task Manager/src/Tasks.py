import json
from pathlib import Path

TASKS_FILES = Path(__file__).parent / "tasks.json"

def add_task (task):
    """Add task."""

    # Open the json file that contains tasks
    try:
        with open(TASKS_FILES, 'r', encoding='utf-8') as file:
            tasks = json.load(file)

    except (FileNotFoundError , json.decoder.JSONDecodeError):
        tasks = []

    # Check if task with the same id already exists

    id_exists = any (elt["Id"] == task["Id"] for elt in tasks  )

    # Add task and Save to JSON file to ensure persistence 
    if not id_exists : 
        tasks.append(task)
        
        with open(TASKS_FILES, 'w', encoding='utf-8' ) as file :
                json.dump(tasks, file , indent= 4 , ensure_ascii= False )
        
 # "Tasks successfully Added"

    return not id_exists # "There's already a task with this id {}".format(task["id"]) # Better Handle