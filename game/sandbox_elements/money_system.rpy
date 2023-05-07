init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost
            

    class Inventory:
        def __init__(self, money=500):
            self.money = money
            self.max_money = 9000
            self.items = []

        #function when player purchases from shop
        def buy(self, item):
            if self.money >= item.cost: 
                self.money -= item.cost
                self.items.append(item)
                renpy.notify("Item purchased. {}".format(item))
            else:
                renpy.notify("Not enough money")

        #When player does jobs and earns money
        def earn(self, amount):
            self.money = min(self.money + amount,self.max_money)

        #To check for an item in inventory return True or false
        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False
        
        #add an item object into inventory
        def add(self, item):
            self.items.append(item)

        #remove an item from an inventory
        def drop(self, item):
            self.items.remove(item)

default inventory = Inventory()

label inventory_values:

    $ laptop = Item("Laptop", 600)
    $ dildo = Item("Plastic_dildo", 100) 
    $ inventory.add(laptop)
    $ inventory.add(dildo)

    return