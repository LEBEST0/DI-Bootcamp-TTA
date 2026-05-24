class BankAccount:
    def __init__(self,username,password,balance,authenticated=False):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = authenticated
    
    def deposit(self, numb):
        if not self.authenticated:
            raise Exception(
                "You are not authenticated"
            )
        if 0>=numb:
                raise Exception("The number should be a positive number")
            
        
        self.balance+=numb
    
    def withdraw(self,numb):
        if not self.authenticated:
            raise Exception(
                "You are not authenticated"
            )

        if numb <= 0:
            raise Exception(
                "The number must be positive"
            )

        self.balance -= numb
    
    def authenticate(self,username,password):
        if self.username==username and self.password==password:
          self.authenticated=True
        else:
            self.authenticated=False
        
       
       
    
class MinimumBalanceAccount(BankAccount):
    def __init__(self,username,password, balance,authenticated,minimum_balance=0):
      super().__init__(username,password,balance,authenticated)
      self.minimum_balance=minimum_balance
    
    def withdraw(self,numb):
        if not self.authenticated:
            raise Exception("You are not authenticated")

        if numb <= 0:
            raise Exception("The number must be positive")

        if (self.balance - numb < self.minimum_balance):
            raise Exception(
                "Minimum balance exceeded"
            )

        self.balance -= numb
        

class ATM:
    def __init__(self,account_list,try_limit):
        for account in account_list:

            if not isinstance(account,(BankAccount,MinimumBalanceAccount)) :
                raise Exception ("Compte invalide")   
        if try_limit <= 0:
                print(
                    "Invalid try_limit. "
                    "Setting to 2."
                )

                try_limit = 2
                
        
        self.account_list=account_list
        self.try_limit=try_limit
        self.current_tries = 0
        self.show_main_menu()
    
    def show_main_menu(self):
        print("======== Menu =========")
        while True:
            print(f"""
           Options :
           (C) - Login
           (S) - Exit
            """)
            rep=input("Enter an option: ").lower()
            if rep in ["s","c"]:
                break
            
        if rep =="c":
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            self.log_in(username,password)
        else:
            print("Your are exiting ...")
            print("Godbye Guy")
            exit()

        

        
    def log_in(self,username,password):
        while self.try_limit>self.current_tries:
            for account in self.account_list:
                account.authenticate(username,password)
                if account.authenticated:
                    self.show_account_menu(account)
                    return
            print("Invalid credentials")
            username=input("Enter your username")
            password=input("Enter your password")
            self.current_tries+=1

        print("Maximum tries reached")
        exit()
    
    def show_account_menu(self, account):

        while True:
            print(f"""
                ======== ACCOUNT MENU ========

                Current balance : {account.balance}

                (D) - Deposit
                (W) - Withdraw
                (E) - Exit
                """)
            choice = input("Choose an option: ").lower()

            if choice == "d":
                amount = int(input("Amount to deposit: "))
                try:
                    account.deposit(amount)
                    print("Deposit successful")
                except Exception as e:
                    print(e)
            elif choice == "w":
                amount = int(input("Amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print("Withdrawal successful")
                except Exception as e:
                    print(e)

            elif choice == "e":
                print("Leaving account menu")
                break
            else:

                print("Invalid option")


                

# ===== TEST =====

acc1 = BankAccount(
    "david",
    "1234",
    5000
)

acc2 = MinimumBalanceAccount(
    "ange",
    "0000",
    10000,
    False,
    2000
)
accounts = [acc1, acc2]

atm = ATM(accounts, 3)


                    