init python:
    import types

    def is_instance_userdefined_and_newclass(inst):
        cls = inst.__class__
        if hasattr(cls, '__class__'):
            return ('__dict__' in dir(cls) or hasattr(cls, '__slots__'))
        return False


    class Item(object):
        def __init__(self, name:str, cost:int):
            self.name = name
            self.cost = cost
            

    class Inventory:
        def __init__(self, money=0):
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
            renpy.notify(" You got {}$".format(amount))

        #To check for an item in inventory return True or false
        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False
        
        #add an item object into inventory
        def add(self, item):
            if is_instance_userdefined_and_newclass(item):
                self.items.append(item)

        #remove an item from an inventory
        def drop(self, item):
            self.items.remove(item)

default inventory = Inventory()
default inventory_items_removed_once = False
label inventory_values:

    $ laptop = Item("Laptop", 600)
    $ dildo = Item("Plastic_dildo", 100) 

    return