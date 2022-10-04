"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, rate, totalTime, totalpay = 0, commissionContracts = 0, commissionPay = 0):
        self.name = name
        self.rate = rate      #hourly or monthly
        self.totalTime = totalTime   #total time spent working, so monthly means totalTime = 1
        self.salary = salary        
        self.commissionContracts = commissionContracts
        self.commissionPay = commissionPay
        self.totalpay = totalpay
    def get_pay(self):
        self.totalpay = (self.salary * self.totalTime) + (self.commissionContracts * self.commissionPay)
        return self.totalpay

    def __str__(self):
        if self.rate == 'monthly':
            return f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}'
        if self.rate == 'hourly' and self.commissionPay != None:
            return f'{self.name} works on a contract of {self.totalTime} hours at {self.salary}/hour and receives a commission for {self.commissionContracts} contracts(s) at {self.comissionPay}/contract. Their total pay is {self.get_pay()} '



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, "monthly", 1)
print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 'hourly', 100, None)
print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 'monthly', 1, None, 4, 200 )

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 'hourly', 150, None, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 'monthly', '1', None, None, 1500 )

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 'hourly', 120, None, None, 600)
