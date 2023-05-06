init python:
    class Fondness(object):
        
        def __init__(self, max_fondness, char_name):
            self.current_fondness = 0
            self.max_fondness = max_fondness
            self.char_name = char_name

        def adjust_fondness(self, fondness_change = 1):
            """
            To increase the fondness add (+) value.
            
            To decrease the fondness add (-) value.
            """
            self.current_fondness = max(min(self.current_fondness + fondness_change,self.max_fondness), 0)
            if self.current_fondness == self.max_fondness:
                renpy.notify("{} fondness cannot be increased anymore.".format(self.char_name))
            elif fondness_change < 0:
                renpy.notify("{} fondness has been decreased.".format(self.char_name))
            else:
                renpy.notify("{} fondness has been increased.".format(self.char_name))

        def increase_max_fondness(self, fondness_value = 5):
            self.max_fondness += fondness_value
            renpy.notify("{} fondness limit has been increased.".format(self.char_name))
                
        #for screen values
        def get_current_fondness(self):
            return self.current_fondness


default daichi_fond = Fondness(10, Daichi)
default xia_fond = Fondness(10, Xia)
default evelyn_fond = Fondness(10, Evelyn)
default aiden_fond = Fondness(10, Aiden)
default natsuko_fond = Fondness(10, Natsuko)

label fondness_test_1:

    show screen fondness_display_test
    show screen mc_stats_display_test
    show screen empty

return

