# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    call inventory_values from _call_inventory_values
    show screen stats_screen
    show screen char_profile_button
    show screen fondness_screen
    jump intro
    #Game end
    
    
    return
