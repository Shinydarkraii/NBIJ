default stats_screen_show = False
default fond_screen_show = False
default rose_stats_hidden = True
default kaisuke_stats_hidden = True
default inventory_screen_show = False 

image titletext = ParameterizedText(size=90, align=(0.5, 0.5))

screen mc_stats_display_test():
    $ corr = str( mc_corruption.current_corruption )
    $ mcorr = str(mc_corruption.max_corruption)
    $ rom = str(mc_corruption.current_romance)
    $ mrom = str(mc_corruption.max_romance)
    frame:
        xalign 1.0
        vbox:
            text "corruption = [corr]"
            text "max corruption = [mcorr]"
            text "romance = [rom]"
            text "max romance = [mrom]"
            text "strength = [mc_corruption.current_strength]"
            text "max strength = [mc_corruption.max_strength]"

        

screen affection_display_test():
    frame:
        xalign 0.0
        yalign 0.2
        vbox:
            text "affection daichi [daichi_aff.current_affection]"
            text "affection xia [xia_aff.current_affection]"
            text "affection evelyn [evelyn_aff.current_affection]"
            text "affection aiden [aiden_aff.current_affection]"
    frame:
        hbox:
            textbutton "inc daichi" action Function(daichi_aff.adjust_affection,1)
            textbutton "inc xia" action Function(xia_aff.adjust_affection,1)
            textbutton "inc evelyn" action Function(evelyn_aff.adjust_affection,1)
            textbutton "inc aiden" action Function(aiden_aff.adjust_affection,1)

screen Inventory_screen():
    $ money = str(inventory.money)
    $ items = inventory.items
    $ height = 3
    $ padding = 5

    tag side_screen

    imagebutton:
        xalign 0.15
        yalign 0.04
        idle im.Scale("UI/handbag.png", 120, 120)
        hover im.Scale("UI/handbag1.png", 120, 120)
        if inventory_screen_show:
            action [SetLocalVariable("inventory_screen_show", False), Show("fondness_screen")]
        else:
            action [SetLocalVariable("inventory_screen_show", True), Hide("fondness_screen")]

    if inventory_screen_show:
        frame:
            background None
            xmaximum 500
            ymaximum 300
            xalign 0.147
            yalign 0.15
            has vbox
            hbox:
                text "Inventory" style "fond_screen_style" 
                text "                   "
                text "{font=gui/fonts/mangatb.ttf}{color=#9AEC7C}$[money]{/color}{/font}" 
            
            vbox:
                align (0.5,0.5)
                xsize 500
                fixed:
                    ysize height
                    null height padding
                    add "#f2f2f2"
                    null height padding
                # text "\n"

            for item in inventory.items:
                textbutton item.name:
                    at to_right()
                    action NullAction()
                    text_style "inv_screen_style"
                    

transform to_right():
    on idle:
        xoffset 0
    on hover:
        linear 0.3 xoffset 20

#empty screen
screen empty():
    text ""



screen stats_screen():
    imagebutton:
        xalign 0.95
        yalign 0.04
        idle im.Scale("UI/stats_icon_idle.png", 100, 100)
        hover im.Scale("UI/stats_icon_hover.png", 100, 100)
        if stats_screen_show == False:
            action [Show("stats_screen_open"), SetVariable("stats_screen_show", True)]
        else:
            action [Hide("stats_screen_open"), SetVariable("stats_screen_show", False)]



screen stats_screen_open():

    frame:
        xalign 0.965
        yalign 0.19
        xmaximum 700
        ymaximum 500
        background None
        vbox:
            yoffset 25
            spacing 40
            frame:
                background None
                hbox:
                    image im.Scale("UI/Kiara2.png", 120, 120) 
                    vbox:
                        yoffset 15
                        bar value AnimatedValue(mc_stats.current_corruption,mc_stats.max_corruption, delay= 1 ): 
                            xmaximum 360
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            left_bar im.Scale("UI/bar_full_corr.png", 360, 40) 
                            right_bar im.Scale("UI/bar_empty_corr.png", 360, 40)
                        bar value AnimatedValue(mc_stats.current_strength,mc_stats.max_strength, delay= 1 ): 
                            xmaximum 360
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None
                            left_bar im.Scale("UI/bar_full_str.png", 360, 40) 
                            right_bar im.Scale("UI/bar_empty_str.png", 360, 40)
            hbox:
                spacing 5
                add im.Scale("UI/Damian2.png", 120, 120)
                bar value AnimatedValue(damian_rom.current_romance,damian_rom.max_romance, delay= 1 ): 
                    yalign 0.5
                    xmaximum 360
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    left_bar im.Scale("UI/bar_full.png", 360, 40)
                    right_bar im.Scale("UI/bar_empty.png", 360, 40)
            
            if kaisuke_stats_hidden == False:
                hbox: 
                    spacing 5 
                    image im.Scale("UI/keisuke2.png", 120, 120)
                    bar value AnimatedValue(keisuke_rom.current_romance,keisuke_rom.max_romance, delay= 1 ): 
                        yalign 0.5
                        xmaximum 360
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        left_bar im.Scale("UI/bar_full.png", 360, 40) 
                        right_bar im.Scale("UI/bar_empty.png", 360, 40) 

            if rose_stats_hidden == False: 
                hbox:
                    spacing 5  
                    image im.Scale("UI/Rose2.png", 120, 120)
                    bar value AnimatedValue(rose_rom.current_romance,rose_rom.max_romance, delay= 1 ): 
                        yalign 0.5
                        xmaximum 360
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                        left_bar im.Scale("UI/bar_full.png", 360, 40) 
                        right_bar im.Scale("UI/bar_empty.png", 360, 40)  
            hbox: 
                spacing 5
                image im.Scale("UI/Azumi2.png", 120, 120)
                bar value AnimatedValue(azumi_rom.current_romance,azumi_rom.max_romance, delay= 1 ):
                    yalign 0.5 
                    xmaximum 360
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    left_bar im.Scale("UI/bar_full.png", 360, 40) 
                    right_bar im.Scale("UI/bar_empty.png", 360, 40)   
            # frame:
            #     background None    
            #     image im.Scale("UI/Rose.png", 120, 120)

screen fondness_screen:

    imagebutton:
        xalign 0.05
        yalign 0.04
        idle im.Scale("UI/fondness_icon_idle.png", 100, 100)
        hover im.Scale("UI/fondness_icon_hover.png", 100, 100)
        if fond_screen_show:
            action [SetLocalVariable("fond_screen_show", False), Show("Inventory_screen")]
        else:
            action [SetLocalVariable("fond_screen_show", True), Hide("Inventory_screen")]

    if fond_screen_show:
        frame:
            background None
            xminimum 200
            xalign 0.027
            yalign 0.15
            vbox:
                
                text "{font=gui/fonts/mangatb.ttf}{u}Fondness{/u}{/font}" size 45 style "fond_screen_style"
                text "[Natsuko] - [natsuko_fond.current_fondness]" style "fond_screen_style"
                text "[Daichi] - [daichi_fond.current_fondness]" style "fond_screen_style"
                text "[Xia] - [xia_fond.current_fondness]" style "fond_screen_style"
                text "[Evelyn] - [evelyn_fond.current_fondness]" style "fond_screen_style"
                text "[Aiden] - [aiden_fond.current_fondness]" style "fond_screen_style"

style fond_screen_style is text:

    font "gui/fonts/mangatb.ttf"
    color "#f2f2f2"

style inv_screen_style is text:
    font "gui/fonts/mangatb.ttf"
    color "#f2f2f2"
    hover_color "#f2f2f2"
    size 40
    # transform "to_right"