#Simple functioning of a bank model with python

class Account:
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    #Accepts deposits:    
    def deposit(self):
        dep_amt = int(input(print('Please enter the deposit amount: ')))
        self.balance += dep_amt
        print('Deposit Sucessfull!')

    #Check's if the funds are available to withdraw and proceed with withdrawing the amount    
    def withdraw(self):
        wd_amt = int(input(print('Please enter the withdraw amount: ')))
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdraw sucessfull!')
        else:
            print('You have insufficient funds :(')

#Assigning the attribute and invoking the function from the methords   
bank = Account('Gokul', 0)

#Checks for the name of the account
bank.owner

#checks for the balance on the account
bank.balance

#Accepts the deposits from the customer as a input
bank.deposit()

#Withdraws the funds from the account
bank.withdraw()