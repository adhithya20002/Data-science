# #PUBLIC 

# class person:
#     def __init__(self,name):
#         self.name=name
# p=person("Alice")
# print(p.name)

##PROTECTED

# class person:
#     def __init__(self,name):
#         self._name=name
        
# class student(person):
#     def get_name(self):
#         return self._name
# s=student("Bob")
# print(s.get_name())

##PRIVATE

# class person:
#     def __init__(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
# p=person("Charlie")
# print(p.get_name())



##BANK ACCOUNT CODE

# class bankaccount:
#     def __init__ ( self,account_holder,balance=0 ):
#         self.account_holder =  account_holder
#         self.balance= balance
        
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print("Deposited rupees",amount)
#             print("New balance",self.balance)
#         else:
#             print ( "Deposit amount must be positive" )
        
#     def withdraw(self,amount):
#         if amount>= self.balance:
#             print("Insufficient Balance")
#         elif amount<=0:
#             print("Amount must be positive")
#         else:
#             self.balance-=amount
#             print(f"Withdrew rupees {amount}.New balance : Rupees{self.balance}")
     
#     def check_balance(self):
#         print(f"Current balance: rupees{self.balance}")


# account = bankaccount("Adhithya" , 20000)
# account.check_balance()
# account.deposit(100000)
# account.withdraw(20000)


# student report

# class student:
#     def __init__(self,name,math,science):
#         self.name=name
#         self.math=math
#         self.science=science
    
#     def total(self):
#         return self.math+self.science
    
#     def display_report(self):
#         print("student name is",self.name)
#         print("math",self.math)
#         print("science",self.science)
    
# p=student("Adhithya",95,98)
# p.display_report()        
    
    
## product discount))

class discount:
    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount
        
    def final_price(self):
        return self.price-self.discount
    
    def show_detials(self):
        print(name ,self.name)
        print(price,self,price)
        print(discount,self.discount)
        
p=Product("shampoo",550,250)
p.display_show()

