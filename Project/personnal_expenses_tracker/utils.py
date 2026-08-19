import json
from collections import defaultdict


def is_num_option_valid(user_input, range_ = range(1,7)):
    """Verify the validity of user option.
        Args :
            input (string) : user input.
            range_ (list(int)) : list of options.
    
    """
    try:
        user_input_parsed = int(user_input)

    except ValueError as e:
        print(f"\n {e}")
        return None

    if user_input_parsed not in range_:
        return None

    return user_input_parsed


def load_expenses(storage):
    """Load depense and return a list ."""

    try:
        with open(storage, mode='r', encoding="utf-8") as storage_content :
            expenses = json.load(storage_content)

    except(FileNotFoundError, json.decoder.JSONDecodeError):
        return []

    return expenses


def save_expenses(storage, expenses):
    """Save expenses list data into json file doc.
    
       Args :
       storage (json) : json file where expenses list data are stored.
       expenses (list(dict)) : expenses data.
    """

    with open(storage, mode='w', encoding='utf-8') as storage_content:
        json.dump(expenses, storage_content , indent=4, ensure_ascii= False)
        


def display_category_menu(categories):

    print("CATEGORIES :\n")
    for num_opt, category in enumerate(categories, start=1):
        print(f"{num_opt}. {category}")


    
def handle_negative_value(amount):

    try:
        amount_parsed = int(amount)
  
    except ValueError as e:
        print(f"\nSomething goes wrong ! (negative Value or {e} )")
        return None

    if amount_parsed > 0:
        return amount_parsed

    print("\nYour amount is negative.\tTry Again.\n")
    return None


 
def sum_expenses(expenses):
    
    return sum( expense["amount"]  for expense in expenses )


def sum_expenses_by_category(expenses):

    summary = defaultdict(int)

    for exp in expenses:

        summary[exp["category"]] += exp["amount"]

    return summary
        





