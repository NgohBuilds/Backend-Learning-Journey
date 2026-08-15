import utils
from pathlib import Path

expenses_file = Path(__file__).parent /"expenses.json"

def add_expenses(exp_dico):

    expenses = utils.load_expenses(expenses_file)
    expenses.append(exp_dico)
    utils.save_expenses(expenses_file, expenses )

def search_expense(expense_id , expenses = utils.load_expenses(expenses_file)):

    index_expense = 0

    while  expense_id != expenses[index_expense]["id"] and index_expense < len(expenses) - 1 :
        index_expense += 1
    
    if expenses[index_expense]["id"] != expense_id  :
        return None
    
    return index_expense


def display_expense(expense_id = None , expense_category = None):

    expenses = utils.load_expenses(expenses_file)

    if expense_id is None and expense_category is None :

        
        print("================= ALL EXPENSES =================\n")
        for expense in expenses:
            print(
                f"""

                |            EXPENSE - INFO                 |
                _____________________________________________

                    ID : {expense["id"]}, 
                    AMOUNT : {expense["amount"]}, 
                    CATEGORY : {expense["category"]}
                    DESCRIPTION : {expense["description"]}
                    DATE : {expense["date"]}
                _____________________________________________



                 """)
            
    elif expense_category:

        print(f"================= ALL EXPENSES FROM {expense_category.upper()} =================\n")

        expenses_filtered_by_category = [x for x in expenses if x["category"] == expense_category]

        for expense in expenses_filtered_by_category:
            print(
                f"""

                |            EXPENSE - INFO                 |
                _____________________________________________

                    ID : {expense["id"]}, 
                    AMOUNT : {expense["amount"]}, 
                    CATEGORY : {expense["category"]}
                    DESCRIPTION : {expense["description"]}
                    DATE : {expense["date"]}
                _____________________________________________



                 """)     
            
    index_expense = search_expense(expense_id, expenses)


    print(
            f"""

                |            EXPENSE - INFO                 |
                _____________________________________________

                    ID : {expenses[index_expense]["id"]}, 
                    AMOUNT : {expenses[index_expense]["amount"]}, 
                    CATEGORY : {expenses[index_expense]["category"]}
                    DESCRIPTION : {expenses[index_expense]["description"]}
                    DATE : {expenses[index_expense]["date"]}
                _____________________________________________



    """)


def update_expenses(expense_id, new_exp_info):

    expenses = utils.load_expenses(expenses_file)

    expense_index = search_expense(expense_id, expenses)

    for info, value in new_exp_info.items():
        expenses[expense_index][info] = value

    utils.save_expenses(expenses_file, expenses)


def delete_expense(expense_id):

    expenses = utils.load_expenses(expenses_file)

    expense_index = search_expense(expense_id, expenses)

    expenses.pop(expense_index)

    utils.save_expenses(expenses_file, expenses)






    



