label after_load():
    $ see_saw_array = [keisuke_rom, azumi_rom, damian_rom, rose_rom]
    if inventory.has_item(100):
        $ inventory.drop(100)

    
    hide screen Inventory_screen
    show screen Inventory_screen
    if inventory.has_item(laptop):
        $ inventory.drop(laptop)
        $ inventory.drop(dildo)