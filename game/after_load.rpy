label after_load():
    $ see_saw_array = [keisuke_rom, azumi_rom, damian_rom, rose_rom]
    if inventory.has_item(100):
        $ inventory.drop(100)

    if inventory_items_removed_once:
        $ inventory.drop(100)
        $ inventory.drop(laptop)
        $ inventory.drop(dildo)
        $ inventory_items_removed_once = False

    $ inventory_items_removed_once = True
    hide screen Inventory_screen
    show screen Inventory_screen