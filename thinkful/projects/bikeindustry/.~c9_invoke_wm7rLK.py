#These are the bike classes, they will be separated by weight class 
class Bike(object):
    def __init__(self, name, weight, unitcost):
        self.name = name
        self.weight = weight
        self.unitcost = unitcost

#Shops, they take inventory and money from Customers
class Shop(object):
    def __init__(self, name, stock, salemargin=.20, profit, inventory=None):
        self.name = name
        self.stock = stock
        self.salemargin = .20
        self.profit = 0
        if inventory != None:
            self.inventory = inventory
        else:
            self.inventory = {}
            
    def store_inventory(self):
        print(self.inventory)
        
    def bike_filter(self,):
        if self.unitcost*self.salemargin 
        if self.unitcost*self.salemargin <= self.budget:
            
#Customers, Shops take money from them    
class Customer(object):
    def __init__(self, name, budget, purchase, inventory=None):
        self.name = name
        self.budget = budget
        self.purchase = purchase
        if self.inventory != None:
            self.inventory = inventory
        else:
            self.inventory = {}
        
    def cust_inventory(self):
        print(self.inventory)
            
    def afford_filter(self, budget):
        
'''Bike'''
        
#This section contains the Bike models with corresponding attributes

    def store_salemargin(self): #Accounts for unit cost and 20% profit margin 
        margin = self.unitcost + (self.unitcost * .20)   

'''Customer'''

      
if name == "main":
    