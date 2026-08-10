import json

def is_num_option_valid(input):

    try:
        input = int(input)
    except ValueError as e:
        print(f"\n {e}")

    if input  not in range(0, 7, 1):
        return None
    return input

def load_expenses(storage):
    """Load depense and return a list ."""

    
    try:
        with open(storage, mode='r', encoding="utf-8") as storage_content :
            expenses = json.loads(storage_content)

    except(FileNotFoundError, json.decoder.JSONDecodeError):
        return []

    return expenses

def save_expenses(storage, expenses):

    with open(storage, mode='w', encoding='utf-8') as storage_content:
        json.dumps(expenses, storage_content , indent= 4 , ensure_ascii= False)

def display_category_menu(categories):
    print("CATEGORIES :\n")
    for num_opt, category in enumerate(categories, start=1):
        print(f"{num_opt}. {category}")
    







