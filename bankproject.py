class Customer:
    bankName = "Punjab National Bank"
    def __init__(self,name,bankBalance = 0.0):
        self.name = name
        self.bankBalance = bankBalance
    def deposit(self,amount):
        self.bankBalance += amount
        print("Bank Balance after deposit is {}".format(self.bankBalance))
    def withdrawl(self,amount):
        if amount > self.bankBalance:
            print("Insufficient Balance.....")
            exit()
        self.bankBalance -= amount
        print("Bank Balance after withdrawl is {}".format(self.bankBalance))
print("Welcome to {}".format(Customer.bankName))
cust = Customer('Lalit')
while True:
    print("d for deposit\nw for withdrawl \ne for exit")
    option = input("Enter Choice : ")
    if option == 'w' or option == 'W':
        amt = int(input("Enter Amount you want to withdrawl : "))
        cust.withdrawl(amt)
    elif option == 'd' or option == 'D':
        amt = int(input("Enter Amount you want to Deposit : "))
        cust.deposit(amt)
    elif option == 'e' or option == 'E':
        exit()
    else:
        print("Invalid Option Please Choose Valid Option !!!")