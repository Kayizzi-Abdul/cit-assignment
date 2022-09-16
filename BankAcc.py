
class Bank_Account: 

    def __init__(self): 
        self.balance = 0
        print("Welcome our dear customer") 

    def deposit(self): 
        amount = float(input("Enter Amount to deposit: ")) 
        self.balance += amount 
        print(f"\nAmount deposited: Ugx {amount} and your new balance is: Ugx.{self.balance} ") 

    def withdraw(self): 
        amount = float(input("Enter amount to withdraw")) 

        if self.balance >= amount: 
            self.balance -= amount 
            print(f"\n You have withdrawn: Ugx.{amount} and your new balance is: Ugx.{self.balance} ") 

        else:
            print("\n Insufficient") 

a = Bank_Account()
a.deposit()
a.withdraw() 