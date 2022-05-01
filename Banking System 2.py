def Restart():
    #
    restart = input("If you want to Deposit or With_draw amount again. Please type (y/yes/Y/Yes/YES)")
    if restart == "yes" or restart == "y" or restart == 'Yes' or restart == 'YES' or restart == 'Y':

        Object = Bank("shubham", 22, "male")

        # Calling the deposit method using object.
        Object.deposit()

        # Calling the with_draw method using object.
        Object.withdraw()

        # Calling the view_balance method using object.
        Object.view_balance()

        # Calling the function again.
        Restart()

    if restart == "n" or restart == "no" or restart == "No" or restart == "NO":
        print("Thankyou. Visit Again!!!")


# Creating User Class
class User:
    # User class constructor with 4 formal arguments including self.
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # User Class Instance Method
    def show_details(self):
        print("Personal Details\n")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Creating Bank Class
class Bank(User):                            # Inheriting User class in Bank class.

    # Bank class constructor, Overriding the User class constructor.
    def __init__(self, name, age, gender):
        # Using super() method to access User class constructor.
        super().__init__(name, age, gender)
        self.amount = 0
        self.balance = 0

    # Bank class Instance Method named deposit with no formal arguments.
    def deposit(self):
        print(f"Initial balance: {self.balance}")

        # Taking the deposit amount input from the user.
        self.amount = int(input("Enter the amount you want to deposit: "))

        # Using conditional statement.
        if self.amount == 0:
            print("Balance: Rs", self.balance)
        else:
            self.balance += self.amount
            print("Updated Balance: ", self.balance)

    # Instance method to withdraw the amount from available balance.
    def withdraw(self):

        # Taking the with_draw amount input from the user.
        self.amount = int(input("Enter the amount you want to withdraw: "))
        if self.amount > self.balance:
            print("Sorry, Insufficient Balance || Available balance is Rs.", self.balance)
        else:
            self.balance = self.balance-self.amount
            print("Withdraw Successful\nRemaining Amount is Rs.", self.balance)

    # Instance method to check balance and user details.
    def view_balance(self):
        print("Name:", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("Available balance is Rs.", self.balance)


# Creating object of Bank class
obj = Bank("shubham", 22, "male")

# Calling the deposit method using object.
obj.deposit()

# Calling the with_draw method using object.
obj.withdraw()

# Calling the view_balance method using object.
obj.view_balance()

# Calling the Restart function to check whether the user want to check data again.
Restart()
