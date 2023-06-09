
#Gallery code
screen gallery():

    style_prefix "navigation"
    add "images/Jpn/Prelude/bg photoshootleather 8.png"
    default gallery_a_list = [
            # [Scene Label, Image, Persistent ]
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), persistent.kiara_scene_1_unlocked],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True],
            ["chap_2_scene_7", im.Scale("images/Jpn/kiagmrscn/bg kiagmrscn 20.jpg", 640, 360), True]
        ]

    default total_scenes = len(gallery_a_list)
    default cg_page_a = 1
    default cg_page_a_max = max(int(total_scenes / 4) + (total_scenes % 4 > 0), 1)

    zorder 100
    tag menu

    text "Page [cg_page_a] of [cg_page_a_max]" xalign 0.5 yalign 0.01 text_align 0.5 color "#0099cc" size gui.interface_text_size
    text "Total Scenes: [total_scenes]" xalign 0.99 yalign 0.01

    hbox:
        #style_prefix "gallery_stuff"
        xalign 0.5
        yalign 0.5

        grid 2 2:
            #style_prefix "gallery_stuff"
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(((cg_page_a-1)*4),(cg_page_a*4)):
                if i < len(gallery_a_list):
                    imagebutton:
                        action Replay(gallery_a_list[i][0], scope={"mc_name": Kiara or "Kiara"}, locked=not (renpy.seen_label(gallery_a_list[i][0]) or gallery_a_list[i][2] or persistent.master_unlock))
                        idle Transform(gallery_a_list[i][1], zoom=1)
                        hover Composite((640, 360), (0, 0), gallery_a_list[i][1], (0, 0), "images/UI/thumbnail_hover.png")
                        insensitive Transform(gallery_a_list[i][1], zoom=1, blur=30, xsize=640, ysize=360, matrixcolor=SaturationMatrix(0))
                else:
                    null

    hbox:
        xalign 0.5
        yalign 0.99
        ## Our buttons for the pages of Character A's Gallery section.

        textbutton _("<") action [SetLocalVariable("cg_page_a", If(cg_page_a>1, cg_page_a-1, cg_page_a_max))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

        #ADD A SCROLL BARE HERE JUST IN CASE
        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, cg_page_a_max+1):
            if page == cg_page_a:
                textbutton "{color=#0099cc}{b}[page]{/b}{/color}"  action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
            else:
                textbutton "[page]" action SetLocalVariable("cg_page_a", page) text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

        textbutton _(">") action [SetLocalVariable("cg_page_a", If(cg_page_a<cg_page_a_max, cg_page_a+1, 1))] text_outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

    #Gallery exit
    textbutton _("Return") action [Return(), Hide("gallery_navigation")] xalign 0.97 yalign 0.95

    # Alternative Return "Escape" and "Mouse Right Click"
    key "K_ESCAPE" action [Return(), Hide("gallery_navigation")]
    key "mouseup_3" action [Return(), Hide("gallery_navigation")]