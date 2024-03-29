from sample_files.finantial_manager.finantial_cal import Calc
from sample_files.database.db_manager import Database
from colorama import Fore, Style
from jdatetime import datetime
from tabulate import tabulate


def reaction(user_name, user_will):

    db = Database(user_name)

    if user_will == 'short report':

        calc = Calc(user_name)
        income = calc.income()
        expense = calc.expense()
        cash_income = calc.cash_income()
        cash_expense =calc.cash_expense()      
        cash_balance = calc.cash_balance()
        acount_balance = calc.acount_balance()
        cash_withdrawal = calc.cash_withdrawal()
    
        data = [
            ["Account Balance", acount_balance],
            ["Cash Balance", cash_balance],
            ["Cash Withdrawal", cash_withdrawal],
            ["Expense", expense],
            ["Cash Expense", cash_expense],
            ["Income", income],
            ["Cash Income", cash_income] 

        ]
        print("\n")
        print(tabulate(data, headers=["Item", "Value"]))
        print("\n")

    if user_will == 'expense':
        data = db.read_data("expense")
        print("\n")
        print(tabulate(data, headers=["Date", "Text", "Amount"], tablefmt= 'fancy_grid'))
        print("\n")

    if user_will == 'income':
        data = db.read_data('income')
        print("\n")
        print(tabulate(data, headers=["Date", "Text", "Amount"], tablefmt= 'fancy_grid'))
        print("\n")

    if user_will == 'cash income':
        data = db.read_data('cash_income')
        print("\n")
        print(tabulate(data, headers=["Date", "Text", "Amount"], tablefmt= 'fancy_grid'))
        print("\n")

    if user_will == 'cash expense':
        data = db.read_data('cash_expense')
        print("\n")
        print(tabulate(data, headers=["Date", "Text", "Amount"], tablefmt= 'fancy_grid'))
        print("\n")

    if user_will == 'cash withdrawal':
        data = db.read_data('cash_withdrawal')
        print("\n")
        print(tabulate(data, headers=["Date", "Text", "Amount"], tablefmt= 'fancy_grid'))
        print("\n")

    if 'add' in user_will:
        user_will = user_will.split('add')[1]
        now = datetime.now()
        formatted_now = now.strftime("%Y/%m/%d - %H:%M")
        text = input('text: ')
        amount = input('amount: ')
        db.store_data(user_will ,formatted_now, text, amount)

    if user_will == 'all':
        income = [list(t) for t in db.read_data("income")]
        expense = [list(t) for t in db.read_data("expense")]
        cash_income = [list(t) for t in db.read_data("cash_income")]
        cash_expense = [list(t) for t in db.read_data("cash_expense")]
        cash_withdrawal = [list(t) for t in db.read_data("cash_withdrawal")]

        for i in expense:
            i[2] = f"{Fore.RED}{i[2]}{Style.RESET_ALL}"
        for i in cash_expense:
            i[2] = f"{Fore.RED}{i[2]}{Style.RESET_ALL}"
        for i in cash_income:
            i[2] = f"{Fore.GREEN}{i[2]}{Style.RESET_ALL}"
        for i in income:
            i[2] = f"{Fore.GREEN}{i[2]}{Style.RESET_ALL}"

        #print(expense, income, cash_income, cash_expense, cash_withdrawal)
        l = [expense, income, cash_income, cash_expense, cash_withdrawal]

        data = []

        for i in l:
            for x in range(len(i)):
                data.append(i[x])
        sorted_data = sorted(data, key=lambda x: datetime.strptime(x[0], "%Y/%m/%d - %H:%M"))
            
        print(tabulate(sorted_data, headers=["Date", "Text", "Amount"], tablefmt='fancy_grid'))