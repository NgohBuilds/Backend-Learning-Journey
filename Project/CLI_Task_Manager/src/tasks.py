from pathlib import Path
import utils
import menu




def add_task(task):
    """Add task."""
    tasks = utils.load_file_content(utils.TASKS_FILE)
    id_exists = any (elt["id"] == task["id"] for elt in tasks  )

    # Add task and Save to JSON file to ensure persistence 
    if not id_exists : 
        tasks.append(task)
        utils.save(utils.TASKS_FILE, tasks)
        
    return not id_exists # "There's already a task with this id {}".format(task["id"]) # Better Handle

def mark_task(status):

    tasks = utils.load_file_content(utils.TASKS_FILE)
    id = str(input('Task ID :\t'))
    pos_task = utils.search_task_by_id(id, utils.TASKS_FILE)

    while pos_task is None:
        print("Id doesn't exists. Please Try Again ! ")
        id = str(input('\nTask ID :\t'))
        pos_task = utils.search_task_by_id(id, utils.TASKS_FILE)

    tasks[pos_task]["status"] = status
    utils.save(utils.TASKS_FILE, tasks)

    return "Task marked as {}.".format(status)

def remove_task(task_pos, json_file):
    """Remove Task (use the task_id)"""

    file = utils.load_file_content(json_file)
    file.pop(task_pos)
    utils.save(utils.TASKS_FILE, file)

    return "Task deleted."

def update(pos_task, json_file):
     """Update task with a specific id"""
     file = utils.load_file_content(json_file)

    # new_task_infos = (handle_user_none_value(input_name, file[pos_task][input_name]) for input_name in ['title', 'description'])

     file[pos_task]['title'], file[pos_task]['description'] = (utils.handle_user_none_value(input_name, file[pos_task][input_name]) for input_name in ['title', 'description'])

     utils.save(json_file, file)

     return "Task successfully updated."

def display_task(status = None):
    """Display tasks according to Status."""

    if status == None:
        for task in utils.load_file_content(utils.TASKS_FILE):
        
         print(""" 
id : {} ,
title : {} , 
Status : {}
________________________________________________________""".format(task["id"], task["title"], task["status"]))


    tasks_filtered = utils.filter_task(status)
    for task in tasks_filtered:
        
         print(""" 
id : {} ,
title : {} , 
Status : {}
________________________________________________________""".format(task["id"], task["title"], task["status"]))
    return 