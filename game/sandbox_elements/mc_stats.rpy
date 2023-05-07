init python:
    class Mc_stats(object):
        
        def __init__(self, max_corruption, max_strength, char_name):
            self.current_corruption = 0
            self.current_strength = 0
            self.max_corruption = max_corruption
            # self.max_romance = max_romance
            self.max_strength = max_strength
            self.char_name = char_name


        ##CORRUPTION FUNCTIONS
        def adjust_corruption(self, corruption_change = 5):
            """
            To increase the corruption add (+) value.
            
            To decrease the corruption add (-) value.
            """
            self.current_corruption = max(min(self.current_corruption + corruption_change,self.max_corruption), 0)
            if self.current_corruption == self.max_corruption:
                renpy.notify("{} Corruption cannot be increased anymore.".format(self.char_name))
            elif corruption_change < 0:
                renpy.notify("{} Corruption has been decreased.".format(self.char_name))
            else:
                renpy.notify("{} Corruption has been increased.".format(self.char_name))

        def increase_max_corruption(self, corruption_value = 5):
            self.max_corruption += corruption_value
            renpy.notify("{} corruption limit has been increased.".format(self.char_name))
        
        ##ROMANCE STAT FUNCTIONS
        # def adjust_romance(self, romance_change = 1):
        #     """
        #     To increase the romance add (+) value.
            
        #     To decrease the romance add (-) value.
        #     """
        #     self.curent_romance = max(min(self.curent_romance + romance_change,self.max_romance), 0)
        #     if self.curent_romance == self.max_romance:
        #         renpy.notify("{} Romance cannot be increased anymore.".format(self.char_name))
        #     elif romance_change < 0:
        #         renpy.notify("{} Romance has been decreased.".format(self.char_name))
        #     else:
        #         renpy.notify("{} Romance has been increased.".format(self.char_name))

        # def increase_max_romance(self, romance_value = 5):
        #     self.max_romance += romance_value
        #     renpy.notify("{} Romance limit has been increased.".format(self.char_name))


        ##STRENGTH START FUNCTIONS
        def adjust_strength(self, strength_change = 1):
            """
            To increase the strength add (+) value.
            
            To decrease the strength add (-) value.
            """
            self.current_strength = max(min(self.current_strength + strength_change,self.max_strength), 0)
            if self.current_strength == self.max_strength:
                renpy.notify("{} Strength cannot be increased anymore.".format(self.char_name))
            elif strength_change < 0:
                renpy.notify("{} Strength has been decreased.".format(self.char_name))
            else:
                renpy.notify("{} Strength has been increased.".format(self.char_name))

        def increase_max_strength(self, strength_value = 5):
            self.max_strength += strength_value
            renpy.notify("{} Strength limit has been increased.".format(self.char_name))
        
        # #for screen values
        # def get_current_corruption(self):
        #     return self.current_corruption

default mc_stats = Mc_stats(500,10, Kiara)


label corruption_test:

    John "This is a corruption test."

    John "My current corruption is [mc_corruption.current_corruption]."

    John "Increase my corruption?"

    show screen corruption_display

    label .part_1:
        menu:
            "Increase.":
                $ mc_corruption.adjust_corruption(1)
                John "My current corruption is [mc_corruption.current_corruption]."
                jump .part_1
            "Decrease.":
                $ mc_corruption.adjust_corruption(-1)
                John "My current corruption is [mc_corruption.current_corruption]."
                jump .part_1

            "Increase Max corruption":
                $ mc_corruption.increase_max_corruption()
                John "My max corruption is [mc_corruption.max_corruption]."
                jump .part_1

            "Exit":
                pass

return


