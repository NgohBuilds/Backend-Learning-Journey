from pathlib import Path
import utils

TASKS_FILE = Path(__file__).parent / "tasks.json"

def add_task(task):
    """Add task."""

    
    tasks = utils.load_file_content(TASKS_FILE)

    # Check if task with the same id already exists

    id_exists = any (elt["id"] == task["id"] for elt in tasks  )

    # Add task and Save to JSON file to ensure persistence 
    if not id_exists : 
        tasks.append(task)
        utils.save(TASKS_FILE, tasks)
        

    return not id_exists # "There's already a task with this id {}".format(task["id"]) # Better Handle