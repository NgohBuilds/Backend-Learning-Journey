import utils
from pathlib import Path

expenses_file = Path(__file__).parent /"expenses.json"
EXPENSES = utils.load_expenses(expenses_file)

def add_expense(exp_dico):

    EXPENSES.append(exp_dico)
    utils.save_expenses(expenses_file, EXPENSES )

def find_expense_index(expense_id):

    index_expense = 0
    expense_id= expense_id.strip()

    if not EXPENSES :
        return None

    while  index_expense < len(EXPENSES) - 1  and expense_id != EXPENSES[index_expense]["id"] :
        index_expense += 1
    
    if EXPENSES[index_expense]["id"] != expense_id  :
        return None
    
    return index_expense


def display_expense(expense_id = None , expense_category = None):

    if expense_id is None and expense_category is None :

        
        print("\n================= ALL EXPENSES =================\n")
        for expense in EXPENSES:
            print(
                f"""

|            EXPENSE - INFO                 |
_____________________________________________

ID : {expense["id"]}
AMOUNT : {expense["amount"]}
CATEGORY : {expense["category"]}
DESCRIPTION : {expense["description"]}
DATE : {expense["date"]}
_____________________________________________




                 """)
            
    elif expense_category is not None:
        expenses_filtered_by_category = [x for x in EXPENSES if x["category"] == expense_category]

        if len(expenses_filtered_by_category) == 0:
                print(f"\nTHERE'S NO EXPENSES FROM THIS CATEGORY --> {expense_category.upper()}\n")
        else:

            print(f"\n================= ALL EXPENSES FROM {expense_category.upper()} =================\n")


            for expense in expenses_filtered_by_category:
                print(f"""

|            EXPENSE - INFO                 |
_____________________________________________

ID : {expense["id"]}
AMOUNT : {expense["amount"]}
CATEGORY : {expense["category"]}
DESCRIPTION : {expense["description"]}
DATE : {expense["date"]}
_____________________________________________


                 """)   
            
    if expense_id is not None:  
            
        index_expense = find_expense_index(expense_id)


        print(
            f"""
|            EXPENSE - INFO                 |
_____________________________________________

ID : {EXPENSES[index_expense]["id"]}, 
AMOUNT : {EXPENSES[index_expense]["amount"]}, 
CATEGORY : {EXPENSES[index_expense]["category"]}
DESCRIPTION : {EXPENSES[index_expense]["description"]}
DATE : {EXPENSES[index_expense]["date"]}
_____________________________________________

    """)
        

def display_total_expense():

    total = utils.sum_expenses(EXPENSES)
    print(f"\nTOTAL : {total}")


def display_total_expense_per_category():

    expenses_summary = utils.sum_expenses_by_category(EXPENSES)

    for category , total in expenses_summary.items():

        print(f"\n{category} : {total}\n")



def update_expense(expense_id, new_exp_info):

    expense_index = find_expense_index(expense_id)

    for info, value in new_exp_info.items():
        EXPENSES[expense_index][info] = value

    utils.save_expenses(expenses_file, EXPENSES)


def delete_expense(expense_id):


    expense_index = find_expense_index(expense_id)

    EXPENSES.pop(expense_index)

    utils.save_expenses(expenses_file, EXPENSES)






    



