import utils
from pathlib import Path

expenses_file = Path(__file__).parent /"expenses.json"
EXPENSES = utils.load_expenses(expenses_file)

def add_expenses(exp_dico):

    EXPENSES.append(exp_dico)
    utils.save_expenses(expenses_file, EXPENSES )

def search_expense(expense_id , expenses = utils.load_expenses(expenses_file)):

    index_expense = 0
    expense_id= expense_id.strip()

    while  expense_id != EXPENSES[index_expense]["id"] and index_expense < len(expenses) - 1 :
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

                    ID : {expense["id"]}, 
                    AMOUNT : {expense["amount"]}, 
                    CATEGORY : {expense["category"]}
                    DESCRIPTION : {expense["description"]}
                    DATE : {expense["date"]}
                _____________________________________________



                 """)
            
    elif expense_category:

        print(f"\n================= ALL EXPENSES FROM {expense_category.upper()} =================\n")

        expenses_filtered_by_category = [x for x in EXPENSES if x["category"] == expense_category]

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
            
    if expense_id :  
            
        index_expense = search_expense(expense_id, EXPENSES)


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





def update_expenses(expense_id, new_exp_info):


    expense_index = search_expense(expense_id, EXPENSES)

    for info, value in new_exp_info.items():
        EXPENSES[expense_index][info] = value

    utils.save_expenses(expenses_file, EXPENSES)


def delete_expense(expense_id):


    expense_index = search_expense(expense_id, EXPENSES)

    EXPENSES.pop(expense_index)

    utils.save_expenses(expenses_file, EXPENSES)






    



