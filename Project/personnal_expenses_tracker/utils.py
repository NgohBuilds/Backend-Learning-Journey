import json

def is_num_option_valid(input, range_ = range(1,7)):

    try:
        input = int(input)
    except ValueError as e:
        print(f"\n {e}")

    if input not in range_:
        return None
    return input

def load_expenses(storage):
    """Load depense and return a list ."""

    
    try:
        with open(storage, mode='r', encoding="utf-8") as storage_content :
            expenses = json.load(storage_content)

    except(FileNotFoundError, json.decoder.JSONDecodeError):
        return []

    return expenses

def save_expenses(storage, expenses):

    with open(storage, mode='w', encoding='utf-8') as storage_content:
        json.dump(expenses, storage_content , indent=4, ensure_ascii= False)

def display_category_menu(categories):
    print("CATEGORIES :\n")
    for num_opt, category in enumerate(categories, start=1):
        print(f"{num_opt}. {category}")
    
def handle_negative_value(amount):
    if amount <= 0:
        return None
    return amount

def search_expense(expense_id , expenses):

    index_expense = 0
    while  expense_id != expenses[index_expense] and index_expense < len(expenses):
        index_expense += 1
    
    if index_expense == len(expenses):
        return None
    
    return index_expense