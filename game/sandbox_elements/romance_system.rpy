init python:
    class Romance(object):

        def __init__(self, max_romance, char_name):
            self.current_romance = 0
            self.max_romance = max_romance
            self.char_name = char_name

        #ROMANCE STAT FUNCTIONS
        def adjust_romance(self, romance_change = 1):
            """
            To increase the romance add (+) value.
            
            To decrease the romance add (-) value.
            """
            self.current_romance = max(min(self.current_romance + romance_change,self.max_romance), 0)
            if self.current_romance == self.max_romance:
                renpy.notify("{} Romance cannot be increased anymore.".format(self.char_name))
            elif romance_change < 0:
                renpy.notify("{} Romance has been decreased.".format(self.char_name))
            else:
                renpy.notify("{} Romance has been increased.".format(self.char_name))
                #see saw system
                for i in see_saw_array:
                    if(i.char_name != self.char_name):
                        i.current_romance = max(min(i.current_romance - 1, i.current_romance), 0)
                    else:
                        continue


        def increase_max_romance(self, romance_value = 5):
            self.max_romance += romance_value
            renpy.notify("{} Romance limit has been increased.".format(self.char_name))


default keisuke_rom = Romance(20, Keisuke)
default azumi_rom = Romance(20, Azumi)
default damian_rom = Romance(20, Damian)
default rose_rom = Romance(20, Rose)
default see_saw_array = [keisuke_rom, azumi_rom, damian_rom, rose_rom]

label test_rom:

    "Keisuke romance incease"
    $ Keisuke_rom.adjust_romance(1)
    "Azumi rom inc"
    $ Azumi_rom

