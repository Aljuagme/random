# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:01:21 2020

@author: alvar
"""

# The reason of this implementation is because I wanted to try new things that 
# I've learned recently and like this become more familiar with them.

def change(money):
    """ Program that calculates the minimum number of bills/coins required
    to give a user change """
     
    #We want to make sure that you paid more than the price
    assert 0 <= money
    
    #Initiate the dictionary and convert the amount into cents
    money_back = {}
    money = round(money * 100, 2)
    
    # Some inner functions 
    def bill_500(money):
        while money >= 50000:
            if "Bill 500€" not in money_back:
                money_back["Bill 500€"] = 1
            else:
                money_back["Bill 500€"] +=1
            money -= 50000
        return money
    
    def bill_200(money):
        while money >= 20000:
            if "Bill 200€" not in money_back:
                money_back["Bill 200€"] = 1
            else:
                money_back['Bill 200€'] +=1
            money -= 20000
        return money
    
    def bill_100(money):
        while money >= 10000:
            if "Bill 100€" not in money_back:
                money_back["Bill 100€"] = 1
            else:
                money_back['Bill 100€'] +=1
            money-=10000
        return money
    
    # Recollect those functions and created a list out of it
    functions = [bill_500, bill_200, bill_100]
    
    # Iterate through every function
    for f in functions:
        money = f(money)
    
    # Lambda function for Bill of 50€
    bill_50 = lambda x: int(x//5000)
    bill_50(money)
    
    # If there is actually 1 or more, then add it to the dictionary
    if bill_50(money):
        money_back["Bill 50€"] = bill_50(money)
        money -= bill_50(money) * 5000
    
    # For the rest, 2 list wrapped
    amount = ["Bill 20€", 'Bill 10€', 'Bill 5€', 'Coin 2€','Coin 1€', 'Coin 0.50cts', 'Coin 0.20cts','Coin 0.10cts','Coin 0.5cts','Coin 0.2cts','Coin 0.1cts']
    rest = [2000,1000,500,200,100,50,20,10,5,2,1]
    
    small_change = zip(amount,rest)
    
    # Iterate through the zip object
    for value in small_change:
        while money >= value[1]:
            if value[0] not in money_back: money_back[value[0]] = 1
            else: money_back[value[0]]+=1
                
            money-=value[1]
    # List comprehension to print the money back in different lines        
    print("\n".join(["--> " + (str(key) + ": " + str(value))for key,value in money_back.items()]))
    print("\n")
    
    return "Thanks for your trust in our company"

# Make sure the user types numbers            
try:
    cost = float(input("How many € did it cost? "))
    give = float(input("How much did you give?  "))
    print("=" * 26, end="\n\n")
    
except:
    print("The inputs must be a numbers")
    
# If everything is fine, call the function
else:
    print(change(give-cost))
    
 