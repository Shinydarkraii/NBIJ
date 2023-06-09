

screen char_profile():
    tag quick_menu

    add "char_profile_bg.jpg"

    add "[preview_img]":
        xpos 200
        ypos 160

    imagebutton:
        xalign 0.99
        yalign 0.01
        idle "images/UI/back_button.png"
        action [Hide("char_profile"), Show("char_profile_button"), Show("quick_menu")]

    vpgrid id "upper_char":
        xalign 0.987
        yalign 0.14
        cols 4
        rows 4
        transpose False
        spacing 5
        mousewheel True
        scrollbars "vertical"
        ymaximum 600

        for i in char_obj:
            imagebutton:
                xysize (170, 200)
                idle i[2]
                hover i[2]
                action [SetVariable("preview_img", i[3]), SetScreenVariable("char_profile_name", i[0]), SetScreenVariable("char_profile_desc", i[4]), SetVariable("char_profile_age", i[1])]
    vbar value YScrollValue("upper_char") ymaximum 550 xalign 0.992 yalign 0.9 thumb "images/UI/bar_top.png" bottom_bar "images/UI/bar_bottom.png" top_bar "images/UI/bar_bottom.png"

    frame:
        background None
        xalign 0.855
        yalign 0.54
        # xmaximum 680
        ymaximum 20
        xsize 650
        xanchor 0.5
        yanchor 0.5
        text "[char_profile_name]" size 100 xalign 0.5 yalign 0.5

    frame:
        background None
        xalign 0.98
        yalign 0.59
        xmaximum 680
        ymaximum 50
        text "Age - [char_profile_age]" size 30

    frame:
        background None
        xalign 0.775
        yalign 0.59
        xmaximum 680
        ymaximum 50
        text "About - " size 30
    
    viewport id "char_profile":
        ymaximum 500
        xmaximum 650
        xalign 0.991
        yalign 0.6
        xanchor 1.0
        yanchor 0.0  
        mousewheel True
        text "[char_profile_desc]" size 30 
    vbar value YScrollValue("char_profile") ymaximum 550 xmaximum 10 xalign 0.998 yalign 0.9 thumb "images/UI/bar_top.png" bottom_bar "images/UI/bar_bottom.png" top_bar "images/UI/bar_bottom.png"
        
screen char_profile_button():

    imagebutton:
        xalign 0.9
        yalign 0.04
        idle im.Scale("images/UI/info.png", 100, 100)
        action Show("char_profile")
    

default preview_img = "images/UI/Kiaraprofile.png"
default char_profile_name = "Kiara"
default char_profile_age = 23
default char_profile_desc = "Kiara is a 23-year-old woman who has faced significant challenges in her past but has emerged from them as a strong and resilient individual. Despite being the daughter of a billionaire, she is humble, kind-hearted, and selfless, always putting the needs of others before her own. Kiara is proud of her mixed heritage, being half-Japanese and half-American, and she values her individuality and independence, wanting to be recognized for her own accomplishments rather than her family's wealth. She has recently recovered from a coma that lasted throughout the COVID-19 pandemic, and while she experiences some amnesia about her past, she remains optimistic and determined to build a better future for herself and those she cares about. Although she can be somewhat reserved, Kiara is a trustworthy and loyal friend who believes in the importance of building strong relationships with others."
default char_obj = [
    ["Kiara", 23, im.Scale("images/UI/Kiaraprofile.png", 170, 190), "images/UI/Kiaraprofile.png", "Kiara is a 23-year-old woman who has faced significant challenges in her past but has emerged from them as a strong and resilient individual. Despite being the daughter of a billionaire, she is humble, kind-hearted, and selfless, always putting the needs of others before her own. Kiara is proud of her mixed heritage, being half-Japanese and half-American, and she values her individuality and independence, wanting to be recognized for her own accomplishments rather than her family's wealth. She has recently recovered from a coma that lasted throughout the COVID-19 pandemic, and while she experiences some amnesia about her past, she remains optimistic and determined to build a better future for herself and those she cares about. Although she can be somewhat reserved, Kiara is a trustworthy and loyal friend who believes in the importance of building strong relationships with others."],
    ["Veronica", 28, im.Scale("images/UI/veronicaprofile.png", 170, 190), "images/UI/veronicaprofile.png", "Veronica Majors is a highly successful lawyer in New York City, known for both her sharp legal mind and stunning looks. Despite her feminine beauty, Veronica has a tomboyish attitude that sets her apart from other women in her field. At 28 years old, she is still quite young, but she has already made a name for herself in the legal community.Veronica is bisexual by nature and has developed a fondness for Evelyn Hall, the older daughter of Mia. She wants everyone around her, including her cousin Mason, to be happy and fulfilled. Despite her outward confidence, Veronica struggles with feelings of loneliness that she keeps hidden from others. There are only two people in the world who can truly touch Veronica's heart: Mason, who she has known since childhood and has watched grow into a successful lawyer like herself, and Evelyn, who she has loved since they first met. Despite her feelings for Evelyn, Veronica is hesitant to express them for fear of being rejected or causing problems within the family dynamic."],
    ["Xia", 39,im.Scale("images/UI/xiaprofile.png", 170, 190), "images/UI/xiaprofile.png", "Xia Watanabe is a fierce and skilled woman who has dedicated her life to the art of wing chun, which she learned to protect her loved ones. At 43 years old, Xia resides in Osaka with her father, and longs for her family to be reunited once again. She is deeply caring and always puts the needs of others before her own. Xia has a daughter named Natsuko, and is happily married to Ichigo. Despite her strength and confidence, Xia harbors a deep-seated hatred for John due to his mistreatment of her sister, Mia. However, she endures his presence for the sake of her family. Xia is emotionally stable and resolute, but becomes vulnerable and defensive when it comes to Ichigo, who loves her unconditionally."],
    ["Mia", 36, im.Scale("images/UI/Miaprofile.png", 170, 190), "images/UI/Miaprofile.png", "Mia Watanabe/Hall is a 40-year-old Japanese woman who moved to New York after marrying Jonathan Hall. She is a kind and caring person who loves her daughters and wants the best for them. Despite the challenges of her marriage to Jonathan, Mia has always put her daughters first and tried to create a happy home for them. Mia often feels torn between her Japanese heritage and her life in New York, and she struggles with feelings of guilt and a sense of not belonging. She misses her family in Japan but fears they may reject her for leaving, and this weighs heavily on her mental health.Despite her struggles, Mia is a resilient person who keeps pushing forward to make a better life for her daughters. She is determined to create a better future for them, even if it means sacrificing her own happiness in the process."],
    ["Keisuke", 27, im.Scale("images/UI/Keisukeprofile.png", 170, 190), "images/UI/Keisukeprofile.png", "Keisuke Takahashi is a successful 27-year-old CEO of an esteemed company in Osaka, Japan. Despite his many accomplishments, there is a deep sense of loneliness that lingers within him. The cause of this feeling can be traced back to his childhood when he met a young girl named Kiara. They instantly connected and spent every moment together until Kiara left to go back home. Keisuke has been unable to forget about her and has never been able to love anyone else. He often thinks about the moments they shared and wonders where Kiara is now. Even though he is financially well off, he feels like something is missing in his life. Despite his success, Keisuke is riddled with self-doubt and depression. He is haunted by the thought that he wasn't good enough for Kiara, which led to her leaving. He longs to reconnect with her but is afraid that it's too late and she has moved on. One of Keisuke's greatest desires is to start a family and have a normal life with someone he loves. But until he finds Kiara, he feels like he will never truly be complete. The memory of Kiara is a constant reminder of what could have been, and he wonders if fate will ever bring them back together."],
    ["Jennifer", 32, im.Scale("images/UI/jenniferprofile.png", 170, 190), "images/UI/jenniferprofile.png", "Jennifer Serkis is an infamous lawyer known for her skills in defending clients in high-profile cases. She's considered one of the best lawyers in the country and will stop at nothing to win a case. Jennifer is a caring person outside the courtroom, but inside, she's cold and ruthless. Her father's murder at the hands of a mob has made her emotionally hardened, and the unrequited love she had for Mason, who fell for someone else, has only added to her bitterness. Jennifer is highly secretive about her personal life, but rumors abound that she has connections with people in the jury and judges, which she may use to gain an advantage in court."],
    ["Azumi", 22, im.Scale("images/UI/azumiprofile.png", 170, 190), "images/UI/azumiprofile.png", "Azumi Hazashi is a 22-year-old Japanese woman who lost her parents at a young age and was subsequently raised by her uncle, Sato Hazashi. Due to her tragic past, Azumi has developed a fear of trusting others and tends to keep to herself. She values kindness above all else and despises lies, as honesty is very important to her. Azumi is a mature and elegant individual who is known for her calm demeanor and reserved personality. She currently resides in Osaka, Japan, where she works as an English teacher at a local school. Azumi is also a lesbian, which adds an extra layer of complexity to her life. Despite her reservations, Azumi strives to build meaningful connections with those around her, though she must overcome her fear of trusting others to do so."],
    ["Jake", 26, im.Scale("images/UI/jakeprofile.png", 170, 190), "images/UI/jakeprofile.png", "Jake Watson is a 25-year-old man who has experienced a lot of hardship in his life. His father passed away from a drug overdose, leaving Jake as the sole child to his mother. His mother, unfortunately, has terminal cancer and requires expensive medical care. Jake is a good person at heart, but due to his circumstances, he often has to do things that aren't considered ethical. He works as a private investigator for clients, using his skills to solve problems and make ends meet for his family. Despite his profession, Jake hates what he does and finds it challenging to balance work and life. However, his love and appreciation for his mother drive him to continue working as hard as he can, even if it means going beyond what is legal or ethical. He's aware of the consequences of his actions, but he's willing to take the risk to ensure that his mother gets the care she needs. Jake's ultimate goal is to save his mother's life and provide her with a comfortable lifestyle, which he believes she deserves. He's willing to do anything to achieve this goal, but he's also aware of the toll it takes on him mentally and emotionally. Despite the challenges he faces, he hopes to one day settle down and live a normal life, free from the burdens of his current profession."],
    ["John", 40,im.Scale("images/UI/johnprofile.png", 170, 190), "images/UI/johnprofile.png", "Jonathan Hall is a wealthy businessman based in New York, renowned for his power and influence among the city's elite. He is known to have ties to the underworld, which has further solidified his reputation as an individual not to be trifled with. Jonathan's success and power have led him to develop a strong sense of ego and a desire to always be on top. He has a fragile self-image, which makes him prone to lash out when he feels threatened or challenged.Unfortunately, this fragile ego has also led to him becoming mentally abusive towards his wife Mia and their two daughters, Kiara and Evelyn. Despite his wealth and power, Jonathan's personal life has been plagued by turmoil and controversy. He has been accused of multiple instances of harassment and blackmail, which have further eroded his reputation.Jonathan is 46 years old, and while he may appear to have everything a person could want on the surface, his actions and behavior reveal a much darker side to his personality."],
    ["Lana", 21,im.Scale("images/UI/lanaprofile.png", 170, 190), "images/UI/lanaprofile.png", "Lana Movesesian is a 22-year-old socialite from one of the most influential families in New York. Her mother, Elizabeth, is the CEO of a major pharmaceutical company, and Lana has always lived a life of luxury and privilege. Despite this, Lana has a kind heart and genuinely cares for those she loves. Lana and Kiara were best friends during their time at university, and Lana is one of the few people who know that Kiara is still alive. She has kept in contact with Kiara, even though most of their memories of each other have been lost. Lana's outgoing personality often makes her the life of the party, but she also has a more serious and caring side that she reserves for her closest friends. Lana had feelings for Damian during their university days, but she stepped back when she learned that he and Kiara were together. Now that Kiara is gone, Lana wants to help Damian move on and find happiness. She knows that he and Kiara had a special connection, but she also believes that Damian deserves to find love again. Despite her good intentions, Lana is often judged by society for her partying lifestyle. However, those who truly know her understand that she has a kind heart and is always willing to help those in need."],
    ["Natsuko", 21, im.Scale("images/UI/natsukoprofile.png", 170, 190), "images/UI/natsukoprofile.png", "Natsuko Watanabe is a young woman who is currently pursuing a degree in medicine at Osaka University. She is 21 years old and is the daughter of Xia, making her Kiara's cousin. Unlike her mother, Natsuko is emotionally sensitive and often puts others' needs before her own. She has a kind heart and always strives to make her family members happy. Despite having her memories of Kiara erased, Natsuko still knows what happened to her cousin and hopes for her safe return. She longs for a united family and fears upsetting her mother, who can be quite overbearing at times. Natsuko has always been focused on her studies and has never had time for romantic relationships. However, she cares deeply for her friends and is always there to support them. She is particularly close to Damian, whom she trusts as a friend and confidant. Knowing what happened with Kiara, Natsuko wants to help Damian move on and find happiness"],
    ["Valentina", 23, im.Scale("images/UI/valentinaprofile.png", 170, 190), "images/UI/valentinaprofile.png", "Valentina Parker is a tech-savvy 22-year-old girl who is passionate about ethical hacking. She and Kiara were good friends during their university days, and she also knew Damian, though they weren't as close. When she heard about Kiara's supposed death, she couldn't believe it, knowing that John was capable of manipulating the truth. Valentina doesn't want anyone, including Damian and Kiara, to suffer due to John's deceitful ways, but she finds it challenging to help them from a distance. Despite being happy with her life, Valentina often finds herself reminiscing about the good old days with her friends at university. She's engaged to Nick, whom she loves deeply, and Aiden is her mentor, teaching her the ins and outs of hacking. Valentina is a strong-minded person, but she's also prone to feeling vulnerable when her loved ones are in trouble. She wants nothing more than to help her friends and keep them safe, but she struggles to find the best way to do so without putting herself or her loved ones in danger."],
    ["Evelyn", 27, im.Scale("images/UI/evelyn profile.png", 170, 190), "images/UI/evelyn profile.png", "Evelyn Hall, the older daughter of Mia and John, is a strong-willed and independent woman at the age of 26. She moved out of her family's home at the age of 16, after being assaulted by her father. This traumatic event has caused her to develop a distrust of society and struggle with mental health issues. Evelyn only trusts two people in her life: her friend Veronica and her younger sister Kiara. However, Kiara has been away from her for the past 10 years, causing Evelyn to feel a great sense of loss and loneliness.\n\nEvelyn has attempted to reconnect with her family, but as long as John remains in the picture, it seems impossible. Despite her own struggles, she desires for her family to be okay. Amidst all of this, Evelyn has developed feelings for Veronica, but feels too emotionally unstable to pursue a relationship with her."],
    ["Damian", 25,im.Scale("images/UI/damianprofile.png", 170, 190), "images/UI/damianprofile.png", "Damian Boyd, a 24-year-old living in Harlem, is a man of unwavering determination and a strong moral compass. Despite the risks, he always tries to do the right thing, making him a highly respected figure in the community. \n \nDamian was a brilliant student at university and now runs his own coaching institute, helping others achieve their goals. To the outside world, Damian appears to be a young man with a bright future ahead of him. But beneath the surface lies a deep pain and heartache that he has kept hidden for years. You see, Damian's true motivation for his success is his love for Kiara, his former girlfriend from university. When Kiara was involved in a terrible accident that left her in a coma, Damian was devastated. He was told that she had died in the crash, which shattered his world. Unbeknownst to him, Kiara survived, but her memories were erased, leaving her with no recollection of Damian. Despite his success, Damian's life has been incomplete without Kiara. He struggles to move on, constantly haunted by the thought of what could have been.Despite not knowing the truth, he's remained loyal to her memory and continues to work hard in the hopes of making her proud. Although he's still processing his grief, Damian is committed to making a difference in his community. He's determined to live a life that would make Kiara proud, even if he can never be with her again."]
]
