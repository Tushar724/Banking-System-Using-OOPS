'''
#What this Mini Project Constitutes :    

Banking System OOPS

Parent Class: User
~ Holds details about an user
~ Has a function to show user details

Child Class: Bank
~ Stores details about the account balance
~ Stores details about the account
~ Allow for deposits withdraw_ver_balance'''

#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        
#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        #We use a super method to call the intialise method of the Parent class
        super().__init__(name,age,gender)
        self.balance = 0
        # We can either define balance in the __init__ method and use self.balance or just self.balance = 0
        
    def deposits(self,amount):
        self.amount = amount
        self.balance = self.balance+self.amount
        print("Account Balance Updates: $", self.balance)
    
    def withdraw(self,amount):
        #if we don't  define a self we get a Type Error
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficent Funds | Balance Available: $",self.balance)
        else: 
            self.balance  = self.balance-self.amount
            #Updating the self balance with the withdraw amount
            print("Account hs been updated: $",self.balance)  
        
    def view_balance(self):
        self.show_details()
        #We can directly call the method from the User as we inherited the class User defining the class User
        print("Account Balance: $",self.balance)


m = Bank("Tushar",24,"Male")
#As the user needs 3 parameters , as init is like whenever we call the funtion , it will need these parameters in the class , not specifed in any method
m.deposits(2000)
m.withdraw(3000)
m.withdraw(500)
m.view_balance()