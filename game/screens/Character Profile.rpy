

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

    $ vp_rows = int((len(char_obj) + 3)/4 ) 
    vpgrid id "upper_char":
        xalign 0.987
        yalign 0.14
        cols 4
        rows vp_rows
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
        text "[char_profile_name]":
            size 100
            xalign 0.5 
            yalign 0.5

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
default char_profile_desc = "Kiara is a 23-year-old woman who has faced significant challenges in her past but has emerged from them as a strong and resilient individual. Despite being the daughter of a billionaire, she is humble, kind-hearted, and selfless, always putting the needs of others before her own. Kiara is proud of her mixed heritage, being half-Japanese and half-American, and she values her individuality and independence, wanting to be recognized for her own accomplishments rather than her family's wealth.\n\nShe has recently recovered from a coma that lasted throughout the COVID-19 pandemic, and while she experiences some amnesia about her past, she remains optimistic and determined to build a better future for herself and those she cares about. Although she can be somewhat reserved, Kiara is a trustworthy and loyal friend who believes in the importance of building strong relationships with others."
default char_obj = [
    ["Kiara", 23, im.Scale("images/UI/Kiaraprofile.png", 170, 190), "images/UI/Kiaraprofile.png", "Kiara is a 23-year-old woman who has faced significant challenges in her past but has emerged from them as a strong and resilient individual. \n Despite being the daughter of a billionaire, she is humble, kind-hearted, and selfless, always putting the needs of others before her own. Kiara is proud of her mixed heritage, being half-Japanese and half-American, and she values her individuality and independence, wanting to be recognized for her own accomplishments rather than her family's wealth.\n\nShe has recently recovered from a coma that lasted throughout the COVID-19 pandemic, and while she experiences some amnesia about her past, she remains optimistic and determined to build a better future for herself and those she cares about. Although she can be somewhat reserved, Kiara is a trustworthy and loyal friend who believes in the importance of building strong relationships with others."],
    ["Veronica", 28, im.Scale("images/UI/veronicaprofile.png", 170, 190), "images/UI/veronicaprofile.png", "Veronica Majors is a highly successful lawyer in New York City, known for both her sharp legal mind and stunning looks. Despite her feminine beauty, Veronica has a tomboyish attitude that sets her apart from other women in her field. At 28 years old, she is still quite young, but she has already made a name for herself in the legal community.\n\nVeronica is bisexual by nature and has developed a fondness for Evelyn Hall, the older daughter of Mia. She wants everyone around her, including her cousin Mason, to be happy and fulfilled. Despite her outward confidence, Veronica struggles with feelings of loneliness that she keeps hidden from others\n\nThere are only two people in the world who can truly touch Veronica's heart: Mason, who she has known since childhood and has watched grow into a successful lawyer like herself, and Evelyn, who she has loved since they first met. Despite her feelings for Evelyn, Veronica is hesitant to express them for fear of being rejected or causing problems within the family dynamic."],
    ["Xia", 39,im.Scale("images/UI/xiaprofile.png", 170, 190), "images/UI/xiaprofile.png", "Xia Watanabe is a fierce and skilled woman who has dedicated her life to the art of wing chun, which she learned to protect her loved ones. At 43 years old, Xia resides in Osaka with her father, and longs for her family to be reunited once again. She is deeply caring and always puts the needs of others before her own. Xia has a daughter named Natsuko, and is happily married to Ichigo.\n\nDespite her strength and confidence, Xia harbors a deep-seated hatred for John due to his mistreatment of her sister, Mia. However, she endures his presence for the sake of her family. Xia is emotionally stable and resolute, but becomes vulnerable and defensive when it comes to Ichigo, who loves her unconditionally."],
    ["Mia", 36, im.Scale("images/UI/Miaprofile.png", 170, 190), "images/UI/Miaprofile.png", "Mia Watanabe/Hall is a 40-year-old Japanese woman who moved to New York after marrying Jonathan Hall. She is a kind and caring person who loves her daughters and wants the best for them. Despite the challenges of her marriage to Jonathan, Mia has always put her daughters first and tried to create a happy home for them.\n\nMia often feels torn between her Japanese heritage and her life in New York, and she struggles with feelings of guilt and a sense of not belonging. She misses her family in Japan but fears they may reject her for leaving, and this weighs heavily on her mental health.\n\nDespite her struggles, Mia is a resilient person who keeps pushing forward to make a better life for her daughters. She is determined to create a better future for them, even if it means sacrificing her own happiness in the process."],
    ["Keisuke", 25, im.Scale("images/UI/Keisukeprofile.png", 170, 190), "images/UI/Keisukeprofile.png", "Keisuke Takahashi is a successful CEO of an esteemed company in Osaka, Japan. Despite his many accomplishments, there is a deep sense of loneliness that lingers within him. The cause of this feeling can be traced back to his childhood when he met a young girl named Kiara. They instantly connected and spent every moment together until Kiara left to go back home.\n\nKeisuke has been unable to forget about her and has never been able to love anyone else. He often thinks about the moments they shared and wonders where Kiara is now. Even though he is financially well off, he feels like something is missing in his life.\n\nDespite his success, Keisuke is riddled with self-doubt and depression. He is haunted by the thought that he wasn't good enough for Kiara, which led to her leaving. He longs to reconnect with her but is afraid that it's too late and she has moved on.\n\nOne of Keisuke's greatest desires is to start a family and have a normal life with someone he loves. But until he finds Kiara, he feels like he will never truly be complete. The memory of Kiara is a constant reminder of what could have been, and he wonders if fate will ever bring them back together."],
    ["Jennifer", 32, im.Scale("images/UI/jenniferprofile.png", 170, 190), "images/UI/jenniferprofile.png", "Jennifer Serkis is an infamous lawyer known for her skills in defending clients in high-profile cases. She's considered one of the best lawyers in the country and will stop at nothing to win a case.\n\nJennifer is a caring person outside the courtroom, but inside, she's cold and ruthless. Her father's murder at the hands of a mob has made her emotionally hardened, and the unrequited love she had for Mason, who fell for someone else, has only added to her bitterness.\n\nJennifer is highly secretive about her personal life, but rumors abound that she has connections with people in the jury and judges, which she may use to gain an advantage in court."],
    ["Azumi", 22, im.Scale("images/UI/azumiprofile.png", 170, 190), "images/UI/azumiprofile.png", "Azumi Hazashi is a 22-year-old Japanese woman who lost her parents at a young age and was subsequently raised by her uncle, Sato Hazashi. Due to her tragic past, Azumi has developed a fear of trusting others and tends to keep to herself. She values kindness above all else and despises lies, as honesty is very important to her. Azumi is a mature and elegant individual who is known for her calm demeanor and reserved personality.\n\nShe currently resides in Osaka, Japan, where she works as an English teacher at a local school. Azumi is also a lesbian, which adds an extra layer of complexity to her life. Despite her reservations, Azumi strives to build meaningful connections with those around her, though she must overcome her fear of trusting others to do so."],
    ["Jake", 26, im.Scale("images/UI/jakeprofile.png", 170, 190), "images/UI/jakeprofile.png", "Jake Watson is a 25-year-old man who has experienced a lot of hardship in his life. His father passed away from a drug overdose, leaving Jake as the sole child to his mother. His mother, unfortunately, has terminal cancer and requires expensive medical care. Jake is a good person at heart, but due to his circumstances, he often has to do things that aren't considered ethical. He works as a private investigator for clients, using his skills to solve problems and make ends meet for his family.\n\nDespite his profession, Jake hates what he does and finds it challenging to balance work and life. However, his love and appreciation for his mother drive him to continue working as hard as he can, even if it means going beyond what is legal or ethical. He's aware of the consequences of his actions, but he's willing to take the risk to ensure that his mother gets the care she needs.\n\nJake's ultimate goal is to save his mother's life and provide her with a comfortable lifestyle, which he believes she deserves. He's willing to do anything to achieve this goal, but he's also aware of the toll it takes on him mentally and emotionally. Despite the challenges he faces, he hopes to one day settle down and live a normal life, free from the burdens of his current profession."],
    ["John", 40,im.Scale("images/UI/johnprofile.png", 170, 190), "images/UI/johnprofile.png", "Jonathan Hall is a wealthy businessman based in New York, renowned for his power and influence among the city's elite. He is known to have ties to the underworld, which has further solidified his reputation as an individual not to be trifled with. Jonathan's success and power have led him to develop a strong sense of ego and a desire to always be on top. He has a fragile self-image, which makes him prone to lash out when he feels threatened or challenged.\n\nUnfortunately, this fragile ego has also led to him becoming mentally abusive towards his wife Mia and their two daughters, Kiara and Evelyn. Despite his wealth and power, Jonathan's personal life has been plagued by turmoil and controversy. He has been accused of multiple instances of harassment and blackmail, which have further eroded his reputation.\n\nJonathan is 46 years old, and while he may appear to have everything a person could want on the surface, his actions and behavior reveal a much darker side to his personality."],
    ["Lana", 21,im.Scale("images/UI/lanaprofile.png", 170, 190), "images/UI/lanaprofile.png", "Lana Movesesian is a 22-year-old socialite from one of the most influential families in New York. Her mother, Elizabeth, is the CEO of a major pharmaceutical company, and Lana has always lived a life of luxury and privilege. Despite this, Lana has a kind heart and genuinely cares for those she loves.\n\nLana and Kiara were best friends during their time at university, and Lana is one of the few people who know that Kiara is still alive. She has kept in contact with Kiara, even though most of their memories of each other have been lost. Lana's outgoing personality often makes her the life of the party, but she also has a more serious and caring side that she reserves for her closest friends.\n\nLana had feelings for Damian during their university days, but she stepped back when she learned that he and Kiara were together. Now that Kiara is gone, Lana wants to help Damian move on and find happiness. She knows that he and Kiara had a special connection, but she also believes that Damian deserves to find love again. Despite her good intentions, Lana is often judged by society for her partying lifestyle. However, those who truly know her understand that she has a kind heart and is always willing to help those in need."],
    ["Natsuko", 21, im.Scale("images/UI/natsukoprofile.png", 170, 190), "images/UI/natsukoprofile.png", "Natsuko Watanabe is a young woman who is currently pursuing a degree in medicine at Osaka University. She is 21 years old and is the daughter of Xia, making her Kiara's cousin. Unlike her mother, Natsuko is emotionally sensitive and often puts others' needs before her own. She has a kind heart and always strives to make her family members happy.\n\nDespite having her memories of Kiara erased, Natsuko still knows what happened to her cousin and hopes for her safe return. She longs for a united family and fears upsetting her mother, who can be quite overbearing at times.\n\nNatsuko has always been focused on her studies and has never had time for romantic relationships. However, she cares deeply for her friends and is always there to support them. She is particularly close to Damian, whom she trusts as a friend and confidant. Knowing what happened with Kiara, Natsuko wants to help Damian move on and find happiness"],
    ["Valentina", 23, im.Scale("images/UI/valentinaprofile.png", 170, 190), "images/UI/valentinaprofile.png", "Valentina Parker is a tech-savvy 22-year-old girl who is passionate about ethical hacking. She and Kiara were good friends during their university days, and she also knew Damian, though they weren't as close. When she heard about Kiara's supposed death, she couldn't believe it, knowing that John was capable of manipulating the truth. Valentina doesn't want anyone, including Damian and Kiara, to suffer due to John's deceitful ways, but she finds it challenging to help them from a distance.\n\nDespite being happy with her life, Valentina often finds herself reminiscing about the good old days with her friends at university. She's engaged to Nick, whom she loves deeply, and Aiden is her mentor, teaching her the ins and outs of hacking. Valentina is a strong-minded person, but she's also prone to feeling vulnerable when her loved ones are in trouble. She wants nothing more than to help her friends and keep them safe, but she struggles to find the best way to do so without putting herself or her loved ones in danger."],
    ["Evelyn", 27, im.Scale("images/UI/evelyn profile.png", 170, 190), "images/UI/evelyn profile.png", "Evelyn Hall, the older daughter of Mia and John, is a strong-willed and independent woman at the age of 26. She moved out of her family's home at the age of 16, after being assaulted by her father. This traumatic event has caused her to develop a distrust of society and struggle with mental health issues.\n\nEvelyn only trusts two people in her life: her friend Veronica and her younger sister Kiara. However, Kiara has been away from her for the past 10 years, causing Evelyn to feel a great sense of loss and loneliness.\n\nEvelyn has attempted to reconnect with her family, but as long as John remains in the picture, it seems impossible. Despite her own struggles, she desires for her family to be okay. Amidst all of this, Evelyn has developed feelings for Veronica, but feels too emotionally unstable to pursue a relationship with her."],
    ["Damian", 25,im.Scale("images/UI/damianprofile.png", 170, 190), "images/UI/damianprofile.png", "Damian Boyd, a 24-year-old living in Harlem, is a man of unwavering determination and a strong moral compass. Despite the risks, he always tries to do the right thing, making him a highly respected figure in the community. \n \nDamian was a brilliant student at university and now runs his own coaching institute, helping others achieve their goals.\n\nTo the outside world, Damian appears to be a young man with a bright future ahead of him. But beneath the surface lies a deep pain and heartache that he has kept hidden for years. You see, Damian's true motivation for his success is his love for Kiara, his former girlfriend from university.\n\nWhen Kiara was involved in a terrible accident that left her in a coma, Damian was devastated. He was told that she had died in the crash, which shattered his world. Unbeknownst to him, Kiara survived, but her memories were erased, leaving her with no recollection of Damian.\n\nDespite his success, Damian's life has been incomplete without Kiara. He struggles to move on, constantly haunted by the thought of what could have been.Despite not knowing the truth, he's remained loyal to her memory and continues to work hard in the hopes of making her proud. Although he's still processing his grief, Damian is committed to making a difference in his community. He's determined to live a life that would make Kiara proud, even if he can never be with her again."],
    ["Daichi", 55,im.Scale("images/UI/Daichi.png", 170, 190), "images/UI/Daichi.png", "Daichi Nakayama, affectionately known as Daichi-san, is an esteemed and revered figure in the local Shinji district of Osaka. As the owner of a quaint tea shop, he has spent decades crafting the perfect blend of traditional teas, captivating the palates of both locals and visitors alike. With his gentle demeanor and wise eyes that hold a wealth of experience, Daichi-san commands respect from all who encounter him.\n\nDespite his advanced age, Daichi-san possesses a remarkable vitality and spirit. It is whispered among the locals that there is much more to him than meets the eye. Stories of his mysterious past have circulated throughout the community, but the details remain shrouded in secrecy. Few are aware of the profound influence he has had on the lives of others, particularly the transformation of Xia, a renowned martial artist, who owes her formidable skills to his tutelage.\n\nWithin the tranquil walls of his tea shop, Daichi-san not only serves fragrant teas but also imparts his wisdom and life lessons to those who seek his guidance. Many come seeking solace, advice, or simply a comforting word from the sage-like figure. Daichi-san's words possess a profound depth, reflecting a life well-lived and the hardships overcome."],
    ["Rin Haru", 20,im.Scale("images/UI/rin.png", 170, 190), "images/UI/rin.png","Rin Haru is a vibrant and free-spirited young woman who recently graduated as a scholar in New York, embarking on a new chapter in her life. Unlike many others, Rin is refreshingly open about her sexuality and embraces it without hesitation, unafraid to express herself authentically. She possesses a fearless nature, often speaking her mind without worrying about societal judgments or expectations.\n\nRin's upbringing and her relationship with her parents have significantly influenced her personality. Her father, Jonathan, instilled in her an open-minded perspective, fostering a sense of acceptance and individuality. This characteristic sets her apart from the crowd and makes her an advocate for personal freedom and self-expression.\n\nHowever, Rin's relationship with her mother is complicated. Her mother holds deep resentment towards Jonathan due to a past betrayal, resulting in their divorce and Jonathan's absence from their lives. As a daughter yearning for the love and presence of a father figure, Rin navigates her emotions in the absence of a stable paternal influence. This absence fuels her determination to enjoy life to the fullest, seeking adventure and spontaneity while also striving for personal growth.\n\nWhile Rin's current focus is on embracing her newfound independence and having fun, she recognizes that settling down may become a desire in the future." ],
    ["Sachiko", 55,im.Scale("images/UI/sachiko.png", 170, 190), "images/UI/sachiko.png", "Sachiko Haru is a mature Japanese woman who was born in Hokkaido and has led a tumultuous life, marred by a series of unexpected events. Initially, she believed she had found the perfect partner in Jonathan, someone she loved deeply. However, she soon discovered that Jonathan had been leading a double life, simultaneously maintaining relationships with both Sachiko and her friend Mia. This shocking revelation shattered Sachiko's world and left her grappling with complex emotions.\n\nThe subsequent legal proceedings surrounding the situation granted Sachiko a significant sum of money. While the financial windfall provided some form of recompense, it did little to assuage the emotional pain she endured. Sachiko's experiences have taken a toll on her mental health, leading her to battle depression and other related issues.\n\nSachiko yearns for her children to break free from the negative influence of their father and forge their own paths. Her primary focus is on providing them with a supportive and nurturing environment, shielded from the emotional scars of the past. In terms of her own romantic future, Sachiko remains uncertain. While she desires love and companionship, the betrayal she experienced has caused deep-seated trust issues that complicate her relationships and her sexual life."],
    ["Elizabeth", 34,im.Scale("images/UI/Elizaberh.png", 170, 190), "images/UI/Elizaberh.png","Elizabeth Movesesian is a highly successful and influential woman in New York, commanding both the headship of an elite family and the leadership of a prominent pharmaceutical giant. She stands as a shining example of an independent and accomplished woman who has carved her own path to success.\n\nDespite her adventurous nature, Elizabeth is happily married and values the stability and love that her relationship brings. While she embraces moments of playfulness, she sets clear boundaries, ensuring that her actions remain within the bounds of mutual respect and consent. Deeply committed to her family, Elizabeth's greatest priority is the well-being and safety of her daughter, Lana. Elizabeth navigates the challenges of parenthood, particularly in dealing with Lana's rebellious streak, with a mixture of understanding, guidance, and unwavering love.\n\nElizabeth's refusal of Jonathan's advances in the past speaks volumes about her character and integrity. She is not easily swayed by superficial charm or material wealth, valuing genuine connections and personal principles above all else. Elizabeth possesses a wealth of knowledge about the city and its workings, making her a valuable resource for those who seek her assistance. She willingly offers her support and guidance, particularly to those who are less fortunate, using her position and influence to uplift and empower those beneath her."],
    ["Rose", 20,im.Scale("images/UI/rose1.png", 170, 190), "images/UI/rose1.png","Rose Kenner, also known as Rosalind, is a compassionate and genuine young woman who hails from Boston but spent her formative years in the Middle East. Driven by a strong sense of familial responsibility, she made the decision to move to Japan to provide financial support for her brother's education.\n\nDespite her initial venture into Japan as a means of supporting her brother, Rose found success in an unexpected field. What started as a simple hobby eventually blossomed into a thriving salon business.\n\nIn matters of relationships, Rose exudes a dominant yet tender demeanor. She embraces her bisexuality and holds a preference for women while remaining open-minded towards men. Honesty is of utmost importance to Rose, and she values open communication and trust in her connections. As she plans to settle in Japan once her brother graduates, Rose hopes to find a loving partner to share her life with." ],
    ["Asa", 21,im.Scale("images/UI/Asa.png", 170, 190), "images/UI/Asa.png","Asa Furuta, a vibrant and helpful young woman, was born and raised in Japan. With a cheerful disposition and a natural inclination to welcome new people into her life, Asa radiates familiarity.\n\nArt holds a special place in Asa's heart, and she has immersed herself in creative pursuits. While working at the salon, she primarily assumes the role of a receptionist, utilizing her artistic sensibilities to create a welcoming atmosphere. Asa's deep appreciation for beauty and aesthetics shines through in her interactions with clients and colleagues alike.\n\nShe prefers to focus on spreading joy and maintaining a positive outlook, often shielding herself from the harsher realities of life.\n\nAsa's unique struggle with a split personality or multiple personality disorder is a problem in her life. At times, a bolder and more assertive personality emerges, causing a duality within her being. This internal conflict can pose challenges as she navigates her interactions and relationships. Despite this complexity, Asa's primary persona is known for her sweetness and kindness, which endears her to those who know her." ],
    ["Ayane", 24,im.Scale("images/UI/Ayane.png", 170, 190), "images/UI/Ayane.png","Ayane Takahashi is a kind-hearted young woman with a strong family background, born and raised in Osaka alongside her brother Keisuke. Growing up in a loving and supportive family, Ayane carries herself with a stoic demeanor, often maintaining a calm and composed exterior. However, beneath her reserved nature, she harbors deep care and concern for her brother, who fell into a state of depression following the loss of Kiara.\n\nAyane is known for her straightforwardness and honest communication. She prefers to address matters directly, saying what needs to be said without beating around the bush. She values sincerity and genuine connections with others. While Ayane identifies as demisexual, not experiencing sexual attraction without a strong emotional bond, she appreciates and welcomes authentic affection from both genders.\n\nAyane's story revolves around inner strength, and the power of connections. Her steadfastness, coupled with her empathetic nature, makes her a reliable and grounding presence for those around her." ],
    ["Patricia", 21,im.Scale("images/UI/Patricia.png", 170, 190), "images/UI/Patricia.png","Patricia Arundel, a young woman hailing from Queens, New York, has endured a challenging life filled with loss and resilience. Orphaned at a young age due to her parents' battle with cancer, she spent her formative years in a foster home until a loving family welcomed her into their lives. Despite finding a new family, Patricia has experienced a sense of estrangement from her biological relatives and has faced adversity in the world around her.\n\nCurrently employed by billionaire Jonathan, Patricia works diligently to support her newfound family, whom she loves deeply. Unfortunately, Jonathan's controversial reputation casts a shadow over Patricia's own character, leading many to perceive her as a morally compromised individual who would do anything for money. However, this perception couldn't be further from the truth. Patricia maintains her integrity and has never been involved in any questionable activities.\n\nWhen confronted with the terrible consequences of Jonathan's actions, Patricia takes it upon herself to aid the victims, offering support and assistance. For instance, she lends a helping hand to Sachiko following her divorce, among other acts of kindness.\n\nPatricia yearns for a meaningful bond or relationship. The constant barrage of judgment and mistreatment from the world weighs heavily on her, and she finds solace in the idea of having someone to lean on, someone who can provide her with emotional support during trying times." ],
    ["Mason", 39,im.Scale("images/UI/Mason.png", 170, 190), "images/UI/Mason.png", "Mason Majors, born and raised on the streets of Harlem, has experienced a humble upbringing alongside his cousin Veronica. Both Mason and Veronica faced a tumultuous home environment, enduring repeated abusive behavior that prompted them to leave their home at an early age. Determined to rise above their circumstances, they pursued careers in law, becoming accomplished lawyers.\n\nWhile Veronica remained focused on her professional life and personal growth, Mason's college years were not marked by the same level of dedication and commitment. However, he persevered, driven by his desire to win the heart of the girl he had always admired, Mia. During those times, Mia's attention was scarce, but she displayed a kinder side towards Mason, likely due to the empathy she felt for him in light of the mistreatment he endured from others.\n\nToday, Mason stands as one of the most successful lawyers in New York State, co-managing a prestigious law firm alongside his cousin Veronica. He deeply loves and cares for Veronica, considering her not only a family member but also a close confidante and partner in their legal endeavors. Mason's devotion to his cousin extends to Mia, who has faced a devastating fate in her marriage to Jonathan. Mason holds no ill will towards anyone else, but he harbors a strong resentment towards Jonathan for the pain he caused Mia.\n\nMason's primary focus is on ensuring Mia's happiness and well-being. He desires nothing but the best for her, supporting her through the aftermath of her tumultuous relationship. Deep down, Mason still holds a flicker of hope that he may one day reconcile with Mia, should circumstances allow. His genuine care and unwavering commitment to those he loves shape his journey, driving him to protect and uplift those who have experienced hardship. Mason's story is one of resilience, loyalty, and the enduring pursuit of love and justice."]
]
