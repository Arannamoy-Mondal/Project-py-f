import random
class Account:
    def __init__(self,name,email,address,acType):
        self.__name=name
        self.__email=email
        self.__address=address
        self.__acType=acType
        self.__acNumber=random.randint(400,999)
        self.__balance=0
        self.__transactionsHistory=[]
        self.__loanTime=0
        self.__loanAmount=0
        print(f"Congratulations! Account created successfully.\nMr. {self.__name} account no is {self.__acNumber}. Please remember it or note down it.")
    
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def address(self):
        return self.__address
    
    @property
    def acType(self):
        return self.__acType
    
    @property
    def acNumber(self):
        return self.__acNumber
    

    def deposit(self,balance,admin,ref): # deposit
        if self.__loanAmount>0:
            if self.__loanAmount>balance:
                self.__loanAmount-=balance
                admin.paidLoan(balance)
                self.__transactionsHistory.append(f"Loan payment ==> {balance}")
                print(f"You loan amount paid {balance}. Due {self.__loanAmount}")
            else:
                balance-=self.__loanAmount
                self.__transactionsHistory.append(f"Loan payment ==> {self.__loanAmount}")
                print(f"You loan amount paid {self.__loanAmount}. Due 0")
                admin.paidLoan(self.__loanAmount)
                self.__loanAmount=0
                self.__balance+=balance
                admin.deposit(balance)
                self.__transactionsHistory.append(f"Deposit by {ref} <== {balance}")
                print(f"Deposit {balance} successfully.")
        else:
         self.__balance+=balance
         admin.deposit(balance)
         self.__transactionsHistory.append(f"Deposit by {ref} <== {balance}")
         print(f"Deposit {balance} successfully.")



    def withdrawl(self,balance,admin): # withdraw
        if self.__balance<balance or self.__balance<=self.totalLoanAmount:
            print(f"Withdrawal amount exceeded")
        else:
            self.__balance-=balance
            admin.withdrawal(balance)
            self.__transactionsHistory.append(f"Withdraw ==> {balance}")



    def takeLoan(self,amount): # take loan
        if self.__loanTime<2 and self.__balance>amount:
            self.__loanTime+=1
            self.__loanAmount+=amount
        elif self.__balance<=amount:
            print("Your are not eligible for loan.")
        else:
            print(f"You get already two loans")
    
    @property
    def availableBalance(self):
        return self.__balance
        # print(f"Available balance: {self.__balance}")
    
    @property
    def transactions(self):
        for i in self.__transactionsHistory:
            print(f"{i}")

    @property
    def totalLoanAmount(self):
        return self.__loanAmount
    

class Bank:
    def __init__(self):
        self.__AccountList={}
        self.__totalBalance=0
        self.__totalLoanAmount=0
        self.__loanFeature=True
        self.__bankRuptcy=False
    
    @property
    def firstBankRuptcy(self):
        if self.__totalBalance<self.__totalLoanAmount:
                # self.__bankRuptcy=True
                pass

    # create a user account
    def createAcc(self,name,email,address,acType):
        account=Account(name,email,address,acType)
        self.__AccountList[account.acNumber]=account

    # delete user account
    def deleteAc(self,accNo):
        if accNo in self.__AccountList:
           del self.__AccountList[accNo]
           print(f"{accNo} delete successfully.")
        else:
            print(f"Account {accNo} not found.")

    # update total bank balance
    def deposit(self,x):
        self.__totalBalance+=x

    # update total bank balance
    def withdrawal(self,x):
        self.__totalBalance-=x

    # checking loan status on off
    def isLoanPossible(self):
        return self.__loanFeature
    
    # total loan amount
    def takeLoan(self,x):
        self.__totalLoanAmount+=x

    # update total loan amount when any user deposit money
    def paidLoan(self,x):
        self.__totalLoanAmount-=x

    # update loan status
    def loanStatus(self,x):
        self.__loanFeature=x  

    # return user object
    def returnUser(self,accNo):
        if accNo in self.__AccountList:
            return self.__AccountList[accNo]
        

    # check account no is exist or not
    def checkAcNo(self,x):
        if x in self.__AccountList:
            return True
        else :
            return False
        
    # check account information for log in
    def checkAcInfo(self,acNo,name,email):
        if acNo in self.__AccountList:
            if self.__AccountList[acNo].name==name and self.__AccountList[acNo].email==email:
                print(f"Welcome, Mr. {name} !")
                return True
            else:
                print("You have entered wrong credential.")
                return False
            
    # change bankruptcy status
    def changeBankRuptcy(self,x):
        self.__bankRuptcy=x

    @property
    def checkBankRuptcy(self):
        if self.__bankRuptcy==True:
            return True
        else:
            return False

    @property
    def bankruptcyStatus(self):
        if self.checkBankRuptcy:
            print("Bankruptcy")
        else:
            print("Not Bankruptcy")   

    @property 
    def checkLoanStatus(self):
        if self.__loanFeature==True:
           print(f"Loan Status of Bank: ON")
        else:
            print(f"Loan Status of Bank: OFF")


    @property
    def availableBalance(self):
        return self.__totalBalance
        # print(f"Total Balance: {self.__totalBalance}")


    @property
    def totalLoanAmount(self):
        print(f"Total loan amount: {self.__totalLoanAmount}")


    @property
    def accList(self):
        for key,value in self.__AccountList.items():
            print(f"{value.name} {value.email} {value.address} {value.acType} {key}")


admin=Bank()

def adminFeatures(option): # admin features
    if option==1:
        name=input("Enter account owner name:")
        email=input("Enter account owner email:")
        address=input("Enter account owner address:")
        accType=input("Enter account type (Savings/Current):")


        if accType.lower()=="savings" or accType.lower()=="current":
            if accType.lower()=="savings":
                accType="Savings"
            else:
                accType="Current"
            admin.createAcc(name,email,address,accType)
        else:
            accType=input("Please correct account type. If you want to cancel the process enter E. OtherWise accountype")
            if accType.lower()=="savings" or accType.lower()=="current":
                admin.createAcc(name,email,address,accType)
            else:
                return
            
    elif option==2: # delete account 
        admin.accList
        x=int(input("Enter account no:"))
        admin.deleteAc(x)

    elif option==3: # account list 
        admin.accList

    elif option==4:
        print(f"Total avialablebalance: {admin.availableBalance}")

    elif option==5: # total loan amount
        admin.totalLoanAmount
        # print(f"Total loan amount: {admin.totalLoanAmount}")

    elif option==6: # loan status on off
        admin.checkLoanStatus
        x=input("Loan feature (ON/OFF):")
        if x.lower()=="on":
            admin.loanStatus("True")
            admin.checkLoanStatus
        elif x.lower()=="off":
            admin.loanStatus("False")
            admin.checkLoanStatus
        else:
            print("Invalid option for loan status")
 
    elif option==7: # for bankruptcy status on off
        admin.bankruptcyStatus
        x=input("Is the bank bankrupt(Yes/No)?")
        if x.lower()=="yes":
            admin.changeBankRuptcy(True)
        elif x.lower()=="no":
            admin.changeBankRuptcy(False)
        else:
            print("Invalid input")
        admin.bankruptcyStatus


def userFeatures(accNo,option): # user features
    admin.firstBankRuptcy
    user=admin.returnUser(accNo)


    if option==2:  # deposit
        amount=int(input("Enter deposit amount:"))
        user.deposit(amount,admin,"self")
        # admin.deposit(amount)


    elif option==3: # Withdrawal 
        if admin.checkBankRuptcy==True:
            print("This bank is bankrupt")
            return
        amount=int(input("Enter withdraw amount:"))
        if user.availableBalance<amount:
            print("Withdrawal amount exceeded")
        elif admin.availableBalance<user.availableBalance or admin.availableBalance<amount:
            print("This bank is bankrupt")
        else:
            user.withdrawl(amount,admin)
            # admin.withdraw(amount)
            print(f"Withdrawal Successful.")


    elif option==4: # Available balance
        print(f"Available balance: {user.availableBalance}")


    elif option==5: # Transactions
        user.transactions


    elif option==6: # Take Loan
        if admin.checkBankRuptcy:
            print("This bank is bankrupt")
            return
        else:
            amount=int(input("Enter loan amount:"))
            if admin.availableBalance>amount:
               if admin.isLoanPossible()==True:
                   user.takeLoan(amount)
                   admin.takeLoan(amount)
               else:
                   print("Loan not possible.")
            else:
                print("This bank is bankrupt.")


    elif option==7:  # Transfer money
        if admin.checkBankRuptcy==True:
            print("This bank is bankrupt")
            return
        accNo1=int(input("Enter transfer money account no:"))
        if admin.checkAcNo(accNo1)==True and accNo!=accNo1:
            print(f"A/C: {accNo1} Found.")
            user2=admin.returnUser(accNo1)
            amount=int(input("Enter transfer amount:"))
            if amount>user.availableBalance:
                print("You have not enough balance.")
            else:
                user.withdrawl(amount,admin)
                user2.deposit(amount,admin,"self")
                print("Transfer successful.")
        else:
            print("Account does not exist")

    
    elif option==8: # Total loan amount
        print(f"Total Loan {user.totalLoanAmount}")
        

while True:
    userType=input("U for User, A for Admin, D for Deposit, E for exit:")
    if userType.lower()=='a':
        while True:
            print("0 for exit.\n1 for creat an account.\n2 for delete user account.\n3 see all user accounts list.\n4 "+
              "total available balance of the bank.\n5 total loan amount.\n6 for on or off the loan feature of the bank.\n"
              +"7 for the bankruptcy")
            option=input("Option:")
            if option=="0":
                break
            elif option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option=="7":
               adminFeatures(int(option))
            else:
                print("Invalid input")
    elif userType.lower()=='u':
        while True:
              print("Welcome to our bank.\n1 for create account.\n2 for log in account.\n0 for exit.")
              option=input("Option:")
              if option=="1":
                  name=input("Enter your name:")
                  email=input("Enter your email:")
                  address=input("Enter your address:")
                  acType=input("Enter account type (Savings/Current):")
                  if acType.lower()=="savings" or acType.lower()=="current":
                      if acType.lower()=="savings":
                          acType="Savings"
                      else:
                          acType="Current"
                    #   print(name+email+address+acType)
                      admin.createAcc(name,email,address,acType)
                  else:
                      print("Incorrect account type.")
              elif option=="2":
                  accNo=int(input("Enter account no:"))
                  flag=False
                  if flag==True:
                      print("Log out successful.")
                      break
                  if admin.checkAcNo(accNo)==False:
                      print("Account not found")
                  else:
                      print("Account identified")
                      name=input("Enter your name:")
                      email=input("Enter your email:")
                      if admin.checkAcInfo(accNo,name,email):
                          while True:
                               print("2 for deposit money.\n3 for withdrawl amount\n4 for check available balance.\n5 transactions history.\n6 get loan from"+
                             "the bank\n7 transfer money from your account to another account.\n8 for total loan amount.\n0 for log out.")
                               userOption=input("Option:")
                               if userOption=="0":
                                   print("Log Out Successful.")
                                   flag=True
                                   break
                               elif userOption=="8" or userOption=="2" or userOption=="3" or userOption=="4" or userOption=="5" or userOption=="6" or userOption=="7":
                                   userFeatures(accNo,int(userOption))
                               else:
                                   print("Invalid input")
                      else:
                          print("You have enter wrong credential.")
              elif option=="0":
                   break
              else:
                  print("Invalid input.")

    elif userType.lower()=='e':
        print("Thanks for visiting")
        break

    elif userType.lower()=="d":
        accNo=int(input("Enter account no:"))
        if admin.checkAcNo(accNo):
            print("Account found")
            name=input("Enter your name:")
            contact=input("Enter your contact no:")
            amount=int(input("Enter deposit amount:"))
            user=admin.returnUser(accNo)
            user.deposit(amount,admin,name+""+contact)
        else:
            print("Account not found")
    else:
        print("You have enter invalid option")
        



