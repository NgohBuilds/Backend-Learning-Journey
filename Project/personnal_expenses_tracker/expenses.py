import utils
from pathlib import Path

expenses_file = Path(__file__).parent /"expenses.json"

def add_expenses(exp_dico):

    expenses = utils.load_expenses(expenses_file)
    expenses.append(exp_dico)
    utils.save_expenses(expenses_file, expenses )
    



