class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Account created for {self.owner} with balance {self.balance}")

        #method to deposit money
        def deposit(self, amount):
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")

            #method to withdraw money
            def withdraw(self, amount):
                if amount > self.balance:
                    print(f"{amount} deposited. New balance: {self.balance}")
                else:
                    print("Insufficient funds!")

                    #Destructor
                    def __del__(self):
                        print(f"Account for {self.owner} is now closed.")

                        #creating objects (constructor is called)
                        account1 = BankAccount("Velma", 1000)

                        #using methods
                        account1.deposit(500)
                        account1.withdraw(200)

                        #deleting object (destructor is called)
                        del account1