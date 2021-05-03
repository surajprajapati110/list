class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print(" Welcome to the Deposit") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
        print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
  
# Driver code 
   
# creating an object of class 
s = Bank_Account() 
   
# Calling functions with that class object 
s.deposit() 
 
s.display() 
