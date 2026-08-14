import utils
from pathlib import Path

expenses_file = Path(__file__).parent /"expenses.json"

def add_expenses(exp_dico):

    expenses = utils.load_expenses(expenses_file)
    expenses.append(exp_dico)
    utils.save_expenses(expenses_file, expenses )



def display_expense(expense_id = None):

    expenses = utils.load_expenses(expenses_file)

    if expense_id is None :
        
        print("================= ALL EXPENSES =================")
        for expense in expenses:
            print(
                f"""
                |           | EXPENSE - INFO |                |
                _____________________________________________

                    ID : {expense["id"]}, 
                    AMOUNT : {expense["amount"]}, 
                    CATEGORY : {expense["category"]}
                    DESCRIPTION : {expense["description"]}
                    DATE : {expense["date"]}
                _____________________________________________



                 """)
    index_expense = utils.search_expense(expense_id, expenses)


    print(
            f"""
                |           | EXPENSE - INFO |                |
                _____________________________________________

                    ID : {expenses[index_expense]["id"]}, 
                    AMOUNT : {expenses[index_expense]["amount"]}, 
                    CATEGORY : {expenses[index_expense]["category"]}
                    DESCRIPTION : {expenses[index_expense]["description"]}
                    DATE : {expenses[index_expense]["date"]}
                _____________________________________________



    """)

    
    



