from finantial_manager.finantial_cal import Calc
from database.db_manager import Database
from tabulate import tabulate

def reaction(user_name, user_wil):
    if user_wil == 'short report':
        calc = Calc(user_name)
        acount_balance = calc.acount_balance()
        expense = calc.expense()
        cash_balance = calc.cash_balance()
        income = calc.income()
        cash_income = calc.cash_income()
        cash_withdrawal = calc.cash_withdrawal()
        cash_expense =calc.cash_expense()
        
        data = [
            ["Account Balance", acount_balance],
            ["Expense", expense],
            ["Cash Balance", cash_balance],
            ["Income", income],
            ["Cash Income", cash_income],
            ["Cash Withdrawal", cash_withdrawal],
            ["Cash Expense", cash_expense]
        ]

        print(tabulate(data, headers=["Item", "Value"]))

    if user_wil == 'expeses':
        db = Database(user_name)
        data = db.read_data('expeses')
        print(tabulate(data, headers=["Date", "Text", "Amount"]))

    if user_wil == 'income':
        db = Database(user_name)
        data = db.read_data('income')
        print(tabulate(data, headers=["Date", "Text", "Amount"]))

    if user_wil == 'cash income':
        db = Database(user_name)
        data = db.read_data('cash_income')
        print(tabulate(data, headers=["Date", "Text", "Amount"]))

    if user_wil == 'cash expense':
        db = Database(user_name)
        data = db.read_data('cash_expense')
        print(tabulate(data, headers=["Date", "Text", "Amount"]))

    if user_wil == 'cash withdrawal':
        db = Database(user_name)
        data = db.read_data('income')
        print(tabulate(data, headers=["Date", "Text", "Amount"]))