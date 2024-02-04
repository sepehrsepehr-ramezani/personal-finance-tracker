from sample_files.database.db_manager import Database

class Calc:
    def __init__(self, db_name):
        self.db = Database(db_name)
    
    def income(self):
        data = self.db.read_data("income")
        sum = 0
        try:
            for i in range(len(data)):
                sum += data[i][2]
        except:
            pass
        return sum
    
    def expense(self):
        data = self.db.read_data("expense")
        sum = 0
        try:
            for i in range(len(data)):
                sum += data[i][2]
        except:
            pass
        return sum
    
    def cash_income(self):
        data = self.db.read_data("cash_income")
        sum = 0
        try:
            for i in range(len(data)):
                sum += data[i][2]
        except:
            pass
        return sum
    
    def cash_expense(self):
        data = self.db.read_data("cash_expense")
        sum = 0
        try:
            for i in range(len(data)):
                sum += data[i][2]
        except:
            pass
        return sum
    
    def cash_withdrawal(self):
        data = self.db.read_data("cash_withdrawal")
        sum = 0
        try:
            for i in range(len(data)):
                sum += data[i][2]
        except:
            pass
        return sum
    
    def acount_balance(self):
        balance = 0 
        ex = self.expense()
        inc = self.income()
        wihtidral = self.cash_withdrawal()
        balance = inc - ex -wihtidral
        return balance
    
    def cash_balance(self):
        balance = 0
        ex = self.cash_expense()
        inc = self.cash_income()
        wihtidral = self.cash_withdrawal()
        balance = inc + wihtidral - ex
        return balance