import uuid
import expenses
from main import main
import utils
from datetime import datetime

CATEGORIES = ("Food", "Transport","Housing","Health","Education","Shopping","Other")

def handle_option(option):

    match option:
        case 1 : option_1()
        case 2 : option_2()
        case 3 : option_3()
        case 4 : option_4()
        case 5 : option_5()
        case 6 : print("Option 6")
    main()

def option_1 ():

     try:
         amount = utils.handle_negative_value(int(input("Amount :\t")))
     except:
         amount = 0

     while not amount :
        try:
            amount = utils.handle_negative_value(int(input("\nIncorrect Value (either negative value or non-digit). Try Again !\nAmount :\t")))
        except:
            amount = 0
         
     # Verifier si le montant est valide (positif et digit)
     id = uuid.uuid4().hex

     utils.display_category_menu(CATEGORIES)
     category = utils.is_num_option_valid(input("Category :\t"), range(1, len(CATEGORIES) + 1))

     while category is None :
        category = utils.is_num_option_valid(input("\nYou have to choose between (1 - 7). Try Again !\nCategory :\t"), range(1, len(CATEGORIES) + 1))

     description = input("Description (optionnal) :\t ")

     date = datetime.now().strftime("%Y/%m/%d at %H:%M:%S")
     
     expenses.add_expenses({
         "id" : id,
         "amount" : amount,
         "category" : CATEGORIES[int(category) - 1],
         "description": description,
         "date": date
     })
     print("\nTask Successfully Added !\n")

def option_2():
    return

def option_3():

     print("===== UPDATE EXPENSE =====\n")

     id = input("Please Enter the ID of expense that you want modify\n ID :\t")

     while expenses.search_expense(id) is None:
         id = input("There's no expense with this ID . Try Again ! \n ID :\t")


     try:
         amount = utils.handle_negative_value(int(input("Amount :\t")))
     except:
         amount = None

     while amount is None :
        try:
            amount = utils.handle_negative_value(int(input("\nIncorrect Value (either negative value or non-digit). Try Again !\nAmount :\t")))
        except:
            amount = None
         
     utils.display_category_menu(CATEGORIES)
     category = utils.is_num_option_valid(input("Category :\t"), range(1, len(CATEGORIES) + 1))

     while category is None :
        category = utils.is_num_option_valid(input("\nYou have to choose between (1 - 7). Try Again !\nCategory :\t"), range(1, len(CATEGORIES) + 1))

     description = input("Description (optionnal) :\t ")

     expenses.update_expenses(expense_id = id, new_exp_info = {"amount": amount, "category": category, "description":description})

     print("\n Expense successfully Updated\n")


def option_4():
     
     print("===== DELETE EXPENSE =====\n")

     id = input("Please Enter the ID of expense that you want modify\n ID :\t")

     while expenses.search_expense(id) is None:
         id = input("There's no expense with this ID . Try Again ! \n ID :\t")

     expenses.delete_expense(id)

     print("\nExpense successfully deleted .\n")

def option_5():

    expense_id = input("Please Enter Expense ID :\t").strip()
    

    while expenses.search_expense(expense_id, utils.load_expenses(expenses.expenses_file)) is None :
        expense_id = input("\nThere's no expense with this Id \n.Please Try Again.\n Enter Expense ID:\t ")

    expenses.display_expense(expense_id)


    

     

     
     