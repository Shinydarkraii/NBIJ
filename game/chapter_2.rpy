label chap_2_prelude:
    "Before chapter 2 please re-select the choices you selected in chapter 1"


    scene bg mumgropdecide with dissolve 
    #- >  DID MIA LET THE BELLHOP GROPE HER? +1 corruption
    menu:
        "DID MIA LET THE BELLHOP GROPE HER?"
        "Yes":
            $ mc_stats.adjust_corruption(5)
        "No":
            pass

    scene bg lanadecidegrope with dissolve
    #-> DID LANA LET THE BELLHOP HAVE HIS WAY? +1 corruption
    menu:
        "DID LANA LET THE BELLHOP HAVE HIS WAY?"
        "Yes":
            $ mc_stats.adjust_corruption(5)
        "No":
            pass
    scene bg photoshootleather 8 with dissolve
    #-> DID KIARA DO THE LEATHER COSPLAY? +1 corruption
    menu: 
        "DID KIARA DO THE LEATHER COSPLAY?"
        "Yes":
            $ mc_stats.adjust_corruption(5)
            $ inventory.earn(500)
        "No":
            pass
    scene bg natsugropedecd  with dissolve
    #-> DID NATSU LET THE MOLESTER HAVE HIS WAY? +1 corruption
    menu: 
        "DID NATSU LET THE MOLESTER HAVE HIS WAY?"
        "Yes":
            $ mc_stats.adjust_corruption(5)
        "No":
            pass
    scene valntdamimomscn 15  with dissolve
    #-> DID VALENTINA WATCH DAMIAN’S MOTHER IN SHOWER? +1 corruption
    menu: 
        "DID VALENTINA WATCH DAMIAN’S MOTHER IN SHOWER?"
        "Yes":
            $ mc_stats.adjust_corruption(5)
        "No":
            pass

    "Thank-you for your choices"
    "Please enjoy chapter 2"
    pass

label chap_2_scene_1:
    scene blackscreen
    show titletext "Osaka , Early morning.." with dissolve
    pause 1.0
    window hide
    scene bg chptstrt 1 with Dissolve(0.8)
    pause
    scene bg chptstrt 2 with Dissolve(0.8)
    pause
    scene bg chptstrt 3  with Dissolve(0.8)
    Kiara "Good morning to me.."
    scene bg chptstrt 4 with Dissolve(0.8)
    pause
    scene bg chptstrt 5 with Dissolve(0.8)
    Kiara "Aah! what the-"
    scene bg chptstrt 6 with Dissolve(0.8)
    Kiara "Wh- Who are you? what are you doing in my r-"
    scene bg chptstrt 7  with Dissolve(0.8)
    Nobi "Good morning Kiara-San , Master Xia ordered to deliver you Tea"
    Kiara "Um.."
    scene bg chptstrt 8  with Dissolve(0.8)
    Kiara "(Eh , is that really how they deliver tea?)"
    scene bg chptstrt 9  with Dissolve(0.8)
    Kiara "Um , could you please next time knock before entering or leave it outside? You actually scared me"
    scene bg chptstrt 10  with Dissolve(0.8)
    Nobi "My humblest of apologies Kiara-san , i made a mistake" 
    Kiara "Hah chill it's okay , just.. yeah be careful next time"
    scene bg chptstrt 11  with Dissolve(0.8)
    Kiara "Also am i dreaming or you look like bruce-"
    scene bg chptstrt 12  with Dissolve(0.8)
    Nobi "I am glad you think of me as the man of your dreams kiara-san , you're beautiful as well"
    Kiara "Wait no , that's not what i meant-" 
    scene bg chptstrt 13  with Dissolve(0.8)
    Nobi "However I unfortunately cannot be with anyone as i must focus on improvement of my strength"
    Kiara "(Oh goly jee what a loss for me) Well-"
    scene bg chptstrt 14   with Dissolve(0.8)
    Nobi "I must empty my mind , Be like water flowing"
    scene bg chptstrt 15   with Dissolve(0.8)
    Nobi "But strong as a stone , immovable"
    scene bg chptstrt 16  with Dissolve(0.8)
    Kiara "Uh.. right , Well thanks for the tea you may leave now." 
    scene bg chptstrt 17  with Dissolve(0.8)
    Nobi "Thank you for accepting my apology Kiara-san , you are truly kind"
    Kiara "( What? i only said it's fine )"
    scene bg chptstrt 18  with Dissolve(0.8)
    Nobi "Have a wonderful day, sayonara"
    scene bg chptstrt 19  with Dissolve(0.8)
    Kiara "Heh , yeah you too.. peace" 
    scene bg chptstrt 20  with Dissolve(0.8)
    Kiara "Well that was... something." 
    scene bg chptstrt 21  with Dissolve(0.8)
    Kiara "Ahh , that was a good sleep!" 
    scene bg chptstrt 22  with Dissolve(0.8)
    Kiara "( Today's the first day i start changing my life.. I'm excited )"  
    scene bg chptstrt 23   with Dissolve(0.8)
    Kiara "Okay , I think i'll go talk to auntie first"
    scene bg chptstrt 24  with Dissolve(0.8)
    Kiara "Or maybe i should talk to mom?.. no she must be busy now" 
    scene bg chptstrt 25  with Dissolve(0.8)
    Kiara "*Phone rings* Hm? , Oh it's lana"  
    scene bg chptstrt 26   with Dissolve(0.8)
    Kiara "Hey lana! , good morning" 
    Lana "Good morning love , did you sleep good?" 
    scene bg chptstrt 27  with Dissolve(0.8)
    Kiara "I did , did you reach safely?"
    Lana "Yeah we're just getting to the hotel now" 
    scene bg chptstrt 28  with Dissolve(0.8)
    Kiara "We? did auntie liz come?" 
    Lana "Oh , um no one of my friends is with me so yeah"
    scene bg chptstrt 29  with Dissolve(0.8)
    Lana "Anyway when are you free? Would love to catchup , also how did my dress fit you?" 
    scene bg chptstrt  30  with Dissolve(0.8)
    Kiara "Dress was.. interesting , but Actually i'm kinda busy for the entire day today . If you want we can on the weekend"
    Lana "Sounds good to me! , so *Background noises* Um .. i gotta go for now you know jet lag and stuff , lets talk in evening?" 
    scene bg chptstrt 31  with Dissolve(0.8)
    Kiara "Oh um yeah no problem , take care" 
    Lana "You too babe , laters"
    scene bg chptstrt 32  with Dissolve(0.8)
    Kiara "Okay , lets meet auntie"
    scene bg chptstrt 33  with Dissolve(0.8)
    Kiara "Auntie?"
    scene bg chptstrt 34  with Dissolve(0.8)
    Kiara "Auntie? She's not even here?"
    scene bg chptstrt 35  with Dissolve(0.8)
    Kiara "I love this design , way more elegant than the modern architecture"
    scene bg chptstrt 36  with Dissolve(0.8)
    Kiara "Auntie?.. Hm"
    scene bg chptstrt  37  with Dissolve(0.8)
    Kiara "Talk about being sunkissed.. mmm so nice"
    scene bg chptstrt 38   with Dissolve(0.8)
    Kiara "Auntie? you here?"
    scene bg chptstrt 39  with Dissolve(0.8)
    Kiara "Wow.."
    scene bg chptstrt 40  with Dissolve(0.8)
    pause
    scene bg chptstrt 41   with Dissolve(0.8)
    pause
    scene bg chptstrt 42  with Dissolve(0.8)
    Xia "Kiara , come sit next to me"
    Kiara "Yes.."
    scene bg chptstrt 43  with Dissolve(0.8)
    Kiara "You do this everyday?"
    Xia "Was a bit late today , I usually finish before 9"
    scene bg chptstrt 44  with Dissolve(0.8)
    Xia "Did you sleep well sweetheart? , had nice dreams i hope"
    Kiara "I did.. thank you auntie"
    scene bg chptstrt 45  with Dissolve(0.8)
    Kiara "So this is how you stay so fit.. no wonder"
    scene bg chptstrt 46  with Dissolve(0.8)
    Xia "Well yoga cleans the mind , what keeps me fit is martial arts" 
    scene bg chptstrt 47  with Dissolve(0.8)
    Kiara "Martial arts?.. Like fighting?"
    Xia "I would call it self defence or practice rather , we only fight when needed"
    Kiara "Oh wow, I'd love to learn"
    scene bg chptstrt 48  with Dissolve(0.8)
    Xia "Well come then , let us begin"
    Kiara "Um.. what? no i mean i'm flexible but no way i can just start learning this stuff"
    scene bg chptstrt 49  with Dissolve(0.8)
    Xia "You can , Do not worry just follow as i say.. and we all start somewhere don't we?"
    Kiara "Um..(What do i do?)"
    #---------- scene bg chptstrtdcd - Choice
    #Choice  1 - Train with her - Aunt fondness 0 / doesn't change
    #Choice 2 - Don't train  - Aunt fondness +1 , Strength + 5
    menu:
        "Train with her":
            jump .part_1
        
        "Don't Train":
            jump .part_2

    label .part_1:

        scene bg trngys 1  with Dissolve(0.8)
        Kiara "Well I'd love to but i don't think i can do it in a baggy shirt , I don't have all of my clothes here either" 
        scene bg trngys 2  with Dissolve(0.8)
        Xia "I've taken care of that do not worry , check the storeroom" 
        Kiara "Wh- really? Okay"
        scene bg trngys 3  with Dissolve(0.8)
        Xia "(It's like having a second daughter , she's differnt yet so similar)"
        scene bg trngys 4  with Dissolve(0.8)
        Kiara "Wow..this is"
        scene bg trngys 5  with Dissolve(0.8)
        Kiara "Auntie ,  this is so cool!"
        Xia "Well wear it and Show me? come outside"
        scene bg trngys  6  with Dissolve(0.8)
        pause
        scene bg trngys 7  with Dissolve(0.8)
        Xia "Fits you better than i thought actually"
        scene bg trngys 8   with Dissolve(0.8)
        Kiara "It's very comfortabble.. but pretty cool too"
        Xia "Well I'm glad you think so , So let us begin?"
        scene bg trngys 9  with Dissolve(0.8)
        Xia "Just follow me"
        scene bg trngys 10 with Dissolve(0.8)
        pause
        scene bg trngys 11  with Dissolve(0.8)
        Kiara "Here i thought i'd need a gym , this is hard enough auntie"
        Xia "You're doing better than most at start , trust me"
        scene bg trngys 12  with Dissolve(0.8)
        Kiara "Uh , I don't think my balance is good enough for that"
        Xia "Just balance your leg and body weight"
        scene bg trngys 13  with Dissolve(0.8)
        Kiara "Aah! *Gasp*"
        scene bg trngys 14  with Dissolve(0.8)
        Xia "Kiara!"
        scene bg trngys 15  with Dissolve(0.8)
        pause
        scene bg trngys 16  with Dissolve(0.8)
        Xia "I'm so sorry , are you alright honey?"
        Kiara "Oh , yeah.. um thanks"
        scene bg trngys 17   with Dissolve(0.8)
        Xia "I believe that's enough for today.. wouldn't you agree?"
        Kiara "Yes.. Um , I can stand now it's okay"
        scene bg trngys 18   with Dissolve(0.8)
        Xia "I am glad you're here , i want you to know that"
        scene bg trngys 19  with Dissolve(0.8)
        Kiara "(She is beautiful..) Y-yes auntie , i am glad you're around me too."
        scene bg trngys 20  with Dissolve(0.8)
        Xia "Do not worry , failures only make us better , you'll improve with time"
        Kiara "I know , I got a great teacher after all heh"
        scene bg trngys 21  with Dissolve(0.8)
        Kiara "Well um , I'll get going then auntie"
        Xia "Yes of course , got a big day ahead of you , take care"
        scene bg trngys 22  with Dissolve(0.8)
        Kiara "(That was kinda fun)"
        Xia "(I'll make sure you're stronger this time kiara.. outside and inside)"

        #stat increase
        $ xia_fond.adjust_fondness()
        $ mc_stats.adjust_strength(1)
        jump .part_3

    label .part_2:
    #IF CHOICE 2  
        scene bg trngsefrstno 1  with Dissolve(0.8)
        Kiara "Ah can we do this perhaps later ? I have a big day ahead of me and i don't want to be late.. I'm sorry if i'm rude auntie" 
        scene bg trngsefrstno 2  with Dissolve(0.8)
        Xia "No , not at all honey . We'll have enough time , i wish you the best for today , stay safe okay?"
        Kiara "I will , Thank you auntie!"
        jump .part_3

    label .part_3:
        scene bg chptstrt 50  with Dissolve(0.8)
        Kiara "Haaa , okay i hope the water isn't cold"
        scene bg chptstrt 51 with Dissolve(0.8)
        pause
        scene bg chptstrt 52  with Dissolve(0.8)
        Kiara "Oh This one has a warm valve here , how did i miss this before?"
        scene bg chptstrt 53  with Dissolve(0.8)
        Kiara "Mmm , nothing like a good shower to start the day"
        scene bg chptstrt 54  with Dissolve(0.8)
        pause
        scene bg chptstrt 55  with Dissolve(0.8)
        pause
        scene bg chptstrt 56 with Dissolve(0.8)
        pause
        scene bg chptstrt 57  with Dissolve(0.8)
        Kiara "Definitely needed that, lets go."
        scene bg chptstrt 58 with Dissolve(0.8)
        $ renpy.end_replay()
        pause
        scene bg chptstrt 59  with Dissolve(0.8)
        Natsuko "Mom , why can't we take in a cat"
        Xia "You won't take care of her properly , you know that too"
        scene bg chptstrt 60  with Dissolve(0.8)
        Natsuko "Well we both could take turns on it"
        scene bg chptstrt 61  with Dissolve(0.8)
        Xia "Absolutely not . You have to take full responsiblity , only then would i consider it" 
        scene bg chptstrt 62  with Dissolve(0.8)
        Natsuko "Okay , I'll share that with kiara then"
        Xia "Hm , maybe then i'm okay with it."
        scene bg chptstrt 63  with Dissolve(0.8)
        Natsuko "You're really happy she's here too right?"
        scene bg chptstrt 64  with Dissolve(0.8)
        Xia "I am natsu she needs family , till mia's situation resolves we both will do what we can"
        scene bg chptstrt 65 with Dissolve(0.8)
        pause
        scene bg chptstrt 66  with Dissolve(0.8)
        Kiara "I'm happy i'm here too"
        scene bg chptstrt 67  with Dissolve(0.8)
        Natsuko "Hm? Ah-"
        scene bg chptstrt 68  with Dissolve(0.8)
        Xia "Kiara! Welcome"
        scene bg chptstrt 69  with Dissolve(0.8)
        Natsuko "Wow , look at you!"
        Xia "You look wonderful honey" 
        scene bg chptstrt 70  with Dissolve(0.8)
        Natsuko "I'd hire you alone on that fashion choice"
        Kiara "Thanks natsu"
        scene bg chptstrt 71   with Dissolve(0.8)
        Xia "It suits you very well , sorry if i sound like a broken record here"
        Kiara "No auntie i appreciate it , I just am a bit nervous"
        scene bg chptstrt 72    with Dissolve(0.8)
        Natsuko "Nervous on what , you got this sis" 
        scene bg chptstrt 73   with Dissolve(0.8)
        Kiara "Heh , Let's hope you're correct on that"
        scene bg chptstrt  74  with Dissolve(0.8)
        Natsuko "So , mind if i go with you then?"
        Kiara "Oh i mean sure , but it might take me alot of time are you okay with that?"
        scene bg chptstrt  75 with Dissolve(0.8)
        pause
        scene bg chptstrt 76  with Dissolve(0.8)
        pause
        scene bg chptstrt 77  with Dissolve(0.8)
        Natsuko "Ah.. right"
        scene bg chptstrt 78  with Dissolve(0.8)
        Kiara "Auntie , are you okay with me & natsu going together?"
        Xia "Oh honey actu-"
        scene bg chptstrt 79  with Dissolve(0.8)
        Natsuko "Actually i have to attend a funeral.. " 
        scene bg chptstrt 80  with Dissolve(0.8)
        Natsuko "I'm so sorry i forgot before asking , Will you be okay?"
        scene bg chptstrt  81  with Dissolve(0.8)
        Kiara "Of course , I mean i have to be on my feet too , don't worry about it"
        scene bg chptstrt 82  with Dissolve(0.8)
        Kiara "Auntie , rest of my clothes will arrive today could you please recieve them?"
        Xia "Sure honey , hold on"
        scene bg chptstrt 83  with Dissolve(0.8)
        Xia "NOBI-san!"
        scene bg chptstrt  84  with Dissolve(0.8)
        Nobi "Master , you called me?"
        scene bg chptstrt 85  with Dissolve(0.8)
        Xia "Kiara here would have her clothes delivered today , would you be so kind to recieve them? I have to go with natsuko"
        Nobi "Yes master , leave it to me"
        scene bg chptstrt  86  with Dissolve(0.8)
        Natsuko "Thanks nobi , morning!"
        scene bg chptstrt  87  with Dissolve(0.8)
        Nobi "Uhm.. welcome"
        scene bg chptstrt 88  with Dissolve(0.8)
        Kiara "Psst , what was that about?"
        scene bg chptstrt  89    with Dissolve(0.8)
        Natsuko "I don't know , he's always this way to me" 
        scene bg chptstrt  90  with Dissolve(0.8)
        Xia "Are you  also okay with helping me with groceries? We can continue training then too"
        Nobi "Rest assured master, It'd be an honor"
        scene bg chptstrt 91  with Dissolve(0.8)
        Kiara "Auntie , I'll get going then"
        Xia "Yes, stay safe honey and don't lose the phone this time hah"
        scene bg chptstrt  92   with Dissolve(0.8)
        Natsuko "Do you mind if i drop you to the gate? I'm free anyway"
        Kiara "Why would i say no , come"
        scene bg chptstrt 93  with Dissolve(0.8)
        pause
        scene bg chptstrt  94  with Dissolve(0.8)
        Xia "(This is all i need , I love you both)"
        scene bg chptstrt 95  with Dissolve(0.8)
        Natsuko "So yeah like mum said , be in touch okay and don't lose the phone"
        Kiara "I won't , i promise haha"
        scene bg chptstrt  96  with Dissolve(0.8)
        Natsuko "Best of luck , you'll do great i'm sure"
        Kiara "Thanks for the faith in me , i need it now more than ever"
        scene bg chptstrt  97  with Dissolve(0.8)
        Natsuko "I'll always have faith in you , please be safe okay? if you need anything just call me" 
        scene bg chptstrt  98  with Dissolve(0.8)
        Kiara "I will , don't worry too much . You too have a great day okay?"
        scene bg chptstrt  99  with Dissolve(0.8)
        pause
        scene bg chptstrt 100  with Dissolve(0.8)
        Natsuko "(There is so much i want to say but can't.. )"
        scene bg chptstrt 101  with Dissolve(0.8)
        pause
        scene bg chptstrt 102  with Dissolve(0.8)
        Xia "Worried about her?"
        Natsuko "I just want her to be happy mom.."
        scene bg chptstrt 103  with Dissolve(0.8)
        Xia "She will , but we have to give her the space she needs , let her feel independent and strong too"
        scene bg chptstrt 104  with Dissolve(0.8)
        Xia "If things go rough , you and i then will intervene and help her"
        Natsuko "Yes.. We- We will"
        scene bg chptstrt 105  with Dissolve(0.8)
        Xia "Honey.. are you alright? I feel like you're hiding something from me , is something bothering you? "
        scene bg chptstrt  106  with Dissolve(0.8)
        Natsuko "(I can't tell her about damian)"
        scene bg chptstrt 107  with Dissolve(0.8)
        Natsuko "No mom , I just don't want her to go back to that place , so thinking about it makes me sad"
        Xia "We can't control what happens , but we can make sure she's strong enough to face it ."

        

        jump chap_2_scene_2

label chap_2_scene_2:
    scene blackscreen
    show titletext "Taka's shop , abit later.." with dissolve
    pause 1.0
    window hide
    scene bg kiafstcsplay 1 with Dissolve(0.8)
    Taka "Man how long are you delay the order?"
    scene bg kiafstcsplay 2 with Dissolve(0.8)
    Taka "Bro I needed that today , ugh whatever"
    scene bg kiafstcsplay 3 with Dissolve(0.8)
    Kiara "Having a rough day?"
    scene bg kiafstcsplay 4 with Dissolve(0.8)
    Taka "Oh Hey and yeah , thanks for brightning it up by meeting . Nice outfit by the way"
    scene bg kiafstcsplay 5 with Dissolve(0.8)
    Kiara "Thank you , so how was the response on the shoot?"
    Taka "You're gonna love it , come lets discuss it in office"
    scene bg kiafstcsplay 6 with Dissolve(0.8)
    Taka "Trust me , I'm glad i chose you"
    Kiara "Well that sounds like it went well"
    scene bg kiafstcsplay 7 with Dissolve(0.8)
    Taka "Went well ? They loved it! they are like offering multiple shoot deals now since it fit you so well"
    scene bg kiafstcsplay 8 with Dissolve(0.8) 
    Taka "Honestly all of them said it's better than the models they have with expirience"
    Kiara "Oh zip it with the flattery , so i get shares of it too right?"
    scene bg kiafstcsplay 9 with Dissolve(0.8)
    Taka "Hell yeah , I'll get them next week and get it to your account"
    Kiara "Perfect.. so did you talk to your agency friend?"
    scene bg kiafstcsplay 10 with Dissolve(0.8)
    Taka "I did , you need to go to the building in business street i've sent it on your phone , once you go at the office building and they'll give you the locations to give interviews , don't stress too much"
    Kiara "Easy to say , hard to do"
    scene bg kiafstcsplay 11 with Dissolve(0.8)
    Taka "So uh, i do have one more shoot . If you want we can do it , won't take too long plus extra cash hurt nobody"
    Kiara "You're right about that , so what are my options? would like to hear them first"
    scene bg kiafstcsplay 12 with Dissolve(0.8)
    Taka "Perfect , Well one is a movie sponsor or something and other is a game outfit cosplay , 50$ vs 100$ your choice."
    Kiara "Um.. (Which one to do?.. I don't want to wear something skin tight again..)"

    scene bg kiafstcsplaychcrndr with Dissolve(0.8)

    # CHOICE - >
    # Cosplychceone - 50 $ Cosplay ( No corruption  , Money add 50 $ +)
    # Cosplychctwo - 100 $ Cosplay ( +5 corruption , Money add 100 $ + )
    # Cosplychcno - No cosplay today. ( No corruption)
    menu:
        "100$ Cosplay":
            jump .part_1
        "250$ Cosplay":
            jump .part_2
        "No Cosplay":
            jump .part_3

    label .part_1:
        # Cosplychcone - 
        scene bg kiaranrmlcsply 1 with Dissolve(0.8)
        Kiara "I'd prefer the 50$ one , movie outfits sound cool"
        scene bg kiaranrmlcsply 2 with Dissolve(0.8)
        Taka "Cool , get changed , I'll get the setup ready"
        scene bg kiaranrmlcsply 3 with Dissolve(0.8)
        Taka "Ready when you are!"
        Kiara "Yes , give me a minute!"
        scene bg kiaranrmlcsply 4 with Dissolve(0.8)
        Taka "You've seen the movies right?"
        scene bg kiaranrmlcsply 5 with Dissolve(0.8)
        Kiara "You're kidding , Jack's my favorite"
        scene bg kiaranrmlcsply 6 with Dissolve(0.8)
        Taka "Perfect then , Lets get started!"
        scene bg kiaranrmlcsply 7 with Dissolve(0.8)
        Kiara "A elegant pose first"
        scene bg kiaranrmlcsply 8 with Dissolve(0.8)
        Taka "Weild the sword!"
        scene bg kiaranrmlcsply 9 with Dissolve(0.8)
        Taka "Do the thrust with the rapier"
        scene bg kiaranrmlcsply 10 with Dissolve(0.8)
        Taka "Poster pose!"
        scene bg kiaranrmlcsply 11 with Dissolve(0.8)
        Taka "Lets do a side with a smile"
        scene bg kiaranrmlcsply 12 with Dissolve(0.8)
        Taka "Sharpen it by hand , lookin good"
        scene bg kiaranrmlcsply 13 with Dissolve(0.8)
        Taka "Just do a style one , we'll use this as poster"
        scene bg kiaranrmlcsply 14 with Dissolve(0.8)
        Taka "Let's do one without the jacket the material is great!"
        scene bg kiaranrmlcsply 15 with Dissolve(0.8)
        Taka "Annnd that's it , That was great kiara!"

        $ inventory.earn(100)

        jump chap_2_scene_3


    label .part_2:

        #Cosplychcetwo - 
        scene bg kiaracrptcsply 1 with Dissolve(0.8)
        Kiara "100$ sounds good to me , where's the outfit?"                     
        scene bg kiaracrptcsply 2 with Dissolve(0.8)
        Taka "I'll get the setup ready , you'll find it in changing room"
        scene bg kiaracrptcsply 3 with Dissolve(0.8)
        Taka "Ready when you are!"
        Kiara "Ah.. Isn't the skirt a bit short?"
        scene bg kiaracrptcsply 4 with Dissolve(0.8)
        Taka "What ? No it looks fine it's how the character looks too"
        scene bg kiaracrptcsply 5 with Dissolve(0.8)
        Kiara "Uh.. okay sure"
        scene bg kiaracrptcsply 6 with Dissolve(0.8)
        Kiara "I can barely see anything by the way"
        Taka "Yeah it's normal , its future robot remmeber?"
        scene bg kiaracrptcsply 7 with Dissolve(0.8)
        Taka "And it begins , a wide pose!"
        scene bg kiaracrptcsply 8 with Dissolve(0.8)
        Taka "Shy side view"
        scene bg kiaracrptcsply 9 with Dissolve(0.8)
        Taka "Hold the leg up!"
        Kiara "It's a cute outfit for sure"
        scene bg kiaracrptcsply 10 with Dissolve(0.8)
        Taka "Oh yeah.. cute it is heh"
        scene bg kiaracrptcsply 11 with Dissolve(0.8)
        Taka "(Heh , so glad i got the side ground cameras installed , lets enjoy the view now) Kiara keep going , you're doing great!"
        scene bg kiaracrptcsply 12 with Dissolve(0.8)
        Taka "Arm to side with confidence!"
        scene bg kiaracrptcsply 13 with Dissolve(0.8)
        Taka "Backview angle  to and look at camera!"
        scene bg kiaracrptcsply 14 with Dissolve(0.8)
        Taka "Sit down , calm and stoic"
        scene bg kiaracrptcsply 15 with Dissolve(0.8)
        Taka "(Oh man look at curve , I'd bury my face between it)"
        scene bg kiaracrptcsply 16 with Dissolve(0.8)
        Taka "Kiara , lets lose the stockings now , they kinda wanted clear legs too since you have great ones"
        scene bg kiaracrptcsply 17 with Dissolve(0.8)
        Kiara "Um.. okay well , It's for the shoot.. you sure these are not seen by anyone else right?"
        scene bg kiaracrptcsply 18 with Dissolve(0.8)
        Taka "Of course not , don't worry"
        scene bg kiaracrptcsply 19 with Dissolve(0.8)
        Taka "Okay now be the same behind angle but arms on waist!"
        Kiara "(I hope nothing is visible.. this wig is half blinding me)"
        scene bg kiaracrptcsply 20 with Dissolve(0.8)
        Kiara "(Why does this character wear a thong anyway.. video games these days..)"
        Taka "(Oh man , those cameras were worth every penny)"
        scene bg kiaracrptcsply 21 with Dissolve(0.8)
        Taka "(Look at those thighs.. fuck , lets see how the side view is)"
        scene bg kiaracrptcsply 22 with Dissolve(0.8)
        Taka "Stay like that! , I'm trying to get closup face shots too! (Man look at that ass , you're a babe fucking camera isn't looking properly dammit)"
        scene bg kiaracrptcsply 23 with Dissolve(0.8)
        Taka "Alright last one! front and arms to the back at neck"
        scene bg kiaracrptcsply 24 with Dissolve(0.8)
        Taka "(Fuck why does she wear thong in the game.. I almost wanna tear that off) Alright kiara , let's do one without the wig so they know its you!"
        scene bg kiaracrptcsply 25 with Dissolve(0.8)
        Taka "Perfect! that'll be all~"
        $ renpy.end_replay()
        $ mc_stats.adjust_corruption(5)
        $ inventory.earn(250)
        jump chap_2_scene_3

    label .part_3:
        #Cosplychcno - 
        scene bg kiarjctcsplay 1 with Dissolve(0.8)
        Kiara "I'd love to actually but i kinda have a hectic day already , sorry taka" 
        scene bg kiarjctcsplay 2 with Dissolve(0.8)
        Taka "Oh.. well alright , see you tomorrow maybe?"
        scene bg kiarjctcsplay 3 with Dissolve(0.8)
        Kiara "I'll visit but i can't promise , see ya around"
        Taka "Yeah.. see ya (Dammit that gamer outfit would've been a good one)" 
        jump chap_2_scene_3
    return

label chap_2_scene_3:

    #SCENE -  bg mtngAgentWong -
    scene blackscreen
    show titletext "Osaka subway station" with dissolve
    pause 1.0
    window hide
    scene bg mtngwng 1 with Dissolve(0.8)
    Kiara "She was not kidding when she said crowded"
    scene bg mtngwng 2 with Dissolve(0.8)
    Kiara "Oh well , It's just 30 minutes i can stand that long"
    scene bg mtngwng 3 with Dissolve(0.8)
    Kiara "(At least the cabs are air conditioned)" 
    scene bg mtngwng 4 with Dissolve(0.8)
    Kiara "(First time i'm doing something for myself , bit of struggle i can handle)"
    scene bg mtngwng 5  with Dissolve(0.8) 
    pause
    scene bg mtngwng 6  with Dissolve(0.8)
    Molester "Hehe , lets see how white skin feels"
    scene bg mtngwng 7  with Dissolve(0.8)
    Molester "Argh!"
    scene bg mtngwng 8  with Dissolve(0.8) 
    pause
    scene bg mtngwng 9  with Dissolve(0.8)
    AgentWong "(Here you are)"
    scene bg mtngwng 10  with Dissolve(0.8)
    AgentWong "(I'll have to keep a low profile)"
    scene bg mtngwng 11 with Dissolve(0.8)
    Kiara "Oh it's lana again.."
    scene bg mtngwng 12 with Dissolve(0.8)
    Kiara "Hey lana!"
    Lana "What's that noise?"
    scene bg mtngwng 13  with Dissolve(0.8)
    Kiara "Oh i'm riding the subway , hold on a sec"
    Molester "Fine then , I'll take you instead"
    scene bg mtngwng 14  with Dissolve(0.8)
    AgentWong "Ugh ! you can't be serious , a molester really?"
    scene bg mtngwng dcd  with Dissolve(0.8)
    AgentWong "What should i do? I can take him out but don't want to attract too much attention either"
    
    #CHOICE - bg mtngwnggrpys (corruption +1)  / bg mtngAgent wonggrpno (No corruption)
    menu:
        "Don't risk it":
            jump .part_1
        "Take him out":
            jump .part_2

    label .part_1:
        #bg mtngwnggrpys -       
        scene bg mtngwnggrpyes 1  with Dissolve(0.8)
        AgentWong "(I shouldn't risk it.. it's just a pervert , I'll handle it)"
        scene bg mtngwnggrpyes 2  with Dissolve(0.8)
        Molester "Nice clothes you got.."
        scene bg mtngwnggrpyes 3  with Dissolve(0.8)
        Molester "I bet what's inside is even nicer though.."
        scene bg mtngwnggrpyes 4  with Dissolve(0.8) 
        pause    
        scene bg mtngwnggrpyes 5  with Dissolve(0.8)
        AgentWong "W-what is he doing?"
        scene bg mtngwnggrpyes 6  with Dissolve(0.8)
        pause                                                     
        scene bg mtngwnggrpyes 7  with Dissolve(0.8)
        AgentWong "Hey cut it out! , what are you doing?"
        scene bg mtngwnggrpyes 8  with Dissolve(0.8)
        Molester "What if i don't?"
        scene bg mtngwnggrpyes 9  with Dissolve(0.8)
        AgentWong "Don't push your luck you're lucky I-"
        scene bg mtngwnggrpyes 10  with Dissolve(0.8)
        Molester "Shut up"
        scene bg mtngwnggrpyes 11  with Dissolve(0.8)
        pause
        scene bg mtngwnggrpyes 12  with Dissolve(0.8)
        AgentWong "*Gasp* Ah! .. what the-"
        scene bg mtngwnggrpyes 13  with Dissolve(0.8)
        Molester "Nice.. these are perfect size"
        scene bg mtngwnggrpyes 14  with Dissolve(0.8)
        AgentWong "*Whispering* Hey , are you insane? stop it"   
        Molester "You're gonna have to do it yourself , but i'll do what i want"
        scene bg mtngwnggrpyes 15  with Dissolve(0.8)
        AgentWong "(This guy can't be real.. we're in a train) Hey.. stop i-"
        scene bg mtngwnggrpyes 16  with Dissolve(0.8)
        Molester "These are soft babies you got , you oil them daily huh?"
        scene bg mtngwnggrpyes 17  with Dissolve(0.8)
        AgentWong "(Ugh , I'll take him when the tunnel comes.. fucking hell what a pain)" 
        scene bg mtngwnggrpyes 18  with Dissolve(0.8)
        pause
        scene bg mtngwnggrpyes 19  with Dissolve(0.8)
        Molester "I like your nipples too , they're getting hard i think"
        AgentWong "Ugh.."
        scene bg mtngwnggrpyes 20  with Dissolve(0.8)
        Molester "What's that? can't hear you over your body showing how much a slut you are"
        scene bg mtngwnggrpyes 21  with Dissolve(0.8)
        AgentWong "(Dammit.. I haven't had time with leon in a while..is this why even a basic thing is exciting me?)"
        scene bg mtngwnggrpyes 22  with Dissolve(0.8)
        Molester "Let's see what you got down there"
        scene bg mtngwnggrpyes 23  with Dissolve(0.8)
        AgentWong "Wh-- is he seriously?"
        scene bg mtngwnggrpyes 24  with Dissolve(0.8)
        Molester "Nice ass too , you're not half bad"
        scene bg mtngwnggrpyes 25  with Dissolve(0.8)
        AgentWong "What the hell - hey stop"
        scene bg mtngwnggrpyes 26 with Dissolve(0.8)
        Lana "Well , good luck for the jobs i hope you do well!"
        Kiara "Thanks ! see you soon"
        scene bg mtngwnggrpyes 27  with Dissolve(0.8)
        AgentWong "This guy! ugh" 
        Molester "Been used once heh , i wonder who was the first to fuck your cunt"
        scene bg mtngwnggrpyes 28  with Dissolve(0.8)
        AgentWong "Ugh.. why am i getting turned on even , this is gross"
        scene bg mtngwnggrpyes 29  with Dissolve(0.8)
        Molester "You won't need these anymore"
        scene bg mtngwnggrpyes 30  with Dissolve(0.8)
        Molester "Let's spread this ass"
        scene bg mtngwnggrpyes 31  with Dissolve(0.8)
        Molester "Ah there's the clit , you're loving this aren't you?"
        scene bg mtngwnggrpyes 32  with Dissolve(0.8)
        AgentWong "Aah.. shit" 
        Molester "Tight still , damn i wonder how my dick would feel in there"
        scene bg mtngwnggrpyes 33  with Dissolve(0.8)
        AgentWong "Aah-.. You're disgusting.."
        Molester "Your love hole says otherwise babe"

        $ renpy.end_replay()
        scene bg mtngwnggrpyes 34  with Dissolve(0.8)
        AgentWong "There's the tunnel.. finally"
        scene bg mtngwngtunnl  with Dissolve(0.8) 
        Kiara "This tunnel sure is dark"
        scene bg mtngwng 15  with Dissolve(0.8) 
        AgentWong "That's taken care of.. now. ah!"
        $ mc_stats.adjust_corruption(5)
        jump .part_3

    label .part_2:
        #bg mtngAgent wonggrpno -
        scene bg mtngwnggrpno 1  with Dissolve(0.8)
        AgentWong "Don't even think about it!" 
        Molester "Argh! f-"
        scene bg mtngwngtunnl with Dissolve(0.8)
        "Muffling sounds"
        Kiara "This tunnel sure is dark"
        scene bg mtngwnggrpno 2 with Dissolve(0.8)
        Crowd "Oh my go , is he oka-" 
        AgentWong "Shhhhh"
        scene bg mtngwng 15  with Dissolve(0.8)
        AgentWong "Now that's taken care of.. ah!"
        jump .part_3 

    label .part_3:
        #CANON - CONTINUE - >
        scene bg mtngwng 16 with Dissolve(0.8)
        Kiara "Um? who's that?"
        scene bg mtngwng 17  with Dissolve(0.8)
        AgentWong "My apologies that was my purse" 
        Kiara "Oh that's okay , hello"
        scene bg mtngwng 18 with Dissolve(0.8)
        Kiara "Wow nice shades"
        scene bg mtngwng 19  with Dissolve(0.8)
        AgentWong "Thank you , although there's too many things to compliment return but you look great too"
        scene bg mtngwng 20  with Dissolve(0.8)
        AgentWong "By the way Name's helena , nice to meet you"
        Kiara "Likewise , I'm kiara"
        scene bg mtngwng 21 with Dissolve(0.8)
        AgentWong "Lovely name as well , So ms kiara what's brings you to japan if i may ask?"
        Kiara "Oh it's a long story , but life you know . It leads to various places"
        scene bg mtngwng 22  with Dissolve(0.8)
        AgentWong "I'd love to hear , how about we go to that corner , has a seat empty"
        scene bg mtngwng 23 with Dissolve(0.8)
        Kiara "Much better , you speak english very well by the way ms helena"
        scene bg mtngwng 24  with Dissolve(0.8)
        AgentWong "Got to learn everything in this small life , life's lead me to various places as well" 
        Kiara "That is true , well i'm glad there's someone i can follow the example of"
        scene bg mtngwng 25 with Dissolve(0.8)
        Kiara "So what do you do ms helena? I mean are you a model or?" 
        AgentWong "Oh no no , I am just a simple manager in a real estate firm , it pays the bills"
        scene bg mtngwng 26 with Dissolve(0.8)
        Kiara "That's all that matters really.. pays the bills , keeps a roof above head and.."
        scene bg mtngwng 27 with Dissolve(0.8)
        Kiara "Someone to hold on to"
        scene bg mtngwng 28  with Dissolve(0.8)
        AgentWong "Someone to hold on to.. So about that last one , have you found anyone?" 
        Kiara "Let's just say i never got lucky , everyone saw the money my father had , not the person i was.. so yeah"
        scene bg mtngwng 29  with Dissolve(0.8)
        AgentWong "(Poor girl..)"
        scene bg mtngwng 30  with Dissolve(0.8)
        AgentWong "Well I'm sure you will , money or not you seem like a wonderful person so far"
        scene bg mtngwng 31 with Dissolve(0.8)
        Kiara "Thank you , I hope so too. By the way what about you?  I mean.. Relationships?"
        scene bg mtngwng 32  with Dissolve(0.8)
        AgentWong "Aah.. what if i told you i swing the other way? haha" 
        scene bg mtngwng 33  with Dissolve(0.8)
        AgentWong "Well to be more specific i haven't found a permanent one either" 
        Kiara "Oh that's.. surprising and no I don't judge so its alright"
        scene bg mtngwng 34  with Dissolve(0.8)
        AgentWong "I've tried and there is this one person.. but its not going so well , so i can't commit to it"
        scene bg mtngwng 35 with Dissolve(0.8)
        Kiara "Well you should , we only have one life.. don't waste it over futile matters , talk to her"
        AgentWong "Um.. well if you say so , I'll definitely consider it"
        scene bg mtngwng 36 with Dissolve(0.8)
        Kiara "Besides i doubt anyone would have a hard time , i mean i just met you and you seem like great company"
        scene bg mtngwng 37  with Dissolve(0.8)
        AgentWong "Thank you , that's very sweet of you"
        scene bg mtngwng 38 with Dissolve(0.8) 
        "Station Announcer" "Business street , Please stay further from the doors"
        scene bg mtngwng 39  with Dissolve(0.8)
        AgentWong "I suppose that's all the time we have for today" 
        Kiara "Seems that way"
        scene bg mtngwng 40  with Dissolve(0.8)
        AgentWong "So do you mind if we keep in touch?"
        Kiara "Of course not , let's hope we meet in a better movable space though"
        scene bg mtngwng 41  with Dissolve(0.8)
        AgentWong "Well I'll be seeing you then"  
        Kiara "You too Ms. helen , thank you again"
        scene bg mtngwng 42  with Dissolve(0.8) 
        Kiara "See ya!"
        AgentWong "Bye bye!"
        scene bg mtngwng 43  with Dissolve(0.8)
        AgentWong "(This must be her mother's side.. there's no way a man like john can grow a daughter like this)"

    jump chap_2_scene_4

label chap_2_scene_4:

    #SCENE - Officechptrsgmnt -
    scene blackscreen
    show titletext "Business street , Osaka city" with dissolve
    pause 1.0
    window hide
    scene bg offchptrsgmnt 1 with Dissolve(0.8)
    Kiara "(Alright , Let's call him now)"
    scene bg offchptrsgmnt 2 with Dissolve(0.8)
    Taka "(Hm , maybe this one)"
    scene bg offchptrsgmnt 3 with Dissolve(0.8)
    Taka "*Phone rings* who could this be? Hello?" 
    Kiara "Hey! its me"
    scene bg offchptrsgmnt 4 with Dissolve(0.8)
    Taka "Oh hi.. yeah?"
    scene bg offchptrsgmnt 5 with Dissolve(0.8)
    Kiara "What do you mean hi ? The Notes you sent say blue building , it only has a blue sign" 
    Taka "Oh yeah blue sign , same thing"
    scene bg offchptrsgmnt 6 with Dissolve(0.8)
    Kiara "They're not the same th-.. ugh leave it"
    Taka "Sorry!"
    scene bg offchptrsgmnt 7 with Dissolve(0.8)
    Kiara "Hm.. Okay"
    scene bg offchptrsgmnt 8 with Dissolve(0.8)
    Kiara "(Stay focused , it's just an interview.. and you're more than qualified)"
    scene bg offchptrsgmnt 9 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 10  with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 11 with Dissolve(0.8)
    Kiara "Excuse me..I'm here for the representative and agency job?"
    scene bg offchptrsgmnt 12 with Dissolve(0.8)
    "Reception lady" "Nani? Sumimasen , Wakarimasen "
    scene bg offchptrsgmnt 13 with Dissolve(0.8)
    Kiara "(Uh.. japanese of course)"
    scene bg offchptrsgmnt 14 with Dissolve(0.8)
    Kiara "Um.. job? Agency.. ano.. how do i" 
    "Reception lady" "Daijobou , wakari-"
    Manager "Hm?" 
    scene bg offchptrsgmnt 15 with Dissolve(0.8)
    Manager "Kono josei ni wa nani ga hitsuyōdesu ka?"
    "Reception lady" "Wakaranai, kanojo itta shigoto" 
    scene bg offchptrsgmnt 16 
    Manager "You're here from ad agency reference?"
    scene bg offchptrsgmnt 17 with Dissolve(0.8)
    Kiara "Yes ! , my friend told me this would be the place for both other references and a job itself"
    Manager "Please wait"
    scene bg offchptrsgmnt 18 with Dissolve(0.8)
    Manager "Watashi wa sugu ni modotte kimasu, korera wa gaikoku hitodesu" 
    "Reception lady" "Ryōkai shita" 
    scene bg offchptrsgmnt 19 with Dissolve(0.8)
    "Reception lady" "Mata chikaiuchini o ai shimashou" 
    Kiara "Yeah.. I'll wait i guess"
    scene bg offchptrsgmnt 20 with Dissolve(0.8)
    Kiara "Ah i hope she doesn't take long "
    scene bg offchptrsgmnt 21 with Dissolve(0.8)
    Kiara "On that note , probably should start learning japanese too while i'm here"
    scene bg offchptrsgmnt 22 with Dissolve(0.8)
    Kiara "Anyway.. let's practice that move i saw in aunt's book"
    scene bg offchptrsgmnt 23 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 24 with Dissolve(0.8)
    Kiara "Lock with the inner while keeping shoulders intact"
    scene bg offchptrsgmnt 25 with Dissolve(0.8)
    Kiara "Squeeze the muscles without losing tension"
    scene bg offchptrsgmnt 26 with Dissolve(0.8)
    Kiara "And HA!" 
    "Man in office" "Aough!"
    scene bg offchptrsgmnt 27 with Dissolve(0.8)
    "Man in the office" "Fuck argh my nose" 
    Kiara "Oh my god!"
    scene bg offchptrsgmnt 28 with Dissolve(0.8)
    Kiara "I'm so sorry! I didn't see you"
    scene bg offchptrsgmnt 29 with Dissolve(0.8)
    "Man in the office" "Ay ay ai , man you got a mean elbow"
    Kiara "I am so sorry , please - are you alright?"
    scene bg offchptrsgmnt 30 with Dissolve(0.8)
    "Man in the office" "Y-yeah , It's fine i think its intact" 
    Kiara "Um- Please getup , take my hand"
    scene bg offchptrsgmnt 31 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 32 with Dissolve(0.8)
    "Man in the office" "(She is.. pretty)"
    scene bg offchptrsgmnt 33 with Dissolve(0.8)
    "Man in the office" "I really am okay , don't worry" 
    Kiara "I apologize still, I'm kiara by the way hello"
    scene bg offchptrsgmnt 34 with Dissolve(0.8)
    Alex "Alex here.. Nah i'm fine , you waiting for interview too?"
    scene bg offchptrsgmnt 35 with Dissolve(0.8)
    Kiara "Yeah , sadly i don't know the language though"
    scene bg offchptrsgmnt 36 with Dissolve(0.8)
    Manager "Hello you two , sorry for the delay"
    scene bg offchptrsgmnt 37 with Dissolve(0.8)
    Manager "Please come in" 
    Alex "Right behind you dude" 
    Kiara "(I don't think his name is dude)"
    scene bg offchptrsgmnt 38 with Dissolve(0.8)
    Manager "Welcome , Welcome I am sorry for the confusion"
    scene bg offchptrsgmnt 39 with Dissolve(0.8)
    Manager "So Ms . Kiara and Mister... Alex"
    scene bg offchptrsgmnt 40 with Dissolve(0.8)
    Manager "I believe you two are here for the job but mister alex's process is already done"
    scene bg offchptrsgmnt 41 with Dissolve(0.8)
    Alex "Yeah it got cleared online" 
    Manager "You are free to go sir , logistics department will get you your ID" 
    scene bg offchptrsgmnt 42 with Dissolve(0.8)
    Alex "Good luck to you champ" 
    Kiara "Thanks , see ya later"
    scene bg offchptrsgmnt 43 with Dissolve(0.8)
    Manager "So ms kiara , how has our city treated you? "
    scene bg offchptrsgmnt 44 with Dissolve(0.8)
    Kiara "It's been wonderful so far , having a home here helps alot too" 
    Manager "I see , home here? are you japanese?" 
    scene bg offchptrsgmnt 45 with Dissolve(0.8)
    Kiara "I'm mixed actually , my mother is on japanese side"
    scene bg offchptrsgmnt 46 with Dissolve(0.8)
    Manager "Splendid , please enjoy here , I know your qualifications already so please tell me your hobbies?"
    scene bg offchptrsgmnt 47 with Dissolve(0.8)
    Kiara "Hobbies.. umm well i love to draw , read books and lastly i love instruments!"
    scene bg offchptrsgmnt 48 with Dissolve(0.8)
    Manager "Instruments? do ouy play any?"
    Kiara "No no , if i tried i'd probably just explode eardrums"
    scene bg offchptrsgmnt 49 with Dissolve(0.8)
    Manager "I am sure you'll improve that too , Well here are the other job locations , i think however you'd enjoy working here more as well , we are a great environment" 
    Kiara "Thank you , I hope so too"
    scene bg offchptrsgmnt 50 with Dissolve(0.8)
    Manager "I would recommend however to still meet the boss before you go , would be good to not stay strangers"
    scene bg offchptrsgmnt 51 with Dissolve(0.8)
    Kiara "Of course , I'll get going now thank you again" 
    Manager "Most welcome" 
    scene bg offchptrsgmnt 52 with Dissolve(0.8)
    Kiara "Oh um one more thing , do you happen to know any japanese tutions? I wanted to learn the language" 
    Manager "Ah i believe one of my friends is one , I'll get you in contact with them" 
    scene bg offchptrsgmnt 53 with Dissolve(0.8)
    Manager "Well I'll get going then , see you around ms kiara" 
    Kiara "You too! , thank you."
    scene bg offchptrsgmnt 54 with Dissolve(0.8)
    Kiara "Alright , just don't come off as nervous"
    scene bg offchptrsgmnt 55 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 56 with Dissolve(0.8)
    Kiara "Uhm , excuse me I-"
    scene bg offchptrsgmnt 57 with Dissolve(0.8)
    Vince "(Who might this be?)"
    scene bg offchptrsgmnt 58 with Dissolve(0.8)
    Kiara "I am Kiara hall , i just got hired in the representative department , i thought i'd meet you as well sir" 
    Vince "(This girl..)"  
    Assistant "Hi there!"
    scene bg offchptrsgmnt 59 with Dissolve(0.8)
    Vince "(Soft skin)"
    scene bg offchptrsgmnt 60 with Dissolve(0.8)
    Vince "(Decent proportions)" 
    Kiara "Um , sir?"
    scene bg offchptrsgmnt 61 with Dissolve(0.8)
    Kiara "I just wanted to have a conversation unless you're busy?"
    scene bg offchptrsgmnt 62 with Dissolve(0.8)
    Vince "(Yummy..)" 
    scene bg offchptrsgmnt 63 with Dissolve(0.8)
    Kiara "Sir am i dist-"
    Vince "Not at all , my apologies please come sit ,  I was lost in thought about work"
    scene bg offchptrsgmnt 64 with Dissolve(0.8)
    Kiara "Hello sir , I', Kira- uh Kiara hall" 
    Vince "Relax ms kiara , we are glad to have new talent always do not be nervous" 
    scene bg offchptrsgmnt 65 with Dissolve(0.8)
    Kiara "Sorry , Um so sir this is a ad agency and a customer care firm?"
    Vince "Precisely"
    scene bg offchptrsgmnt 66 with Dissolve(0.8)
    Kiara "So are rotational shifts okay? since i might apply at other positions?"
    Vince "(The only position i'd want you is on my face sweety)"
    scene bg offchptrsgmnt 67 with Dissolve(0.8)
    Vince "Of course , if our manager approved your profile you're free to work as you applied" 
    Kiara "Thank you sir , just trying to get on my own feet"
    scene bg offchptrsgmnt 68  with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 69 with Dissolve(0.8)
    Vince "Speaking of which , how about you give this sample project a try?" 
    Kiara "Oh sure , i'd love to"
    scene bg offchptrsgmnt 70 with Dissolve(0.8)
    Kiara "Pleae give me a moment" 
    Vince "Take your time.." 
    scene bg offchptrsgmnt 71 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 72 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 73 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 74 with Dissolve(0.8)
    Assistant "(Ah!.. now?)"
    scene bg offchptrsgmnt 75 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 76 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 77 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 78 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 79 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 80 with Dissolve(0.8)
    pause
    scene bg offchptrsgmnt 81 with Dissolve(0.8)
    Kiara "(Seems like it's done)"
    scene bg offchptrsgmnt 82 with Dissolve(0.8)
    Kiara "Here you go sir" 
    Vince "That was very quick , let me take a look"
    scene bg offchptrsgmnt 83 with Dissolve(0.8)
    Vince "Hmmm"
    scene bg offchptrsgmnt 84 with Dissolve(0.8)
    Vince "(Not just pretty but brains too.. i gotta keep this girl)"
    scene bg offchptrsgmnt 85 with Dissolve(0.8)
    Vince "Very impressive ms kiara , I would even promote you if not against the policy laws" 
    Kiara "Hah I appreciate it sir , but I want to be equal and grow with others"
    scene bg offchptrsgmnt 86 with Dissolve(0.8)
    Kiara "Sir no to be rude but I've got to go for the other locations , Thank you for the opportunity again" 
    Vince "Yes , Ms. kiara i wish you luck on other jobs as well" 
    scene bg offchptrsgmnt 87 with Dissolve(0.8)
    Vince "(Though i'll make sure to turn you into the puppy that stays in my office)"
    scene bg offchptrsgmnt 88 with Dissolve(0.8)
    Kiara "(That went way better than i thought , great)"
    scene bg offchptrsgmnt dcdone 
    Kiara "Dammit I forgot to ask him about the incentives , should i? "
    #CHOICE  ASK NOW  , ASK LATER
    menu:
        "Ask him now":
            jump .part_1
        
        "Ask Later":
            jump .part_2

    label .part_1:
        #IF CHOICE ASK NOW
        scene bg offchptrsgmnt 89  with Dissolve(0.8)
        Assistant "Aaah! sir.. wai-" 
        scene bg offchptrsgmnt 90  with Dissolve(0.8)
        pause
        scene bg offchptrsgmnt 91  with Dissolve(0.8)
        pause
        scene bg offchptrsgmnt 92  with Dissolve(0.8)
        Kiara "What's that sound?"
        scene bg offchptrsgmnt 93 with Dissolve(0.8)
        Kiara "W-.. what the.."
        scene bg offchptrsgmnt 94 with Dissolve(0.8)
        Vince "She made me horny.. get these out" 
        scene bg offchptrsgmnt 95 with Dissolve(0.8)
        Assistant "Ah!" 
        scene bg offchptrsgmnt dcdtwo 
        Kiara "W-what is happening.. this.. I should leave" 
        #CHOICE  - Kiara dialogue first  - 
        pass
    if _in_replay:
        jump .part_3
    
    #CHOICE -  Keep watching ( + 5 Corruption) , Don’t watch (No corruption).
    menu:
        "Keep Watching":
            jump .part_3
        "Don't Watch":
            jump .part_4
    
    label .part_3:
        #IF KEEP WATCHING - RENDERS OF THE FOLDER -  offccptwtch
        scene bg offccptwtch 1  with Dissolve(0.8)
        Assistant "Sir.. someone might-" 
        scene bg offccptwtch 2 with Dissolve(0.8)
        Vince "Shut up , take this shit off"
        scene bg offccptwtch 3 with Dissolve(0.8)
        Kiara "My god.. he's stripped her naked"
        scene bg offccptwtch 4 with Dissolve(0.8)
        Kiara "W-why can't i move?"
        scene bg offccptwtch 5 with Dissolve(0.8)
        Kiara "This can't be happening , he was so-"
        scene bg offccptwtch 6 with Dissolve(0.8)
        Assistant "Mmmph.."  
        Vince "I'm gonna get her just like this one day.."
        scene bg offccptwtch 7 with Dissolve(0.8)
        Vince "Get on here"
        scene bg offccptwtch 8 with Dissolve(0.8)
        Vince "Your asshole hasn't been used properly , lets stretch it first" 
        scene bg offccptwtch 9 with Dissolve(0.8)
        Assistant "Ah!.. sir slowly.."  
        Kiara "This , no maybe they i-"
        scene bg offccptwtch 10 with Dissolve(0.8)
        Vince "You're gonna take a vacation you got that? .. I need to reel in the new girl"
        scene bg offccptwtch 11 with Dissolve(0.8)
        Assistant "Yes sir.. I understand" 
        scene bg offccptwtch 12 with Dissolve(0.8)
        Kiara "I- this is just.. am i dreaming or something , I should just go"
        scene bg offccptwtch 13 with Dissolve(0.8)
        Kiara "*Shoe hits glass* Shit!"
        scene bg offccptwtch 14 with Dissolve(0.8)
        Vince "Huh?"
        scene bg offccptwtch 15 with Dissolve(0.8)
        Vince "Swear i heard something.."
        scene bg offccptwtch 16 with Dissolve(0.8)
        Kiara "Oh my god , he could've spotted me.. I- i gotta go now"

        $ renpy.end_replay()
        scene bg offccptwtch 17 with Dissolve(0.8)
        Kiara "This was.. what just happened?"
        scene bg offccptwtch 18 with Dissolve(0.8)
        Kiara "No , they , they must be in a relationship or something"
        scene bg offccptwtch 19 with Dissolve(0.8)
        Kiara "M-Maybe people do that here.. i don't know , but in public?"
        scene bg offccptwtch 20 with Dissolve(0.8)
        Alex "So that's why they had to get me here in the end" 
        "Desk girl" "Hontone.."
        scene bg offccptwtch 21 with Dissolve(0.8)
        Alex "Oh , hey kiara!"
        scene bg offccptwtch 22 with Dissolve(0.8)
        Alex "She just left , is everything alright with her?"
        scene bg offccptwtch 23 with Dissolve(0.8)
        Alex "I hope you're okay Kiara.."
        $ mc_stats.adjust_corruption(5)
        jump chap_2_scene_5

    label .part_4:
        #IF DON’T WATCH   RENDERS OF THE FOLDER  offccptdntwtch
        scene bg offchptryes 1  with Dissolve(0.8)
        Kiara "I- that must've been a mistake , no."
        scene bg offchptryes 2 with Dissolve(0.8)
        Kiara "Maybe they're in a relationship.. or something i don't know.."
        scene bg offchptryes 3 with Dissolve(0.8)
        Kiara "But in public..? I -.. No.."
        scene bg offchptryes 4  with Dissolve(0.8)
        Alex "So that's why they had to get me here in the end" 
        "Desk girl" "Wakarimaska"
        scene bg offchptryes 5 with Dissolve(0.8)
        Alex "Oh , hey kiara!"  
        scene bg offchptryes 6 with Dissolve(0.8)
        Alex "She just left , is everything alright with her?" 
        scene bg offchptryes 7 with Dissolve(0.8)
        Alex "I hope you're okay Kiara.." 

        $ mc_stats.adjust_corruption(5)
        jump chap_2_scene_5


    label .part_2:
        #IF CHOICE ASK LATER  RENDERS OF THE FOLDER  offccptdntgo
        scene bg offccptdntgo 1 with Dissolve(0.8)
        Kiara "I'll just do it later"
        scene bg offccptdntgo 2 with Dissolve(0.8)
        pause
        scene bg offccptdntgo 3 with Dissolve(0.8)
        Alex "So that's why they tried to get me here" 
        "Desk girl" "Hai , meska"
        scene bg offccptdntgo 4 with Dissolve(0.8)
        Alex "H-Hey kiara!" 
        scene bg offccptdntgo 5 with Dissolve(0.8)
        Kiara "Oh hi! , you're here?"
        scene bg offccptdntgo 6 with Dissolve(0.8)
        Alex "Seems we're in the same department , pretty cool"  
        Kiara "Now i regret the punch earlier even more haha"
        scene bg offccptdntgo 7 with Dissolve(0.8)
        "Desk girl" "Kanojo wa totemo kawaīdesu" 
        Alex "Dōi shimasu"
        scene bg offccptdntgo 8  with Dissolve(0.8)
        Kiara "What did she say?" 
        Alex "Heh , She said you're cute"
        scene bg offccptdntgo 9  with Dissolve(0.8)
        Kiara "Oh , ha tell her she's adorable as well"
        scene bg offccptdntgo 10 with Dissolve(0.8)
        Kiara "Anyway I gotta be skidaddle , see you around"
        Alex "Yeah , see you around"

        jump chap_2_scene_5

label chap_2_scene_5:

    #SCENE - > 
    scene blackscreen
    show titletext "Business street , Afternoon" with dissolve
    pause 1.0
    window hide
    scene bg kiascool 1 with Dissolve(0.8)
    Kiara "Took longer than i would've wanted , at least it's in the bag"
    scene bg kiascool 2 with Dissolve(0.8)
    Kiara "Alright now before i go off to the other jobs , should visit azumi's school first"
    scene bg kiascool 3 with Dissolve(0.8)
    pause
    scene bg kiascool 4 with Dissolve(0.8)
    "Take the subway again?"
    scene bg kiascool 5 with Dissolve(0.8)
    pause
    scene bg kiascool 6 with Dissolve(0.8)
    "Ah.. its crowded I don’t really wanna stand.."
    scene bg kiascool 7 with Dissolve(0.8)
    TaxiDriver "Hey over there! Need a drive?"
    Kiara "Oh hi! uh yeah might take longer tho"
    scene bg kiascool 8 with Dissolve(0.8)
    TaxiDriver "We're all free people here , don't worry hop on in"
    Kiara "Sure then! , give me one sec stupid chewing gum"
    scene bg kiascool 9 with Dissolve(0.8)
    TaxiDriver "Take your time"
    scene bg kiascool 10 with Dissolve(0.8)
    Kiara "Ha , thank you so much , riding the subway would've been a nightmare again"
    TaxiDriver "Understatement , trust me"
    scene bg kiascool 11 with Dissolve(0.8)
    Kiara "You know it amazes me how japan keeps ancient and modern architecture both"
    scene bg kiascool 12 with Dissolve(0.8)
    Kiara "It's like you guys stay with your roots , while growing in everything else"
    TaxiDriver "We have a tendency to do that"
    scene bg kiascool 13 with Dissolve(0.8)
    Kiara "It really is amazing , I am new here but i hope i get to explore more"
    scene bg kiascool 14 with Dissolve(0.8)
    TaxiDriver "It's a lovely city , I'm sure you will enjoy it. So what's with the school?"
    scene bg kiascool 15 with Dissolve(0.8)
    Kiara "Oh i'm applying as a english teacher , normal gig nothing special , are you born here by the way?"
    scene bg kiascool 16 with Dissolve(0.8)
    TaxiDriver "Yes , Born and brought up here"
    Kiara "Your english is very good , It's quite impressive"
    TaxiDriver "Thank you"
    scene bg kiascool 17 with Dissolve(0.8)
    TaxiDriver "Seems we're at your school , good luck teacher"
    Kiara "Thanks , I'll be back quick"
    scene bg kiascool 18 with Dissolve(0.8)
    Kiara "(Hm.. it said the right office but there's only one here in left)"
    scene bg kiascool 19 with Dissolve(0.8)
    Kiara "Oh well , probably a translation error"
    scene bg kiascool 21 with Dissolve(0.8)
    Kiara "Let's go . I should call Azumi as well"
    scene bg kiascool 22 with Dissolve(0.8)
    Azumi "*Humming*"
    scene bg kiascool 23 with Dissolve(0.8)
    Azumi "(Tastes perfect..)"
    scene bg kiascool 24 with Dissolve(0.8)
    Azumi "(Today's been tiring , I wonder how kiara is doing)"
    scene bg kiascool 25 with Dissolve(0.8)
    Azumi "I wonder what she likes to eat.. maybe sushi? rice cakes?"
    scene bg kiascool 26 with Dissolve(0.8)
    Azumi "Hmm.. i don't wanna annoy her too much , I am clingy enough as it is"
    scene bg kiascool 27 with Dissolve(0.8)
    Azumi "Perhaps i should just take things slow.. if nothing else at least friends"
    scene bg kiascool 28 with Dissolve(0.8)
    Azumi "(I should maybe ask her when she'll be at school)"
    scene bg kiascool 29 with Dissolve(0.8)
    Azumi "*Phone rings* Hm? oh! its her"
    scene bg kiascool 30 with Dissolve(0.8)
    Azumi "H-hi kiara , i was just about to call you"
    scene bg kiascool 31 with Dissolve(0.8)
    Azumi "What? you've reached the school? um is my uncle there?"
    Kiara "Yes but i cannot find him , could you please come to the office if you're nearby?"
    scene bg kiascool 32 with Dissolve(0.8)
    Azumi "Ah! yea- yes i'm near , will be there in 15 minutes okay"
    Kiara "Alright sure , I'll wait "
    scene bg kiascool 33 with Dissolve(0.8)
    Azumi "Uncle cmon pickup.."
    scene bg kiascool 34 with Dissolve(0.8)
    Azumi "Ah i don't wanna risk it , I'll just go myself please wait for me kiara"
    scene bg kiascool 35 with Dissolve(0.8)
    Kiara "Well now i wait again"
    scene bg kiascool 36 with Dissolve(0.8)
    Kiara "(This office is pretty nice)"
    scene bg kiascool 37 with Dissolve(0.8)
    pause
    scene bg kiascool 38 with Dissolve(0.8)
    pause
    scene bg kiascool 39 with Dissolve(0.8)
    Kiara "One day i'll have an office like this as well"
    scene bg kiascool 40 with Dissolve(0.8)
    Kiara "A chair like this.. i can't wait"
    scene bg kiascool 41 with Dissolve(0.8)
    Kiara "Okay , just once.. it won't hurt anyone"
    scene bg kiascool 42 with Dissolve(0.8)
    Kiara "Ahhh"
    scene bg kiascool 43 with Dissolve(0.8)
    Kiara "One day.. , I'll have this too"
    scene bg kiascool 44 with Dissolve(0.8)
    Sato "Stay in your class idiots! Ugh kids these days"
    scene bg kiascool 45 with Dissolve(0.8)
    Sato "What a pain"
    scene bg kiascool 46 with Dissolve(0.8)
    Kiara "*Gasp* Ah! I- I'm so-"
    scene bg kiascool 47 with Dissolve(0.8)
    Sato "Who are you?"
    Kiara "Sir , I didn't mean to-"
    scene bg kiascool 48 with Dissolve(0.8)
    Kiara "I apologize i was just.."
    Sato "Relax , Relax"
    scene bg kiascool 49 with Dissolve(0.8)
    Kiara "I was just sitting to see how the-"
    Sato "It's okay , calm down please sit"
    scene bg kiascool 50 with Dissolve(0.8)
    Sato "So who are you ms?"
    Kiara "I'm Kiara hall , I applied for a-"
    scene bg kiascool 51 with Dissolve(0.8)
    Sato "Ah yes , my niece told me about you"
    scene bg kiascool 52 with Dissolve(0.8)
    Kiara "Oh , well i mainly wanted to apply for a temporary job , would that be okay?"
    scene bg kiascool 53 with Dissolve(0.8)
    Sato "Of course , a substitute teacher is what we need anyway"
    scene bg kiascool 54 with Dissolve(0.8)
    Sato "You are new in japan correct?"
    Kiara "Yes sir"
    scene bg kiascool 55 with Dissolve(0.8)
    Sato "Well , English and french will the subjects you teach either is fine by your degree from the documents i recieved "
    scene bg kiascool 56 with Dissolve(0.8)
    Kiara "That would be perfect sir , sir don't mind me asking but.. you're her uncle and she didn't open too much but where are parents?"
    Sato "Oh you do not know it seems"
    Kiara "What?"
    scene bg kiascool 57 with Dissolve(0.8)
    Sato "Azumi did not grow up with her parents"
    Kiara "I.. Don't understand sir"
    scene bg kiascool 58 with Dissolve(0.8)
    Sato "She lost her parents to a car crash , I've been the one taking care of her since then"
    Kiara "(W-.. This is why she was so hesistant in the plane to talk about it?)"
    scene bg kiascool 59 with Dissolve(0.8)
    Sato "Her family also mostly stays away from her because they blame her for their deaths , as it happened right after she was born while they were going home"
    Kiara "(No.. Azumi I didn't know yet i kept asking , I'm sorry)"
    scene bg kiascool 60 with Dissolve(0.8)
    Sato "The job she offered to you while may be to help you on one side , but is probably in reality to have a friend as she described it"
    Kiara "I-I'll do my best"
    scene bg kiascool 61 with Dissolve(0.8)
    Sato "Do not punish yourself , she's a good child always has been , god takes what he loves"
    Kiara "That he does.. no doubt on it"
    scene bg kiascool 62 with Dissolve(0.8)
    Kiara "Sir um.. the interview , I don't know if"
    Sato "I understand , just tell me you are comfortable in the French and english classes right?"
    Kiara "Yes"
    scene bg kiascool 63 with Dissolve(0.8)
    Sato "Aside from that your job is rotational and substitute , the only mandatory part is in the examinations"
    Kiara "Of course sir . I'll be here during any prelims"
    scene bg kiascool 64 with Dissolve(0.8)
    Kiara "Anything else sir?"
    Sato "How are you with kids of young adult age? , we have both kinds here so"
    scene bg kiascool 65 with Dissolve(0.8)
    Kiara "I am  , I've done substitute in my own uni back in NY as well"
    Sato "You should be a great fit then , okay lastly what do you think-"
    scene bg kiascool 66 with Dissolve(0.8)
    Azumi "Kiara?.."
    scene bg kiascool 67 with Dissolve(0.8)
    Kiara "Azumi.."
    Sato "Hey sweety , you don't have work today but welcome"
    Azumi "Kiara.."
    scene bg kiascool 68 with Dissolve(0.8)
    Azumi "Kiara H- hi!"
    Kiara "Hey , you look great"
    scene bg kiascool 69 with Dissolve(0.8)
    Azumi "Thanks , you do too I-I'm so happy to see you!"
    scene bg kiascool dcdhug 
    Kiara "*surprised* Ah! um.."
    #CHOICE -> Kiara dialogue Hug back? (Romance + Azumi) / Don’t hug (No romance +)
    menu:
        "Hug Back":
            jump .part_1
        "Don't Hug":
            jump .part_2

    label .part_1:
        #If hug back then renders folder - kiscolhgys - >
        scene bg kiascooldtyes 1 with Dissolve(0.8)
        Kiara "(Heh.. this is the least i can do for you)"
        scene bg kiascooldtyes 2 with Dissolve(0.8)
        Azumi "(I could be in this moment forever..)"
        scene bg kiascooldtyes 3 with Dissolve(0.8)
        Kiara "(I can tell she doesn't wanna let go)"
        $ azumi_rom.adjust_romance(1)
        jump .part_2
    
    label .part_2:
        #IF No hug back - Resume canon renders .
        scene bg kiascool 70 with Dissolve(0.8)
        Azumi "Thank you so much for coming"
        Kiara "You came faster than 15 minutes by the way haha"
        scene bg kiascool 71 with Dissolve(0.8)
        Azumi "I just wanted to see you sorry , Um.. do you want to grab some lunch?"
        Kiara "Oh i'd love to but my interview here hasn't finished"
        scene bg kiascool 72 with Dissolve(0.8)
        Sato "No need Kiara-san , you may go"
        Azumi "Really uncle ? is that okay?"
        scene bg kiascool 73 with Dissolve(0.8) 
        Kiara "Are you sure sir?" 
        Sato "If azumi trusts you then i do too , please enjoy your afternoon"
        scene bg kiascool datedcd with Dissolve(0.8) 
        #CHOICE ->Azumi dialogue-> Go to date? (+  Azumi romance), Don’t go.(No romance+)
        menu:
            "Go to Lunch?":
                jump .part_3
            "Don't go":
                jump .part_4

        #IF GO TO DATE ->  USE RENDERS OF FOLDER kiafstdateys ->
    label .part_3:
        scene bg kiascooldteyes 1 with Dissolve(0.8)
        Azumi "Thanks uncle!"
        Sato "Don't mention it"
        scene bg kiascooldteyes 2 with Dissolve(0.8)
        Azumi "I've got many places i wanna show  , but let's visit the restro i love for now"
        Kiara "Sure anything is fine , you're the expert here"
        scene bg kiascooldteyes 3 with Dissolve(0.8)
        Azumi "I don't know about expert , I really want you enjoy the cousine here"
        Kiara "Well surprise me then let's see"
        scene bg kiascooldteyes 4 with Dissolve(0.8)
        Azumi "Thank you again for coming , I know your day's busy as it is"
        Kiara "Please don't mention it , you're my first friend here after all"
        scene bg kiascooldteyes 5 with Dissolve(0.8)
        Kiara "Besides I'd rather have a little break between the hectic day with someone who's good company"
        Azumi "I'm glad you think so"
        scene bg kiascooldteyes 6 with Dissolve(0.8)
        Azumi "Sir , would you please take us to the akibara's?"
        TaxiDriver "Good choice , Sure!"
        scene bg kiascooldteyes 7 with Dissolve(0.8)
        Azumi "Do you like the place?"
        scene bg kiascooldteyes 8 with Dissolve(0.8)
        Kiara "It's beautiful , ambiance is very nice"
        scene bg kiascooldteyes 9 with Dissolve(0.8)
        Azumi "It's the only place that has my favorite food , so i wanted to bring my new favorite person"
        Kiara "Hehe , I'm very happy to be here. Let's see what's the surprise"
        scene bg kiascooldteyes 10 with Dissolve(0.8)
        Azumi "Sumimasen!"
        scene bg kiascooldteyes 11 with Dissolve(0.8)
        "Lady" "Hm?"
        Azumi "Tabemono o onegaishimasu!"
        scene bg kiascooldteyes 12 with Dissolve(0.8)
        "Lady" "Gesuto sanka onegaishimasu"
        "Waiter" "Hai!"
        scene bg kiascooldteyes 13 with Dissolve(0.8)
        "Waiter" "What can i bring you ladies?"
        Azumi "I'd love some sushi and a mojito"
        scene bg kiascooldteyes 14 with Dissolve(0.8)
        "Waiter" "What about you Ms? "
        Kiara "A strawberry shake and whatever your special is"
        scene bg kiascooldteyes 15 with Dissolve(0.8)
        Azumi "So , are you okay with sharing office? If you want seperate i can arrange it"
        Kiara "No why would i? like i said I'd rather check copies and eat lunch with company than stare at a screen"
        scene bg kiascooldteyes 16 with Dissolve(0.8)
        Kiara "Besides I don't want to nag anyone really , I want to just stand for now so i don't want to make demands"
        Azumi "It's not about demands , I just want you to be comfortable and maybe do full time there once"
        scene bg kiascooldteyes 17 with Dissolve(0.8)
        Kiara "Seems like i didn't exaggerate at all when i talked to natsuko about you"
        Azumi "Hm? Who's natsuko? what did you say also?"
        scene bg kiascooldteyes 18 with Dissolve(0.8)
        Kiara "I told her about how we met and how you're so nice , oh also she called you very cute"
        scene bg kiascooldteyes 19 with Dissolve(0.8)
        Azumi "Heh , she's the only one who called me cute?"
        Kiara "What no i was the first one."
        scene bg kiascooldteyes 20 with Dissolve(0.8)
        Kiara "Ahh i see what you did there, fishing compliments huh"
        scene bg kiascooldteyes 21 with Dissolve(0.8)
        Azumi "What can i say i like sushi , no pun intended!"
        scene bg kiascooldteyes 22 with Dissolve(0.8)
        Kiara "Well you don't need to fish em , You're very cool and cute"
        Azumi "Same to you , It's quite easy to compliment when it's the truth"
        scene bg kiascooldteyes 23 with Dissolve(0.8)
        Kiara "So what do you do at school? I mean teach?"
        scene bg kiascooldteyes 24 with Dissolve(0.8)
        Azumi "I teach english!"
        scene bg kiascooldteyes 25 with Dissolve(0.8)
        Kiara "Wait.. so you hired me despite having a english teacher?"
        Azumi "Yes , I told you I'd help anyway i can"
        scene bg kiascooldteyes 26 with Dissolve(0.8)
        Azumi "I didn't want you to suffer , I know you're applying for others but if its too stressful just work here"
        scene bg kiascooldteyes 27 with Dissolve(0.8)
        Kiara "I-.. Thanks azumi. I appreciate it"
        scene bg kiascooldteyes 28 with Dissolve(0.8)
        Azumi "I Well seems food's here , lets dig in"
        Kiara "Yes!"
        scene bg kiascooldteyes 29 with Dissolve(0.8)
        Azumi "Thank you for coming to lunch , I am repeating myself but its been a while since anyone shared a genuine conversation with me"
        Kiara "Why so?"
        scene bg kiascooldteyes 30 with Dissolve(0.8)
        Kiara "I mean don't you go out to lunch with collegues?"
        Azumi "They uh , they don't really prefer talking to me , everyone thinks i'm bad luck"
        scene bg kiascooldteyes 31 with Dissolve(0.8)
        Azumi "I mean even that aside , It's hard for me to trust people so i am glad you and i vibe this well"
        scene bg kiascooldteyes 32 with Dissolve(0.8)
        Azumi "I just appreciate you , thanks for making me feel like i won't be isolated at least  "
        Kiara "You don't have to thank me for what you deserve you know . I was scared to be alone too but now i got you"
        scene bg kiascooldteyes 34 with Dissolve(0.8)
        Azumi "You really mean it?"
        scene bg kiascooldteyes 35 with Dissolve(0.8)
        Kiara "You know i do"
        scene bg kiascooldteyes 36 with Dissolve(0.8)
        Azumi "Well , still i am a bit clingy i hope you don't find that annoying"
        $ azumi_rom.adjust_romance(1)

        scene bg kiascooldteyesflrtdcd with Dissolve(0.8)

        menu:
            "Flirt?":
                jump .part_5
            "Don't flirt":
                jump .part_6
        # #CHOICE -  FLIRT? ( AZUMI ROMANCE + ) , DON’T FLIRT ( NO ROMANCE+)
        label .part_5:
        # IF FLIRT THEN USE RENDERS OF  datflrtys ->

            scene bg datflrtys 1  with Dissolve(0.8)
            Kiara "Why would i? After all a clingy person who has this cute of a smile is always great"
            scene bg datflrtys 2 with Dissolve(0.8)
            Azumi "*Blushes* Thank you (She just- maybe she feels the same way?)"
            scene bg datflrtys 3 with Dissolve(0.8)
            Azumi "Promise you'll stick around?.. Most people just leave I know you're different but-"
            Kiara "Azumi , most people leave because they need something , I already have it so yes i promise , No-"
            scene bg datflrtys 4 with Dissolve(0.8)
            Kiara "Pinky - Promise , you're not getting rid of me"
            Azumi "Heh thanks.. (I plan to do the opposite)"
            scene bg datflrtys 5 with Dissolve(0.8)
            Kiara "Do you want me to drop you back at school?"
            Azumi "No i'll call my driver , you go ahead and best of luck"
            
            $ azumi_rom.adjust_romance(1)
            jump chap_2_scene_6

        label .part_6:
            # IF FLIRT THEN USE RENDERS OF datdntflrt ->
            scene bg datdntflrt 1  with Dissolve(0.8)
            Kiara "Of course i don't , you're a good person azumi you don't have to seek value from others around you but i'll stick around always"
            scene bg datdntflrt 2 with Dissolve(0.8)
            Azumi "Thank you , and yes i've got to be more confident as well"
            Kiara "Well I better get going now"
            scene bg datdntflrt 3 with Dissolve(0.8)
            Azumi "Oh yes , um i'll go home by my own you go ahead and best of luck"
            Kiara "Thanks , see you again soon."
            jump chap_2_scene_6

    label .part_4:

        # If DON’T GO DATE THEN USE RENDERS OF kiafstdateno ->
        scene bg kiascooldtno 1 with Dissolve(0.8)
        Kiara "There's one more issue.. I have to go to the other jobs i'm already running late.. I'm sorry"
        Azumi "(I..Dnn't pressure her ) Um yes it's alright.."
        scene bg kiascooldtno 2 with Dissolve(0.8)
        Kiara "I hope you understand , I just want to make sure today is done then we can maybe"
        Azumi "No i - i understand , it's okay please attend the job stuff first"
        scene bg kiascooldtno 3 with Dissolve(0.8)
        Kiara "Thanks for understanding , bye azumi"
        scene bg kiascooldtno 4 with Dissolve(0.8)
        Sato "Sweety are you okay?"
        Azumi "Y-Yes.. Uncle i'll go back home i'ma bit tired."
        jump chap_2_scene_6



label chap_2_scene_6:

    # SCENE - > kiacfescn =
    scene bg kiacafescn 1 with Dissolve(0.8)
    Kiara "Okay , now for the cafe"
    scene bg kiacafescn 2 with Dissolve(0.8)
    Kiara "This might take quite a while honestly , are you okay with that?"
    TaxiDriver "I don't mind it at all"
    scene bg kiacafescn 3 with Dissolve(0.8)
    Kiara "Thank you , doing it alone would've been annoying"
    scene bg kiacafescn 4 with Dissolve(0.8)
    Kiara "*Phone rings* Hm? Natsuko?"
    scene bg kiacafescn 5 with Dissolve(0.8)
    Kiara "Hey natsu sup?"
    Natsuko "Hey will you be late? Me and mom are back but i have to bounce for a party so"
    scene bg kiacafescn 6 with Dissolve(0.8)
    Kiara "Oh yea , it might take me a while don't worry my phone is still charged enough"
    Natsuko "Okay sure , just ping me if you need help alright?"
    scene bg kiacafescn 7 with Dissolve(0.8)
    Kiara "I will but don't worry i found a decent cab , he knows english as well"
    Natsuko "Oh nice! , alright in case you arrive early food is on the side table okay?"
    Kiara "Got it, thanks!"
    scene blackscreen
    show titletext "Shubhashira Coffee" with dissolve
    pause 1.0
    window hide
    scene bg kiacafescn 8 with Dissolve(0.8)
    Kiara "(Okay , this one's probably gonna be quick)"
    scene bg kiacafescn 9 with Dissolve(0.8)
    pause
    scene bg kiacafescn 10 with Dissolve(0.8)
    Kiara "Seems quite empty for a city coffee shop.."
    scene bg kiacafescn 11 with Dissolve(0.8)
    pause
    scene bg kiacafescn 12 with Dissolve(0.8)
    Genji "Hello ms, what would you like?"
    scene bg kiacafescn 13 with Dissolve(0.8)
    Kiara "Oh i'm here for the waitress job.. the ad agency name's Kiara"
    Genji "Yes but it said a japanese resident?"
    scene bg kiacafescn 14 with Dissolve(0.8)
    Kiara "I'm a resident and i'm mixed as well so yes"
    Genji "Do you have any expirience working as a waitress before?"
    scene bg kiacafescn 15 with Dissolve(0.8)
    Genji "Even if not , It is alright let us discuss further in office"
    Kiara "Sure , right behind you"
    scene bg kiacafescn 16 with Dissolve(0.8)
    pause
    scene bg kiacafescn 17 with Dissolve(0.8)
    Kiara "*Whisper* Hey wish me luck!"
    scene bg kiacafescn 18 with Dissolve(0.8)
    "Girl in cafe" "(She's very beautiful)"
    scene bg kiacafescn 19 with Dissolve(0.8)
    "Girl in cafe" "Good luck~"
    scene bg kiacafescn 20 with Dissolve(0.8)
    pause
    scene bg kiacafescn 21 with Dissolve(0.8)
    "Girl with boyfriend" "Hm?"
    scene bg kiacafescn 22 with Dissolve(0.8)
    pause
    scene bg kiacafescn 23 with Dissolve(0.8)
    pause
    scene bg kiacafescn 24 with Dissolve(0.8)
    Genji "I am very glad you've arrived , We are placed greatly but need someone to attend guests as i'm too old for the counter"
    scene bg kiacafescn 25 with Dissolve(0.8)
    Genji "Please sit , let us discuss your terms"
    Kiara "Sure , thank you"
    scene bg kiacafescn 26 with Dissolve(0.8)
    Kiara "So have you read the resume from the agency? I am doing a temporary job so-"
    Genji "I have not but if you are approved from the agency i do not have further questions , We'd love to have you full time of course but that's upto you"
    scene bg kiacafescn 27 with Dissolve(0.8)
    Genji "We are more than happy to your terms , I might hire one more just so you can have company here as well"
    Kiara "That's great , any help is more than welcome"
    scene bg kiacafescn 28 with Dissolve(0.8)
    Kiara "So the pay is hourly right? or is for service?"
    Genji "It is , you can take the tips fully as well"
    scene bg kiacafescn 29 with Dissolve(0.8)
    Kiara "That's great , i am also new to it so please guide me through it"
    Genji "Yes yes , I would gladly-(Gladly guide those breasts too with my hands)"
    Kiara "Sir?"
    scene bg kiacafescn 30 with Dissolve(0.8)
    Genji "Yes , I'll assist you do not worry"
    scene bg kiacafescn 31 with Dissolve(0.8)
    Genji "Are you aware with the outfit required however ? Do you have one?"
    scene bg kiacafescn 32 with Dissolve(0.8)
    Kiara "Um no . I was skimming through the ad i might've missed it , what is it?"
    scene bg kiacafescn 33 with Dissolve(0.8)
    Genji "The cafe has a watiress dress , you can grab yours or we can get it made for you"
    Kiara "Er I have no clue where to get one , could you help me?"
    scene bg kiacafescn 34 with Dissolve(0.8)
    Kiara "I mean , it's just a waitress dress right? Who makes them?"
    Genji "We get them made here , we have a tailor"
    scene bg kiacafescn 35 with Dissolve(0.8)
    Kiara "Oh who?"
    Genji "You're looking at him! , all it would take is just a small measurement"
    scene bg kiacafescn dcd  with Dissolve(0.8)
    Genji "Shall we get started? It would take barely 10 minutes"
    Kiara "Oh i- (This doesn't seem right.. why would he measure if i can get it custom made too?.. what do i do?)"
    # #CHOICE -> Kiara dialogue -> Let him take ( + Corruption / can only do if corruption reached 10) ,  Make an excuse.( No corruption)
    menu:
        "Let him take" if mc_stats.current_corruption >= 10:
            jump .part_1
        # "Let him take" if mc_stats.current_corruption <= 10:
        #     jump .part_1
        "Make an excuse":
            jump .part_2

    label .part_1:
        # #IF LET HIM TAKE THEN USE RENDERS OF FOLDER -  msrmntyes ->
        scene bg msrmntaccpt 1 with Dissolve(0.8)
        Kiara "Right sure ( I shouldn't be so suspicious of everyone he's just an old man)"
        scene bg msrmntaccpt 2 with Dissolve(0.8)
        Genji "Very well let us get started"
        scene bg msrmntaccpt 3 with Dissolve(0.8)
        Genji "Please stay stil"
        Kiara "Um won't you need measuring tape?"
        scene bg msrmntaccpt 4 with Dissolve(0.8)
        Genji "No , these hands are expirienced Kiara-san , fret not"
        Kiara "Alright ( Why do i feel like I'll regret this )"
        scene bg msrmntaccpt 5 with Dissolve(0.8)
        Genji "Please stay still"
        scene bg msrmntaccpt 6 with Dissolve(0.8)
        Genji "Hmmm"
        scene bg msrmntaccpt 7 with Dissolve(0.8)
        Genji "Argh.. Hm"
        scene bg msrmntaccpt 8 with Dissolve(0.8)
        Kiara "Is.. everything okay?"
        scene bg msrmntaccpt 9 with Dissolve(0.8)
        Genji "Kiara-san , the jacket is coming in the way would you please remove it?"
        Kiara "Uh-- alright sure (It's just measurements)"
        scene bg msrmntaccpt 10 with Dissolve(0.8)
        Genji "Please feel comfortable"
        scene bg msrmntaccpt 11 with Dissolve(0.8)
        Kiara "(Comfortable? He knows i'm wearing a tank top.. ugh whatever)"
        scene bg msrmntaccpt 12 with Dissolve(0.8)
        Kiara "Alright is it fine now?"
        scene bg msrmntaccpt 13 with Dissolve(0.8)
        Genji  "Yes very good , Shall i begin"
        Kiara "Sure alright please make it quick i have to go soon"
        scene bg msrmntaccpt 14 with Dissolve(0.8)
        Genji "I'll do my best ,please stay still"
        scene bg msrmntaccpt 15 with Dissolve(0.8)
        Genji "We have to not rush this process , we don't want lose clothing or too tight do we"
        Kiara "Yeah , certainly (Why is he grabbing my waist?)"
        scene bg msrmntaccpt 16 with Dissolve(0.8)
        Genji "Clothes not only make the man but the woman too , presentation matters above anything"
        scene bg msrmntaccpt 17 with Dissolve(0.8)
        Kiara "( His hands are just crusing through , why can't he do this faster )"
        Genji "( Such soft skin , what would i not give to measure it with my lips )"
        scene bg msrmntaccpt 18 with Dissolve(0.8)
        Genji "The back management is very neccessary , we don't want you to have any problems while on service"
        scene bg msrmntaccpt 19 with Dissolve(0.8)
        Genji " The waist is very required too , it is crucial to be able to turn without issues"
        scene bg msrmntaccpt 20 with Dissolve(0.8)
        Genji "As you can see if it was like this skirt , it'd be very hard to move quickly"
        Kiara "(I get what he's saying but can he not have his hands on my ass the entire time..)"
        scene bg msrmntaccpt 21 with Dissolve(0.8)
        Genji "(What a lovely behind , I would love to measure this without the skirt too)"
        scene bg msrmntaccpt 22 with Dissolve(0.8)
        Genji "The legs are very important as well , we want ample distance to be walking"
        Kiara "Right. (B- but don't waitresses usually have skirts?)"
        scene bg msrmntaccpt 23 with Dissolve(0.8)
        Kiara "(His hands are just rubbing my inner thighs.. this feels so wrong)"
        scene bg msrmntaccpt 24 with Dissolve(0.8)
        Genji "The thighs are very important , we want the space measured so you can sit without worrying about stretch in clothing"
        scene bg msrmntaccpt 25 with Dissolve(0.8)
        Kiara "(This is gross he's just sliding his hands upwards)"
        scene bg msrmntaccpt 26 with Dissolve(0.8)
        Genji "(Let's see how far can i push it)"
        scene bg msrmntaccpt 27 with Dissolve(0.8)
        Genji "The inner thigh is very important as well"
        scene bg msrmntaccpt 28 with Dissolve(0.8)
        Genji "Muscles of glutes are what define clothing fitting"
        scene bg msrmntaccpt 29 with Dissolve(0.8)
        Genji "Specially this one"
        Kiara "Ah! um"
        scene bg msrmntaccpt 29ptwo  with Dissolve(0.8)
        Genji "As you can see the diameter is much more than the skirt you're wearing now"
        scene bg msrmntaccpt 30 with Dissolve(0.8)
        Kiara "Sir , would that be not enough? .. I kinda have to go"
        scene bg msrmntaccpt 31 with Dissolve(0.8)
        Genji "Yes yes , that will be all"
        scene bg msrmntaccpt 32 with Dissolve(0.8)
        Genji "Now let us finish with shoulders ( I don't want to push too far too soon )"
        scene bg msrmntaccpt 33 with Dissolve(0.8)
        Kiara "Do you do this to every waitress , I mean for the clothes?"
        Genji "Yes!, It is needed as we want you to work without worrying about the wardrobe"
        scene bg msrmntaccpt 34 with Dissolve(0.8)
        Genji "(Damn.. I wanted to see abit more skin.. maybe i should try this)"
        scene bg msrmntaccpt 35 with Dissolve(0.8)
        Genji "Aah!"
        scene bg msrmntaccpt 36 with Dissolve(0.8)
        pause
        scene bg msrmntaccpt 37 with Dissolve(0.8)
        Kiara "Shit! hey-"
        scene bg msrmntaccpt 38 with Dissolve(0.8)
        Kiara "Please grab my hand!"
        scene bg msrmntaccpt 39 with Dissolve(0.8)
        Genji  "I- yes"
        scene bg msrmntaccpt 40 with Dissolve(0.8)
        pause
        scene bg msrmntaccpt 41 with Dissolve(0.8)
        Kiara "Are you okay? sorry i was focused on something else"
        scene bg msrmntaccpt 42 with Dissolve(0.8)
        Kiara "Is it - *Looks down*"
        scene bg msrmntaccpt 43 with Dissolve(0.8)
        Kiara "*Gasp* give me a moment please"
        scene bg msrmntaccpt 44 with Dissolve(0.8)
        Genji "It's alright , sorry for your clothes"
        Kiara "No it's fine , I'm sorry too for not catching you earlier"
        scene bg msrmntaccpt 45 with Dissolve(0.8)
        Kiara "Well , I'll get going then"
        Genji "We'll await you , the dress will be done on monday feel free to come afterwards"
        scene bg msrmntaccpt 46 with Dissolve(0.8)
        Kiara "Sure , thank you (God i'm glad i was wearing bra)"
        scene bg msrmntaccpt 47 with Dissolve(0.8)
        Genji "Good day kiara-san (One day i'll measure your insides as well..)"
        $ renpy.end_replay()
        $ mc_stats.adjust_corruption(5)
        jump chap_2_scene_7
    
    label .part_2:
        # IF MAKE AN EXCUSE THEN USE RENDERS OF FOLDER -> msrmntno ->
        scene bg msrmntrjct 1  with Dissolve(0.8)
        Kiara "Um actually i have a interview very soon , I really don't want to be late is that okay?"
        scene bg msrmntrjct 2 with Dissolve(0.8)
        Genji "Oh i understand , it won't take long let me get started"
        Kiara "No i know but i have to leave now sorry"
        scene bg msrmntrjct 3 with Dissolve(0.8)
        Kiara "I'll get the dress made , my mom knows a friend"
        Genji "Oh , will it fit you well"
        scene bg msrmntrjct 4 with Dissolve(0.8)
        Genji "Clothing is what makes a woman too along with man"
        Kiara "Don't worry she even made my Gi and her clothes fit me so i'll be fine"
        Genji "Very well then ( Don't want to lose this one , not gonna push here )"

        jump chap_2_scene_7

label chap_2_scene_7:


    # SCENE -> kiasalonscn ->
    scene bg kiasalonscn 1 with Dissolve(0.8)
    Kiara "What a nuisance.."
    scene bg kiasalonscn 2 with Dissolve(0.8)
    TaxiDriver "All good back there?"
    scene bg kiasalonscn 3 with Dissolve(0.8)
    Kiara "Oh you know.. Making and breaking , adulting is hard. Do you make enough by doing this cab thing?"
    scene bg kiasalonscn 4 with Dissolve(0.8)
    TaxiDriver "Pays the bills , covers the roof  what else can i ask for?"
    scene bg kiasalonscn 5 with Dissolve(0.8)
    Kiara "(Did he just say what i?.. ) Um yeah"
    scene bg kiasalonscn 6 with Dissolve(0.8)
    Kiara "You missed one thing though"
    scene bg kiasalonscn 7 with Dissolve(0.8)
    TaxiDriver "Oh yeah? What's that?"
    Kiara "I'll tell you once this next one is done for"
    scene blackscreen
    show titletext "Style like none , City center" with dissolve
    pause 1.0
    window hide
    scene bg kiasalonscn 8 with Dissolve(0.8)
    Kiara "Hm , i wouldn't mind trying out a new style either anyway that's for later"
    scene bg kiasalonscn 9 with Dissolve(0.8)
    Asa "Hello over there , can i help you?"
    Kiara "I am here for the job posting , a hairstylist?"
    scene bg kiasalonscn 10 with Dissolve(0.8)
    Asa "Oh i see , yes yes , we needed one more"
    Kiara "Yeah I've interened at barbers previously and style and dye my own hair so"
    scene bg kiasalonscn 11 with Dissolve(0.8)
    Asa "All of us start somewhere , but my boss is who decides it so let me get her?"
    scene bg kiasalonscn 12 with Dissolve(0.8)
    Kiara "Okay , where's your boss?"
    scene bg kiasalonscn 13 with Dissolve(0.8)
    Asa "She's on a call , I'll go get her for you I won't be long"
    Kiara "Take your time"
    scene bg kiasalonscn 14 with Dissolve(0.8)
    Kiara "(She's quite nice)"
    scene bg kiasalonscn 15 with Dissolve(0.8)
    pause
    scene bg kiasalonscn 16 with Dissolve(0.8)
    pause
    scene bg kiasalonscn 17 with Dissolve(0.8)
    Hideo "Hm?"
    scene bg kiasalonscn 18 with Dissolve(0.8)
    Hideo "Psst , asuka"
    scene bg kiasalonscn 19 with Dissolve(0.8)
    Asuka "What?"
    Hideo "Look over there , i think that's our new partner"
    scene bg kiasalonscn 20 with Dissolve(0.8)
    Asuka "Oh , she has great hair"
    scene bg kiasalonscn 21 with Dissolve(0.8)
    Kiara "Hello there"
    scene bg kiasalonscn 22 with Dissolve(0.8)
    Hideo "Hey there , just one second"
    scene bg kiasalonscn 23 with Dissolve(0.8)
    Kiara "You don't have to run its okay, hi"
    scene bg kiasalonscn 24 with Dissolve(0.8)
    Hideo "Sorry , I'm hideo yo. You are?"
    scene bg kiasalonscn 25 with Dissolve(0.8)
    Asuka "Idiot!"
    Hideo "Ow!"
    scene bg kiasalonscn 26 with Dissolve(0.8)
    Hideo "What was that for?"
    Asuka "Is that how you greet someone?"
    scene bg kiasalonscn 27 with Dissolve(0.8)
    Kiara "It's okay don't hit him"
    Asuka "You don't know him , he's a bafoon anyway let's sit"
    scene bg kiasalonscn 28 with Dissolve(0.8)
    Asuka "I'm asuka , this is hideo my cousin"
    Kiara "I'm kiara , are you two working here from start?"
    Hideo "(Man she's pretty)"
    scene bg kiasalonscn 29 with Dissolve(0.8)
    Asuka "So you're from america right?"
    Kiara "Yeah but my home is here for now its in shinji district"
    scene bg kiasalonscn 30 with Dissolve(0.8)
    Asuka "That's great , I live there too let's hangout sometime"
    scene bg kiasalonscn 31 with Dissolve(0.8)
    Hideo "Yeah you'd love it , besides it'd be cool to know your culture as well , you guys have got like halloween and stuff right?"
    Asuka "Anyone asked for your opinion?"
    scene bg kiasalonscn 32 with Dissolve(0.8)
    Kiara "Don't be so rough on him haha ,  thank you Hideo"
    scene bg kiasalonscn 33 with Dissolve(0.8)
    Asuka "We'd be glad to have you , you also have wonderful hair by the way"
    Kiara "Thank you asuka , yours is great too"
    scene bg kiasalonscn 34 with Dissolve(0.8)
    Hideo "I think you'd enjoy here , we're small but rose is great and very helpful"
    scene bg kiasalonscn 35 with Dissolve(0.8)
    Asa  "He's not wrong on that , Rose is the best boss"
    Hideo "Oh hey asa"
    scene bg kiasalonscn 36 with Dissolve(0.8)
    Asa "You two done bothering her?"
    Kiara "No they weren't bothering me haha , so is she free?"
    scene bg kiasalonscn 37 with Dissolve(0.8)
    Asa "Yes go on ahead to the left room at end"
    Kiara "Alright , see ya guys"
    Asuka "See ya"
    Hideo "Stay cool!"
    scene bg kiasalonscn 38 with Dissolve(0.8)
    u "Did you still not finish the design , wow"
    scene bg kiasalonscn 39 with Dissolve(0.8)
    u "I wanted it today you know , but you are lazy as usual"
    scene bg kiasalonscn 40 with Dissolve(0.8)
    u "Well to be fair i am lazy too so it's fine"
    scene bg kiasalonscn 41 with Dissolve(0.8)
    u "But please get it done by weekend okay?"
    scene bg kiasalonscn 42 with Dissolve(0.8)
    Kiara "Um hi? am i bothering?"
    u "O-hey! it's you!"
    scene bg kiasalonscn 43 with Dissolve(0.8)
    Rose "Hi , Kiara right?"
    #revealing rose stats 
    $ rose_stats_hidden = False

    scene bg kiasalonscn 44 with Dissolve(0.8)
    Rose "Why are you standing , Come sit"
    Kiara "Ah! okay.. (She's quite formal)"
    scene bg kiasalonscn 45 with Dissolve(0.8)
    Rose "I am so glad you're here , i saw your resume from agency and just kept waiting"
    Kiara "Oh.. but didn't you have multiple ones for approval?"
    scene bg kiasalonscn 46 with Dissolve(0.8)
    Rose "I did , but it was hard to ignore yours you look fantastic by the way"
    Kiara "Well thanks.. i - you look great too."
    scene bg kiasalonscn 47 with Dissolve(0.8)
    Rose "Do i? don't worry about the job you got it alredy , be honest this dress looks makes me look homeless doesn't it?"
    Kiara  " No of course not , it's very comfortable probably and i love the color as well"
    scene bg kiasalonscn 48 with Dissolve(0.8)
    Rose "Then i'll make sure i get one for you as well"
    Kiara "Haha no need . So um.. i don't really have alot of stylist expirience , i wanted to learn too so can-"
    scene bg kiasalonscn 49 with Dissolve(0.8)
    Rose "I'll help you , so will the guys outside don't worry money ain't the reason i do this , it's passion so if i can share that passion even better then"
    Kiara "thank you , i appreciate that"
    scene bg kiasalonscn 50 with Dissolve(0.8)
    Rose "Speaking of which i love yours , the to the side is great mine never grew that long so can't try it"
    scene bg kiasalonscn 51 with Dissolve(0.8)
    Kiara "Honestly i really like the hood kind you got , it'd be my go to if i had shorter hair too"
    scene bg kiasalonscn 52 with Dissolve(0.8)
    Rose "Also don't mind this but you are easy on the eyes as well , so helps to have a good looking stylist"
    Kiara "Aheh.. Well I-"
    scene bg kiasalonscndcd  with Dissolve(0.8)
    Kiara "(She just flirted.. maybe not?.. How should i respond?)"
    #> CHOICE  with Dissolve(0.8)
    #> Compliment back ( Romance Rose + ) ""
    #Don’t Compliment ( No romance +) ""
    menu:
        "Compliment Back":
            jump .part_1
        "Don't Compliment":
            jump .part_2

    label .part_1:
    # IF COMPLIMENT -> USE RENDERS OF complmntrse ->
        scene bg complmnt 1  with Dissolve(0.8)
        Kiara "Honestly you're underselling yourself here , you're amazing as well"
        Rose "You think so?"
        scene bg complmnt 2 with Dissolve(0.8)
        Kiara "Yeha i mean , early 20's got her life together , got a business and quite good too"
        Rose "Well I'd be more than glad to have you join on this journey then"
        scene bg complmnt 3 with Dissolve(0.8)
        Rose "Honestly even the job aside , I would love to know you more . I mean i moved here for starting a new life , i presume you want the same?"
        Kiara "Yeah i do & I hope i can , thanks to people like you it gets alot easier"
        scene bg dntcomplmnt 4  with Dissolve(0.8)
        Rose "It's just the beginning , you'll enjoy it trust me"
        Kiara "Thanks , I'll be on my way then have a great evening Rose"
        Rose "I will ( I hope i didn't make a fool of myself being too excited )"
        $ rose_rom.adjust_romance(1)
        jump chap_2_scene_8

    label .part_2:
        # IF DON’T COMPLIMENT -> USE RENDERS OF -> dntcomplmntrse ->
        scene bg dntcomplmnt 1 with Dissolve(0.8)
        Kiara "I appreciate you think so , I'm just trying to maintain all that still"
        Rose "You'll do great and if not we're all here to help too"
        scene bg dntcomplmnt 2 with Dissolve(0.8)
        Rose "Well i know you have other interviews already but i appreciate you coming , please consider full time if you like the enviorment here"
        Kiara "Yeah certainly , this all is security i'll only do what i want and i love hair styling so who knows!"
        scene bg dntcomplmnt 3 with Dissolve(0.8)
        Rose "Sorry if i came sorta nutso.. i'm not really haha"
        Kiara "No it's fine , i appreciate it ~ you too take care. I'll get going"
        jump chap_2_scene_8

label chap_2_scene_8:


    # SCENE -> kiagmrscn -
    # 
    scene blackscreen
    show titletext "Downtown Osaka , Evening" with dissolve
    pause 1.0
    window hide
    scene bg kiagmrscn 1 with Dissolve(0.8)
    TaxiDriver "So last one?"
    Kiara "Yep , last one"
    scene bg kiagmrscn 2 with Dissolve(0.8)
    TaxiDriver "You said earlier i missed one thing , what was it?"
    Kiara "Oh.. heh , it was someone to hold on to.."
    scene bg kiagmrscn 3 with Dissolve(0.8)
    TaxiDriver "Oh.. right , that's true too"
    Kiara "You got anyone?"
    scene bg kiagmrscn 4 with Dissolve(0.8)
    TaxiDriver "I had one.. was too late to tell her tho , maybe she now won't accept"
    scene bg kiagmrscn 5 with Dissolve(0.8)
    Kiara "Well maybe talk to her? Who knows she waited for you to make the first move?"
    scene bg kiagmrscn 6 with Dissolve(0.8)
    TaxiDriver "Oh i doubt that very much or well maybe i'm not good enough"
    Kiara "Don't ever discount yourself , thought and care go long way just ask her again okay?"
    TaxiDriver "Alright , I'll give it a go then thanks"
    scene bg kiagmrscn 7 with Dissolve(0.8)
    Kiara "Ha.. I'm very tired , do you mind if i take a nap? just wake me up once we reach since its far i think"
    TaxiDriver "Oh yeah sure , don't worry about it"
    scene bg kiagmrscn 8 with Dissolve(0.8)
    Kiara "Okay small night night"
    TaxiDriver "Rest well."
    scene blackscreen
    show titletext "Late evening , Downtown osaka" with dissolve
    pause 1.0
    window hide
    scene bg kiagmrscn 9 with Dissolve(0.8)
    pause
    scene bg kiagmrscn 10 with Dissolve(0.8)
    pause
    scene bg kiagmrscn 11  with Dissolve(0.8)
    TaxiDriver "What kinda place even is this"
    scene bg kiagmrscn 12 with Dissolve(0.8)
    TaxiDriver "Good thing i came , coming here on her own would've been just tiresome"
    scene bg kiagmrscn 13 with Dissolve(0.8)
    TaxiDriver "Arcadia.. this is it i think"
    scene bg kiagmrscn 14 with Dissolve(0.8)
    TaxiDriver "Hey back there , good morning"
    scene bg kiagmrscn 15 with Dissolve(0.8)
    pause
    scene bg kiagmrscn 16 with Dissolve(0.8)
    Kiara "Ah.. Where?"
    scene bg kiagmrscn 17 with Dissolve(0.8)
    Kiara "What the-.. how long was i out for?"
    TaxiDriver "Quite a while , you're a heavy sleeper"
    scene bg kiagmrscn 18 with Dissolve(0.8)
    Kiara "Uh.. dammit , thanks for not stealing my kidney i guess. Either i sleep too hard or you drive too well"
    TaxiDriver "Haha don't mention it also let's just say both on the second statement"
    scene bg kiagmrscn 19 with Dissolve(0.8)
    TaxiDriver "The cab can't go inside but i'll stay here , let me know if you need help"
    Kiara "Yeah , I-I'll be fine don't worry"
    scene bg kiagmrscn 20  with Dissolve(0.8)
    Kiara "Arcadia , is this the door really?"
    scene bg kiagmrscn 21 with Dissolve(0.8)
    Kiara "What's with this obsession of blue , It's blinding almost"
    scene bg kiagmrscn 22 with Dissolve(0.8)
    pause
    scene bg kiagmrscn 23 with Dissolve(0.8)
    Kiara "Hey there , I-"
    scene bg kiagmrscn 24 with Dissolve(0.8)
    Jako "Heyo , Jako here you wanna game? pc's are empty so feel free"
    scene bg kiagmrscn 25 with Dissolve(0.8)
    Kiara "No I- i uh was here for a job , taka"
    scene bg kiagmrscn 26 with Dissolve(0.8)
    Jako "Your outfit is wack , looks boring"
    Kiara "Excuse me?"
    scene bg kiagmrscn 27 with Dissolve(0.8)
    Kiara "You're gonna call this boring while you're dressed like a homeless hobo?"
    Jako "Ha , I like your style tho very spicy huh"
    scene bg kiagmrscn 28 with Dissolve(0.8)
    Jako "*Phone rings* Taka?"
    scene bg kiagmrscn 29 with Dissolve(0.8)
    Jako "Turns out you're friend of the boss's brother , go on then it's the middle door to your left"
    scene bg kiagmrscn 30 with Dissolve(0.8)
    Jako "(Damn look at that , she kinda bad)"
    scene bg kiagmrscn 31 with Dissolve(0.8)
    Kiara "This many computers?"
    scene bg kiagmrscn 32 with Dissolve(0.8)
    Kiara "I knew gaming was big in asia but didn't think this much"
    scene bg kiagmrscn 33 with Dissolve(0.8)
    Kiara "I guess this is it , Let's go"
    scene bg kiagmrscn 34 with Dissolve(0.8)
    u "Kill the dude what ya doing my g"
    scene bg kiagmrscn 35 with Dissolve(0.8)
    Kiara "Hello there , Kiara here  I-"
    scene bg kiagmrscn 36 with Dissolve(0.8)
    Yamazaki "Hey Kiara! I'm Yama , Taka's brother please come sit"
    Kiara "Thanks (Brother? well that makes sense alright)"
    scene bg kiagmrscn 37 with Dissolve(0.8)
    Yamazaki "Give me just one minute , I'll turn it off"
    scene bg kiagmrscn 38 with Dissolve(0.8)
    Yamazaki "Dude i gotta go , I got a new employee here so peace"
    Kiara "(That computer does look pretty cool)"
    scene bg kiagmrscn 39 with Dissolve(0.8)
    Kiara "So taka told me that a work from home-"
    Yamazaki "Yes yes , i talked to him already , please sit let's discuss"
    scene bg kiagmrscn 40 with Dissolve(0.8)
    Yamazaki "It's a work from home job , I'm so sorry you had to come so far for the interview had i known earlier i'd have arranged a meeting on call"
    Kiara "It's fine.. so um i don't really have expirience here , what do i do ?"
    scene bg kiagmrscn 41 with Dissolve(0.8)
    Yamazaki "You're going to be a sponsored streamer!"
    Kiara "But i don't really play games that much , i mean i've tried but i'm kinda bad at them"
    scene bg kiagmrscn 42 with Dissolve(0.8)
    Yamazaki "Everyone starts there , Don't worry"
    scene bg kiagmrscn 43 with Dissolve(0.8)
    Kiara "So what will i have to do exactly?"
    Yamazaki "Well you're gonna stream a sponsored game or some stream , you entertain fans gain audience and yeah the more people watch , the more money you get!"
    scene bg kiagmrscn 44 with Dissolve(0.8)
    Kiara "So i just play games and get paid?.. I mean even without many viewers?"
    Yamazaki "Yes , It's a salary job anyway but let's say you do something like play a specific game or do something for fans like charity event , that money is yours too after our 15 pecent cut"
    scene bg kiagmrscn 45  with Dissolve(0.8)
    Yamazaki "Best thing about this job is , we'll deliver a sweet rig to your place as well so all you have to do is just set it up and start"
    Kiara "That sounds easy enough.. um so can i go then?"
    Yamazaki "Yeah you're free to go , we have the address already thanks to your resume so"
    scene bg kiagmrscn 46 with Dissolve(0.8)
    Kiara "Well see ya then"
    Yamazaki "Call me if you need help during setup okay!"
    scene bg kiagmrscn 47  with Dissolve(0.8)
    Yamazaki "( I'll pray she enjoys streaming , also dammit taka i hope you're nice to her )"
    jump chap_2_scene_9


label chap_2_scene_9:
    # SCENE -> kiabathroom ->
    scene bgkiabathroom 1  with Dissolve(0.8)
    Kiara "Okay , I'll just take itt and leave for home"
    scene bgkiabathroom 2 with Dissolve(0.8)
    Kiara "what's with the blue everywhere .. ah , he bettter have a explanation for this"
    scene bgkiabathroom 3 with Dissolve(0.8)
    pause
    scene bgkiabathroom 4 with Dissolve(0.8)
    pause
    scene bgkiabathroom 5 with Dissolve(0.8)
    Kiara "Alright , I'll just take a shower at home anyway it's fine"

    label .part_4:
        scene bgkiabathroom 6 with Dissolve(0.8)
        Kiara "Whew.. what a relief , day went better than i thought honestly"
        scene bgkiabathroom 7 with Dissolve(0.8)
        Kiara "That said though i have to decide a roadmap for this many things to do"
        scene bgkiabathroom 8 with Dissolve(0.8)
        Kiara "Huh? the lights , what the-"
        scene bgkiabathroom 9 with Dissolve(0.8)
        Kiara "He-.. oh they're back"
        scene bgkiabathroom 10 with Dissolve(0.8)
        Kiara "Weird , you'd expect a gaming cafe to not have power cuts , anyway let's g-"
        scene bgkiabathroom 11 with Dissolve(0.8)
        Kiara "Wh-- what the? where's my"
        Jako "Hey you in there , all good? Lights just went out"
        scene bgkiabathroom 12 with Dissolve(0.8)
        Kiara "It was a power a cut..um excuse me what are you doing in the ladies bathroom?"
        Jako "At night it's a mixed one babe"
        scene bgkiabathroom 13 with Dissolve(0.8)
        Kiara "What the-.. uh , (whatever) Um have you seen my skirt? It was here and power went out i think i kicked it out by accident"
        scene bgkiabathroom 14 with Dissolve(0.8)
        Jako "Oh no you didn't kick it out , I stole it"
        Kiara "WHAT?! Hey give it back!"
        scene bgkiabathroom 15 with Dissolve(0.8)
        Jako "No problem babe , but ima need something first"
        Kiara "W-.. what?"
        scene bgkiabathroom 16 with Dissolve(0.8)
        Jako "I'll give your skirt back , but i want your panties for 10 seocnds"
        Kiara "Are you fucking serious? hey cut it out return it!"
        Jako "I will , cross my heart just need your panties for 10 seconds"
        scene bgkiabathroom 17 with Dissolve(0.8)
        Kiara "(What the hell.. is he for real?)"
        scene bgkiabathroom dcd  with Dissolve(0.8)
        Kiara "What do i do here? I just wanna go home"
    #> CHOICE  with Dissolve(0.8)
    #> CALL HIS BOSS ( + No Corruption) 
    #Give panties (REQUIRES 20 CORRUPTION) (ALSO  + Corruption) 
    if _in_replay:
        jump .part_2
    menu:
        "Call his boss":
            jump .part_1
        "Give panties" if mc_stats.current_corruption >= 20:
            jump .part_2

    label .part_1:
        # IF CALL HIS BOSS CHOICE -> USE RENDERS OF callboss ->
        scene bgkiabathcallboss  1 with Dissolve(0.8)
        Kiara "(Right! , I have yamazaki's number.)"
        scene bgkiabathcallboss  2 with Dissolve(0.8)
        Kiara "Hey you out there , Give it back now or i'll fucking call your boss and complain"
        Jako "You're bluffing , you don't got his number"
        scene bgkiabathcallboss  3 with Dissolve(0.8)
        Kiara "Oh you think i don't , Just you fucking wait"
        Jako "What the-"
        scene bgkiabathcallboss  4 with Dissolve(0.8)
        Jako "If she calls him i'm done for , ain't no pussy worth losing this job"
        Kiara "Hello? Yama?"
        scene bgkiabathcallboss  5 with Dissolve(0.8)
        Jako  "Relax relax , It's at the door handle just fucking take it. Bye"
        scene bgkiabathcallboss  6 with Dissolve(0.8)
        Kiara "Ugh.. what a asshole"
        scene bgkiabathcallboss  7 with Dissolve(0.8)
        Kiara "Where the fuck is he..?"
        scene bgkiabathcallboss  8 with Dissolve(0.8)
        Kiara "Whatever.. let's just head home"
    jump .part_3

    label .part_2:
        # IF CHOICE GIVE PANTIES -> USE RENDERS OF givepanties ->
        scene bgbathkiagivepants 1 with Dissolve(0.8)
        Kiara "I really don't want to bother this on the first day.. I'll just give them and he'll leave then"
        scene bgbathkiagivepants 2 with Dissolve(0.8)
        Kiara "Fine , you can have them.. please stand back"
        Jako "Don't worry take your time"
        scene bgbathkiagivepants 3 with Dissolve(0.8)
        Kiara "Ugh.. you're gross"
        Jako "If i was i'd be peeking , which i'm not"
        scene bgbathkiagivepants 4 with Dissolve(0.8)
        Kiara "Yeah jee what a gentleman , fucking asshole"
        scene bgbathkiagivepants 5 with Dissolve(0.8)
        Kiara "I can't believe this .. is this seriously happening?"
        scene bgbathkiagivepants 6 with Dissolve(0.8)
        Kiara "Ugh , they're at the door.. please return quickly"
        Jako "Yes just a bit few seconds!"
        scene bgbathkiagivepants 7 with Dissolve(0.8)
        Jako "Stand back i don't wanna see anything"
        Kiara "(Fucking weirdo..)"
        scene bgbathkiagivepants 8 with Dissolve(0.8)
        Jako "Hm.. these are nice.. so you're like butt naked in there huh?"
        Kiara "W-.. why do you care , just return quickly"
        scene bgbathkiagivepants 9 with Dissolve(0.8)
        Jako "Relax , man i bet your ass is smooth this fiber is pretty high quality"
        Kiara "The fact you know the fiber of women underwear is just gross"
        scene bgbathkiagivepants 10 with Dissolve(0.8)
        Jako "Heh , *Sniff* man you smell nice too i bet you take care down there"
        Kiara "Can you not fucking do this?"
        scene bgbathkiagivepants 11 with Dissolve(0.8)
        Jako "What? I'm complimenting you , You shave right? I can smell the scent"
        Kiara "Ugh.. ( I hate this )"
        scene bgbathkiagivepants 12 with Dissolve(0.8)
        Kiara "Please return it.. I'm begging you"
        Jako "Whoa whoa , chill here I'm done just a prank babe"
        scene bgbathkiagivepants 13 with Dissolve(0.8)
        Jako "There you go , I'ma buzz off now"
        Kiara "Thank god he returned both of them"
        scene bgbathkiagivepants 14 with Dissolve(0.8)
        Kiara "Ugh , what a fucking asshole"
        scene bgbathkiagivepants 15 with Dissolve(0.8)
        Kiara "Where the hell is he?"
        scene bgbathkiagivepants 16 with Dissolve(0.8)
        Kiara "Whatever.. let's just go home"

        $ renpy.end_replay()

        $ mc_stats.adjust_corruption(5)
    jump .part_3

    label .part_3:
        # CANON RESUME ->
        scene bg kiagmrscn 48 with Dissolve(0.8)
        TaxiDriver "Well that's great , free carwash"
        scene bg kiagmrscn 49 with Dissolve(0.8)
        Kiara "What a fucking idiot.. people sometimes ugh"
        scene bg kiagmrscn 50 with Dissolve(0.8)
        Kiara "Oh you've got to be kidding me"
        scene bg kiagmrscn 51 with Dissolve(0.8)
        Kiara "It had to rain now too? how did this day start so good and end weird"
        scene bg kiagmrscn 52 with Dissolve(0.8)
        TaxiDriver "Hey! , come on in!"
        Kiara "Yeah just keep door open!"
        scene bg kiagmrscn 53 with Dissolve(0.8)
        Kiara "Aw man , why did it have to rain?"
        TaxiDriver "Had any more plans?"
        Kiara "Oh just wanted to join a yoga class . It is what it is i guess"
        scene bg kiagmrscn 54 with Dissolve(0.8)
        TaxiDriver "That's okay you're here for long anyway , no problem"
        Kiara "Yeah you're right , well let's head home"
        scene bg kiagmrscn 55 with Dissolve(0.8)
        Kiara "You know the one thing i learned today is to just plan things better"
        TaxiDriver "Tell me about it haha"
        scene bg kiagmrscn 56 with Dissolve(0.8)
        Kiara "Sorry you probably thought it'd be a small ride and here you are since noon"
        TaxiDriver "It all comes with the job , no worries"
        scene bg kiagmrscn 57 with Dissolve(0.8)
        Kiara "This jacket got wet.. let me just-"
        scene bg kiagmrscn 58 with Dissolve(0.8)
        pause
        scene bg kiagmrscn 59 with Dissolve(0.8)
        TaxiDriver "Um"
        scene bg kiagmrscn 60 with Dissolve(0.8)
        TaxiDriver  "No.. what am i doing , I'm sorry miss"
        scene bg kiagmrscn 61 with Dissolve(0.8)
        Kiara "Hm? sorry for what?"
        TaxiDriver "I was - I was just looking to check if you're okay i didn't mean to stare when you were taking off your jacket . I Apologize"
        scene bg kiagmrscn 62 with Dissolve(0.8)
        Kiara "Aheh (There's that guy and there's people like this.. what a mix)"
        TaxiDriver "I hope you're not angry , I can discount the ride if so"
        scene bg kiagmrscn 63 with Dissolve(0.8)
        Kiara "It's fine chill , um.. you're a good person"
        TaxiDriver "Good? how so?"
        scene bg kiagmrscn 64 with Dissolve(0.8)
        Kiara "I won't explain why , just remember you're a good one"
        TaxiDriver "Well free compliments are something i always accept so thanks"
        scene bg kiagmrscn 65 with Dissolve(0.8)
        TaxiDriver "By the way should we help that guy?"
        Kiara "Huh?"
        scene bg kiagmrscn 66 with Dissolve(0.8)
        Alex "Fuckin a great , had to rain now didn't it"
        scene bg kiagmrscn 67 with Dissolve(0.8)
        Alex "I was just grabbing food , dammit everything is closed too"
        scene bg kiagmrscn 68 with Dissolve(0.8)
        Kiara "HEY! ALEX!"
        Alex "Wh-? is that?"
        scene bg kiagmrscn 69 with Dissolve(0.8)
        Kiara "COME ON IN! , IT'S EMPTY HERE"
        Alex "Talk about being an actual angel"
        scene bg kiagmrscn 70 with Dissolve(0.8)
        Alex "Comin , keep door side open"
        Kiara "Yes yes!"
        scene bg kiagmrscn 71 with Dissolve(0.8)
        Alex "Got lucky .. man it sure is heavy today isn't it?"
        scene bg kiagmrscn 72 with Dissolve(0.8)
        Kiara "Yeah we are in japan and on top of that rainy season after all so"
        scene bg kiagmrscn 73 with Dissolve(0.8)
        Alex "True that , what happened to your jacket aren't you getting cold?"
        Kiara "I'm fine , it got wet so i'd rather just relax , sorry if it's uncomfortable for you"
        Alex "No I'm good just don't catch a cold or something"
        scene bg kiagmrscn 74 with Dissolve(0.8)
        Kiara "So you and i both got jobs today"
        Alex "Oh yeah i saw your profile resume , must be nice huh"
        scene bg kiagmrscn 75 with Dissolve(0.8)
        Alex "Man walkig through this would've been a pain , thanks kiara"
        Kiara "Don't mention it , so how was your first day at work?"
        scene bg kiagmrscn 76 with Dissolve(0.8)
        Alex "It was fine , you know how executive support is usually"
        Kiara "I'll know soon enough but i do have an idea"
        scene bg kiagmrscn 77 with Dissolve(0.8)
        Kiara "So I forgot to ask , where are you from in states?"
        Alex "Boston , moved here because i've kinda liked japan for a while"
        scene bg kiagmrscn 78 with Dissolve(0.8)
        Kiara "Well let's hope work is easy , i have options idk about yours so yeah"
        Alex "Same , i can't exactly be a waitress haha"
        Kiara "Hey you never know!"
        scene bg kiagmrscn 79 with Dissolve(0.8)
        Alex "Ah . dammit ( Why is she calling me now of all times )"
        Kiara "What's wrong?"
        scene bg kiagmrscn 80 with Dissolve(0.8)
        Alex "Oh it's just.. my girlfriend , we're kinda a new couple so yknow"
        Kiara "Oh i get that , well pick it up unless its too personal"
        Alex "No actually , we're kinda having a rough patch at the moment so"
        scene bg kiagmrscn 81 with Dissolve(0.8)
        Kiara "Then talk to her now , rough patches get resolved after communication you know"
        Alex "Uh , yeah but i- okay."
        scene bg kiagmrscn 82 with Dissolve(0.8)
        Alex "H-hey lucy , sorry i was with someone i met in office today"
        Valentina "(Office? .. this must be kiara ) Oh , hi yeah are you busy?"
        scene bg kiagmrscn 83 with Dissolve(0.8)
        Valentina "I mean do you wanna talk when free"
        Alex "Yeah i uh , we can talk when free"
        Kiara "Psst talk to her now!"
        scene bg kiagmrscn 84 with Dissolve(0.8)
        Alex "I was just wondering.. what are you having for dinner?"
        Valentina "Um , just some fries.. you had dinner?"
        scene bg kiagmrscn 85 with Dissolve(0.8)
        Kiara "Oh god , gimme the phone"
        Alex "No - w-wait uh"
        scene bg kiagmrscn 86 with Dissolve(0.8)
        Kiara "Hey Lucy , this is kiara i am so sorry for hitting him today i didn't mean to"
        Valentina "(hit him?) Oh no he told me it's fine , besides that is still better than the other hitting on"
        scene bg kiagmrscn 87 with Dissolve(0.8)
        Kiara "Haha don't worry no such thing , so i wanted to tell you he was worried about you actually"
        Valentina "Worried about me? why?"
        scene bg kiagmrscn 88 with Dissolve(0.8)
        Valentina "I mean what is he saying?"
        Kiara "I mean i'm no one to comment here but i think you're both going through something rough rn"
        scene bg kiagmrscn 89 with Dissolve(0.8)
        Kiara  "Look i think he's a really nice guy and again i don't know what's happening but i would say give it a second chance , he was very upset all day even figuring out what roses you'd like"
        Valentina "Oh .. wow well i like white roses and yes i'll consider what you said again, can i um talk to him?"
        scene bg kiagmrscn 90 with Dissolve(0.8)
        Alex "Hi lucy , so lets talk when back home?"
        Kiara  "*quietly* Hey tell her-"
        scene bg kiagmrscn 91 with Dissolve(0.8)
        Kiara "Tell her you love her!"
        Alex "Um.. uh wait lucy."
        Valentina "Y-yes?"
        scene bg kiagmrscn 92 with Dissolve(0.8)
        Alex "I- uh , I love you babe please take care"
        Valentina "(Heh , never thought id hear that from aiden's mouth) I love you too , talk soon"
        scene bg kiagmrscn 93 with Dissolve(0.8)
        Kiara "See ? was that so hard?"
        Alex "No , it wasn't."
        scene bg kiagmrscn 94 with Dissolve(0.8)
        Kiara "Look even the rain stopped , it's a good sign!"
        scene bg kiagmrscn 95 with Dissolve(0.8)
        Kiara "I'll see you on monday okay? Bye!"
        Alex "Yeah , Laters"
        scene bg kiagmrscn 96 with Dissolve(0.8)
        pause
        scene bg kiagmrscn 97 with Dissolve(0.8)
        Aiden "*Sigh* Jesus.." #(call him aiden here rest is alex)
        scene bg kiagmrscn 98 with Dissolve(0.8)
        pause
        scene bg kiagmrscn 99 with Dissolve(0.8)
        Aiden "Talk about being a strange day"
        scene bg kiagmrscn 100 with Dissolve(0.8)
        Aiden "Should sleep now , i better settle in fast"
        scene bg kiagmrscn 101 with Dissolve(0.8)
        Aiden "*Phone rings* Who could it be now?"
        scene bg kiagmrscn 102 with Dissolve(0.8)
        Valentina "I love you babee , hahahahaha"
        Alex "*sigh* Zip it "
        Valentina "Whattt it was cute the way you said it"
        scene bg kiagmrscn 103 with Dissolve(0.8)
        Alex "Yeah yeah , well now you know too."
        Valentina "Yeah.. i knew that man lied , how is she?"
        Alex "Doing fine it seems , didn't recognize you even"
        scene bg kiagmrscn 104 with Dissolve(0.8)
        Valentina "Seems the memory thing is true.. I'll go to the doctor tomorrow"
        Alex "Good luck with it"
        Valentina "Wait one more thing"
        Alex "Hm?"
        scene bg kiagmrscn 105 with Dissolve(0.8)
        Valentina "Give me a goodnight kiss honey?"
        Alex "Oh fuck off"
        Valentina "Hahahahah , goodnighttt"
        # 
        jump chap_2_scene_10

label chap_2_scene_10:
    scene blackscreen
    show titletext "Home street , Night" with dissolve
    pause 1.0
    window hide
    # SCENE -> kiagdnight ->
    scene bg kiagdnit 1 with Dissolve(0.8)
    Kiara "(What a day , definitely didn't expect it to go this way)"
    scene bg kiagdnit 2 with Dissolve(0.8)
    Kiara "Better get used to it though , it only is the start here"
    TaxiDriver "You will do well , have confidence in yourself that's all"
    scene bg kiagdnit 3 with Dissolve(0.8)
    Kiara "Thanks , I hope so too"
    scene bg kiagdnit 4 with Dissolve(0.8)
    TaxiDriver "We have arrived"
    Kiara "Ahh , home sweet home"
    scene bg kiagdnit 5 with Dissolve(0.8)
    Kiara "I'm so sorry again for taking your entire day , I didn't think it would take that long"
    scene bg kiagdnit 6 with Dissolve(0.8)
    TaxiDriver "It's fine really , feel free to call me if you need a ride again . I live nearby here."
    scene bg kiagdnit 7 with Dissolve(0.8)
    Kiara "I will! , oh by the way you have pretty cool hair"
    TaxiDriver "Thanks , same to you"
    scene bg kiagdnit 8 with Dissolve(0.8)
    Kiara "Have a good night , see ya!"
    TaxiDriver "Yeah see ya ( Heh.. cool hair )"
    scene bg kiagdnit 9 with Dissolve(0.8)
    TaxiDriver "You said the same words to me 6 years ago , and i never changed it then"
    scene bg kiagdnit 10 with Dissolve(0.8)

    #keisuke stats reveal
    $ kaisuke_stats_hidden = False
    Keisuke "You haven't changed at all Kiara"
    scene bg kiagdnit 11 with Dissolve(0.8)
    Keisuke "(If this is how we meet again , then so be it . I should head home now)"
    scene bg kiagdnit 12 with Dissolve(0.8)
    Kiara "Auntie! Natsuko?!"
    scene bg kiagdnit 13 with Dissolve(0.8)
    Xia "Ah she's back"
    Kiara "Auntie!"
    scene bg kiagdnit 14 with Dissolve(0.8)
    Xia "Coming!"
    scene bg kiagdnit 15 with Dissolve(0.8)
    Kiara "Tadaima!"
    scene bg kiagdnit 16 with Dissolve(0.8)
    Xia "Oh look at you , someone is adapting i see"
    Kiara "Heh , Trying. Today was great auntie"
    scene bg kiagdnit 17 with Dissolve(0.8)
    Kiara "I got selected for all of them , It was awesome!"
    Xia "That's wonderful to hear , I told you you didn't have to be nervous"
    scene bg kiagdnit 18 with Dissolve(0.8)
    Kiara "Well seems you were right about confidence , there's so much i want to tell you"
    Xia "I know honey , we'll talk about it however"
    scene bg kiagdnit 19 with Dissolve(0.8)
    Xia "Let's discuss it after you've freshned up , i'll go make dinner okay?"
    Kiara "Okay auntie!"
    scene bg kiagdnit 20 with Dissolve(0.8)
    Kiara "*Humming music*"
    Xia "I'll make you some hot tea as well , take your time okay"
    scene bg kiagdnit 21 with Dissolve(0.8)
    Xia "(She's growing up right before my eyes , it's soothing)"
    scene bg kiagdnit 22 with Dissolve(0.8)
    Xia "(Hm?..)"
    scene bg kiagdnit 23 with Dissolve(0.8)
    Xia "I swear i sense'd something.."
    Kiara "Auntie! i can't find the towel"
    scene bg kiagdnit 24 with Dissolve(0.8)
    Xia "Oh , sorry honey i had placed them in my room! coming!"
    scene bg kiagdnit 25 with Dissolve(0.8)
    AgentWong "In house now.. that was close"
    scene bg kiagdnit 26 with Dissolve(0.8)
    AgentWong "That lady noticed me even when i was hiding , she's not ordinary gotta be careful"
    scene bg kiagdnit 27 with Dissolve(0.8)
    AgentWong "Nothing to do now , I'll leave i suppose"
    scene blackscreen
    show titletext "Sato Household.." with dissolve
    pause 1.0
    window hide
    scene bg kiagdnit 28 with Dissolve(0.8)
    pause
    scene bg kiagdnit 29 with Dissolve(0.8)
    Azumi "It was nice seeing her again"
    scene bg kiagdnit 30 with Dissolve(0.8)
    Azumi  "I wonder how her day went.. I hope nothing less than good"
    scene bg kiagdnit 31 with Dissolve(0.8)
    Sato "My secret sauce for the night , this should bring the spice up"
    scene bg kiagdnit 32 with Dissolve(0.8)
    "Woman downstairs" "Sato-san , come down or i'm leaving for the hotel now!"
    scene bg kiagdnit 33 with Dissolve(0.8)
    Sato "Ah shit coming coming! , Azumi! i'm going out for the night!"
    scene bg kiagdnit 34 with Dissolve(0.8)
    Azumi "Okay uncle, bye!"
    scene bg kiagdnit 35 with Dissolve(0.8)
    Azumi "This late? I never understand party people.."
    scene bg kiagdnit 36 with Dissolve(0.8)
    Azumi "Let me lock the door , doubt he did it."
    scene bg kiagdnit 37 with Dissolve(0.8)
    Azumi "Uncle sato 's been so busy taking care of me though , i suppose i should cut him some slack if he wants to live too"
    scene bg kiagdnit 38 with Dissolve(0.8)
    Azumi "I was hungry.. should i order?"
    scene bg kiagdnit 39 with Dissolve(0.8)
    Azumi "What's that? An orange juice?"
    scene bg kiagdnit 40 with Dissolve(0.8)
    Azumi "This'll be perfect! , It's all i need for a good sleep"
    scene bg kiagdnit 41 with Dissolve(0.8)
    Azumi "*gulp*"
    scene bg kiagdnit 42 with Dissolve(0.8)
    Azumi "Haa , nice"
    scene bg kiagdnit 43 with Dissolve(0.8)
    Azumi "I should sleep soon , i wanna have some plans with her for the weekend"
    scene bg kiagdnit 44 with Dissolve(0.8)
    Azumi "Uh , my head hurts.. should've had tea instead"
    scene bg kiagdnit 45 with Dissolve(0.8)
    Azumi "Why is the room suddenly getting so warm.. is it because i didn't shower after school?"
    label .part_7:
        scene bg kiagdnit 46 with Dissolve(0.8)
        pause
        scene bg kiagdnit 47 with Dissolve(0.8)
        pause
        scene bg kiagdnit 48 with Dissolve(0.8)
        pause
        scene bg kiagdnit 49 with Dissolve(0.8)
        Azumi "Why am i still sweating? ugh i should just take a shower"
        scene bg kiagdnit 50 with Dissolve(0.8)
        Azumi "Where's my brush"
        scene bg kiagdnit 51 with Dissolve(0.8)
        Azumi "What is happening.. I feel dizzy too"
        scene bg kiagdnit 52 with Dissolve(0.8)
        Azumi "It's like something is just burning right next to me"
        scene bg kiagdnit 53 with Dissolve(0.8)
        Azumi "*Phone rings* What the?.. Kiara? " 
        scene bg kiagdnitazmidcd  with Dissolve(0.8)
        Azumi "I don't feel like now is the right time to talk, but i don't wanna ignore her"
    #> CHOICE  with Dissolve(0.8)
    #> TALK WITH KIARA (+1 corruption) ""
    #TELL HER YOU’RE BUSY ""
    if _in_replay:
        jump .part_1
    menu:
        "Talk with [Kiara].":
            jump .part_1
        "Tell her you are busy.":
            jump .part_2

    
    label .part_1:
        # IF CHOICE TALK WITH KIARA -> USE RENDERS -> azmipikcall
        # 
        scene azmitalkoncall  1 with Dissolve(0.8)
        Azumi "I can't afford to ignore this , I'll just talk"
        scene azmitalkoncall  2 with Dissolve(0.8)
        Kiara "Hey azumi , sorry were you asleep?" 
        Azumi "No not at all , how was your day?"
        scene azmitalkoncall  3 with Dissolve(0.8)
        Kiara "It was great , I am sorry we couldn't spend more time together"  
        Azumi "No it's all good , i'm glad you had a nice day"
        scene azmitalkoncall  4 with Dissolve(0.8)  
        Kiara "Yeah , rain is insane too , all my clothes got wet trying to get that off now with a steam shower"
        scene azmitalkoncall  5
        Azumi "(Wait.. she's talking to me while in shower?.. she's naked?)"
        Kiara "What about you? how was your day" 
        Azumi "It-it was good , um so you're okay with meeting in weekend again?"
        scene azmitalkoncall  6 with Dissolve(0.8)
        Azumi "I mean do you wanna maybe just hang out since we're both free"  
        Kiara "Of course , I'll call you don't worry"
        scene azmitalkoncall  7 with Dissolve(0.8)
        Kiara "This shower is nice , I'll show you someday i love the bathroom"
        scene azmitalkoncall  8 with Dissolve(0.8)
        Azumi "Yeah i'd love to see it , Unf.."
        scene azmitalkoncall  9 with Dissolve(0.8)
        Kiara "Can you also help me pick out some clothes? I kinda want new faishon and your sense is great so"
        scene azmitalkoncall  10 with Dissolve(0.8)
        Kiara "I mean , i know you've got enough on your hand too but i only trust you with clothing choice"  
        Azumi "Yeah.. you can trust me with your bo- i mean clothes"
        scene azmitalkoncall  11 with Dissolve(0.8)
        Azumi "Aah.. *Gasps*"  
        Kiara "Thanks , I'd love to try out some new stuff and also explore oska too"
        scene azmitalkoncall  12 with Dissolve(0.8)
        Kiara "You'd help me in that please?" 
        Azumi "Yeah.. I'll help you explore (Fuck.. I can't hold back anymore)"
        scene azmitalkoncall  13 with Dissolve(0.8)
        Azumi "Haa *Blushing and gasps* (Shit.. i'm so wet)"  
        Kiara "Thanks you're so kind , i am so glad you were on that plane"
        scene azmitalkoncall  14 with Dissolve(0.8)
        Kiara "Azumi , you okay?" 
        Azumi "Fuck , uh..(Shh don't let her hear it)"
        scene azmitalkoncall  15 with Dissolve(0.8)
        Azumi "Aaaaah!,, ( God , this is so good)" 
        Kiara "Azumi? you there?"
        scene azmitalkoncall  16 with Dissolve(0.8)
        Azumi "Ah.. yeah.. sorry kiara , just some network problems."  
        Kiara "Oh that's fine , do you need to sleep? I feel like i called you midway"
        scene azmitalkoncall  17 with Dissolve(0.8)
        Azumi "Yeah , we'll talk tomorrow if that's okay"  
        Kiara "Sure , goodnight! sleep well"
        scene azmitalkoncall  18 with Dissolve(0.8)
        Azumi "Yeah , Goodnight.. *Smooch*"
        scene azmitalkoncall  19 with Dissolve(0.8)
        Azumi "Definitely need that shower now.."

        $ renpy.end_replay()
        $ mc_stats.adjust_corruption(1)
        jump .part_3
    
    label .part_2:
        #IF CHOICE TELL HER YOU’RE BUSY -> USE RENDERS OF -> scene azmidntpckcall ->
        scene azmidntpick 1 with Dissolve(0.8)
        Azumi "H-hi kiara"  
        Kiara "Are you okay? I just wanted to talk sorry if you were asleep"
        scene azmidntpick 2 with Dissolve(0.8)
        Azumi "Yeah i was just heading to sleep actually .. but  tell me was it important?"  
        Kiara "Oh no just some casual talk , i was bored so"
        scene azmidntpick 3 with Dissolve(0.8)
        Azumi "I'm sorry i would love to but i need to sleep early for classes tomorrow"  
        Kiara "Oh of course i understand , let's meet at school then?"
        scene azmidntpick 4 with Dissolve(0.8)
        Azumi "Yeah , We'll meet at school.. i promise"
        scene azmidntpick 5 with Dissolve(0.8)
        Kiara "Okay , goodnight sleep well!" 
        Azumi "You too , um one more thing" 
        scene azmidntpick 6 with Dissolve(0.8)
        Kiara "Yeah?"
        Azumi "You're amazing.. *smooch*"
        scene azmidntpick 7 with Dissolve(0.8)
        Azumi "Okay.. shower time"
        jump .part_3

    label .part_3:
        # CANONRESUME ->
        scene bg kiagdnit 54 with Dissolve(0.8)
        Kiara "(Was that a kiss?.. heh cute.)"
        scene bg kiagdnit 55 with Dissolve(0.8)
        Xia "Come honey , dinner is ready"
        scene bg kiagdnit 56 with Dissolve(0.8)
        Kiara "Hey auntie , sorry was just talking to a friend"
        Xia "No worries , come join me"
        scene bg kiagdnit 57 with Dissolve(0.8)
        Kiara "Auntie , where's natsuko?"
        Xia "She had to go to a friend's will be staying there tonight"
        scene bg kiagdnit 58 with Dissolve(0.8)
        Xia "I'm proud of you for today by the way"
        Kiara "Thank you auntie , I'm doing my best"
        scene bg kiagdnit 59 with Dissolve(0.8)
        Kiara "So yeah .. like i was saying , it went great i got selected at all of them"
        Xia "That's splendid , what of the work from home one?"
        scene bg kiagdnit 60 with Dissolve(0.8)
        Kiara "Oh yeah that one too , I believe some components were delivered to the home?"
        scene bg kiagdnit 61  with Dissolve(0.8)
        Xia "They're in your room , I'm not that great with technology so you'd have to figure that out with your cousin"
        scene bg kiagdnit 62 with Dissolve(0.8)
        Kiara "No worries , I'll handle it . Let's dig in!"
        scene bg kiagdnit 63 with Dissolve(0.8)
        Xia "So kiara .. did you talk to mia? any updates on that?"
        scene bg kiagdnit 64 with Dissolve(0.8)
        Kiara "I did , the lawsuit is today.."
        Xia "Are you nervous?"
        scene bg kiagdnit 65 with Dissolve(0.8)
        Kiara "I'd be lying if i said i wasn't but.."
        Xia "But?"
        Kiara "Even i'm safe from it , I just want mom to be happy"
        scene bg kiagdnit 66 with Dissolve(0.8)
        Xia "Do not worry , she has her friends there as well . You've just got stay strong and for that we both are here for you."
        scene bg kiagdnit 67 with Dissolve(0.8)
        Kiara "Thank you auntie , I appreciate it"
        Xia "No thanks in family honey , you deserve it"
        scene bg kiagdnit 68 with Dissolve(0.8)
        Kiara "Yeah.. (She.. her Gi is open)"
        scene bg kiagdnit 69 with Dissolve(0.8)
        Kiara "(When did she take off her bra?.. They're quite..)"
        scene bg antstaredcd  with Dissolve(0.8)
        #> CHOICE  
        #> STARE(REQUIRES CORRUPTION 10) (+ Corruption) 
        #LOOK AWAY  
        #> ""
        menu:
            "Stare" if mc_stats.current_corruption >= 10:
                jump .part_4
            "Look Away":
                jump .part_5

        label .part_4:
            # IF STARE -> USE RENDERS OF -> antstare ->
            scene bg antstare 1 with Dissolve(0.8)
            Kiara "(They're so mesmerizing..)"
            scene bg antstare 2 with Dissolve(0.8)
            Kiara "(Bigger than mine even)"
            scene bg antstare 3 with Dissolve(0.8)
            Kiara  "(Those lips , so soft too)"
            scene bg antstare 4 with Dissolve(0.8)
            Xia "So kiara , i wanted to say-(Where is she staring?)"
            scene bg antstare 5 with Dissolve(0.8)
            Xia "Ah.(I shouldn't have taken that off)"
            scene bg antstare 6 with Dissolve(0.8)
            Xia "Kiara , are you not liking the rice cakes?"
            scene bg antstare 7 with Dissolve(0.8)
            Kiara "What? no , i love them auntie you're cooking is very good"
            scene bg antstare 8 with Dissolve(0.8)
            Xia "Well i asked because you're staring the muffins so.."
            scene bg antstare 9 with Dissolve(0.8)
            Kiara "Ah *Gasp*"
            scene bg antstare 10 with Dissolve(0.8)
            Kiara "Im sorry auntie , I didn't mean to-"
            Xia "It's okay honey , sometimes feelings occur. You're that age now"
            scene bg antstare 11 with Dissolve(0.8)
            Kiara "Actually i'm just surprised at how fit you are.. How do you manage it?"
            scene bg antstare 12 with Dissolve(0.8)
            Xia "Well It's the martial arts really , they keep me strong and fit"
            Kiara "Ah i see.. heh I'll practice more too then"
            $ mc_stats.adjust_corruption(5)
            jump .part_6

        label .part_5:
            # IF CHOICE LOOK AWAY -? USE RENDERS -> dntstareant ->
            scene bg antdntstare 1 with Dissolve(0.8)
            Kiara "(What am i doing , focus on food)"
            scene bg antdntstare 2 with Dissolve(0.8)
            Xia "Honey , anything worrying you?"
            scene bg antdntstare 3 with Dissolve(0.8)
            Kiara "Oh no auntie , i was just curious how you're so maintained , you look so great too"
            scene bg antdntstare 4 with Dissolve(0.8)
            Xia "That's one way to compliment a chef but its actually the martial arts that keep me fit"
            Kiara "Oh i see , I'll practice more too then"
            jump .part_6

        label .part_6:
            # CANONRESUME- >
            scene bg kiagdnit 70 with Dissolve(0.8)
            Kiara "Speaking of which , how did you get started in this auntie?"
            scene bg kiagdnit 71 with Dissolve(0.8)
            Xia  "Well to be honest it happened because of your uncle ichigo"
            scene bg kiagdnit 72 with Dissolve(0.8)
            Kiara "Uncle ichigo?"
            Xia "Oh you (she's forgotten) You haven't met him i think , we met during the academy days actually"
            scene bg kiagdnit 73 with Dissolve(0.8) 
            Kiara "I see.. what then?"
            Xia "Well we were training and some guys tried to harass me , he intervened to stop them all"
            scene bg kiagdnit 74 with Dissolve(0.8)
            Kiara "Oh then?"
            Xia "He jumped in to stop them all , there were 6 people"
            Kiara "Oh wow! what did uncle do then? beat them up?"
            scene bg kiagdnit 75 with Dissolve(0.8)
            Xia "No he got his butt kicked by all of them"
            Kiara "Oh wow , that did not go where i was expecting it.. what then?"
            scene bg kiagdnit 76 with Dissolve(0.8)
            Xia "I beat them up then.. and your uncle with his slightly broken cheek , said something very adorable"
            Kiara "Which was?"
            scene bg kiagdnit 77 with Dissolve(0.8)
            Xia "He said , I know this might be the worst time to ask.. but you're beautiful and i really want us to have a future together"
            scene bg kiagdnit 78 with Dissolve(0.8)
            "[Xia] and [Kiara]"  "Hahahahaa , wow" #( Laughing together dialogue)
            scene bg kiagdnit 79 with Dissolve(0.8)
            Xia "At that moment though i realized he loved me , didn't want anything else but my heart"
            scene bg kiagdnit 80 with Dissolve(0.8)
            Kiara "That's lovely auntie"
            Xia "After that , I realized i have to be strong one and he'll be the man of the house . Somehow somewhere we eventually got to the end"
            scene bg kiagdnit 81 with Dissolve(0.8)
            Xia "Now things are where you see them , I'm happy with a lovely husband , a daughter and a lovely niece"
            scene bg kiagdnit 82 with Dissolve(0.8)
            Kiara "I hope i find someone like that too one day"
            scene bg kiagdnit 83 with Dissolve(0.8)
            Xia "(You did.. , but who took it from you is what i can't say. I'm sorry kiara)"
            scene bg kiagdnit 84 with Dissolve(0.8)
            Xia "I'm sure you will , don't worry honey good people find good souls"
            scene bg kiagdnit 85 with Dissolve(0.8)
            Kiara "Hope so , I'll head to bed then"
            Xia "Sleep well and remember this is your home , don't ever feel strange in it"
            scene bg kiagdnit 86 with Dissolve(0.8)
            Kiara "Thanks auntie , I'll be off now"
            scene bg kiagdnit 87 with Dissolve(0.8)
            Kiara "Goodnight auntie"
            Xia "Goodnight kiara"
            scene bg kiagdnit 88 with Dissolve(0.8)
            Xia "(I can't help you with the past but future i'll make sure no one hurts you anymore , I hope she trusts me too)"
            scene bg kiagdnit 89 with Dissolve(0.8)
            Kiara "Hm.. alright , all that's left is to plan out now"
            scene bg kiagdnit 90 with Dissolve(0.8)
            Kiara "Tiring day , I'll have to filter out everything tomorrow"
            scene bg kiagdnit 91 with Dissolve(0.8)
            Kiara "This must be the computer , I'll unpack it tomorrow"
            scene bg kiagdnit 92 with Dissolve(0.8)
            Kiara "Time to sleep.."
            scene bg kiagdnit 93 with Dissolve(0.8)
            Kiara "Hard part's over , small steps from tomorrow."
            scene bg kiagdnit 94 with Dissolve(0.8)
            Kiara "(I pray you're okay mom.. Hope to see you soon here too)"
            pause
            # testing python code
            
            # python:
            #     for i in range(1, 7):
            #         if renpy.slot_json('quick-' + str(i)) == None:
            #             renpy.save('quick-' + str(i))
            #             break
            $ renpy.save('quick-1')
            #$ renpy.save('quick-1')
            scene bg kiagdnit 95 with Dissolve(0.8)
            pause

            
            pause 1
            jump chap_2_scene_11


label chap_2_scene_11:

    # SCENE -> nyhmestrt->
    scene blackscreen
    show titletext "Brooklyn , New york" with dissolve
    pause 1.0
    window hide
    scene bg nyhmestrt 1  with Dissolve(0.8)
    pause
    scene bg nyhmestrt 2  with Dissolve(0.8)
    Evelyn "(Ah.. when did i sleep?)"
    scene bg nyhmestrt 3 with Dissolve(0.8)
    Mia "Honey , did i wake you up? I'm sorry i was just grabbing the remote"
    scene bg nyhmestrt 4  with Dissolve(0.8)
    Evelyn "Mom , you were here all night?"
    Mia "You were so tired you fell asleep on me , I didn't want to move"
    scene bg nyhmestrt 5 with Dissolve(0.8)
    Evelyn "I've missed this mom"
    scene bg nyhmestrt 6 with Dissolve(0.8)
    Mia "I did too , seeing you in my lap finally was far more peaceful than any sleep"
    scene bg nyhmestrt 7 with Dissolve(0.8)
    Evelyn "You must be tired still but thanks"
    scene bg nyhmestrt 8 with Dissolve(0.8)
    Mia "You look very pretty when sleeping"
    Evelyn "Heh , thanks mom"
    scene bg nyhmestrt 9 with Dissolve(0.8)
    Evelyn "You should really get some rest now , I'll handle the chores"
    Mia "Don't worry i slept on the couch too , I'm good"
    scene bg nyhmestrt 10 with Dissolve(0.8)
    Evelyn "I'm sorry mom , I shouldn't have left you back then i made a mistake"
    Mia "You don't have to be , I made a wrong choice as well"
    scene bg nyhmestrt 11 with Dissolve(0.8)
    Evelyn "The lawsuit is today.. are you worried?"
    Mia "I am , even more now because i don't want to lose you or kiara"
    scene bg nyhmestrt 12  with Dissolve(0.8)
    Evelyn "We'll make it through this last hurdle too mom , we're together here again , it means fate wants us to be"
    Mia "Yeah , maybe we can finally be in peace and harmony"
    scene bg nyhmestrt 13 with Dissolve(0.8)
    Mia "Eve.. I wanted to ask something"
    Evelyn "Sure , Ask?"
    scene bg nyhmestrt 14  with Dissolve(0.8)
    Mia "What do you think of mason?"
    Evelyn "Mason? um.. he's a good person , seems like someone who wants the world to be better . Why?"
    scene bg nyhmestrt 15  with Dissolve(0.8)
    Mia "I - Actually i just-"
    Veronica "Let me help you here"
    scene bg nyhmestrt 16 with Dissolve(0.8)
    Veronica "She's asking about her new husband eve or your dad in this context"
    Evelyn "Oh.. hi V"
    Mia "Ah! Veronica"
    scene bg nyhmestrt 17 with Dissolve(0.8)
    Evelyn "Also what? really mom? that's unbelievable"
    Mia "Um-- I"
    scene bg nyhmestrt 18  with Dissolve(0.8)
    Evelyn "No i mean unbelievable in a good way, he's a great guy i'm really happy for you!"
    Mia "Do you really think so?.. I just don't know"
    scene bg nyhmestrt 19 with Dissolve(0.8)  
    Evelyn "You don't know what?"
    Mia  "I just don't think i'm good enough for him"
    scene bg nyhmestrt 20 with Dissolve(0.8)
    Mason "That's where you're wrong"
    Mia "Mason"
    Evelyn "Hey , good morning"
    scene bg nyhmestrt 21  with Dissolve(0.8)
    Mason "You're more than enough , you always were"
    Mia "Thank you.."
    scene bg nyhmestrt 22 with Dissolve(0.8)
    Mason "Thanks evelyn , I was so worried what you'd say but it seems i am not the worst after all"
    Evelyn "You know i never sugarcoat things , I'm truly happy for you both"
    scene bg nyhmestrt 23 with Dissolve(0.8)
    Veronica "Told you she'd be fine"
    Mason "Yeah , I'm just glad to hear it from herself"
    scene bg nyhmestrt 24  with Dissolve(0.8)
    Mia "This is all i need , really you all are here soon we'll have kiara too"
    scene bg nyhmestrt 25  with Dissolve(0.8)
    Mia "We'll fianlly have a family again , unless.."
    Mason "No unless."
    scene bg nyhmestrt 26 with Dissolve(0.8)
    Mason "It will happen , I don't care what it takes I'll make sure you get it"
    Mia "Mason I-"
    scene bg nyhmestrt 27  with Dissolve(0.8)
    Mason "No I or buts , just trust me you're all i need to be strong and I'll make it happen"
    Evelyn "(This is what it looks like , genuine affection)"
    scene bg nyhmestrt 28 with Dissolve(0.8)
    Veronica "(I'm proud of you mason)"
    scene bg nyhmestrt 29 with Dissolve(0.8)
    Veronica "Mason , we have to discuss something about the suit today , do you want to?"
    Mason "Yeah , I'll be in office"
    scene bg nyhmestrt 30  with Dissolve(0.8)
    Mason "I gotta go for now , I'll see you . Smile for me okay?"
    Mia "I will for you , take your time"
    scene bg nyhmestrt 31 with Dissolve(0.8)
    Veronica  "So are you on the documents already?"
    Mason "Yes got everything sorted"
    Mia "(This life is just one step away.. please let it happen)"
    scene bg nyhmestrt 32  with Dissolve(0.8)
    Evelyn "So mom.. Kiara , she's with auntie then?"
    Mia "Yes.. actually i was thinking to send you there as well while this settles"
    scene bg nyhmestrt 33 with Dissolve(0.8)
    Mia "I'm sure she would love her older sister's company and my sis would like both her nieces too"
    Evelyn "I'd love to.. its been so long"
    scene bg nyhmestrt 34 with Dissolve(0.8)
    Evelyn "What about you here though ? Isn't my testimony today as well"
    Mia "Yes I mean after today , if everything is alright.. you should go meet her . She needs you more than she needs me now"
    scene bg nyhmestrt 35  with Dissolve(0.8)
    Mia "Take care of her , you're stronger than all of us so teach her to be to that too"
    Evelyn "I will , but let me finish up here first"
    scene bg nyhmestrt 36 with Dissolve(0.8)
    Evelyn "I want to make sure you're well emotionally and physically first , then i'll go . Is that okay?"
    Mia "I appreciate that , okay we'll do it your way then"
    scene bg nyhmestrt 37  with Dissolve(0.8)
    Evelyn "Well I'll get some fresh air mom , see you in a bit?"
    scene bg nyhmestrt 38  with Dissolve(0.8)
    Veronica "Um hey , Mason apparently is gonna cover everything on own.. do you mind if go along?"
    scene bg nyhmestrt 39   with Dissolve(0.8)
    Evelyn "You really think you need to ask?"
    Veronica "I don't know you can be scary sometimes"
    Evelyn "Heh , come"
    scene bg nyhmestrt 40  with Dissolve(0.8)
    Veronica "Psst , mia"
    Mia  "Hm?"
    scene bg nyhmestrt 41  with Dissolve(0.8)
    Veronica "Enjoy! *wink*"

    jump chap_2_scene_12
# 


label chap_2_scene_12:
    # SCENE -> jhnlwyrny ->
    scene blackscreen
    show titletext "Attorney's Office" with dissolve
    pause 1.0
    window hide
    scene bg jhnlwyrny 1  with Dissolve(0.8)
    pause
    scene bg jhnlwyrny 2 with Dissolve(0.8)
    pause
    scene bg jhnlwyrny 3 with Dissolve(0.8)
    John "Stay outside , I'll join you later"
    scene bg jhnlwyrny 4 with Dissolve(0.8)
    Jennifer "You're late Mr. Jonathan"
    John "My apologies ms Jennifer , you know parties they can get quite noisy"
    scene bg jhnlwyrny 5 with Dissolve(0.8)
    John "Plus had to attend some business meetings , came as quick as i could"
    Jennifer "Please sit"
    scene bg jhnlwyrny 6 with Dissolve(0.8)
    John "Ha , okay so you said you had good news for me"
    Jennifer "Yes , The judge for your trial is Dominic Desiato , He's a strict by the facts judge . Emotional values do not matter to him so that's one plus point"
    scene bg jhnlwyrny 7  with Dissolve(0.8)
    John "Splendid that means i won't have to worry about her whining in court affecting the decision right?"
    Jennifer "Correct , any other judge would've counted those in the testimony"
    scene bg jhnlwyrny 8 with Dissolve(0.8)
    Jennifer "I've looked at your file as well , this might be a longer case then intended"
    John "Fine by me , as long as we get whatt we want in the end"
    scene bg jhnlwyrny 9  with Dissolve(0.8)
    Jennifer "I know legal fees isn'the issue for you , however you're reducing the alimony as well?"
    scene bg jhnlwyrny 10  with Dissolve(0.8)
    John "I am , it's prove a point no whore takes money from me and runs without consequnces"
    Jennifer "Alright"
    scene bg jhnlwyrny 11  with Dissolve(0.8)
    Jennifer "One more thing , I don't understand why you don't want to present the evidence being deleted in court as evidence tampering now?"
    John "Actually the reason for that is the girl who did it , Mr mason's cousin I have some special plans to discipline her"
    scene bg jhnlwyrny 12 with Dissolve(0.8)
    John "I'll make sure she never talks the way she does to me again and for that i need leverage"
    Jennifer "Right.. discipline"
    scene bg jhnlwyrny 13  with Dissolve(0.8)
    Jennifer "I believe i already know where this is going"
    John "Yes you do Indeed"
    scene bg jhnlwyrny 14 with Dissolve(0.8)
    Jennifer "So one more thing.. you've never done this to your staff , employees or people you work with , how come that so?"
    John "I Don't mix pleasure and business Ms. Jennifer , It's the sole reason why I'm so sucessful"
    scene bg jhnlwyrny 15   with Dissolve(0.8)
    Jennifer "Understood , You're still walking on thin ice here sir"
    John "I know"
    scene bg jhnlwyrny 16 with Dissolve(0.8)
    Jennifer "She's a fighter , you won't get her as easy"
    John "I know , leave that to me Ms. jennifer"
    scene bg jhnlwyrny 17 with Dissolve(0.8)
    Jennifer "Alright , i would still advise you to reduce these passions , as multiple offences in same nature can eventually drag you down"
    John "Certainly , Veronica will be lasting for a while do not worry"
    scene bg jhnlwyrny 18  with Dissolve(0.8)
    Jennifer "Alright then , did you want to ask anything else?"
    scene bg jhnlwyrny 19  with Dissolve(0.8)
    John "Nothing , just destroy them in court today. I want mia to suffer"
    Jennifer "I'll do my job at the pace i've done in past"
    scene bg jhnlwyrny 20  with Dissolve(0.8)
    Jennifer "I hope that answers your question"
    John "It does"
    scene bg jhnlwyrny 21  with Dissolve(0.8)
    Jennifer "Be at court at 2 pm , We'll meet up outside"
    John "Yes , see you soon Ms. Jennifer"

    jump chap_2_scene_13


label chap_2_scene_13:

    # SCENE -> msonmiamrngscn ->
    scene blackscreen
    show titletext "Back at Mason's" with dissolve
    pause 1.0
    window hide
    scene bg miamsnmrngscn 1  with Dissolve(0.8)
    Mason "This must be the previous instance , no conviction is a little annoying in all these cases"
    scene bg miamsnmrngscn 2  with Dissolve(0.8)
    Mason "Sachiko's files might help but i need more still"
    scene bg miamsnmrngscn 3  with Dissolve(0.8)
    Mason "For the first trial i have enough , maybe i can arrange until 2nd happens"
    scene bg miamsnmrngscn 4  with Dissolve(0.8)
    Mason "What a pain.. fucking asshole paid off every single judge in past i can tell"
    scene bg miamsnmrngscn 5  with Dissolve(0.8)
    Mason "I need some coffee"
    scene bg miamsnmrngscn 6  with Dissolve(0.8)
    Mason  "Huh?.. I can't see"
    Mia "Let me help you.."
    #> GIVE OPTION TO SKIP TO THE NEXT SCENE FROM HERE.

    menu:
        "Skip to the next scene?"
        "Yes":
            jump chap_2_scene_14
        "No":
            jump .part_1

    label .part_1:
        # If not skipped then continue from here
        scene bg miamsnmrngscn 7  with Dissolve(0.8)
        Mason "Huh?.. are those?"
        Mia "Yes"
        scene bg miamsnmrngscn 8  with Dissolve(0.8)
        Mason "Man.. they're so soft"
        Mia "Coffee would've taken long so"
        scene bg miamsnmrngscn 9  with Dissolve(0.8)
        Mia "This is easier i suppose and you like it more i think"
        Mason "I do for sure"
        scene bg miamsnmrngscn 10 with Dissolve(0.8)
        Mason "I like sucking em more though"
        Mia "Mm... yeah , they're all yours"
        scene bg miamsnmrngscn 11 with Dissolve(0.8)
        Mia "Ha.. yes , bury your face between them"
        Mason "You're so fucking hot"
        scene bg miamsnmrngscn 12  with Dissolve(0.8)
        Mia "Your hands feel so great"
        scene bg miamsnmrngscn 13  with Dissolve(0.8)
        Mason "*Sucking tits* mm"
        Mia "Yeah babe.. bite them"
        scene bg miamsnmrngscn 14  with Dissolve(0.8)
        Mason "I wanna do more than just bite"
        scene bg miamsnmrngscn 15  with Dissolve(0.8)
        pause
        scene bg miamsnmrngscn 16 with Dissolve(0.8)
        Mason "I wanna taste too"
        scene bg miamsnmrngscn 17 with Dissolve(0.8)
        Mia "Yes , take me.. here and now"
        Mason "You're so pretty"
        scene bg miamsnmrngscn 18  with Dissolve(0.8)
        Mia "You're lovely as well.. fuck keep going please"
        scene bg miamsnmrngscn 19 with Dissolve(0.8)
        Mia "I'm all yours , just take me"
        scene bg miamsnmrngscn 20  with Dissolve(0.8)
        Mason  "Let's go then"
        scene bg miamsnmrngscn 21  with Dissolve(0.8)
        Mia "Heh , do we have enough time?"
        Mason "We'll make time for this"
        scene bg miamsnmrngscn 22  with Dissolve(0.8)
        pause
        scene bg miamsnmrngscn 23 with Dissolve(0.8)
        pause
        scene bg miamsnmrngscn 24  with Dissolve(0.8)
        Mason "I love you"
        Mia "I love you too"
        scene bg miamsnmrngscn 25 with Dissolve(0.8)
        pause
        scene bg miamsnmrngscn 26 with Dissolve(0.8)
        pause
        scene bg miamsnmrngscn 27  with Dissolve(0.8)
        pause
        scene bg miamsnmrngscn 28  with Dissolve(0.8)
        Mason "You're so fucking yummy"
        Mia "Mmmm.. keep going"
        scene bg miamsnmrngscn 29 with Dissolve(0.8)
        Mia "Mason.. stay stil.."
        Mason "Okay, wow it's like living a dream"
        scene bg miamsnmrngscn 30  with Dissolve(0.8)
        Mason "Damn, i don't wanna wake up if it is"
        scene bg miamsnmrngscn 31  with Dissolve(0.8)
        Mia "It's not .. let me make it better than a dream even"
        Mason "Fuck.. you're so good"
        scene bg_miamsnmrngscn_anim_1  with Dissolve(0.8)
        Mia  "You liking this?."
        scene bg_miamsnmrngscn_anim_2  with Dissolve(0.8)
        Mason "I love it.. fuck my dick is so tight it hurts"
        Mia "I'll help you with that as well *licking*"
        scene bg_miamsnmrngscn_anim_3  with Dissolve(0.8)
        Mia "Your dick feels so good rubbing between my tits"
        Mason "Fuckkk , Mia i'm about to cum"
        scene bg miamsnmrngscn 35  with Dissolve(0.8)
        Mia "Do it , do it on your college crush's face"
        scene bg miamsnmrngscn 36  with Dissolve(0.8)
        Mason "Aaaah! fuck"
        scene bg miamsnmrngscn 37  with Dissolve(0.8)
        Mason "Awh yeah , damn i can't even stop"
        Mia "Keep it coming love"
        scene bg miamsnmrngscn 38  with Dissolve(0.8)
        Mia "(Wow , he came so much seems he likes my tits the most)"
        scene bg miamsnmrngscn 39  with Dissolve(0.8)
        Mason "Sorry I covered your face.."
        Mia "I love it , it's yummy.."
        $ renpy.end_replay()
        jump chap_2_scene_14


label chap_2_scene_14:

    # SCENE  -> jkemomscn ->
    scene blackscreen
    show titletext "Fronis Hospital , Manhattan" with dissolve
    pause 1.0
    window hide
    scene bg jkmomscn 1  with Dissolve(0.8)
    Jake "Mom how are you feeling ?"
    scene bg jkmomscn 2  with Dissolve(0.8)
    Jake "I hope you like the new nurse , we've made sure you have no problems with the tv anymore"
    scene bg jkmomscn 3  with Dissolve(0.8)
    "Jake’s mother" "I'm fine honey , so what did you want to say?"
    scene bg jkmomscn 4  with Dissolve(0.8)
    Jake "Mom.. i did meet someone , her name is evelyn she was great "
    scene bg jkmomscn 5 with Dissolve(0.8)
    "Jake’s mother" "See , i told you someone will come along eventually that you fall for"
    Jake "It's not just looks mom.. She has such a pure heart, the words she said , it reminded me so much of the things you used to say"
    scene bg jkmomscn 6  with Dissolve(0.8)
    "Jake’s mother" "Sounds like a wonderful girl jake , don't let her go okay?"
    Jake "Yeah i won't"
    scene bg jkmomscn 7  with Dissolve(0.8)
    Jake "She just helped me as well.. despite not knowing me , I really hope i can talk to her more if nothing else"
    "Jake’s mother" "I believe that's called love honey , send me pictures of you two on your next date "
    scene bg jkmomscn 8  with Dissolve(0.8)
    Jake "We're not dating mom.. idk if we even will.. she's way out of my league"
    "Jake’s mother" "Don't believe in such frivlous things , the way you describe her i doubt she'll care for looks"
    scene bg jkmomscn 9  with Dissolve(0.8)
    Jake "I hope so too then mom , I'll get going now call me if you need anyhting okay?"
    "Jake’s mother" "I will and jake , good luck may evelyn give you a hug today!"
    scene bg jkmomscn 10  with Dissolve(0.8)
    Jake "Hug?.. I'm happy even around her . I hope we meet again"
    scene bg jkmomscn 11 with Dissolve(0.8)
    Jake "Oh hey , It's you thanks for wiring the money quickly"
    John "Don't mention it , could you drop my limo outside court? I'll be with my lawyer so might be busy"
    scene bg jkmomscn 12  with Dissolve(0.8)
    Jake "You got it , see you at 2"
    # 
    jump chap_2_scene_15
    # 
    # 

label chap_2_scene_15:
    # SCENE - > veroevlnprkscn ->
    scene blackscreen
    show titletext "Statue Park , Brooklyn" with dissolve
    pause 1.0
    window hide
    scene bg vereveprk 1 with Dissolve(0.8)
    pause
    scene bg vereveprk 2 with Dissolve(0.8)
    pause
    scene bg vereveprk 3 with Dissolve(0.8)
    Veronica "You've got a knack for sitting in the most alone places don't you"
    Evelyn "It's peaceful and pretty though"
    scene bg vereveprk 4 with Dissolve(0.8)
    Veronica "It is indeed , Eve.. are you happy?"
    Evelyn "Yeah i am , thank you for making me see i was wrong"
    scene bg vereveprk 5  with Dissolve(0.8)
    Veronica "You weren't wrong , what you did was to make yourself not lose sanity okay . All i did was to pull you out of the box you were trapped in"
    Evelyn "Yeah , I just wish i didn't waste so much time"
    scene bg vereveprk 6  with Dissolve(0.8)
    Evelyn "I do miss the house in the nature still though"
    Veronica "Well we can always go there time to time"
    Evelyn "No , not much point now"
    scene bg vereveprk 7 with Dissolve(0.8)
    Veronica "What do you mean no point ? Wouldn't you wanna live with me?"
    Evelyn "With you? Well.. then maybe i would heh"
    scene bg vereveprk 8 with Dissolve(0.8)
    Evelyn "V , I want to ask . What if things go south?"
    Veronica "What do you mean?"
    scene bg vereveprk 9 with Dissolve(0.8)
    Evelyn "Well you know , The case goes wrong or.. something else later on happens cuz of my dad"
    Veronica "Even if it does and worst case scenario if john tries something , rest assured i'll do whatever i can to protect you and mia and mason"
    scene bg vereveprk 10  with Dissolve(0.8)
    Veronica "Trust me , I won't let this family break apart again"
    scene bg vereveprk 11  with Dissolve(0.8)
    Evelyn "But what about you?"
    Veronica "What about me?"
    scene bg vereveprk 12  with Dissolve(0.8)
    Evelyn "Who's gonna be there for you then?"
    Veronica "Um I never really depended on anyone , so i don't know"
    scene bg vereveprk 13  with Dissolve(0.8)
    Evelyn "But don't you crave the feeling of affection or love in those hard times?"
    Veronica "Eve.. you know the answer to that already"
    scene bg vereveprk 14 with Dissolve(0.8)
    Evelyn "I'm sorry , I'm stupid for asking that"
    Veronica "No you're not stupid.. It's just that i'm a mess that's all and i don't think anyone should suffer because of that"
    scene bg vereveprk 15  with Dissolve(0.8)
    Veronica "It's the same for you isn't it?"
    Evelyn "Well yes.. but i do believe in love , It's rare and hard to find nowadays but it exists i'm sure of it"
    scene bg vereveprk 16  with Dissolve(0.8)
    Veronica "Who knows maybe we'll find someone too like mia did again"
    Evelyn "(Again?.. i see ) Um yeah , or you could just move in with me as roommates like the college days"
    scene bg vereveprk 17  with Dissolve(0.8)
    Veronica "That's not too bad either , one problem though"
    Evelyn "Oh which is?"
    scene bg vereveprk 18  with Dissolve(0.8)
    Evelyn "Let me guess , open showers?"
    scene bg vereveprk 19  with Dissolve(0.8)
    Veronica "You guessed it haha"
    Evelyn "Well i doubt that'd be an issue , You've seen me plenty i think"
    scene bg vereveprk 20  with Dissolve(0.8)
    Evelyn "I've seen you too , it amazes me how your neck doesn't kill you"
    Veronica "Let's just say push up bras help"
    scene bg vereveprk 21  with Dissolve(0.8)
    Veronica "What if this time it ends in more than roommates though?"
    Evelyn "Hm?"
    scene bg vereveprk 22 with Dissolve(0.8)
    Veronica "I mean.. do you remember why we stopped living together?"
    Evelyn "Ah yeah.. I just didn't know how to respond back then so I-"
    scene bg vereveprk 23  with Dissolve(0.8)
    Veronica "What about now then?"
    Evelyn "Now? Well I-"
    scene bg vereveprk 24  with Dissolve(0.8)
    Veronica "Nothing stops us now you know.. we could just start over"
    Evelyn "I-"
    scene bg vereveprk 25  with Dissolve(0.8)
    Veronica "Just the two of us , like it was meant to be"
    scene bg vereveprk 26  with Dissolve(0.8)
    Veronica "Nothing between us this time"
    pause
    scene bg vereveprk 26pttwo  with Dissolve(0.8)
    Evelyn "Yes"
    scene bg vereveprk 27  with Dissolve(0.8)
    Veronica "Ah shit sorry.. old habits die hard i guess"
    Evelyn "*Blushes* Heh , It's okay I - um.. do you want to grab some food?"
    scene bg vereveprk 28  with Dissolve(0.8)
    Evelyn "Or some ice cream?"
    Veronica "I'd love some ice cream"
    scene bg vereveprk 29  with Dissolve(0.8)
    Evelyn "Let's go then"
    Veronica "Yeah (Why did i stop myself?)"

    jump chap_2_scene_16
 


label chap_2_scene_16:
    # SCENE - > valdctrscn ->
    scene blackscreen
    show titletext "State Hospital , Mental Ward" with dissolve
    pause 1.0
    window hide
    scene bg vlntndctr 1  with Dissolve(0.8)
    pause
    scene bg vlntndctr 2  with Dissolve(0.8)
    pause
    scene bg vlntndctr 3  with Dissolve(0.8)
    pause
    scene bg vlntndctr 4 with Dissolve(0.8)
    Valentina "Excuse me , I'd like to meet Dr. Rachel . I've got an appointment"
    Nurse "I see , yes mam give me a minute"
    scene bg vlntndctr 5  with Dissolve(0.8)
    Nurse "Ward number 4 , Room number 7"
    scene bg vlntndctr 6  with Dissolve(0.8)
    Valentina "Thank you (Time to get some answers)"
    scene bg vlntndctr 7 with Dissolve(0.8)
    pause
    scene bg vlntndctr 8 with Dissolve(0.8)
    pause
    scene bg vlntndctr 9  with Dissolve(0.8)
    Sofia "(This is the only thing i can do now)"
    scene bg vlntndctr 10  with Dissolve(0.8)
    pause
    scene bg vlntndctr 11  with Dissolve(0.8)
    Valentina "Excuse me.. Doctor rachel"
    scene bg vlntndctr 12  with Dissolve(0.8)
    Valentina "I'm here , we talked on-"
    Sofia "Valentina i believe , please sit"
    scene bg vlntndctr 13  with Dissolve(0.8)
    Valentina "Doctor , I understand you can't share everything but i just want to know what happened.. she's alive i know that"
    Sofia "I know you do"
    scene bg vlntndctr 14 with Dissolve(0.8)
    Valentina "Why make the death certificate then?.. What exactly happened?"
    Sofia "I believe saying it won't do it justice.. so i want you to just read it yourself"
    scene bg vlntndctr 15  with Dissolve(0.8)
    Sofia "I know you're angry with me as well but maybe after this , you might understand my position too"
    Valentina "I'm an understanding person , I give chances to everyone"
    scene bg vlntndctr 16  with Dissolve(0.8)
    Sofia "Here take a look.."
    Valentina "This is.. Her last note?"
    scene bg vlntndctr 17  with Dissolve(0.8)
    Valentina "What?..what is this she-"
    Sofia "I'm sorry , These were her last words.. and much like you , I was tricked too"
    scene bg vlntndctr 18  with Dissolve(0.8)
    Valentina "This?.. her mother knew about it as well?"
    Sofia "She did , we were going to do only what was best for her.. but her father intervened"
    scene bg vlntndctr 19  with Dissolve(0.8)
    Valentina "Kiara , why didn't you tell us anything?"
    Sofia "She couldn't have , she was going through all of that alone , as the note says tired of burdening everyone"
    scene bg vlntndctr 20  with Dissolve(0.8)
    Valentina "I'm a useless friend, how could i have been so blind?"
    scene bg vlntndctr 21  with Dissolve(0.8)
    Valentina "Kiara , why did you.. *sobs*"
    Sofia "Valentina , please calm yourself"
    scene bg vlntndctr 22  with Dissolve(0.8)
    Sofia  "Drink some water please"
    scene bg vlntndctr 23  with Dissolve(0.8)
    Sofia "Now you know why i agreed , it wasn't money , wasn't force , she needed it and then that man just took advantage of the situation as well.."
    scene bg vlntndctr 24  with Dissolve(0.8)
    Sofia  "I can't give these files away.. but what i can say is making her remember the past without a procedure is a bad idea"
    Valentina "They erased more , continously according to you .. so he really was the culprint behind it"
    scene bg vlntndctr 25  with Dissolve(0.8)
    Sofia "I had no contorl over the later drafts as they took the patient papers form me.. they took me away , she couldn't resist but because she was unconcious"
    Valentina "Is there really no way?"
    scene bg vlntndctr 26  with Dissolve(0.8)
    Valentina "She deserves the truth , if not all then at least some of it"
    Sofia "Maybe might be doable..  parts of restoration can happen either through triggers or manually from here"
    scene bg vlntndctr 27  with Dissolve(0.8)
    Sofia "Before you go, one more thing"
    Valentina "What?"
    scene bg vlntndctr 28  with Dissolve(0.8)
    Sofia "Once you do, apologize to her from my side.. I made a grave mistake , I never should've accepted"
    Valentina "I will but you have to live with it for now like all of us"
    scene bg vlntndctr 29  with Dissolve(0.8)
    Valentina "The trial starts soon , I pray it goes well aunt mia"

    jump chap_2_scene_17 


label chap_2_scene_17:

    # SCENE -> lanamommsg ->
    # 
    scene blackscreen
    show titletext "Deep Massage Center , Harlem" with dissolve
    pause 1.0
    window hide
    scene bg lanamommsg 1 with Dissolve(0.8)
    pause
    scene bg lanamommsg 2 with Dissolve(0.8)
    Lana "Mom , It's late so i'll get some rest now & He's with us yeah"
    Elizabeth "Take care of him okay ? You're the only friend he has that he can trust"
    scene bg lanamommsg 3  with Dissolve(0.8)
    Elizabeth "Let me know if you need any help okay?"
    Lana "I will , just have to make sure he doesn't meet her"
    scene bg lanamommsg 4  with Dissolve(0.8)
    Lana "Anyway , Goodnight mom."
    Elizabeth "Goodnight sweetheart"
    scene bg lanamommsg 5  with Dissolve(0.8)
    Elizabeth "Awfully late today isn't she?"
    scene bg lanamommsg 6  with Dissolve(0.8)
    Elizabeth "Been almost half an hour"
    scene bg lanamommsg 7  with Dissolve(0.8)
    Elizabeth "Probably just traffic"
    scene bg lanamommsg 8 with Dissolve(0.8)
    pause
    scene bg lanamommsg 9 with Dissolve(0.8)
    Elizabeth "Um who are you?"
    scene bg lanamommsg 10  with Dissolve(0.8)
    Masseur "Ms . Kriti could not come today due to an wrist injury , I'll be taking her place today"
    Elizabeth "(This is absurd , I can't let a man just massage me but my muscles are so sore.. what do i do?)"
    # Bglanamomdcd -> CHOICE -> Let him massage , Don’t accept it ( +1 corruption if let him massage)
    menu:
        "Let him massage.":
            jump .part_1
        "Don't accept it.":
            jump .part_2

    label .part_2:
        # IF DON’T MasSaGe USE RENDERS OF ->dontmsg-
        scene bg lanamommsgrjct 1  with Dissolve(0.8)
        Elizabeth "I'm sorry , I cannot accept that"
        scene bg lanamommsgrjct 2  with Dissolve(0.8)
        Masseur "But Ms , I am a professional"
        Elizabeth "I'm sure you are , it's just a preference do not take this personally"
        scene bg lanamommsgrjct 3   with Dissolve(0.8)
        Elizabeth "I'll pay for the session still , do not worry"
        Masseur "(Dammit , good babe i missed out on today)"
        jump chap_2_scene_18

    label .part_1:
        # IF LET HIM MASSAGE THEN USE RENDERS OF  -> lethimsglana-
        scene bg lanamommsgaccpt 1  with Dissolve(0.8)
        Elizabeth "Uh alright , well please make it quick then"
        Masseur "No point in rushing mam , I am a professional you need not to worry"
        scene bg lanamommsgaccpt 2  with Dissolve(0.8)
        Masseur "Well then I am ready , shall we begin?"
        scene bg lanamommsgaccpt 3  with Dissolve(0.8)
        Masseur "It'll be aroma oil so you won't feel moisture either"
        scene bg lanamommsgaccpt 4  with Dissolve(0.8)
        Masseur "Mam?"
        scene bg lanamommsgaccpt 5  with Dissolve(0.8)
        Elizabeth "(That's certainly easy on the eyes)"
        scene bg lanamommsgaccpt 6   with Dissolve(0.8)
        Masseur "Are you an athlete mam? your back muscles are quite tense"
        Elizabeth "Kind of you to say , but no just a busy housewife"
        scene bg lanamommsgaccpt 7 with Dissolve(0.8)
        Masseur "It's quite tension heavy mam , you should get this more often done"
        Elizabeth "I do weekly but then business and timings you know"
        scene bg lanamommsgaccpt 8  with Dissolve(0.8)
        Masseur "Understandable , you always get it done by a female masseuce?"
        Elizabeth "Yes , I prefer it because i don't really want my husband to get angry"
        scene bg lanamommsgaccpt 9  with Dissolve(0.8)
        Masseur "Yes mam , rest assured i am a professional"
        scene bg lanamommsgaccpt 10 with Dissolve(0.8)
        Masseur "Having extra strength always is a good point in massage"
        scene bg lanamommsgaccpt 11  with Dissolve(0.8)
        Masseur "(Relaxed it seems , Let's make my move)"
        scene bg lanamommsgaccpt 12  with Dissolve(0.8)
        Masseur "You're very soft skinned mam"
        Elizabeth "Um-- thanks i guess"
        scene bg lanamommsgaccpt 13  with Dissolve(0.8)
        Elizabeth "(Why is he touching my inner thigh.. I have no panties on)"
        scene bg lanamommsgaccpt 14  with Dissolve(0.8)
        Masseur "(Not resisitng? Time to feel further)"
        scene bg lanamommsgaccpt 15  with Dissolve(0.8)
        Elizabeth "(Is he spreading my legs? why?)"
        scene bg lanamommsgaccpt 16  with Dissolve(0.8)
        pause
        scene bg lanamommsgaccpt 17  with Dissolve(0.8)
        Masseur "You're quite tense down here  as well mam , you should rest for a week"
        Elizabeth "I'll give that a thought yeah"
        scene bg lanamommsgaccpt 18  with Dissolve(0.8)
        Masseur "(You wanna play innocent huh , alright then)"
        scene bg lanamommsgaccpt 19 with Dissolve(0.8)
        Masseur "(Let's see what she's got)"
        scene bg lanamommsgaccpt 20 with Dissolve(0.8)
        pause
        scene bg lanamommsgaccpt 21dcd   with Dissolve(0.8)
        Elizabeth "What is he doing?.. I should stop before he gets too further"
        #CHOICE 
        #Let him continue? 
        #Stop  this now ( IF STOP THIS NOW THEN USE RENDERS OF dntmsg like above ) ( IF LET HIM CONTINUE RESUME AHEAD LIKE NORMAL 
        if _in_replay:
            jump .part_3
        menu:
            "Stop this now":
                jump .part_2

            "Let him continue":
                pass

        label .part_3:
            pause
            scene bg lanamommsgaccpt 22  with Dissolve(0.8)
            Masseur  "All good mam?"
            scene bg lanamommsgaccpt 23 with Dissolve(0.8)
            Elizabeth "Y-yes.. just your hands were touching a little upside"
            scene bg lanamommsgaccpt 24  with Dissolve(0.8)
            Masseur "I understand , but its part of the massage mam"
            scene bg lanamommsgaccpt 25  with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 26  with Dissolve(0.8)
            Masseur  "(Holy shit look at this bitch's tight ass)"
            scene bg lanamommsgaccpt 27  with Dissolve(0.8)
            Elizabeth "(He can probably see my pussy.. what am i doing)"
            scene bg lanamommsgaccpt 28  with Dissolve(0.8)
            Masseur "You've got a beautiful behind mam"
            Elizabeth "W-what?"
            scene bg lanamommsgaccpt 29 with Dissolve(0.8)
            Masseur "Your behind pectoral muscles mam ,                                                                                                   "
            Elizabeth "R-right.. thanks"
            scene bg lanamommsgaccpt 30  with Dissolve(0.8)
            Masseur "Please relax mam , it's just a massage"
            scene bg lanamommsgaccpt 31  with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 32  with Dissolve(0.8)
            Masseur "(Let's spread these a little)"
            scene bg lanamommsgaccpt 33 with Dissolve(0.8)
            Elizabeth "(Why am i letting this happen?)"
            scene bg lanamommsgaccpt 33pttwo  with Dissolve(0.8)
            Masseur "(Look at that asshole , this slut is tight)"
            scene bg lanamommsgaccpt 34  with Dissolve(0.8)
            Masseur "(She's just letting me spread her , what a whore )"
            Elizabeth "(I don't have much excuse anymore.. I hope he stops there)"
            scene bg lanamommsgaccpt 35  with Dissolve(0.8)
            Masseur "(Beautiful snatch too)"
            scene bg lanamommsgaccpt 36  with Dissolve(0.8)
            Masseur "Mam , this is now a special glute massage"
            scene bg lanamommsgaccpt 37  with Dissolve(0.8)
            Masseur "(You're mine now babe)"
            scene bg lanamommsgaccpt 38  with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 39 with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 40  with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 41  with Dissolve(0.8)
            Masseur "Look at that.. she wants it now"
            scene bg lanamommsgaccpt 42  with Dissolve(0.8)
            Masseur "Let's see how tight you are"
            scene bg lanamommsgaccpt 43  with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 44  with Dissolve(0.8)
            Elizabeth "(No!.. he's-)"
            scene bg lanamommsgaccpt 45  with Dissolve(0.8)
            Elizabeth "Um excuse me your-"
            Masseur "Shut up , you want this too"
            scene bg lanamommsgaccpt 46  with Dissolve(0.8)
            Masseur "Cute asshole you got , its wrapping around my thumb"
            Elizabeth "Please stop talking like that I-"
            scene bg lanamommsgaccpt 47  with Dissolve(0.8)
            Elizabeth "*Gasp* Aaahh.."
            scene bg lanamommsgaccpt 48  with Dissolve(0.8)
            Elizabeth "Fuck.."
            scene bg lanamommsgaccpt 49  with Dissolve(0.8)
            Masseur "Let's see your love hole"
            scene bg lanamommsgaccpt 50  with Dissolve(0.8)
            pause
            scene bg lanamommsgaccpt 51  with Dissolve(0.8)
            Elizabeth "J-hey stop playing with it"
            scene bg lanamommsgaccpt 52  with Dissolve(0.8)
            Masseur "What ya gonna do about it?"
            Elizabeth "I-"
            scene bg lanamommsgaccpt 53 with Dissolve(0.8)
            Masseur "You love this don't you?"
            scene bg lanamommsgaccpt 54  with Dissolve(0.8)
            Masseur "What a good fucking pussy"
            Elizabeth "(Fuck.. he feels good inside)"
            scene bg lanamommsgaccpt 55  with Dissolve(0.8)
            Elizabeth "AAahhh.. um.."
            scene bg lanamommsgaccpt 55ptscnd  with Dissolve(0.8)
            Masseur "Let me taste your juices now"
            Elizabeth "Wait i have a hus-"
            scene bg lanamommsgaccpt 56  with Dissolve(0.8)
            Elizabeth  "Ahhh..."
            scene bg lanamommsgaccpt 57  with Dissolve(0.8)
            Elizabeth "Unf.. plea-"
            Masseur "Shhh"
            scene bg lanamommsgaccpt 57ptfrst  with Dissolve(0.8)
            Elizabeth "(Fuck why is his tongue so fast..)"
            scene bg lanamommsgaccpt 57pttwo  with Dissolve(0.8)
            Elizabeth "aah.. please slow.."
            scene bg lanamommsgaccpt 58  with Dissolve(0.8)
            Masseur "You smell good and taste good , quite a gem i got today"
            scene bg lanamommsgaccpt 58pttwo  with Dissolve(0.8)
            Elizabeth "Ha.. wait please I-"
            scene bg lanamommsgaccpt 59  with Dissolve(0.8)
            Masseur "Zip it , *slurping*"
            scene bg lanamommsgaccpt 60  with Dissolve(0.8)
            Elizabeth "Mm.., fuck wait wait!"
            scene bg lanamommsgaccpt 61  with Dissolve(0.8)
            Elizabeth "Aaaaaaah! (god...he's so good)"
            scene bg lanamommsgaccpt 62  with Dissolve(0.8)
            Elizabeth "(I can't believe i came..)"
            Masseur "You look beautiful babe"
            scene bg lanamommsgaccpt 63  with Dissolve(0.8)
            Masseur "Oh don't look away now , shy is useless when your pussy is flowing on my tongue"
            scene bg lanamommsgaccpt 64  with Dissolve(0.8)
            Elizabeth "Yes.. you're right um.. can i go now?"
            Masseur "Oh no , you had your fun time to return the favor"
            scene bg lanamommsgaccpt 65  with Dissolve(0.8)
            Elizabeth "Wh-? Hey wait!"
            scene bg lanamommsgaccpt 66  with Dissolve(0.8)
            Elizabeth "*Gulp*"
            scene bg lanamommsgaccpt 67  with Dissolve(0.8)
            Elizabeth "(My jaw)"
            # ANIMATION LOOPS - >
            scene bg_lanamsgsideang_anim_1  with Dissolve(0.8)
            Elizabeth "*Gurg* *gulp I- *gulp*"
            Masseur "Fuck that mouth is so soft holy shit"
            scene bg_lanamsgsideang_anim_2  with Dissolve(0.8)
            Masseur "That's right baby suck that dick.. fuck yeah"
            Elizabeth "(This dick is so good)"
            scene bg_lanamsgsideang_anim_3  with Dissolve(0.8)
            Masseur "Ohhh fuck , I'm cumming"
            scene bg_lanamsgsideang_anim_3  with vpunch
            scene bg_lanamsgsideang_anim_3  with vpunch
            scene bg_lanamsgsideang_anim_3  with vpunch
            # Elizabeth "W*glurg* not in m *glurp*"
            scene bg lanamommsgaccpt 68  with Dissolve(0.8)
            Masseur "Ohhhhh... Fuck that was good"
            scene bg lanamommsgaccpt 69  with Dissolve(0.8)
            Elizabeth "(He came so much i can't even br-)"
            scene bg lanamommsgaccpt 70  with Dissolve(0.8)
            Masseur "Ohhh... man that mouth is magical"
            scene bg lanamommsgaccpt 71 with Dissolve(0.8)
            Masseur "Oh yeah that's right , swallow that baby"
            scene bg lanamommsgaccpt 72  with Dissolve(0.8)
            Elizabeth "Ha.. um"
            $ renpy.end_replay()
            scene bg lanamommsgaccpt 73  with Dissolve(0.8)
            Masseur "Shit , you okay?"
            scene bg lanamommsgaccpt 74  with Dissolve(0.8)
            Elizabeth "Yeah.. could you please take me to the showers?"
            Masseur "Oh uh.. yeah sure"
            scene bg lanamommsgaccpt 75  with Dissolve(0.8)
            Masseur "Let me help you clean up too"
            Elizabeth "Thank you , I'd appreciate that"
            jump chap_2_scene_18


label chap_2_scene_18:
    scene blackscreen
    show titletext "District Court , Brooklyn" with dissolve
    pause 1.0
    window hide
    # SCENE -> courtril / ENDING OF V0.1 ->
    scene bgcourttrl 1  with Dissolve(0.8)
    Stenographer "Attention all present in court."
    scene bgcourttrl 2  with Dissolve(0.8)
    Stenographer "Honourable Judge Dominic Sr. Desiato gracing the court with his presense , please stand"
    scene bgcourttrl 3  with Dissolve(0.8)
    Stenographer "Let the Proceedings begin."

    menu: 
        "Skip court Trial?"

        "Yes":
            jump .part_1
        "No":
            pass

    scene bgcourttrl 4  with Dissolve(0.8)
    "Judge Desiato" "This is a hearing for a divorce settlement between Mister Jonathan hall and Mrs. Mia watanabe"
    scene bgcourttrl 5  with Dissolve(0.8)
    "Judge Desiato" "Respectively with their councils on either side "
    scene bgcourttrl 6 with Dissolve(0.8)
    "Judge Desiato" "Both parties have requested and mutually agreed the jury to be not present in the case , let us proceed"
    scene bgcourttrl 7 with Dissolve(0.8)
    "Judge Desiato" "The hearing concerns the prosecution by Mason majors"
    scene bgcourttrl 8 with Dissolve(0.8)
    "Judge Desiato" "With defence side Jennifer Serkis"
    scene bgcourttrl 9 with Dissolve(0.8)
    "Judge Desiato" "The prosecution may intiate their arguements"
    scene bgcourttrl 10 with Dissolve(0.8)
    Mason "Thank you, Your Honor. Mr. Jonathan Hall has been involved in clear cases of repeated offenses of sexual harassment."
    Mason "While he hasn't been convicted, the repeated accusations do indicate a pattern and nature of such behavior."
    scene bgcourttrl 11 with Dissolve(0.8)
    Mason "There have been various instances of attempted mental and sexual abuse towards my client, Mia Watanabe."
    scene bgcourttrl 12 with Dissolve(0.8)
    Mason "Mr jonathan also made advances towards their daughter 3 days ago due to which she had to run away from the home as well"
    scene bgcourttrl 13 with Dissolve(0.8)
    Mason "Mr. Jonathan before the hearing had tried earlier to bribe one of my juniors on this case to give defence favorable claims to prepare , which needless to say failed"
    scene bgcourttrl 14 with Dissolve(0.8)
    Mason "Your Honor, in the past, Mr. Jonathan had made similar attempts with his older daughter, who is currently with us. As we have provided notice to the defense, we would like to request permission to record her testimony"
    scene bgcourttrl 15 with Dissolve(0.8)
    "Judge Desiato" "The court allows it , proceed"
    scene bgcourttrl 16 with Dissolve(0.8)
    Mason "Thank you   , Please come evelyn"
    Jennifer "(Ah i didn't expect her to come..)"
    scene bgcourttrl 17 with Dissolve(0.8)
    Mason "Ms Evelyn  , what has your relationship been with your father .. importantly why did you move a state away at the qge of 15"
    scene bgcourttrl 18 with Dissolve(0.8)
    Evelyn "My father.. Pardon Mr. Jonathan attempted to.. ah"
    Mason "Take a breath.. It's alright , speak"
    scene bgcourttrl 19 with Dissolve(0.8)
    Evelyn "He groped me , when i was 15 and filmed taking my clothes off when i was asleep.. and uh"
    scene bgcourttrl 20 with Dissolve(0.8)
    Evelyn "Live streamed it to his.. friends and then he I - I woke up a bit later and he was about to penent-"
    scene bgcourttrl 21 with Dissolve(0.8)
    Evelyn "He was on top of me and before he could enter , I- I pushed him away and just ran"
    scene bgcourttrl 22 with Dissolve(0.8)
    Evelyn "I just kept running i didn't know what to do , mom was asleep and I just-"
    scene bgcourttrl 23 with Dissolve(0.8)
    Evelyn "I cried the entire night , I didn't knew what to do people that he knew tried to get me back and i fought and survived"
    scene bgcourttrl 24 with Dissolve(0.8)
    Evelyn "Veronica helped me to move away safely.. I just , I never was the same again"
    Mason "That will be enough , you may go (I'm sorry evelyn..)"
    scene bgcourttrl 25 with Dissolve(0.8)
    Mason "(You deserved a normal life and he took that from you too not just mia)"
    Evelyn "(Sigh.. how could someone ugh)"
    scene bgcourttrl 26 with Dissolve(0.8)
    John "(Did it really hurt that badly?.. I pushed too far)"
    scene bgcourttrl 27 with Dissolve(0.8)
    Mason "The prosecution pleads to give Mr. Jonathan a punishment for their treatment towards their wife mia"
    scene bgcourttrl 28 with Dissolve(0.8)
    Mason "We would also like to grant the divorce settlement with the custody of children included alongside a restraining order , that'll be it your honor"
    scene bgcourttrl 29 with Dissolve(0.8)
    "Judge Desiato" "Defence may present their arguements"
    Jennifer "Thank you your honor"
    scene bgcourttrl 30 with Dissolve(0.8)
    Jennifer "My fellow colleague here has said a wonderful thing, Your Honor."
    scene bgcourttrl 31 with Dissolve(0.8)
    Jennifer "Facts, facts do matter, and in their naivety, it has made them believe that accusations are facts and emotions are convictions."
    scene bgcourttrl 32 with Dissolve(0.8)
    Jennifer "The fact, however, is, Your Lordship, that my client has never been convicted of a single case filed against him."
    scene bgcourttrl 33 with Dissolve(0.8)
    Jennifer "It may be easy to present to the court only the cases that are in the nature of this suit, but there are a lot of cases against my client due to his position of power."
    scene bgcourttrl 34 with Dissolve(0.8)
    Jennifer "A lot of individuals, Your Honor, clearly want to do wrong to my client and have tried several times, playing by law behind his money."
    scene bgcourttrl 35 with Dissolve(0.8)
    Jennifer "They have tried to defame my client, damage his reputation, and take assets that clearly belong to him as theirs in the retrospect of compensation."
    scene bgcourttrl 36 with Dissolve(0.8)
    Jennifer "If my client is the demon that the prosecution is trying to make him out to be, the employees of Mr. Jonathan and his offices are proof that no such behavior exists from my client."
    scene bgcourttrl 37 with Dissolve(0.8)
    Jennifer "As per the testimony Ms. Evelyn Hall provided, I'm not going to deny the events. However, as per the annexure 3 attachment, Mr. Jonathan was outside the country the night this supposed event took place."
    Evelyn "What..?"
    scene bgcourttrl 38 with Dissolve(0.8)
    Jennifer "I apologize to Ms. Evelyn and the experience she had to go through. However, she was in an asleep state, and it was someone else who had sexually harassed her, as per the DNA report as well."
    scene bgcourttrl 39 with Dissolve(0.8)
    Jennifer "As a woman, I feel sad and sorry to hear it. However, I apologize, but I cannot let that be used against my client when he was not present at the time this occurred."
    scene bgcourttrl 40 with Dissolve(0.8)
    Jennifer "I apologize, Ms. Evelyn. I hope nothing but good recoveries lie ahead for you, but I cannot go against the facts. However, you have my sympathy."
    Evelyn "(How.. I - no does money really absolve everything?)"
    scene bgcourttrl 41 with Dissolve(0.8)
    Jennifer "Your Lordship, the defense council seeks nothing more than for the court to see justice done and for the divorce plea to be accepted. Law is above everyone."
    scene bgcourttrl 42 with Dissolve(0.8)
    Jennifer "The defense would like the court to note that Ms. Mia did assault my client, as per the provided medical records."
    scene bgcourttrl 43 with Dissolve(0.8)
    Jennifer "However, we are happy to grant the divorce she seeks. But my client deserves what he should: custody of Ms. Kiara Hall and reduced alimony, as it is a clear attempt to extract money from my client."
    scene bgcourttrl 44 with Dissolve(0.8)
    "Judge Desiato" "Prosecution may continue"
    scene bgcourttrl 45 with Dissolve(0.8)
    Mason "Right.. Your honor prosecution would like to cross Mr. Jonathan if the court allows it"
    "Judge Desiato" "Proceed"
    scene bgcourttrl 46 with Dissolve(0.8)
    Mason "Mr. Jonathan , is it true that you were present at the time 4 days ago at the night that this assault occured?"
    John "Yes , It is correct that i was home"
    scene bgcourttrl 47 with Dissolve(0.8)
    Mason "Good , so what happened that night?"
    John "I was returning from my friends meeting and i was then returning home. I asked where is my daughter kiar and mia siddenly lost her temper trying to attack me with a a wine glass"
    scene bgcourttrl 48 with Dissolve(0.8)
    Mason "I see , so you are saying my client attacked you with a wine glass however there were no stains or any damage to your apartment home?"
    John "Mia may have cleaned it and i did dodge it"
    scene bgcourttrl 49 with Dissolve(0.8)
    Mason "I do not need your reasoning for it mr jonathan , just an answer"
    John "Yes.. "
    scene bgcourttrl 50 with Dissolve(0.8)
    Mason "So , despite my client being the agitator as you claim why did your daughter leave the house ?"
    John "My daughter was manipulated into thinking that i had hit mia , she is sensitive and very innocent , It's clear i didn't hit my wife"
    scene bgcourttrl 51 with Dissolve(0.8)
    Mason "Fair , so why were you transported to another apartment of yours and  visited a doctor at night after the event"
    John "Yeah because mia had assaulted me with the glass"
    Mason "But you just claimed to dodge it?"
    scene bgcourttrl 52 with Dissolve(0.8)
    John "Uh , mia assaulted me later as well"
    Mason "Then that would be the genital trauma correct?"
    John "(You bastard..) Yes i was hit"
    scene bgcourttrl 53 with Dissolve(0.8)
    Mason "Point to be noted my lord , Mr. Jonathan claims that ms mia attacked him twice however the report submitted only has one injury caused by utensil"
    scene bgcourttrl 54 with Dissolve(0.8)
    Mason "Which as he claims he dodged , even if believed the location where this happened was at an angle my client could not throw it to his groin in any possible way"
    scene bgcourttrl 55 with Dissolve(0.8)
    Mason "Truth is your honor , Mr. jonathan attempted to grope the 2nd daughter and when my client saw it as a mother she pushed him away and got his daughter out"
    scene bgcourttrl 56 with Dissolve(0.8)
    Mason "Between that exchange Mr. jonathan hit himself to claim an injury that didn't exist later and now is trying to blame my client because hd eson't want the world to see the vile man he is preying his daughters"
    scene bgcourttrl 57 with Dissolve(0.8)
    Jennifer "I object, Your Honor! Character assassination of my client!"
    scene bgcourttrl 58 with Dissolve(0.8)
    "Judge Desiato" "Sustained, Mr masson please let the court decide the character and stick to point"
    Mason "Apologies, Your Honor. All I am saying is that the claims and evidence don't make sense."
    scene bgcourttrl 59 with Dissolve(0.8)
    Mason "Whatever the defense may claim, the reality is that Mr. Jonathan attempted to do what he did with Ms. Evelyn. She was a teenager who was drugged, and that is why the facts are clouded, sadly used by the defense in this way."
    scene bgcourttrl 60 with Dissolve(0.8)
    Mason "Ms. Kiara had mental health issues as well, and what Mr. Jonathan did only further damaged it. That is why she ran away."
    scene bgcourttrl 61 with Dissolve(0.8)
    Mason "That is why the reason why today this case exists, so he can continue to do it more and ruin her life, just as he has done to my client."
    scene bgcourttrl 62 with Dissolve(0.8)
    Jennifer "I object, Your Honor! My client is being led on without evidence and false claims."
    "Judge Desiato" "Taken , Mr. Mason please wrap your arguement"
    scene bgcourttrl 63 with Dissolve(0.8)
    Mason "Your Honor, my conclusion here is that Mr. Jonathan knew what he was doing and why. Excusing it based on the past is not how the law works."
    scene bgcourttrl 64 with Dissolve(0.8)
    Mason "We simply want custody of the children and are willing to receive 0 alimony or compensation if it balances the situation."
    scene bgcourttrl 65 with Dissolve(0.8)
    "Judge Desiato " "Alright. Thirty-minute recess. Please maintain order"
    scene bgcourttrl 66 with Dissolve(0.8)
    pause
    scene bgcourttrl 67 with Dissolve(0.8)
    pause
    scene bgcourttrl 68 with Dissolve(0.8)
    Mason "What do you think you're doing?"
    Jennifer "Defending my client , isn't that what you are too?"
    scene bgcourttrl 69 with Dissolve(0.8)
    Mason "Jennifer , you know that man stop it. This isn't right and you know that"
    Jennifer "I'm doing my job , as an attorney i don't judge that's the role of the system"
    scene bgcourttrl 70 with Dissolve(0.8)
    Jennifer "You know that too , we're just doing what we get paid for"
    Mason "Is this because of our past?.. me and you?"
    scene bgcourttrl 71 with Dissolve(0.8)
    Jennifer "I don't know what you're talking about"
    Mason "You and i didn't end on a good note ,  I understand.. but why take it out on someone innocent?"
    scene bgcourttrl 72 with Dissolve(0.8)
    Jennifer "WE DIDN'T END MIND YOU! , you chose to give up on me for that asian bitch and never got back even after she left you"
    Mason "That's not true you know the reality of it"
    scene bgcourttrl 73 with Dissolve(0.8)
    Mason "I loved mia from the start , you deserved better i didn't want you to feel lead on"
    Jennifer "What about me then?"
    scene bgcourttrl 74 with Dissolve(0.8)
    Jennifer "I loved you , i fucking waited for you and what did you do?"
    scene bgcourttrl 75 with Dissolve(0.8)
    Jennifer "That's right , fucking nothing just broke me nothing else"
    Mason "I'm sorry i really am  but Jennifer don't do this , mia deserves justice here"
    scene bgcourttrl 76 with Dissolve(0.8)
    Jennifer "She's getting the divorce as she wanted  , my client requested custody and that i have to do"
    Mason "Jenny please listen"
    scene bgcourttrl 77 with Dissolve(0.8)
    Jennifer "Move the fuck away don't touch me!"
    Mason "Ah!"
    scene bgcourttrl 78 with Dissolve(0.8)
    Jennifer "Don't call me that.. you lost the right to use that name years ago"
    Mason "Jennifer i just..- Alright."
    scene bgcourttrl 79 with Dissolve(0.8)
    Mason "(Dammit..)"
    Jennifer "(I thought i had moved on , why did that hurt me)"
    scene bgcourttrl 80 with Dissolve(0.8)
    Stenographer "Court resumes"
    scene bgcourttrl 81 with Dissolve(0.8)
    Jennifer "The defence would like to call Ms Mia to the witness box"
    "Judge Desiato" "Court allows it"
    scene bgcourttrl 82 with Dissolve(0.8)
    Jennifer "Ms. Mia how do you know your defence council? Let me rephrase how well do you know Mr. mason?"
    Mia "He's my lawyer and he has helped me in past regarding legal matters related to evelyn and he's my friend's cousin"
    scene bgcourttrl 83 with Dissolve(0.8)
    Jennifer "Alright , so you and Mr. Mason have no other aspects that you're not disclosing then?"
    Mia "I don't understand whaet you mean i jus-"
    scene bgcourttrl 84 with Dissolve(0.8)
    Jennifer "That's alright Ido , so is it true that you knew of these alleged events with your daughter evelyn hall, correct?"
    Mia "Yes i did and-"
    scene bgcourttrl 85 with Dissolve(0.8)
    Jennifer "Yet you stayed with my client despite being the disgusting man he is according to you instead of filing divorce back then"
    Mia "Yes because i did love him and i didn't know much so i gave him a second chance and i-"
    scene bgcourttrl 86 with Dissolve(0.8)
    Jennifer "That'll be all ms mia you can go"
    scene bgcourttrl 87 with Dissolve(0.8)
    Jennifer "Your honor , my client has been accused , humiliated and defamed in court of infarious things however in the eyes of law , has been absolved by all of them"
    scene bgcourttrl 88 with Dissolve(0.8)
    Jennifer "the prosection tried their best to also trigger them in court and yet my client remained what he is , A innocent humble man"
    scene bgcourttrl 89 with Dissolve(0.8)
    Jennifer "The reason for that sir is that the prosecution has also hidden an important fact from the court that directly affects the suit , If court allows we'd like to provide this evidence"
    Mason "I object your honor , no pre - notice was given for this evidence it cannot be counted for"
    scene bgcourttrl 90 with Dissolve(0.8)
    "Judge Desiato" "Overruled , If the evidence helps the case then i will not let it be destroyed , you can request for a forgery verification if you want , however let's not waste time here"
    Mason "My apologies your honor.. alright"
    scene bgcourttrl 91 with Dissolve(0.8)
    Jake "No.. evelyn , what the hell"
    scene bgcourttrl 92 with Dissolve(0.8)
    Jake "This can't be happening , I- i didn't know"
    Jennifer "Your honor the file is on the desk provided to you with some images in it"
    scene bgcourttrl 93 with Dissolve(0.8)
    Jennifer "As youc ans ee your honor , I respect the dignity of clients so we're not going to display them"
    scene bgcourttrl 94 with Dissolve(0.8)
    Jennifer "However as per the pictures provided to you , this is just one of these instances"
    Mason "What?.."
    Mia "What?"
    scene bgcourttrl 95 with Dissolve(0.8)
    Jennifer "The party and the prosecution have a relationship  in past and secretly have continued it , as the pictures show.. both in shower together without clothing"
    scene bgcourttrl 96 with Dissolve(0.8)
    Mia "What? no! I-that wasn't"
    scene bgcourttrl 97 with Dissolve(0.8)
    "Judge Desiato" "Tell your client mr mason if they wish to speak , do it in the witness box"
    scene bgcourttrl 98 with Dissolve(0.8)
    Jennifer "Ms mia and the prosecutor here together in  shower.. I believe that's alot more than just my lawyer"
    "Judge Desiato" "Mr. Mason.. what is this? Are you not aware of the rule of conducts which prohibits relatinships with clients be it sexual or romantic? If so it is to be shown by a notice"
    Mason "Your honor , I-"
    scene bgcourttrl 99 with Dissolve(0.8)
    "Judge Desiato" "Would you like to cross this or verify that is true? please do not waste the court's time"
    Mason "It's true your honor.. No cross , I'm sorry"
    "Judge Desiato" "Do not be sorry , be better."
    scene bgcourttrl 100 with Dissolve(0.8)
    "Judge Desiato" "Defence , continue"
    Jennifer "Y-yes your honor"
    scene bgcourttrl 101 with Dissolve(0.8)
    Jennifer "Mrs. Mia didn't leave that night because no such event took place , it was rather to plan this long ploy alongside to get my client's money , even if alimony is skipped half or properties are signed to 30 percent to her , It's clear what her motivation was."
    scene bgcourttrl 102 with Dissolve(0.8)
    Mia "No! , He made me sign that i didn't want any of it!"
    "Judge Desiato" "Mr. Mason i do not like to repeat myself tell your client kindly"
    Mason "Mia.. please"
    scene bgcourttrl 103 with Dissolve(0.8)
    Jennifer "Not only that your honor but i believe that this affair was sexual way before ahead of the events and our private investigator only discovered little of it"
    Mia "(No.. that's not true)"
    scene bgcourttrl 104 with Dissolve(0.8)
    Jennifer "It is quite ironic then to claim of my client as this devil and abuser while Mrs. Mia was the one doing such acts"
    John "(Damn and i thought i was brutal)"
    scene bgcourttrl 105 with Dissolve(0.8)
    Jennifer "Your honor i do not wish to demean Mrs. Mia here , Her life and her body is her choice to give to whomsoever but doing so while married is adultry and framing my cleint while it happens is just hypocricy"
    scene bgcourttrl 106 with Dissolve(0.8)
    Jennifer "However we do not want to intiate that proceess , my client has done everything right and hence we don't consider it defamation , the only thing we seek is custody and alimony to be reduced to 5 percent."
    scene bgcourttrl 107 with Dissolve(0.8)
    Jennifer "My client is a family man , he just wants to care for his daughters and make them know how much he values them , that's all your honor"
    "Judge Desiato" "Prosecution , continue"
    Mason "..."
    scene bgcourttrl 108 with Dissolve(0.8)
    "Judge Desiato" "Mr. Mason! Talk"
    Mason "Y-yes your honor"
    scene bgcourttrl 109 with Dissolve(0.8)
    Mason "Your honor i apologize for not disclosing this earlier.. as this was a recent event"
    scene bgcourttrl 110 with Dissolve(0.8)
    Mason "However It's not the motive of our case or leads here , even if presented to court it is impossible to deny other facts"
    scene bgcourttrl 111 with Dissolve(0.8)
    Mason "Instances and accounts of Mr. Jonathan trying to get what he wants , text mesages of his group chats on how they talk about their daughters and women in general"
    scene bgcourttrl 112 with Dissolve(0.8)
    Mason "We also submitted Mrs. Sachiko Haru's testimony in previous case where despite being married to my client Mr. Jonathan was raising another family till he was caught"
    "Judge Desiato" "Court will take another receess , 10 minutes"
    scene bgcourttrl 113 with Dissolve(0.8)
    Evelyn "Fuck this.."
    Veronica "Eve , plese wait!"
    scene bgcourttrl 114 with Dissolve(0.8)
    Veronica "Sigh..(Please , for me)"
    scene bgcourttrl 115 with Dissolve(0.8)
    Mason "Fuck , fuck fuck! , How could i have been so fucking stupid!"
    scene bgcourttrl 116 with Dissolve(0.8)
    Jake "No no no , not this . Evelyn.. I'll get out of this , I have to"
    scene bgcourttrl 117 with Dissolve(0.8)
    Stenographer "Court resumes"
    scene bgcourttrl 118 with Dissolve(0.8)
    "Judge Desiato" "With both the sides heard , the court needs more time to evaluate the situations and on next hearing will give out more extensive breakdowns"
    scene bgcourttrl 119 with Dissolve(0.8)
    "Judge Desiato" "It is clear that the prosecution hid facts from the court that have revealed new intrests to the overall matter and hence court cannottake what's given for face value"
    scene bgcourttrl 120 with Dissolve(0.8)
    "Judge Desiato" "That said , Mr. Jonathan and the defence have also tried to play around the rules of law just enough to bide but the leaked conversations and messages and testimony of previous partner puts a shadow over your claims as well"
    scene bgcourttrl 121 with Dissolve(0.8)
    "Judge Desiato" "The court therefore allows Mrs. Mia's divorce to go through once proceedings and case settles , Mr jonathan will have to pay double the alimony  due to his repeated court endeavors"
    scene bgcourttrl 122 with Dissolve(0.8)
    "Judge Desiato" "With that said , Mr. Jonathan clearly has as per facts provided , tried to be a better man and law gives priority to facts"
    "Judge Desiato" "Therefore , child in question , Kiara hall's custody shall be shared between the two parties on a month basis , upon agreed terms with security cameras in respective locations for future safety of the trial and the involved parties"
    scene bgcourttrl 123 with Dissolve(0.8)
    "Judge Desiato" "As for the prosecutors , Mr mason after the trial has ended your license will be supspended for 15 months for this violation , and Ms. Jennifer please talk with decency to clients"
    Jennifer "I apologize your honor , I will keep it in mind"
    Mason "Yes , Your honor.. I accept it"
    scene bgcourttrl 124 with Dissolve(0.8)
    "Judge Desiato" "Court is dismissed , next hearing will be on 13th"
    scene bgcourttrl 124pttwo with Dissolve(0.8)
    Mia "(Kiara.. Evelyn..)"
    Veronica "Mia.. come"
    scene bgcourttrl 124ptthree with Dissolve(0.8)
    Veronica "Mia? let's go home"
    scene bgcourttrl 124ptfour with Dissolve(0.8)
    Veronica "Mia! , mason come here!"
    Mason "Mia! mia!"
    scene bgcourttrl 124ptfive with Dissolve(0.8)
    Mason "What happened?"
    Mia "(Father..)"
    label .part_1:
        scene bgcourttrl 125 with Dissolve(0.8)
        Mason "(Mia , I'll fix this i promise)"
        scene bgcourttrl 126 with Dissolve(0.8)
        Veronica "Are you.. coming?"
        Mason "No I'm taking her to hospital first , you go home"
        scene bgcourttrl 127 with Dissolve(0.8)
        Veronica "Mason are you alright?"
        Mason "I don't know and i don't care about myself right now , go home we'll talk later"
        scene bgcourttrl 128 with Dissolve(0.8)
        Veronica "(Why did this go so wrong.. this was suppsoed to be a happy ending)"
        scene bgcourttrl 129 with Dissolve(0.8)
        Veronica "I don't even know where eve is , sigh what a mess"
        scene bgcourttrl 130 with Dissolve(0.8)
        John "Hello Ms. veronica! what a lovely evening , how are you?"
        scene bgcourttrl 131 with Dissolve(0.8)
        Veronica "You've got some nerve trying to talk after what you did today , fucking pathetic"
        scene bgcourttrl 132 with Dissolve(0.8)
        John "As far as it's concerned , I played by the law unlike your cousin and specially you"
        Veronica "What do you mean?"
        scene bgcourttrl 133 with Dissolve(0.8)
        John "See I know about your little stunt you pulled at the bar of deleting the footage"
        scene bgcourttrl 134 with Dissolve(0.8)
        Veronica "What?.. How do you?"
        scene bgcourttrl 135 with Dissolve(0.8)
        John "That isn't the concern for now , all i want is conversation and ill drop you home as well so shall we?"
        Veronica "(So he had someone spy me too)"
        scene bgcourttrl 136 with Dissolve(0.8)
        Veronica "Try anything funny and i'll break your face in"
        John "I won't even touch you , I'll sit on the other side so you're comfortable , please come in"
        scene bgcourttrl 137 with Dissolve(0.8)
        John "Now then a bit more relaxed we are, you should take the jacket off too the car is temperature controlled"
        Veronica "What is this?.. what are you thinking?"
        scene bgcourttrl 138 with Dissolve(0.8)
        Veronica "If you think you can blackmail me , you're in for a rude awakening"
        John "Relax this is merely a conversation , we both want the best in intrests don't we?"
        scene bgcourttrl 139 with Dissolve(0.8)
        Veronica "Get to the point"
        John "You see the reason i didn't file for evidence tamperning because mr mason would get his license suspended indefinitely and that would delay the case , wouldn't benefit your cousin or your friend mia right?"
        Veronica "What are you implying?"
        scene bgcourttrl 140 with Dissolve(0.8)
        John "You see , it was very smart of you indeed to delete the footage even though on the outside it might've helped mia because-"
        Veronica " Becausse you'd have bribed a fake witnes and call it non voluntary intoxication rather than voluntary , which would've resulted in us proving it and making the case longer"
        scene bgcourttrl 141 with Dissolve(0.8)
        John "Smart as ever , you're the best for a reason , so it is clear we want this to be resolved fast , correct?"
        Veronica "Yes , cut to the chase already"
        scene bgcourttrl 142 with Dissolve(0.8)
        John "Fine then , here is my offer "
        John "I will not present that evidence tamperning in court  nor will i bother mia or her family after it.. all i ask in return is a week of your company"
        Veronica "What the fuck do you mean? I'm not someone you can ground that way , I know what you mean by this company"
        scene bgcourttrl 143 with Dissolve(0.8)
        John "Relax , realx , such a pretty face but so much anger. I  will not force myself upon you"
        John "All i ask are two simple things , to attend a meeting with my arab friends , they are impressed by your style"
        Veronica "What is the second?"
        scene bgcourttrl 144 with Dissolve(0.8)
        John "Second would be to play a round of poker with me and my few invester friends , the only caviat is.. It's strip poker."
        Veronica "How dare you-"
        scene bgcourttrl 145 with Dissolve(0.8)
        John "Hear me out kindly"
        John "If you win this , I will never ever look back at on mia , your cousin , you or my daughters ever again"
        Veronica "Why would i trust you?"
        scene bgcourttrl 146 with Dissolve(0.8)
        John "I'm  a man of my words ask anyone , like i said we both want this over fast don't we?"
        scene bgcourttrl 147 with Dissolve(0.8)
        John "If i get the deal with the arabs , my business will grow in dubai as well , increasing my networth even more"  
        scene bgcourttrl 148 with Dissolve(0.8)
        Veronica "Is money really all that matters to you? don't you have enough?"
        John "I do but even with it i can't get the best like you .. so what do you think?"
        scene bgcourttrl 149 with Dissolve(0.8)
        Veronica "Listen here you shithead , I am not doing anything you want here ., If you want to sue  me , go for it. I'll take on that bitch and you alone and destr-"
        John "Now now , hear me out"
        scene bgcourttrl 150 with Dissolve(0.8)
        John "I know you can fight , it's what i love about you."
        John "However due to your fragile ego here you'd be denying the life your cousin and mia have waited for so long and perhaps.. the life you want with evelyn as well"
        scene bgcourttrl 151 with Dissolve(0.8)
        Veronica "(Eve.. no) Sigh if i win , you leave.. forever?"
        John "Cross my heart , I'll even sign a bond"
        scene bgcourttrl 152 with Dissolve(0.8)
        John "Let me make it better for you , even if you lose. I will still leave them , the only difference is that you and i will make lov-"
        Veronica "Stop.. ugh"
        scene bgcourttrl 153 with Dissolve(0.8)
        Veronica "I need some time to think about it"
        John "Take it! , we have a month after all so don't fret too much though sooner would be prefered"
        scene bgcourttrl 154 with Dissolve(0.8)
        John "Look at that we're at your home , you deserve so much better honestly"
        scene bgcourttrl 155 with Dissolve(0.8)
        John "The next time we meet , you will be sitting on my face sweetheart"
        scene bgcourttrl 156 with Dissolve(0.8)
        Veronica "What do i do..?"
        scene bgcourttrl 157 with Dissolve(0.8)
        Veronica "Evelyn , mia , mason"
        scene bgcourttrl 158 with Dissolve(0.8)
        Veronica "I can fix it all , but what if i lose?"
        scene bgcourttrl 159 with Dissolve(0.8)
        Veronica "This feels like a nightmare but i can't wake up"
    jump chap_2_scene_19

label chap_2_scene_19:
    scene bg evlynprkscn 1 with Dissolve(0.8)
    Evelyn "V's text , Mom i hope you're alright"
    scene bg evlynprkscn 2 with Dissolve(0.8)
    Evelyn "I don't care.. I took him on once , I'll do it again"
    scene bg evlynprkscn 3 with Dissolve(0.8)
    Evelyn "Kiara , I'll protect you too"
    scene bg evlynprkscn 4 with Dissolve(0.8)
    Jake "Hey , you said butterscotch"
    Evelyn "Ah"
    scene bg evlynprkscn 5 with Dissolve(0.8)
    Evelyn "Heh hi , you remembered?"
    Jake "Kinda hard to forget considering how we met haha"
    scene bg evlynprkscn 6 with Dissolve(0.8)
    Evelyn "I do remmeber , come sit"
    scene bg evlynprkscn 7 with Dissolve(0.8)
    Jake "Sorry i didn't bring the family pack , ran out of stock"
    Evelyn "I love ice cream but not that much , it's alright"
    scene bg evlynprkscn 8 with Dissolve(0.8)
    Jake "I like butterscotch too , tho i love strawberry don't judge me"
    Evelyn "Heh , strawberry is decent too"
    scene bg evlynprkscn 9 with Dissolve(0.8)
    Jake "The weather is pretty decent today"
    Evelyn "I suppose so.."
    scene bg evlynprkscn 10 with Dissolve(0.8)
    Jake "I basically had like 5 alarms for this since i didn't wanna miss it"
    Evelyn "Yeah , I appreciate that"
    scene bg evlynprkscn 11 with Dissolve(0.8)
    Jake "You alright? You seem a bit low"
    Evelyn "I-"
    scene bg evlynprkscn 12 with Dissolve(0.8)
    Evelyn "Do you want me to lie or say the truth?"
    Jake "Whichever helps , in the end you being okay matters"
    scene bg evlynprkscn 13 with Dissolve(0.8)
    Evelyn "I can't say too much but my family is.. messsed up right now , I thought it'd end today but it got worse"
    scene bg evlynprkscn 14 with Dissolve(0.8)
    Evelyn "Stuff keeps happening and it's beyond my control  and i just don't know what to do"
    Jake "Well i think you shou ld be with those who matter to you the most"
    scene bg evlynprkscn 15 with Dissolve(0.8)
    Jake "Wrong apples you can ignore but don't leave the good ones in dust over it"
    Evelyn "(Stay with family instead of running again?) but there 's a problem.. I'm not confident"
    scene bg evlynprkscn 16 with Dissolve(0.8)
    Evelyn "What if my mind gets changed? What if i don't want to later on?"
    Jake "Then leave , but you won't know till you try right?"
    scene bg evlynprkscn 17 with Dissolve(0.8)
    Jake "I mean think of it like this , you just said what if you don't want to but what if you did want it and you killed that part of you for no reason?"
    Jake "Maybe it's exactly what you need?"
    scene bg evlynprkscn 18 with Dissolve(0.8)
    Evelyn "You know i often think about how people can be so happy after traumatic events in life , I never learned that as a kid so i'm stuck with my past ghosts"
    Jake "Well i was too , but my mom told me something good"
    Jake "She's alot like you actually"
    scene bg evlynprkscn 19 with Dissolve(0.8)
    Jake "When my dad ran away and we found out he overdosed , I said everyone makes fun of me mom , or bullies me for it , or just doesn't realize how much pain i'm in."
    Evelyn "I'm sorry.. I didn't mean to -"
    scene bg evlynprkscn 20 with Dissolve(0.8)
    Jake "No , It's alright. See the point is she said you don't owe anyone anything in this world , no explanations , no tears  , no laughs or nothing"
    Jake "They're expressions you don't fake them and expect to be positive , just be yourself"
    scene bg evlynprkscn 21 with Dissolve(0.8)
    Jake "Just like you i said but after so much bad has happened how could i ever hope for something good? remain positive afrer such a change?"
    scene bg evlynprkscn 22 with Dissolve(0.8)
    Jake "Mom said it's like in those old wars or conflicts jake , there were alot of people or legends that could've just gave up and ran away after suffering , but they didn't because they had something to live for"
    Jake "Something worth saving , to keep living , to hold on to"
    Evelyn "What do we hold on to?"
    scene bg evlynprkscn 23 with Dissolve(0.8)
    Jake "I asked the same and she said.."
    Jake "She said that there's some kindness in this world and we can't ever let it die , the good if you see it fade away , become the reason instead and you'll find positivity again"
    scene bg evlynprkscn 24 with Dissolve(0.8)
    Jake "I mean look at you for example , you helped me even though you didn't have to , you're a part of it too"
    Evelyn "I - um"
    scene bg evlynprkscn 25 with Dissolve(0.8)
    Evelyn "I have to go"
    Jake "Um did i say anything wrong?"
    scene bg evlynprkscn 26 with Dissolve(0.8)
    Evelyn "No no , i just got my motivation i think thanks to you , see ya later okay"
    Jake "Yeah sure you too"
    scene bg evlynprkscn 27 with Dissolve(0.8)
    Jake "Evelyn.."
    scene bg evlynprkscn 28 with Dissolve(0.8)
    Jake "I will get you out of this mess , i don't know if you'll forgive me but it's the right thing to do"
    scene bg evlynprkscn 29 with Dissolve(0.8)
    Jake "Mom will she forgive me? will you forgive me? I feel like -"
    scene bg evlynprkscn 30 with Dissolve(0.8)
    Jake "Ah!"
    Evelyn "Thank you , truly i mean it i needed that"
    scene bg evlynprkscn 31 with Dissolve(0.8)
    Jake "I needed that too , thanks"
    Evelyn "The ice cream was great.. tell your mom i said hi"
    scene bg evlynprkscn 32 with Dissolve(0.8)
    Jake "I will , so see you again soon?"
    Evelyn "Yeah soon"
    scene bg evlynprkscn 33 with Dissolve(0.8)
    Jake "Remember to share , it helps always"
    Evelyn "You too , see ya"
    jump chap_2_scene_20

label chap_2_scene_20:
    scene bg jhnbljhbscn 1 with Dissolve(0.8)
    John "Hehe , Keep going at it girls"
    scene bg jhnbljhbscn 2 with Dissolve(0.8)
    pause
    scene bg jhnbljhbscn 3 with Dissolve(0.8)
    pause
    scene bg jhnbljhbscn 4 with Dissolve(0.8)
    pause 
    scene bg jhnbljhbscn 5 with Dissolve(0.8)
    pause 
    scene bg jhnbljhbscn 6 with Dissolve(0.8)
    John "Oh yeah , nice baby lick the balls" 
    scene bg jhnbljhbscn 7 with Dissolve(0.8)
    John "I wonder how soft veronica's lips are"
    scene bg jhnbljhbscn 8 with Dissolve(0.8)
    "*Calling sounds from laptop*"
    scene bg jhnbljhbscn 9 with Dissolve(0.8)
    John "Hello ms wong! good morning to you!"
    AgentWong "Evening to you , I'm fine"
    scene bg jhnbljhbscn 10 with Dissolve(0.8)
    John "I hope all the hotel is to your liking"
    AgentWong "It is.. , what's that sound?"
    scene bg jhnbljhbscn 11 with Dissolve(0.8)
    John "Do you mean this?"
    AgentWong "Ugh the fuck is wrong with you? , move the fucking camera"
    scene bg jhnbljhbscn 12 with Dissolve(0.8)
    John "Well you had asked so , anyway i was about to call you as well"
    scene bg jhnbljhbscn 13 with Dissolve(0.8)
    John "SInce you've done already so , any updates?"
    scene bg jhnbljhbscn 14 with Dissolve(0.8)
    AgentWong "She's got few jobs that she'll be working now , so i'll have to monitor those in person"
    John "Job? The fuck why is my precious daughter working for those fucking poor cunts? Did she get hurt? anyone get close? Where-"
    scene bg jhnbljhbscn 15 with Dissolve(0.8)
    AgentWong "Calm down , she is old enough to take care of herself too , but yes she's doing it since she wants to stand on her own feet"
    John "Dammit , ms wong please take care of her!"
    scene bg jhnbljhbscn 16 with Dissolve(0.8)
    AgentWong "I'm doing my job if that's what you're asking"
    John "I will get the case resolved here soon but i need her to be safe , why is she doing this? I've given her everything she could want"
    scene bg jhnbljhbscn 17 with Dissolve(0.8)
    AgentWong "If you were a good father you'd understand why"
    John "Oh save your noble comments ms wong , you're doing this for money too so don't pretend like you care"
    scene bg jhnbljhbscn 18 with Dissolve(0.8)
    AgentWong "Tsk.."
    John "Ah i apologize please don't ruin your lovely face by anger , I am just worried"
    scene bg jhnbljhbscn 19 with Dissolve(0.8)
    AgentWong "I'll keep her safe don't worry, bye for now."
    $ renpy.end_replay()
    scene bg jhnbljhbscn 20 with Dissolve(0.8)
    John "Wait ! One thing ms wong"
    AgentWong "What?"
    scene bg jhnbljhbscn 21 with Dissolve(0.8)
    John "Every woman has a price , the girl in my lap right now is the nationals winner , how much would it be from your pretty lips?"
    AgentWong "Fuck off"
    John "Understood!"
    scene bg miamasonlatevescn 1 with Dissolve(0.8)
    Mason "Mia , I understand if you can't forgive me this is my mistake"
    Mia "No it isn't , It's partly mine too.. or both , I don't know."
    scene bg miamasonlatevescn 2 with Dissolve(0.8)
    Mason "I should've just stopped , you probably hate me and i understand and accept it"
    scene bg miamasonlatevescn 3 with Dissolve(0.8)
    Mia "Hey hey no , I don't .. Look i don't regret what we did , I liked it why would i hate you?"
    scene bg miamasonlatevescn 4 with Dissolve(0.8)
    Mason "I will try my best i promise , I don't care what it takes I'll get you the life and peace you deserve "
    scene bg miamasonlatevescn 5 with Dissolve(0.8)
    Mia "I know you will , I'm sorry about your license"
    Mason "Fuck that thing , I don't care about it , I'd bring the moon if i had to for you"
    scene bg miamasonlatevescn 6 with Dissolve(0.8)
    Mason "Whatever it takes , believe me i'll do it"
    Mia "(He is just amazing)"
    scene bg miamasonlatevescn 7 with Dissolve(0.8)
    Mia "I know you will , stop hurting yourself please we're together that's all that matters"
    Mason "Yeah , It's all i need too"
    scene bg miamasonlatevescn 8 with Dissolve(0.8)
    Mia "I'm just worried about evelyn and kiara , I want them to be happy"
    scene bg miamasonlatevescn 9 with Dissolve(0.8)
    Mason "Kiara has family there too , Evelyn is strong.. don't worry she'll handle it and we're there for her in the end"
    Mia "Thank you , Let's get to bed together now i don't care what the world thinks"
    jump chap_2_scene_21

label chap_2_scene_21:
    scene bg valevenitscn 1 with Dissolve(0.8)
    pause
    scene bg valevenitscn 2 with Dissolve(0.8)
    pause
    scene bg valevenitscn 3 with Dissolve(0.8)
    Veronica "(I can't decide on anything , am i that selfish or scared?)"
    scene bg valevenitscn 4 with Dissolve(0.8)
    Veronica "(Even if i lose , it's still a better life for everyone)"
    scene bg valevenitscn 5 with Dissolve(0.8)
    Veronica "(At this point I don't know but i have to decide soon)"
    scene bg valevenitscn 6 with Dissolve(0.8)
    pause
    scene bg valevenitscn 7 with Dissolve(0.8)
    John "You don't have to , we could just do it now baby"
    scene bg valevenitscn 8 with Dissolve(0.8)
    Veronica "*Gasp* , Wha-.. ha."
    scene bg valevenitscn 9 with Dissolve(0.8)
    Veronica "(I heard his voice.. i felt something , what the hell)"
    scene bg valevenitscn 10 with Dissolve(0.8)
    Veronica "(This is just unfair , why do i feel weak for the first time in my life)"
    "*Door Bell rings*"
    scene bg valevenitscn 11 with Dissolve(0.8)
    Veronica "Who could it be at this time?"
    scene bg valevenitscn 12 with Dissolve(0.8)
    pause
    scene bg valevenitscn 13 with Dissolve(0.8)
    Veronica "Eve.. Hey I uh-"
    Evelyn "I didn't know who else i could go to"
    scene bg valevenitscn 14 with Dissolve(0.8)
    Evelyn "I'm sorry for leaving the way i did"
    Veronica "It's alright , please don't apologize"
    scene bg valevenitscn 15 with Dissolve(0.8)
    Evelyn "Can i come in?"
    Veronica "Of course, please come in make yourself comfortable"
    scene bg valevenitscn 16 with Dissolve(0.8)
    Veronica "I had dinner already but if you want i can order something or make it"
    Evelyn "No it's fine , I ate outside already"
    scene bg valevenitscn 17 with Dissolve(0.8)
    Evelyn "(Stick to those who matter to you.. you'll be positive again)"
    scene bg valevenitscn 18 with Dissolve(0.8)
    pause
    scene bg valevenitscn 19 with Dissolve(0.8)
    Veronica "I just sent masona a text , he doesn't seem to reply but if you want i can drop you off home"
    scene bg valevenitscn 20 with Dissolve(0.8)
    Evelyn "Actually.. I was thinking i could sleep over if it's okay with you?"
    Veronica "What? - Um sure alright , this is your home too"
    scene bg valevenitscn 21 with Dissolve(0.8)
    Veronica "Let me just grab my laptop and stuff and you can rest then so-"
    scene bg valevenitscn 22 with Dissolve(0.8)
    Evelyn "Can you stay instead?.. I'm sorry i just don't want to sleep alone with nightmares today"
    Veronica "Oh I , yeah i understand let's sleep then"
    scene bg valevenitscn 23 with Dissolve(0.8)
    Evelyn "Are you alright? Today's been rough on both of us so just asking"
    Veronica "..."
    scene bg valevenitscn 24 with Dissolve(0.8)
    Veronica "I'm fine , just hoping for the best for you all that's all"
    Evelyn "Yeah , I'll be gone to japan soon and get kiara back , will you be okay meanwhile?"
    scene bg valevenitscn 25 with Dissolve(0.8)
    Veronica "I will , you take care of her okay i'm sure she's missed you alot too"
    Evelyn "I will , I don't even know how kiara will respond to this , but i have faith she'll trust me"
    scene bg valevenitscn 26 with Dissolve(0.8)
    Evelyn "If she doesn't i understand , Sigh.. I just want things to be simple , live normally"
    Veronica "They will , I'll try my best too"
    scene bg valevenitscn 27 with Dissolve(0.8)
    Evelyn "I'm repeating myself here but Mason is taking care of mom , family's with kiara but what about you?"
    Veronica "Me? Um I'm gonna be okay don't worry"
    scene bg valevenitscn 28 with Dissolve(0.8)
    Evelyn "No , I mean your emotional state v . You never express but it's clear you're upset too"
    Veronica "I - well (I can't even lie to her , it hurts)"
    scene bg valevenitscn 29 with Dissolve(0.8)
    Evelyn "You've been this tough person for so long , you never even let anyone get close so it must be hard during those times"
    Veronica "Well I , actually it's not-"
    scene bg valevenitscn 30 with Dissolve(0.8)
    Evelyn "It's fine to have a protective barrer v but don't just be alone , promise me you'll open up to me at least?"
    Veronica "Alrgiht i wil , I just want you guys to be happy that's all"
    scene bg valevenitscn 31 with Dissolve(0.8)
    Evelyn "Even now you're worried about me instead of you , you matter too you know?"
    Veronica "Well of course after all you're import-"
    scene bg valevenitscn 32 with Dissolve(0.8)
    Veronica "*Gasp*"
    Evelyn "*Smooch*"
    scene bg valevenitscn 33 with Dissolve(0.8)
    pause
    scene bg valevenitscn 34 with Dissolve(0.8)
    pause
    scene bg valevenitscn 35 with Dissolve(0.8)
    Evelyn "You're the only one i see a future with , please don't consider yourself alone"
    Veronica "I- yeah but-"
    scene bg valevenitscn 36 with Dissolve(0.8)
    Evelyn "No buts, come here"
    Veronica "(Ah.. I can't resist her at all)"
    scene bg valevenitscn 37 with Dissolve(0.8)
    Evelyn "I've waited for this too"
    Veronica "Eve wait i-"
    scene bg valevenitscn 38 with Dissolve(0.8)
    pause
    scene bg valevenitscn 39 with Dissolve(0.8)
    Veronica "Mmm..eve"
    scene bg valevenitscn 40 with Dissolve(0.8)
    Evelyn "It's okay , let it happen"
    Veronica "(It's like i'm frozen.. god and it's evelyn too)"
    scene bg valevenitscn 41 with Dissolve(0.8)
    pause
    scene bg valevenitscn 42 with Dissolve(0.8)
    Evelyn "Let me make you happy"
    Veronica "Eve um please wait I-"
    scene bg valevenitscn 43 with Dissolve(0.8)
    Evelyn "Shh.. it's alright"
    scene bg valevenitscn 44 with Dissolve(0.8)
    Veronica "Fuck..(No , I've got to stop this now)"
    scene bg valevenitscn 45 with Dissolve(0.8)
    Veronica "Eve! please no..move"
    Evelyn "Ah! , uh"
    scene bg valevenitscn 46 with Dissolve(0.8)
    Evelyn "Did i go too far?.. I didn't , i mean i thought you and i"
    scene bg valevenitscn 47 with Dissolve(0.8)
    Veronica "You didn't , I just.. don't want to think about sex today.. , It's not you it's me"
    scene bg valevenitscn 48 with Dissolve(0.8)
    Evelyn "I understand , I'm sorry i'll leave the room"
    Veronica "Wait no!"
    scene bg valevenitscn 49 with Dissolve(0.8)
    Veronica "Please stay , i love your company"
    Evelyn "I love yours too , I'm sorry still"
    scene bg valevenitscn 50 with Dissolve(0.8)
    Evelyn "V, I want you to know you're not alone and once this all settles , me and you can have that future we used to talk about"
    Veronica "I would love that , we'll get out of this soon. I'm sure of it."
    scene bg valevenitscn 51 with Dissolve(0.8)
    Evelyn "I really mean it  , i suck at expressing it but i want you to one day look back on this night in future when we're together"
    Veronica "Yeah , you and i creating memories to look back to , I love you evelyn"
    scene bg valevenitscn 52 with Dissolve(0.8)
    Evelyn "I love you more , let's get to bed.. thank you for this , goodnight"
    Veronica "Goodnight eve"
    scene bg valevenitscn 53 with Dissolve(0.8)
    Veronica "(I could have this.. mason can have mia , I have to take this chance)"
    scene bg valevenitscn 54 with Dissolve(0.8)
    Veronica "(However it goes , It'll be worth it.. Maybe i'll tell eve about it eventually)"
    scene bg valevenitscn 55 with Dissolve(0.8)
    pause
    jump chap_2_scene_22

label chap_2_scene_22:   
    # Scene - > daytwomrngstrt ->
    scene bg daytwomrngstrt 1 with Dissolve(0.8)
    pause
    scene bg daytwomrngstrt 2 with Dissolve(0.8)
    pause
    scene bg daytwomrngstrt 3 with Dissolve(0.8)
    Kiara "(I want to sleep a little more)"
    scene bg daytwomrngstrt 4 with Dissolve(0.8)
    Kiara "(Sadly i got work today even if not as much)"
    scene bg daytwomrngstrt 5 with Dissolve(0.8)
    Kiara "(At least it won't be as hectic)"
    scene bg daytwomrngstrt 6  with Dissolve(0.8)
    Kiara "Should go meet aunt first"
    scene bg daytwomrngstrt 7 with Dissolve(0.8)
    pause
    scene bg daytwomrngstrt 8 with Dissolve(0.8)
    Kiara "I should clean the welcome pad a bit"
    scene bg daytwomrngstrt 9 with Dissolve(0.8)
    Kiara "Hu-ah!*Gasp*"
    scene bg daytwomrngstrt 10 with Dissolve(0.8)
    Kiara "Whaaa"
    scene bg daytwomrngstrt 11 with Dissolve(0.8)
    pause
    scene bg daytwomrngstrt 12  with Dissolve(0.8)
    Kiara "Ouch!, what are you doing?!"
    Nobi "Kiara-san , Tea"
    scene bg daytwomrngstrt 13 with Dissolve(0.8)
    Kiara "I know you brought fucking tea , what did i say about scaring me!"
    Nobi "You said to wait outside the door Kiara-san"
    scene bg daytwomrngstrt 14  with Dissolve(0.8)
    Kiara "When i say outside , it doesn't mean right front of the gate!"
    Nobi "Ah.. Such a mistake , how could i have been so naive?"
    scene bg daytwomrngstrt 15  with Dissolve(0.8)
    Nobi "Kiara-san! Please wait"
    Kiara "J-Jesus , what?"
    scene bg daytwomrngstrt 16 with Dissolve(0.8)
    Kiara "What are you doing?"
    scene bg daytwomrngstrt 17  with Dissolve(0.8)
    Nobi  "Please forgive me , I made a severe lapse of judgement and such a mistake is damaging , you may hit me"
    Kiara "Wh-what?"
    scene bg daytwomrngstrt 18 with Dissolve(0.8)
    Kiara "Hey what are you doing ? Getup please"
    scene bg daytwomrngstrt 19 with Dissolve(0.8)
    Kiara "You didn't commit some crime chill out & Look it's fine , just leave the tea outside next time after a knock or something"
    Nobi  "Thank you for your kindness and yes this will be great since i will get more time to train now too!"
    scene bg daytwomrngstrt 20 with Dissolve(0.8)
    Kiara "Train time? how long did you wait?"
    Nobi "2 Hours"
    Kiara "Two hours??!?!! , are you for real"
    scene bg daytwomrngstrt 21  with Dissolve(0.8)
    Nobi "Two hours and 35 minutes , 16 seconds to be precise since i remade the tea and heated it up kiara-san"
    Kiara "(Now i just feel bad for shouting at him)"
    scene bg daytwomrngstrt 22  with Dissolve(0.8)
    Kiara "Hey you don't have to do that okay , I'm sorry for yelling earlier"
    Nobi "Understood Kiara-san , I will still try my utmost to not dissappoint"
    scene bg daytwomrngstrt 23  with Dissolve(0.8)
    Nobi "Kiara - san , I have a small favor to ask if you would help me it'd be very kind"
    Kiara "Um sure , shoot what is it?"
    scene bg daytwomrngstrt 24  with Dissolve(0.8)
    Nobi "Ah , It is regarding natsuko-san , I believe however you may judge me but-"
    Kiara "Oh cmon i won't , please come sit and feel free to talk"
    scene bg daytwomrngstrt 25 with Dissolve(0.8)
    Nobi "Is there any possiblity that i in this weekend could ask natsuko-san to share a tea with me?"
    Kiara "Natsuko?..Tea? (Ohh i see)"
    scene bg daytwomrngstrt 26 with Dissolve(0.8)
    Kiara "(Heh so much for that strength talk , even the toughest melt huh)"
    scene bg daytwomrngstrt 27  with Dissolve(0.8)
    Kiara "You like natsu?"
    Nobi "What> No! , that's absurd natsuko san and me ? no I-"
    scene bg daytwomrngstrt 28 with Dissolve(0.8)
    Kiara "Relax relax , She's very pretty i don't blame you"
    Nobi "I apologize , but i have no foul intentions she's just very nice and so i thought-"
    scene bg daytwomrngstrt 29  with Dissolve(0.8)
    Kiara "You want to intiiate conversation , It's fine."
    Kiara "Um well she likes sakuras maybe gift her some first?"
    Nobi  "Yes! , cherry blossoms.. what then?"
    scene bg daytwomrngstrt 30  with Dissolve(0.8)
    Kiara "You could also help her with stuff , girls like it when they're treated well even for tasks they can handle"
    Nobi "I see , I will not let any hardwork bother her then"
    scene bg daytwomrngstrt 31  with Dissolve(0.8)
    Nobi "Thank you kiara-san! , I shall be the best version of me for this"
    Kiara "Just be you , flaws don't make us weak. It makes us human. "
    scene bg daytwomrngstrt 32  with Dissolve(0.8)
    Nobi "Just be me.. yes , Natsuko san , can tea? no?"
    Kiara "Why are men so bad at this , it's cute though"
    scene bg daytwomrngstrt 33  with Dissolve(0.8)
    Kiara "Alright better get started since i'm up early anyway"
    scene bg daytwomrngstrt 34  with Dissolve(0.8)
    Xia "Kiara? Good morning honey "
    Kiara "Oh hi auntie i was just about to see you"
    scene bg daytwomrngstrt 35  with Dissolve(0.8)
    Xia "Did you sleep well?"
    Kiara "Yes i did , did you?"
    scene bg daytwomrngstrt 36  with Dissolve(0.8)
    Xia "I did , I noticed you're up early so i came."
    Kiara "Oh well thank you , I slept fully though don't worry"
    scene bg daytwomrngstrt 37  with Dissolve(0.8)
    Xia "Well if you're alright with it perhaps wanna train?"
    Kiara  "(Train? um wouldn't hurt too much but i do have stuff to do)"
    scene bg dy2mngantchc  with Dissolve(0.8)
    #CHOICE RENDER  
    #  CHOICES  
    # IF TRAIN WITH XIA - USE RENDERS OF antd2chcys - FONDNESS INCREASE , STRENGTH INCREASE
    # IF DON’T TRAIN - USE RENDERS OF antd2chcno -> NO CHANGES

    menu:
        "Train with [Xia]":
            jump .part_1

        "Don't Train":
            jump .part_2
    
    label .part_1:
        # IF TRAIN WITH XIA ->
        scene bg antd2chcys 1  with Dissolve(0.8)
        Kiara  "Well i had the computer to setup actually"
        Xia "Oh then?"
        scene bg antd2chcys 2  with Dissolve(0.8)
        Kiara "But why not , let's start"
        Xia "Great and don't worry about the computer , I'll ask natsuko to help you"
        scene bg antd2chcys 3  with Dissolve(0.8)
        Xia "Come in the basement , that's where  we'll train now"
        Kiara "Basement?(Wonder what this could be)"
        scene bg antd2chcys 4 with Dissolve(0.8)
        Kiara "Wow , It's so big! is this where-"
        Xia "Yes , your grandfather trained here too"
        scene bg antd2chcys 5 with Dissolve(0.8)
        Kiara "Um auntie are you sure about not wearing protective gear"
        Xia "Don't worry , I'll be fine"
        scene bg antd2chcys 6  with Dissolve(0.8)
        Xia "Besides , one day you won't need it either but i don't want you to get hurt right now"
        Kiara "Well okay , so should we start?"
        scene bg antd2chcys 7  with Dissolve(0.8)
        Xia "Yes , Just try to hit me"
        Kiara "Alright , Here i go!"
        scene bg antd2chcys 8  with Dissolve(0.8)
        Xia "Remember , Power and speed both are required"
        scene bg antd2chcys 9  with Dissolve(0.8)
        Xia "You're going to have to hit alot harder than that to affect me"
        scene bg antd2chcys 10 with Dissolve(0.8)
        pause
        scene bg antd2chcys 11 with Dissolve(0.8)
        Kiara "Ha!"
        scene bg antd2chcys 12 with Dissolve(0.8)
        pause
        scene bg antd2chcys 13  with Dissolve(0.8)
        Kiara "Ungh!"
        scene bg antd2chcys 14  with Dissolve(0.8)
        Kiara "Ah.. ,  how are you so fast?"
        Xia "In the world of martial arts , one who masters speeds remains at top"
        scene bg antd2chcys 15  with Dissolve(0.8)
        Kiara  "Please teach me , I want to learn too"
        scene bg antd2chcys 16 with Dissolve(0.8)
        Xia "Fine , follow as i say"
        Kiara "Alright , let's do this"
        scene bg antd2chcys 17 with Dissolve(0.8)
        Kiara "Haa.. that was tiring"
        scene bg antd2chcys 18 with Dissolve(0.8)
        $ xia_fond.adjust_fondness(1)
        pause
        scene bg antd2chcys 19 with Dissolve(0.8)
        Kiara "I need a good bath after that"
        $ mc_stats.adjust_strength(1)
        jump chap_2_scene_23

    label .part_2: 
        # IF DON’T TRAIN ->
        scene bg antd2chcno 1 with Dissolve(0.8)
        Kiara "Actually auntie i have to setup this computer soon , since i have to do login on it"
        Xia "Oh i understand , do you need any help?"
        scene bg antd2chcno 2  with Dissolve(0.8)
        Kiara "Well I think i can handle-"
        Xia "No don't , I'll send natsuko go freshen up till then"
        scene bg antd2chcno 3  with Dissolve(0.8)
        Kiara  "Thanks..(I hope she didn't mind it)"
        scene bg antd2chcno 4  with Dissolve(0.8)
        Kiara "Here we go , bath time"
        jump chap_2_scene_23


label chap_2_scene_23:
    
    # SCENE - > dytwobathscn 
    scene bg dytwobathscn 1  with Dissolve(0.8)
    Kiara "Hm.. no shower today , I need a good sink"
    scene bg dytwobathscn 2 with Dissolve(0.8)
    pause
    scene bg dytwobathscn 3 with Dissolve(0.8)
    Kiara "I've got all the jobs but managing them and life will be kinda hard"
    scene bg dytwobathscn 4 with Dissolve(0.8)
    Kiara "That said though at least i'm meeting some nice people"
    scene bg dytwobathscn 5 with Dissolve(0.8)
    Kiara "(I really don't want to bother auntie too much , she's doing enough as it is)"
    scene bg dytwobathscn 6 with Dissolve(0.8)
    Kiara "(I wonder how mom is doing)"
    scene bg dytwobathscn 7 with Dissolve(0.8)
    Kiara "(Hm.. should i try it? I just want to remember once)"
    scene bg dytwobathscn 8 with Dissolve(0.8)
    "There's no choice"
    "You can't do this to her"
    "I miss you"
    "You have to let me go"
    "Talk to me kiara"
    scene bg dytwobathscn 9 with Dissolve(0.8)
    "Will she be alright?"
    "Kiara , where are you?"
    "No certainty , too risky to stop now"
    scene bg dytwobathscn 10 with Dissolve(0.8)
    "I don't want this"
    "You can never tell"
    "I deserve-"
    scene bg dytwobathscn 11 with Dissolve(0.8)
    Kiara "Ha.. ha.. , I can't recognize any of them"
    scene bg dytwobathscn 12 with Dissolve(0.8)
    Kiara "I don't know what's wrong with me , i have to remember , they say my name"
    scene bg dytwobathscn 13 with Dissolve(0.8)
    Kiara "It maybe is important and maybe isn't , but i hope i'll know one day"
    scene bg dytwobathscn 14 with Dissolve(0.8)
    Kiara "Alright , no distractions now. Let's get started with the day"
    scene bg dytwobathscn 15 with Dissolve(0.8)
    Kiara "(I can manage this new life , just need to take one step at a time)"
    scene bg dytwobathscn 16 with Dissolve(0.8)
    Kiara "(There we go , I really stare at myself too much sometimes)"
    $ renpy.end_replay()
    jump chap_2_scene_24

label chap_2_scene_24:

    # SCENE -> pcsetupsgment -:
    scene bg pcsetupsgment 1  with Dissolve(0.8)
    Kiara "*Humming music*"
    scene bg pcsetupsgment 2 with Dissolve(0.8)
    Kiara "(Alright , that takes care of morning routine)"
    scene bg pcsetupsgment 3 with Dissolve(0.8)
    Kiara "I forgot my eyeliner i think"
    Natsuko "Kiara?"
    scene bg pcsetupsgment 4 with Dissolve(0.8)
    Natsuko "Kiara , you in here?"
    scene bg pcsetupsgment 5 with Dissolve(0.8)
    Natsuko "There you are , mom said you needed some help"
    Kiara "Oh just gimme one second"
    scene bg pcsetupsgment 6 with Dissolve(0.8)
    Natsuko "so which computer exactly , is it the boxes"
    Kiara "It's this , need to set it up but my room's table isn't big enough"
    scene bg pcsetupsgment 7 with Dissolve(0.8)
    Natsuko "Well why don't you use my room then?"
    Kiara "Um are you okay with that?"
    scene bg pcsetupsgment 8 with Dissolve(0.8)
    Natsuko "What do you mean? I barely even use it and sleep in dads room mostly so"
    Kiara "Um alright well let me carry these"
    scene bg pcsetupsgment 9 with Dissolve(0.8)
    Natsuko "No need , Nobi! please come here!"
    Nobi "Coming natsuko-san!"
    scene bg pcsetupsgment 10 with Dissolve(0.8)
    Natsuko "He'll carry these don't worry , come i'll help you set it up"
    Kiara "Alright , let's start then"
    scene bg pcsetupsgment 11 with Dissolve(0.8)
    Natsuko "Well .. what do you think?"
    Kiara "Wow , this is certainly something."
    scene bg pcsetupsgment 12 with Dissolve(0.8)
    Natsuko "What you don't like it?"
    Kiara "No it looks pretty but just didn't expect the contrast haha"
    Natsuko "Well i do love pink heh"
    scene bg pcsetupsgment 13 with Dissolve(0.8)
    Kiara "Is that?"
    Natsuko "Yep that's where little me used to sit , so i'm sentimental to throw it"
    scene bg pcsetupsgment 14 with Dissolve(0.8)
    Kiara "The bed pink too? Natsuko you really are a barbie girl"
    Natsuko "Well it's very comfy and pink makes me feel nice"
    scene bg pcsetupsgment 15 with Dissolve(0.8)
    Kiara "That's nice to hear"
    Natsuko "So that's the corner where we'll setup your computer"
    scene bg pcsetupsgment 16 with Dissolve(0.8)
    Kiara "The corner is very clean for even unused , you cleaned it just now didn't you?"
    Natsuko "Um.. well."
    scene bg pcsetupsgment 17 with Dissolve(0.8)
    Natsuko "Dammit am i that bad at pretending"
    Kiara "You don't have to , I appreciate it really"
    scene bg pcsetupsgment 18 with Dissolve(0.8)
    Kiara "No one does stuff for me without expecting something in return but you just did it so thank you"
    Natsuko "Well i didn't want you to be troubled so sorry for lying"
    scene bg pcsetupsgment 19 with Dissolve(0.8)
    Kiara "Feel free to lie more , also you were right this is comfy"
    Natsuko "Told you , the reason i don't sleep is that exactly too . It is way too comfy so i don't wake up on time"
    scene bg pcsetupsgment 20 with Dissolve(0.8)
    Natsuko "So let's just say having baby sleep and studying architecture ain't the best mix"
    Kiara "I get that honestly , I hope your career goes well"
    scene bg pcsetupsgment 21 with Dissolve(0.8)
    Nobi "Natsuko-san , where to put these?"
    Natsuko "Oh just here , thanks so much for the help"
    scene bg pcsetupsgment 22 with Dissolve(0.8)
    Nobi "Mention not , anything else natsuko-san?"
    Natsuko "Not really , you should go have some lunch now though please"
    scene bg pcsetupsgment 23 with Dissolve(0.8)
    Kiara "Hey nobi i have something for you , could you please wait outside the door and i'll call you shortly then?"
    Nobi "Of course kiara-san"
    scene bg pcsetupsgment 24 with Dissolve(0.8)
    Kiara "Alright let's get this started"
    Natsuko "i'll grab the otner stuff you hold the components"
    scene bg pcsetupsgment 25 with Dissolve(0.8)
    Natsuko "Okay tableis se good and nice"
    Kiara "I'm bringing this computer , look it has sakuras on it!"
    scene bg pcsetupsgment 26 with Dissolve(0.8)
    Kiara "Chair is set , seems flexible enough"
    Natsuko "The keyboard is kinda cool , wish my laptop had this"
    scene bg pcsetupsgment 27 with Dissolve(0.8)
    Kiara "Lighting and microphone done"
    Natsuko "Just give me a minute , I'll bring the monitor"
    scene bg pcsetupsgment 28 with Dissolve(0.8)
    Natsuko "It's kinda heavy jeez"
    Kiara "Wait let me help you hold on"
    scene bg pcsetupsgment 29 with Dissolve(0.8)
    Natsuko "This is kinda fancy not gonna lie"
    Kiara "It does look pretty good"
    scene bg pcsetupsgment 30 with Dissolve(0.8)
    Natsuko "Okay that's that , i think it should be all of it"
    Kiara "Natsuko do you mind if i ask something?"
    scene bg pcsetupsgment 31 with Dissolve(0.8)
    Natsuko "Not at all , go on"
    Kiara "Well it's just i'm curious"
    scene bg pcsetupsgment 32 with Dissolve(0.8)
    Kiara "How on earth are you still single?"
    Natsuko "Heh , why ask that suddenly?"
    scene bg pcstpchcrndr  with Dissolve(0.8)
    #GIVE CHOICE HERE  
    #Compliment Natsuko (Increase fondness natsuko) ""
    #Say simply ( no changes) ""

    menu:
        "Say Simply":
            jump .part_1
        "Compliment [Natsuko]":
            $ natsuko_fond.adjust_fondness(1)
            jump .part_2
    
    label .part_1:
        # IF SAY SIMPLY -> USE RENDERS OF asksimplynatsu ->
        scene bg asksimplynatsu 1 with Dissolve(0.8)
        Kiara "Well you're just really good company and soothing to talk to so i thought i'd ask"
        Natsuko "Thanks , you are too kiara but yeah it's mostly studies"
        scene bg asksimplynatsu 2 with Dissolve(0.8)
        Natsuko "I barely get time as it is , plus mom would probably interogate the guy worse than fbi so"
        Kiara "Oh right, auntie surely will haha"
        jump .part_5
        
    
    label .part_2:
        # IF COMPLIMENT NATSUKO , USE RENDERS OF -> cmplmntnatsu
        scene bg cmplmntnatsu 1  with Dissolve(0.8)
        Kiara "Well you're so beautiful , it's kinda impossible to believe no one's asked you out"
        scene bg cmplmntnatsu 2  with Dissolve(0.8)
        Natsuko "Look who's talking , I could ask the same to you pretty one"
        Kiara "No!, I really mean it you're very nice to talk too so just curious"
        scene bg cmplmntnatsu 3 with Dissolve(0.8)
        Natsuko "Alright then , well it's mostly studies and stuff and me being an introvert"
        Natsuko "Plus mom would most likely kill any guy trying to be too smart , so i'd rather not scare people"
        Kiara "Oh yeah , I just realized that too"
        scene bg cmplmntnatsu 4 with Dissolve(0.8)
        Natsuko "Though i wouldn't mind being with someone , I'm sure it's nice when it works"
        scene bg cmplmntnatsu 5  with Dissolve(0.8)
        Natsuko "Thanks realy ,  I really appreciate it and i like genuine compliments"
        scene bg cmplnmtagnchc  with Dissolve(0.8)
        Kiara "Welcome honestly I-"
        
        pass
    #GIVE CHOICE AGAIN HERE  
    #> COMPLIMENT Again ((+FONDNESS) 
    #Say simply  

    menu:
        "Compliment Again":
            $ natsuko_fond.adjust_fondness(1)
            jump .part_3
        "Say Simply":
            jump .part_4
    
    label .part_3:
        # IF COMPLIMENT AGAIN -> USE RENDERS OF -> ntsucalsxy ->
        scene bg ntsucalsxy 1 with Dissolve(0.8)
        Kiara "Let me rephrase then , people must be blind to not see how sexy and adorable you are"
        Natsuko "Oh hah , smooth are we?"
        scene bg ntsucalsxy 2 with Dissolve(0.8)
        Natsuko "Well then i'll say something too then"
        scene bg ntsucalsxy 3 with Dissolve(0.8)
        Natsuko "You're a better sight to the eyes than a pizza at night in fridge when hungry"
        Kiara "Awh my heart just melted i think haha"
        jump .part_5

    label .part_4:
        # IF SAY SIMPLY -> USE RENDERS OF -> ntsusimplycmplnt->
        scene bg ntsusimplycmplnt 1 with Dissolve(0.8)
        Kiara "Well your most welcome , I'm just glad to have a cousin like you"
        scene bg ntsusimplycmplnt 2 with Dissolve(0.8)
        Natsuko "Ditto , you are someone i adore too so just stay smiling , it suits you"
        Kiara "I will , thanks natsu"
        jump .part_5

    label .part_5:
        # - END ALL CHOICECS->
        scene bg pcsetupsgment 33 with Dissolve(0.8)
        Natsuko "Well i'll be going to get groceries , shoot me a dm if you want me to bring something"
        Kiara "Wait one thing natsuko hold on"
        scene bg pcsetupsgment 34 with Dissolve(0.8)
        Kiara "Nobi please come in"
        Nobi "Yes Kiara-san , what can i do?"
        scene bg pcsetupsgment 35 with Dissolve(0.8)
        Kiara "Natsuko's going to get some groceries , remember i gave you the list this morning? Do you mind accompanying her?"
        Nobi "Oh yes the list.. but is natsuko-san okay with it?"
        Natsuko "Why wouldn't i be , carrying stuff will be easier with you around too"
        scene bg pcsetupsgment 36 with Dissolve(0.8)
        Natsuko "Cmon let's get going , we don't wanna anger mom"
        Nobi "Yes natsuko-san , right behind you"
        scene bg pcsetupsgment 37 with Dissolve(0.8)
        pause
        scene bg pcsetupsgment 38 with Dissolve(0.8)
        Kiara "(Good luck champ)"
        jump chap_2_scene_25

label chap_2_scene_25:
    # 
    # SCENE - > ymacallsgmnt -> 
    scene bg ymacallsgmnt  1 with Dissolve(0.8)
    Kiara "Ah , why won't this thing start?"
    scene bg ymacallsgmnt  2 with Dissolve(0.8)
    Kiara "If only all computers worked the same way"
    scene bg ymacallsgmnt  3 with Dissolve(0.8)
    Kiara "What am i even doing wrong? All the cables seem to fit so far"
    scene bg ymacallsgmnt  4 with Dissolve(0.8)
    Kiara "Ob wait! I can probably call yamazaki!"
    scene bg ymacallsgmnt  5 with Dissolve(0.8)
    Kiara "Let's hope he's not too busy"
    scene bg ymacallsgmnt  6 with Dissolve(0.8)
    Yamazaki "Man movies are predicitible as fuck these days , a child could write better"
    "*Phone rings*"
    scene bg ymacallsgmnt  7 with Dissolve(0.8)
    Yamazaki "Who is it this early?"
    scene bg ymacallsgmnt  8 with Dissolve(0.8)
    Yamazaki "Shit , It's Kiara!"
    scene bg ymacallsgmnt  9 with Dissolve(0.8)
    Yamazaki "Uh hey kiara! , morning what's up?"
    Kiara "Hey i'm sorry for bugging you , I set up the computer but it won't start for some reason"
    scene bg ymacallsgmnt  10 with Dissolve(0.8)
    Yamazaki "No you didn't and the pc won't start? Did you follow the included gide?"
    scene bg ymacallsgmnt  11 with Dissolve(0.8)
    Kiara "I did ,  the computer is on but monitor is not i don't know , I'll video call you and just guide me okay?"
    Yamazaki "Sure no worries i'm set"
    # FROM HERE USE RENDERS OF - Splituseaftr11
    scene bg yamasplitcall 1 with Dissolve(0.8)
    Yamazaki "You look great by the way , so what's the issue?"
    Kiara "Thanks , Um not really sure actually other than it not starting"
    scene bg yamasplitcall 2 with Dissolve(0.8)
    Yamazaki "Did you set up the psu and mounting bracket correctly?"
    Kiara "Um.."
    scene bg yamasplitcall 3 with Dissolve(0.8)
    Yamazaki "The gpu has to be set in this angle as well with the anti sag bracket"
    Kiara "Well I-"
    scene bg yamasplitcall 4 with Dissolve(0.8)
    Yamazaki "Also see if you put the ram sticks in dual channel or single?"
    Kiara "Wait wait! Jesus"
    scene bg yamasplitcall 5 with Dissolve(0.8)
    Kiara "I've got no idea about any of this stuff"
    Yamazaki "O right.."
    scene bg yamasplitcall 6 with Dissolve(0.8)
    Kiara "Yeah it's why i called you since you said yesterday"
    Yamazaki "I apologize , alright just show me the computer"
    # 
    scene bg ymacallsgmnt  12 with Dissolve(0.8)
    Kiara "Alright this is the backside and i don't know what i'm doing wrong here?"
    Yamazaki "Ah kiara you plugged the hdmi into the vga socket"
    scene bg ymacallsgmnt  13 with Dissolve(0.8)
    Kiara "Why does it have two of these?"
    Yamazaki "Well tbere used to be computers with vga sockets and cables so"
    scene bg ymacallsgmnt  14 with Dissolve(0.8)
    Kiara "But no one uses them anymore!"
    Yamazaki "Well some old boomer organizations still do"
    Kiara "That's nuisance"
    scene bg ymacallsgmnt  15 with Dissolve(0.8)
    Kiara "Alrght so just plug that into the other socket and restart right?"
    Yamazakl "Yep , it should work then"
    scene bg ymacallsgmnt  16 with Dissolve(0.8)
    Kiara "Give me just a moment okay , I'll get it done"
    Yamazaki "Alright , I think you got it for most part"
    scene bg ymacallsgmnt 17 with Dissolve(0.8)
    Kiara "Okay so this cable in the other one , got it"
    # 
    scene bg yamavidchcrndr with Dissolve(0.8)
    Kiara "Am i forgetting something?.. I feel like something obvious is-"
    #GIVE CHOICE  
    #> It’s probably nothing. (Adds corruption) 
    #Let me check again ( no changes) 

    menu:
        "It's probably nothing":
            jump .part_1
        "Let me check again":
            jump .part_2

    label .part_1:
        # IF ITS PROBABLY NOTHING THEN USE RENDERS OF -> Itsprobnothin ->
        scene bg itsprobnothin 1 with Dissolve(0.8)
        Kiara "It's probably nothing , I shouldn't bother him for long and solve this"
        scene bg itsprobnothin 2 with Dissolve(0.8)
        Yamazaki "Yeah i'll be up up in 20 minutes!"
        scene bg itsprobnothin 3 with Dissolve(0.8)
        Yamazaki "What the-"
        scene bg itsprobnothin 4 with Dissolve(0.8)
        Yamazaki "Holy fuck.. is that her?"
        scene bg itsprobnothin 5 with Dissolve(0.8) 
        Yamazaki "Shit , it's like the perfect size (Dammit i can't look away even if i try)"
        scene bg itsprobnothin 6 with Dissolve(0.8)
        Kiara "Eh! , it's so at the back such an short cable"
        Yamazaki "Jesus kiara you're killing me here, such a beautiful butt"
        scene bg itsprobnothin 7 with Dissolve(0.8)
        Yamazaki "Those feet , sorry kiara i'm gonna have to do this"
        "*Screenshots*"
        scene bg itsprobnothin 8 with Dissolve(0.8)
        Kiara "Ah annd i think i got it!"
        Yamazaki "Oh uh yeah , did it work? (Wow they look so yummy)"
        scene bg itsprobnothin 9 with Dissolve(0.8)
        Kiara "Yes , it's on thank you so much!"
        Yamazaki "Don't mention it , just login your details and then i'll verify em , bye!"
        scene bg itsprobnothin 10 with Dissolve(0.8)
        Kiara "Okay what's this- Wha- Oh no.."
        scene bg itsprobnothin 11 with Dissolve(0.8)
        Kiara "The camera was on i forgot , he must've thought i was showing him intentionally..dammit"
        scene bg itsprobnothin 12 with Dissolve(0.8)
        Kiara "Hope he understands  , probably gave off the wrong impression"
        $ mc_stats.adjust_corruption(5)
        jump .part_3

    label .part_2: 
        #  IF LET ME CHECK AGAIN THEN USE RENDERS OF -> pyattentinvidcall -:
        scene bg pyattentinvidcall 1 with Dissolve(0.8)
        Kiara "Ah shit , the camera was still on the phone"
        scene bg pyattentinvidcall 2 with Dissolve(0.8)
        Kiara "Sorry i forgot to put it to side"
        Yamazaki "No worries , take your time"
        scene bg pyattentinvidcall 3 with Dissolve(0.8)
        Yamazaki "Hello darkness my old friend"
        scene bg pyattentinvidcall 4 with Dissolve(0.8)
        Kiara "Okay .. okay.. Yes!"
        Yamazaki "Did it work?"
        scene bg pyattentinvidcall 5 with Dissolve(0.8)
        Kiara "Yes!! it's on thank you so much"
        Yamazaki "Don't mention it , just login and i'll verify your details from here"
        jump .part_3
    # 
    label .part_3:
        scene bg ymacallsgmnt 18 with Dissolve(0.8)
        Kiara "Well that takes care of the login , time to go outside"
    jump chap_2_scene_26


label chap_2_scene_26:
    # SCENE -> levinhmdtwo -> 
    scene bg levinhmdtwo 1 with Dissolve(0.8)
    Kiara "Grandfather , I never met you but i know some of your blood is in me and i hope i can make you proud one day"
    scene bg levinhmdtwo 2 with Dissolve(0.8)
    Kiara "(Wish me luck please , I don't know how hard the road gets from here but i'll do my best)"
    scene bg levinhmdtwo 3 with Dissolve(0.8)
    pause
    scene bg levinhmdtwo 4 with Dissolve(0.8)
    Xia "Saying prayers to father?"
    Kiara "Yes , just want his grace upon me too so i can turn out like you one day"
    scene bg levinhmdtwo 5 with Dissolve(0.8)
    Xia "You'll turn out better , anyway you'll be home soon i hope?"
    Kiara "Yes i'll be back before evening this time"
    scene bg levinhmdtwo 6 with Dissolve(0.8)
    Xia "Wait close your eyes , I have something to give you"
    Kiara "Um alright"
    scene bg levinhmdtwo 7 with Dissolve(0.8)
    Kiara "(This feels so good , i hope i make you proud too auntie)"
    scene bg levinhmdtwo 8 with Dissolve(0.8)
    Xia "Please stay in touch and call me or natsuko if anything is required okay?"
    Kiara "I Will auntie , don't worry"
    scene bg levinhmdtwo 9 with Dissolve(0.8)
    Kiara "Besides even if i am on my own feet , it's you and family who i'll always be back at"
    Xia "thank you for trusting me , it means everything to me too"
    scene bg levinhmdtwo 10 with Dissolve(0.8)
    Xia "(Kiara.. , you will find happyness again. Be it with or without us I'm sure of it.)"
    scene bg levinhmdtwo 11 with Dissolve(0.8)
    Xia "I should clean up now , natsuko will come back soon too"
    scene bg levinhmdtwo 12 with Dissolve(0.8)
    pause
    scene bg levinhmdtwo 13 with Dissolve(0.8)
    Xia "I can make her strong physically but mentally it's upto her , please help her god"
    scene bg levinhmdtwo 14 with Dissolve(0.8)
    "*Phone rings*"
    scene bg levinhmdtwo 15 with Dissolve(0.8)
    Xia "A call? Oh its ichigo!"
    scene bg levinhmdtwo 16 with Dissolve(0.8)
    Xia "Ichigo-san! , how are you i was just about to call you"
    Ichigo "Hello love , um I'm fine..where is kiara?"
    scene bg levinhmdtwo 17 with Dissolve(0.8)
    Xia "She just left for work, what happened?"
    Ichigo "Xia , i have some updates regarding mia's trial"
    scene bg levinhmdtwo 18 with Dissolve(0.8)
    Xia "WHAT?! No! h-how could this be?"
    Ichigo "Relax , hear me out and i will explain then."
    jump chap_2_scene_27

label chap_2_scene_27:
    scene blackscreen
    show titletext "Osaka central hotel , Early noon" with dissolve
    pause 1.0
    window hide
    scene bg rinsxscndytwo 1  with Dissolve(0.8)
    Rin "When will you be back exactly?"
    Lana "Uh don't know , I'm with damain so it might a little bit time"
    scene bg rinsxscndytwo 2  with Dissolve(0.8)
    Rin "Getting him into the changing rooms arey you hehe?"
    Lana "Oh rin , cmon you know he's my friend"
    scene bg rinsxscndytwo 3  with Dissolve(0.8)
    Rin "I'm your friend too , didn't stop us last year's new eve"
    Lana "Okay that was a one time thing and i was kinda drunk"
    scene bg rinsxscndytwo 4 with Dissolve(0.8)
    Rin "Drunk or not you sure as hell made quite the mess and we had fun in morning too"
    Rin "Pretending to not like it now eh?"
    Lana "Jesus chrst , okay fine i liked it but hey i've reduced it now"
    scene bg rinsxscndytwo 5 with Dissolve(0.8)
    Rin "Heh sure babe , well just bringsome food okay?"
    Lana "I'll get some local snacks don't worry"
    scene bg rinsxscndytwo 6 with Dissolve(0.8)
    Rin "Shame that guy isn't here , would've given him a way better meal"
    scene bg rinsxscndytwo 7 with Dissolve(0.8)
    "Door bell"
    scene bg rinsxscndytwo 8 with Dissolve(0.8)
    Rin "Who is it?"
    "Hotel waiter" "Room service mam!"
    scene bg dytworinchcrndr  with Dissolve(0.8)
    Rin "(Hmm she did say some time , i'm bored might as well have some fun)"
    #> CHOICE RENDER  
    #> GIVE CHOICE  
    #> HAVE SOME FUN (CORRUPTION +1)  
    #DON’T RISK IT. 

    menu:
        "Have some fun":
            jump .part_2

        "Don't risk it":
            jump .part_1

    label .part_1:
        # IF DON’T RISK IT THEN USE RENDERS OF rinnosxscn ->
        scene bg rinnosxscn 1 with Dissolve(0.8)
        Rin "(Rather not , lana's gonna get triggerd again)"
        scene bg rinnosxscn 2 with Dissolve(0.8)
        Rin "(I'll definitely have that guy eventually though)"
        jump chap_2_scene_28

    label .part_2:
        # IF HAVE SOME FUN THEN USE RENDERS OF -> rinsxscnstrt ->
        scene bg rinsxscnstrt 1 with Dissolve(0.8)
        Rin "Come on in! (Let's do this)"
        scene bg rinsxscnstrt 2 with Dissolve(0.8)
        "Hotel waiter" "Door is locked mam!"
        Rin "Comin comin"
        scene bg rinsxscnstrt 3 with Dissolve(0.8)
        pause
        scene bg rinsxscnstrt 4 with Dissolve(0.8)
        "Hotel waiter" "Hello ms. just a quality assurance check , is everything to yor liking?"
        scene bg rinsxscnstrt 5 with Dissolve(0.8)
        Rin "Oh yeah it got even better , I do need some help though"
        "Hotel waiter" "Yes mam , what is it?"
        scene bg rinsxscnstrt 6 with Dissolve(0.8)
        Rin "Come in , there's this thing i can't reach so"
        "Hotel waiter" "Sure mam gladly"
        scene bg rinsxscnstrt 7 with Dissolve(0.8)
        Rin "See , it's like super high and i wanted to write something"
        "Hotel waiter" "My apologies mam i'll getthat lowered but  try reaching it on table>"
        scene bg rinsxscnstrt 8 with Dissolve(0.8)
        Rin "See? it's like beyond the reach , just carry me and then climb we'll get it"
        scene bg rinsxscnstrt 9  with Dissolve(0.8)
        "Hotel waiter" "Okay mam "
        scene bg rinsxscnstrt 10 with Dissolve(0.8)
        "Hotel waiter" "Are you able to reach it now mam?"
        Rin "Yeah just keep steady please"
        scene bg rinsxscnstrt 11 with Dissolve(0.8)
        Rin "(His hands feel kinda nice)"
        scene bg rinsxscnstrt 12 with Dissolve(0.8)
        Rin "Just a minute i'm trying to do this"
        "Hotel Waiter" "Do not worry , you won't fall"
        scene bg rinsxscnstrt 13 with Dissolve(0.8)
        Rin "(Oh but i want to cutie)"
        scene bg rinsxscnstrt 14 with Dissolve(0.8)
        "Hotel waiter" "Ah!"
        Rin "Sorry just hold for a bit i almost got it!"
        scene bg rinsxscnstrt 15 with Dissolve(0.8)
        Rin "Sorry for the view , I'll be quick"
        "Hotel waiter" "Do not worry mam , my eyes are closed but please hurry up"
        scene bg rinsxscnstrt 16 with Dissolve(0.8)
        Rin  "(Eyes closed? I'm giving him a treat and he's just lookin away?)"
        scene bg rinsxscnstrt 17 with Dissolve(0.8)
        "Hotel waiter" "Aah1 mam i am fall-"
        Rin "Oh wait (perfect hehe)"
        scene bg rinsxscnstrt 18 with Dissolve(0.8)
        "Hotel waiter" "Aough.."
        Rin "You okay?"
        scene bg rinsxscnstrt 19 with Dissolve(0.8)
        Rin "Sorry i hope you're alright"
        "Hotel waiter" "Yes yes i'm alright , did you get the diary?"
        scene bg rinsxscnstrt 20 with Dissolve(0.8)
        Rin "Oh i kinda don't care about it anymore"
        "Hotel waiter" "So um may i go?"
        scene bg rinsxscnstrt 21 with Dissolve(0.8)
        Rin "Heh , you sure you wanna go stil?"
        "Hotel waiter" "W-wo , um mam our policy"
        scene bg rinsxscnstrt 22 with Dissolve(0.8)
        Rin "What? your policy? what was it?"
        "Hotel waiter" "Mam it doesn't allow us to"
        scene bg rinsxscnstrt 23 with Dissolve(0.8)
        Rin "You care about some dumb policy while this pussy is in front of you?"
        scene bg rinsxscnstrt 24 with Dissolve(0.8)
        Rin "How about you give me some room service personally?"
        scene bg rinsxscnstrt 25 with Dissolve(0.8)
        Rin "Perhaps i could give you something way better than a tip hehe"
        "Hotel waiter" "I would love that mam ( shit she'sway too hot for me to deny this)"
        scene bg rinsxscnstrt 26 with Dissolve(0.8)
        Rin "Just wait , I'll fit into something good"
        "Hotel waiter" "Oh , yeah surely no problem"
        scene bg rinsxscnstrt 27 with Dissolve(0.8)
        "Hotel waiter" "Shit is this a prank or what ? IS this really happening?"
        scene bg rinsxscnstrt 28 with Dissolve(0.8)
        "Hotel waiter" "I don't see any cameras , damn am i really?"
        scene bg rinsxscnstrt 29 with Dissolve(0.8)
        Rin "yoohoo , lookie here"
        "Hotel waiter" "Fuckin wow .. you look-"
        scene bg rinsxscnstrt 30 with Dissolve(0.8)
        "Hotel waiter" "So fucking hot"
        Rin "I know hun , let's begin"
        scene bg rinsxscnstrt 31 with Dissolve(0.8)
        Rin "Keep this between us and during my stay we'll have alot of these service sessions"
        "Hotel waiter" "Definitely mam , confidential as hell"
        scene bg rinsxscnstrt 32 with Dissolve(0.8)
        Rin "Okay give me that cute face"
        scene bg rinsxscnstrt 33 with Dissolve(0.8)
        "Hotel waiter" "Even through the net so lovely"
        Rin "That's right rub that nose , give me that pretty face"
        scene bg rinsxscnstrt 34 with Dissolve(0.8)
        Rin "Now let's speed this up"
        scene bg rinsxscnstrt 35 with Dissolve(0.8)
        Rin "Nice cock , you've groomed it well"
        "Hotel waiter" "Yes mam , it looks even nicer in your hands"
        scene bg rinsxscnstrt 36 with Dissolve(0.8)
        pause
        scene bg rinsxscnstrt 37 with Dissolve(0.8)
        Rin  "You guys love ball play don't you?"
        scene bg rinsxscnstrt 38 with Dissolve(0.8)
        Rin "Look at that cold but hot at same time"
        "Hotel waiter" "Ohhhh! so good mam"
        scene bg rinsxscnstrt 39 with Dissolve(0.8)
        Rin  "Name's rin babe , so how about you and i kiss each other but different angles?"
        scene bg rinsxscnstrt 40 with Dissolve(0.8)
        "Hotel waiter" " I see what you mean hehe"
        Rin "Smart boy"
        scene bg rinsxscnstrt 41 with Dissolve(0.8)
        "Hotel waiter" "She smeells nice"
        Rin "Well go on , we don't got all day"
        scene bg rinsxscnstrt 42 with Dissolve(0.8)
        Rin "Mmmm.. lick that pussy you dirty boy"
        scene bg rinsxscnstrt 43 with Dissolve(0.8)
        Rin "*Gulp(His tongue is longue too , nice)"
        "Hotel waiter" "(Tastes nice too , this bitch is so fine)"
        scene bg rinsxscnstrt 44 with Dissolve(0.8)
        "Hotel waiter" "(I'm gonna make her cum for sure)"
        Rin "(Dick is pretty decent , I would definitely take it inside other plcaces too)"
        scene bg rinsxscnstrt 45 with Dissolve(0.8)
        Rin "(Why does being a whore feel so good? heh)"
        "Hotel waiter" "(I am so fucking lucky!)"
        $ renpy.end_replay()
        scene bg rinsxscnstrt 46 with Dissolve(0.8)
        Lana "So that's why we couldn't do what we wanted"
        Damian "I see , well either way i'm sure we'll figure it out"
        scene bg rinsxscnstrt 47 with Dissolve(0.8)
        Lana "Hope so , but in any case at least i got you for company"
        Damian "Yeah no problem, I'm here for long so won't be an issue"
        scene bg rinsxscnstrt 48 with Dissolve(0.8)
        Damian "Ah stupid shoe lace"
        Lana "Tie it up later, come lets eat something"
        scene bg rinsxscnstrt 49 with Dissolve(0.8)
        Lana "Rin , i brough lun-"
        scene bg rinsxscnstrt 50 with Dissolve(0.8)
        Lana "8Gasp* Oh my god.."
        scene bg rinsxscnstrt 51 with Dissolve(0.8)
        Lana "Damian plan change, let's just eat at a bbq"
        Damian "Oh why ? We just got here"
        Lana "Please please , I'm really craving it"
        scene bg rinsxscnstrt 52 with Dissolve(0.8)
        Rin "Mmmmm , nice cock"
        scene bg rinsxscnstrt 53 with Dissolve(0.8)
        Rin "Heh, she thinks i didn't notice"
        scene bg rinsxscnstrt 54 with Dissolve(0.8)
        Rin "(Shame though , i wanted the guy to see)"
        $ mc_stats.adjust_corruption(1)
        jump chap_2_scene_28


label chap_2_scene_28:
    # SCENE -> dytwocsplay->
    scene bg dytwocsplay 1 with Dissolve(0.8)
    "Man in background" "You would look great in this"
    "Girl in background" "No , this one is better!"
    scene bg dytwocsplay 2 with Dissolve(0.8)
    Customer "I had oredered it last week taka , why isn't it here?"
    Taka "Relax , I'll get it i've booked it for you"
    scene bg dytwocsplay 3 with Dissolve(0.8)
    Taka "Hm? Kiara?"
    Customer "Where and when then?"
    scene bg dytwocsplay 4 with Dissolve(0.8)
    Taka "Jinshi , please handle the customer here!"
    Kiara "Hopefully that girl doesn't get angry on me"
    scene bg dytwocsplay 5 with Dissolve(0.8)
    Taka "Hey kiara , how's it going?"
    Kiara "Did i come in at a busy time?"
    scene bg dytwocsplay 6 with Dissolve(0.8)
    Kiara "I mean i hope i'm not bothering that's all"
    Taka "No you ain't don't worry customers are just this way usually"
    scene bg dytwocsplay 7 with Dissolve(0.8)
    Taka  "So how'd the interviews go?"
    scene bg dytwocsplay 8 with Dissolve(0.8)
    Kiara "Um well okay i think , i was here to collect the review on the first cosplay we did"
    scene bg dytwocsplay 9 with Dissolve(0.8)
    Taka "Oh right right, yeah come in."
    Kiara "Alright then , hope it's good news"
    scene bg dytwocsplay 10 with Dissolve(0.8)
    Taka "It is , i'll get your funds transfered by evening i hope that's okay, so how was the first day?"
    Kiara "It is and it was alright , off to school now for introductory class"
    scene bg dytwocsplay 11 with Dissolve(0.8)
    Taka "That's great to hear , I knew you could do it"
    Kiara "Thank you , most people were nice to me too so it helped"
    scene bg dytwocsplay 12 with Dissolve(0.8)
    Taka "Nce suit by the way looks great , it's for school i'm guessing? also since it's weekend it might be a relaxed schedule right?"
    Kiara "Yeha it is, as for schedule i guess so i wanna enjoy the weekend so just doing indtroductory now"
    scene bg dytwocsplay 13 with Dissolve(0.8)
    Taka "Well I'm going outside town but how about another shoot? It'll only benefit in the long run so"
    scene bg dytwocsplay 14 with Dissolve(0.8)
    Taka "Besides it won't take that long either"
    Kiara "I suppose you're right but"
    scene bg chcrndrdtwocsply  with Dissolve(0.8)
    Kiara "(Hm do i really want to? It wouldn't hurt but i do have to go too)"
#CHOICE RENDER  
#CHOICES  
# Not interested ( no changes)
# 50 $ NO CHANGES , 
# 80 $  ( + 5 CORRUPTION) , 
# 120 $ ( +10 corruption , requires 35 Corruption)
# ^ money add to all depending on options
  
menu:
    "Not Intrested":
        jump .part_1

    "100$":
        
        jump .part_2

    "180$":
        
        jump .part_3
    "300$" if mc_stats.current_corruption > 35:
        
        jump .part_4

label .part_1:     
    # - - IF NOT INTERESTED THEN USE RENDERS OF -> dtwontintrstd ->
    scene bg dtwontintrstd 1 with Dissolve(0.8)
    Kiara "Sorry taka , It's not really my thing maybe sometime later , I have to go anyway"
    scene bg dtwontintrstd 2 with Dissolve(0.8)
    Kiara "See ya , have a good one"
    Taka "Yeah you too , laters (Damn it's the only moment i geto to see her skin , oh well another day)"
    jump chap_2_scene_29

label .part_2:
    # If 50$ THEN USE RENDERS OF dtwoindin ->
    scene bg dtwoindin 1 with Dissolve(0.8)
    Kiara "50$ must be smaller one , let's just get it done"
    Taka "You'd like this , it's indian!"
    scene bg dtwoindin 2 with Dissolve(0.8)
    Kiara "Oh my god this looks so nice!"
    scene bg dtwoindin 3 with Dissolve(0.8)
    Kiara "Taka look at this , oh my god can i keep this?"
    Taka "Well after shoot sure , not like i'll wear or sell it"
    Taka "Anyawy , let's start!"
    scene bg dtwoindin 4 with Dissolve(0.8)
    Taka "Standard look at it"
    scene bg dtwoindin 5 with Dissolve(0.8)
    Taka "Bit of indian holding waist"
    scene bg dtwoindin 6 with Dissolve(0.8)
    Taka "Look at the sky and smile!"
    scene bg dtwoindin 7 with Dissolve(0.8)
    Taka "Express freedom!"
    scene bg dtwoindin 8 with Dissolve(0.8)
    Taka "Just point like a teacher!"
    Taka "Bravo! all good shots kiara!"
    $ inventory.earn(100)
    jump chap_2_scene_29

label .part_3:
    # IF 80 $ , USE RENDERS OF -> dtwocoolcsply ->
    scene bg dtwocoolcsply 1 with Dissolve(0.8)
    Kiara "80$ sounds not too much trouble , let's do it"
    scene bg dtwocoolcsply 2 with Dissolve(0.8)
    Kiara "Okay what is this fascination you guys have with latex clothing"
    scene bg dtwocoolcsply 3 with Dissolve(0.8)
    Kiara  "I mean it's not bad but just kinda tight"
    scene bg dtwocoolcsply 4 with Dissolve(0.8)
    Taka "Well they love video games and this character is like a princess so"
    Kiara "What princess wears this ? anyway let's just start"
    scene bg dtwocoolcsply 5 with Dissolve(0.8)
    Taka "Air guitar with fists closed"
    scene bg dtwocoolcsply 6 with Dissolve(0.8)
    Taka  "Do a namastey with leg up!"
    scene bg dtwocoolcsply 7 with Dissolve(0.8)
    Taka "Do like a yeah but move sideways"
    Taka "Alright mask off , let's see some smiles!"
    scene bg dtwocoolcsply 8 with Dissolve(0.8)
    Taka "Cover yourself but leg up too"
    Taka "let's get the fan weapon props!"
    scene bg dtwocoolcsply 9 with Dissolve(0.8)
    Taka "Leg up and show off the open fans"
    scene bg dtwocoolcsply 10 with Dissolve(0.8)
    Taka "Look to sky and left"
    scene bg dtwocoolcsply 11 with Dissolve(0.8)
    Taka "(I can't get enough of her body , so fucking perfect)"
    scene bg dtwocoolcsply 12 with Dissolve(0.8)
    Taka "Last pose , just side amgle with looking at hand"
    scene bg dtwocoolcsply 13 with Dissolve(0.8)
    Taka "(I would eat that ass every day if i was with her)"
    $ inventory.earn(180)
    $ mc_stats.adjust_corruption(3)
    jump chap_2_scene_29

label .part_4:
    # IF 120 $ -> USE RENDERS OF - >dtwolewdcsply ->
    scene bg dtwolewdcsply 1  with Dissolve(0.8)
    Kiara "What do i gotta do in this one?"
    Taka "It's a script we need to follow , it's for an ad"
    scene bg dtwolewdcsply 2  with Dissolve(0.8)
    Kiara"Do people really buy sleep wear based off ads?"
    Taka "Well ads help to promote so , the better they look in catalog the more chance of buyers"
    scene bg dtwolewdcsply 3  with Dissolve(0.8)
    Kiara "Yeah but what adult would wear this?"
    Taka "We all do , it's comfy you know"
    Taka "Aight , let's start"
    scene bg dtwolewdcsply 4  with Dissolve(0.8)
    Taka "Yawn and be like waking up"
    scene bg dtwolewdcsply 5  with Dissolve(0.8)
    Taka "Hands around the neck"
    scene bg dtwolewdcsply 6  with Dissolve(0.8)
    Taka "Alright open the shirt , kinda like a lazy wake up look"
    Kiara "Um , what why?"
    scene bg dtwolewdcsply 7  with Dissolve(0.8)
    Taka "It's a shoot script kiara , they need you to be realistic it's a sleep suit not business, some like it abit unbuttoned"
    Kiara "But why in sleepwear? ( This is just odd.. what do i do? )"
    $ inventory.earn(300)
    $ mc_stats.adjust_corruption(5)
    #Kiara (GIVE OPTION TO REFUSE HERE AND IF REFUSED USE RENDER OF rejectdtwocsplaymid ""
    #if not continue) (Optins 
    #> Unbutton 
    #Do not . 
    if _in_replay:
        jump .part_6
    menu:
        "Unbutton":
            jump .part_6
        "Stop here":
            jump .part_7
    
    label .part_6:
        scene bg dtwolewdcsply 8  with Dissolve(0.8)
        Taka "There we go  , see it's just a shoot"
        Kiara  "( Easy for you to say , i would've worn the bra if i knew this )"
        scene bg dtwolewdcsply 9  with Dissolve(0.8)
        Taka "(so happy i do this shit midway , look at those soft tiddies)"
        scene bg dtwolewdcsply 10 with Dissolve(0.8)
        Taka "Alright just the bottom buttons , you can close the top"
        Kiara "Who on earth buys it based on this?"
        scene bg dtwolewdcsply 11 with Dissolve(0.8)
        Taka "Many do kiara , sometimes it opens from below and so we gotta see if it don't come off"
        Kiara "Makes kinda sense but still weird"
        Taka "( Man i would clean that tummy button with my tongue every single day)"
        scene bg dtwolewdcsply 12 with Dissolve(0.8)
        Taka "Okay just lok to the side now , so your face is hidden with it mostly open"
        Kiara "(Gow does it make a difference , my face is in the previous pictures alredy)"
        scene bg dtwolewdcsply 13 with Dissolve(0.8)
        Kiara "Look can i close it now? , this is very loose"
        Taka "Yes yes okay , you can close the upper buttons fully"
        scene bg dtwolewdcsply 14 with Dissolve(0.8)
        Kiara "Alright thanks"
        Taka  "( Time to use those ground cameras )"
        scene bg dtwolewdcsply 15 with Dissolve(0.8)
        Taka "You're doing great don't worry"
        Kiara "(Why is he so focused on the my stomach)"
        scene bg dtwolewdcsply 16 with Dissolve(0.8)
        Taka "( Let's see now, oh boy i see something )"
        scene bg dtwolewdcsply 17 with Dissolve(0.8)
        Taka "Kiara keep it closed dw but move the right side a but further , so the top's inside clothing is visible?"
        Kiara "Like this?"
        Taka "Yeah.. ( Oh baby , that underboob is soft) "
        scene bg dtwolewdcsply 18 with Dissolve(0.8)
        Taka "( Keeping this one for my fap collection )"
        scene bg dtwolewdcsply 19 with Dissolve(0.8)
        Taka  "Alright kiara ,just stand straight now"
        scene bg dtwolewdcsply 20 with Dissolve(0.8)
        Kiara "Alright? this?"
        Taka "Yeah , great"
        scene bg dtwolewdcsply 21  with Dissolve(0.8)
        Taka "Okay Kiara now we gotta do promo for just the top"
        Kiara "What do you mean?"
        Taka "As in just the top , so you can lose the pajmas now"
        scene bg dtwolewdcsply 22  with Dissolve(0.8)
        Kiara "What?! Are you serious?"
        Taka "Yes , kiar it's just a shoot and some people sleep without pjs so that's why"
        scene bg dtwolewdcsply 23chc  with Dissolve(0.8)
        Kiara "(This is absurd.. it's a shoot i know but.. ugh)"
    #> CHOICE  
    #> Take off Pajamas (+ 5 corruption 
    #requires 40 Corruption) 
    #Refuse to do so ( No changes)
    if _in_replay:
        jump .part_8 
    menu:
        "Take off pajamas" if mc_stats.current_corruption > 40:
            jump .part_8
        "Refuse":
            jump .part_7


    label .part_7:
        # IF REJECT TO DO SO THEN USE RENDERS OF -> rejectdtwocsplaymid ->
        scene bg rejectdtwocsplaymid 1  with Dissolve(0.8)
        Kiara "Forget it , I'm not doing it"
        Taka "Ah  , okay no worries i understand"
        jump chap_2_scene_29

    label .part_8:
        # IF TAKE OFF PAJAMAS then USE RENDERS OF dytwopntsoffcsply->
        scene bg dytwopntsoffcsply 1 with Dissolve(0.8)
        Kiara "Ah.. Fine , please make this quick okay?"
        scene bg dytwopntsoffcsply 2 with Dissolve(0.8)
        Taka "Don't worry we will!( Holy shit she's actually taking em off )"
        scene bg dytwopntsoffcsply 3 with Dissolve(0.8)
        Taka "(Ohh mamma mia, look at those legs)"
        scene bg dytwopntsoffcsply 4 with Dissolve(0.8)
        Kiara "Now what? , this is really a bit too much taka"
        Taka "Don't worry , just sit down it's mostly floor poses"
        scene bg dytwopntsoffcsply 5 with Dissolve(0.8)
        Kiara "Is this okay? I hope nothing is visible"
        Taka "Yeah nothing is visible but you gotta smile kiara (Look at those thighs , bet i wouldn't last a minute between them)"
        scene bg dytwopntsoffcsply 6 with Dissolve(0.8)
        Taka "There it is!"
        scene bg dytwopntsoffcsply 7 with Dissolve(0.8)
        Taka "hold your arm and at camera!"
        scene bg dytwopntsoffcsply 8 with Dissolve(0.8)
        Taka "( Even floor poses you're not safe baby , mm i like the black panties )"
        scene bg dytwopntsoffcsply 9 with Dissolve(0.8)
        Kiara "Is this good?"
        Taka "Yeah yeah all good ( Babe's tryna cover but her busty body wont help it hehe )"
        scene bg dytwopntsoffcsply 10 with Dissolve(0.8)
        Taka "( Kiara , one day i'm going to strip you naked here )"
        scene bg dytwopntsoffcsply 11 with Dissolve(0.8)
        Taka "Legs crossed and look to the side!"
        scene bg dytwopntsoffcsply 12 with Dissolve(0.8)
        Taka "( Hell wh stop at naked? I'll fuck this sweet innocent babe real nice )"
        scene bg dytwopntsoffcsply 13 with Dissolve(0.8)
        Taka "Sit simply with hands at back"
        scene bg dytwopntsoffcsply 14 with Dissolve(0.8)
        Taka "Alright that's a wrap! ( I'll nut in her as well , she's too good to let go )"
        $ renpy.end_replay()
        Kiara "Alright , I'ma go change go back to office"
        jump chap_2_scene_29

label chap_2_scene_29:
    # SCENE - > kiaaftrcsplaydaytwo -:
    scene bg kiaaftrcsplaydaytwo 1 with Dissolve(0.8)
    Kiara "( Reaching noon start , I should be home on time )"
    scene bg kiaaftrcsplaydaytwo 2 with Dissolve(0.8)
    Kiara "( I suppose first the school to azumi , then salon and then the yoga center )"
    scene bg kiaaftrcsplaydaytwo 3 with Dissolve(0.8)
    Kiara "( Sounds like a good plan , alright let's call him )"
    scene bg kiaaftrcsplaydaytwo 4 with Dissolve(0.8)
    Kiara  "Hey! It's me , I'm sending you the location can you come?"
    Keisuke "On it!"
    scene bg kiaaftrcsplaydaytwo 5 with Dissolve(0.8)
    Kiara "(Glad i found someone who knows the city a bit)"
    scene bg kiaaftrcsplaydaytwo 6 with Dissolve(0.8)
    Taka "Kiara , hey kiara!"
    Kiara "Hm?"
    scene bg kiaaftrcsplaydaytwo 7 with Dissolve(0.8)
    Taka "Hey , i hope you're not angry or anything"
    Kiara "Hm? why would i be?"
    scene bg kiaaftrcsplaydaytwo 8 with Dissolve(0.8)
    Taka "Well you know just we haven't talked and its just either a shop visit or money i probably seem greedy"
    Kiara "Not really you're not , also it's fine don't be so hard on yourself"
    scene bg kiaaftrcsplaydaytwo 9 with Dissolve(0.8)
    Taka "Yeah kinda hard to when no one would even bother to company for long"
    Kiara "Lonely then ? Well we all are in someway it's fine"
    scene bg kiaaftrcsplaydaytwo 10  with Dissolve(0.8)
    Taka "Well that but even date wise , I ain't exactly a looker so"
    Kiara "Looks fade away with time anyway , just be yourself and you'll find someone eventually"
    scene bg kiaaftrcsplaydaytwo 11 with Dissolve(0.8)
    Taka "(Be myself? I don't even know the real me anymore)"
    scene bg kiaaftrcsplaydaytwo 12 with Dissolve(0.8)
    Keisuke "Hey there! best rain driver has arrievd"
    Kiara "Hey!! hah , comin!"
    scene bg kiaaftrcsplaydaytwo 13 with Dissolve(0.8)
    Kiara "What i meant was try to find new things , even if old gives dopamine, take care!"
    Taka "Yeah thanks , you too kiara!"
    scene bg kiaaftrcsplaydaytwo 14 with Dissolve(0.8)
    Taka "What a girl , not just beautiful but kind too"
    Keisuke "So shall we go?"
    Kiara "No before we do anything you have to do something or we're not moving"
    scene bg kiaaftrcsplaydaytwo 15 with Dissolve(0.8)
    Keisuke "What would that be?"
    Kiara "Remove the stupid mask , it's like i'm talking to a doctor"
    scene bg kiaaftrcsplaydaytwo 16 with Dissolve(0.8)
    Keisuke "um but I-"
    Kiara "No buts , you either do it or i'm leaving"
    scene bg kiaaftrcsplaydaytwo 17 with Dissolve(0.8)
    Keisuke "Ah no please , alright i'll get it off"
    scene bg kiaaftrcsplaydaytwo 18 with Dissolve(0.8)
    Keisuke "Happy now?"
    Kiara "See , at least now i know who i'm talking to"
    Keisuke "Heh , alright"
    scene bg kiaaftrcsplaydaytwo 19 with Dissolve(0.8)
    Kiara "Vamenos senior!"
    Keisuke "As you wish!"
    scene bg kiaaftrcsplaydaytwo 20 with Dissolve(0.8)
    Kiara "Ahh.. um hey i need to ask"
    scene bg kiaaftrcsplaydaytwo 21 with Dissolve(0.8)
    Kiara "Do you know any restros around ? I didn't have lunch so kinda hungry"
    Keisuke "Of course no need to ask , I'll get you to a good place i know."
    scene bg kiaaftrcsplaydaytwo 22 with Dissolve(0.8)
    Kiara "Alright, surprise me then."
    scene bg ksukedatedytwo 1 with Dissolve(0.8)
    Keisuke "It's right around this corner , Don't worry"
    Kiara "Oh I'm not worried really , just hungry"
    Keisuke "Heh I know , just a sec"
    scene bg ksukedatedytwo 2 with Dissolve(0.8)
    Kiara "Ahh look at those pretty lanterns , I bet it looks lovely at night time"
    Keisuke "It does , you should visit it sometime with your friends"
    scene bg ksukedatedytwo 3 with Dissolve(0.8)
    Kiara "Well if food is decent , we'll definitely come again"
    Keisuke "It is , anyway go on enjoy your food . I'll wait"
    scene bg ksukedatedytwo 4 with Dissolve(0.8)
    Kiara "What do you mean enjoy the food? Aren't you coming?"
    Keisuke "Uh me? .. I mean actually-"
    Keisuke "I already have my sandwich with me in the car so.."
    scene bg ksukedatedytwo 5 with Dissolve(0.8)
    Kiara "What do you mean? We are at a restro and you want to eat a sandwich outside in car?"
    Keisuke "Well actually , I mean i'm just a driver and not really dressed properly & besides i'm sure you'd want to enjoy your food in peace"
    scene bgchckskedtfst with Dissolve(0.8)
    Kiara "(What? why is he being this way?)"
    menu:
        "Insist on it":
            jump .part_1
        "Accept his reason":
            jump .part_2

    label .part_1:
        scene keisukedateyes1 with Dissolve(0.8)
        Kiara "Okay fine , I'm not eating either then!"
        Keisuke "What? but why?"
        scene keisukedateyes2 with Dissolve(0.8)
        Kiara "I don't wanna eat alone firstly and secondly i don't want you to sit in car while i sit in ac"
        Keisuke "But kiara I-"
        scene keisukedateyes3 with Dissolve(0.8)
        Keisuke "Ah alright , let's go eat"
        Kiara "Yay thank you! , cmon it'll be fun"
        scene keisukedateyes4 with Dissolve(0.8)
        Kiara "Place looks lovely , don't you think?"
        Keisuke "It's one of the finest korean restros here so yeah"
        scene keisukedateyes5 with Dissolve(0.8)
        Kiara "I see , well come on let's get this done"
        Keisuke "I think that table looks good , let's sit there"
        scene keisukedateyes6 with Dissolve(0.8)
        Keisuke "We probably need to talk to reception first"
        scene keisukedateyes7 with Dissolve(0.8)
        "Reception Lady" "Hello sir and mam , what can we help you with?"
        Kiara "Food!"
        Keisuke "Uhm , we would like a table"
        scene keisukedateyes8 with Dissolve(0.8)
        "Reception lady" "I'll send someone to get your order shortly , please enjoy the ambiance"
        scene keisukedateyes9 with Dissolve(0.8)
        Keisuke "Thank you"
        Kiara "Thanks!"
        scene keisukedateyes10 with Dissolve(0.8)
        Kiara "Hey , why are you sitting there?"
        Keisuke "Um i thought probably would want enough room to sit"
        scene keisukedateyes11 with Dissolve(0.8)
        Kiara "I'm no model but i'm pretty sure i'm not that fat so just come , it looks odd anyway"
        Keisuke "No that's not what i - , um yeah alright"
        scene keisukedateyes12 with Dissolve(0.8)
        Kiara "This place is really nice , I'll definitely visit it again"
        Keisuke "( Ah don't stare at her , don't stare at her..)"
        scene keisukedateyes13 with Dissolve(0.8)
        Kiara "I'm not that scary you know , you can relax a little bit"
        scene keisukedateyes14 with Dissolve(0.8)
        Keisuke "No , not at all! . I'm just a bit shy because i usually eat alone hence i'm not too confident in conversation"
        scene bgksukedtyschcfstaftrfourteen with Dissolve(0.8)
        Kiara "( Why would we think like that about himself? I should -)"
        menu:
            "Say Simply":
                jump .part_4
            "Compliment":
                jump .part_5
        
    label .part_4:
        scene bg saysmplykske 1 with Dissolve(0.8)
        Kiara "Well it's alright to be shy and reserved , I am too but don't lose confidence okay? It's all we got nowadays"
        scene bg saysmplykske 2 with Dissolve(0.8)
        Keisuke "Yes , you're right i'm confident just a bit scared"
        Kiara "Which is completely fine, nothing wrong with it"
        scene bg saysmplykske 3 with Dissolve(0.8)
        Kiara "You're human too , no pressure to be perfect"
        Keisuke "Thank you , Kiara"
        jump .part_3
        
    label .part_5:
        scene bg cmplmntkske 1 with Dissolve(0.8)
        Kiara "Shy? First that mask and now this"
        Kiara "You look very good , don't just lose confidence over one girl rejecting you . You're alot more than that"
        scene bg cmplmntkske 2 with Dissolve(0.8)
        Keisuke "Thanks ,  but i don't think everyone around me thinks the same"
        Kiara "So what if they don't?"
        scene bg cmplmntkske 3 with Dissolve(0.8)
        Kiara "I think so , and i'm here right now aren't i? deosn't that count?"
        Keisuke "Y-yeah , it does count.. I appreciate it"
        scene bg cmplmntkske 4 with Dissolve(0.8)
        Kiara "Don't appreciate it , get used to it instead okay it's the easiest life hack to be happy hehe"
        Keisuke "( You are all that matters to me.. , thank you kiara)"
        $ keisuke_rom.adjust_romance(1)
        jump .part_3
            


    label .part_2:
        scene gone with Dissolve(0.8)
        Kiara "Okay i get it , I'll try to finish up fast so you don't have to wait long"
        Keisuke "Don't worry about it , take your time and eat well"
        scene gtwo with Dissolve(0.8)
        Kiara "Alright , well i'll grab some food for you at least tell me your full name? I mean for the order."
        Keisuke "It's Keisuke takahashi , you really don't have to trouble yourself for this"
        scene gthree with Dissolve(0.8)
        Kiara "Too bad i will ! , stay put okay i'll see you in a bit"
        scene gfour with Dissolve(0.8)
        Keisuke "Enjoy your food okay? and thanks!"
        scene gfive with Dissolve(0.8)
        Keisuke "(I don't want to make her uncomfortable , this is fine..)"
        jump chap_2_scene_30
        
    label .part_3:
        scene keisukedateyes15 with Dissolve(0.8)
        "Lady" "Hello sir and mam , what can we bring you?"
        Keisuke "Some udon noodles and watermelon juice with extra spice"
        scene keisukedateyes16 with Dissolve(0.8)
        "Lady" "Perfect , what about you mam?"
        Kiara "Oh- um.. same actually haha"
        "Lady" "Please give us a moment"
        scene keisukedateyes17 with Dissolve(0.8)
        Keisuke "( *Humming music*)"
        Kiara "Um hey.."
        scene keisukedateyes18 with Dissolve(0.8)
        Kiara "Hey!"
        Keisuke "Ah yeah ? what happened?"
        Kiara "How did you know i was gonna order the same thing?"
        scene keisukedateyes19 with Dissolve(0.8)
        Keisuke "Well i uh didn't know really . I mean everyone loves watermleon right and a quick snack is noodles"
        Kiara "Um yeah i suppose so.. , okay"
        Keisuke " ( Dammit i should be careful , will let her order next times)"
        scene keisukedateyes20 with Dissolve(0.8)
        Kiara "Well anyway so i only know your initial name as Kei , is it or kay?"
        Kiara "I mean what is your name really? Since you know mine it's only fair to ask"
        Keisuke "Oh yes it is , It's keisuke takahashi"
        scene keisukedateyes21 with Dissolve(0.8)
        Kiara "Wow , that's.. a nice name. I mean-"
        Kiara "Sorry If i'm rude here just the last one is kinda scary"
        Keisuke "No don't be  , It's abit overwhelming i know"
        scene keisukedateyes22 with Dissolve(0.8)
        Kiara "So keisuke , other than this cab thing do you have any plans for future?"
        Keisuke "Yeah my father has a small business , probably handle that or get into it"
        scene keisukedateyes23 with Dissolve(0.8)
        Kiara "Wait , then why the cab thing?"
        Keisuke "Oh it's just i kind of wanted to be a little independent and not rely on family"
        scene keisukedateyes24 with Dissolve(0.8)
        Kiara "Oh  well ditto on that i suppose"
        Keisuke "Yeah was wondering about why you're doing this too despite that house , I guess i have my answer."
        scene keisukedateyes25 with Dissolve(0.8)
        Kiara "I want to be known as.. you know , someone people remember"
        Kiara "Someone who did everything herself , i want them to remmeber my first name , not my last"
        scene keisukedateyes26 with Dissolve(0.8)
        Kiara "I know i'm alone in that path , and hey maybe i'll fail and fall several times"
        Keisuke "( Kiara..)"
        scene keisukedateyes27 with Dissolve(0.8)
        Kiara "Though i won't give up , we only fall to get up again and become stronger right?"
        Keisuke "( You are not alone.. I-)"
        scene keisukedateyes28 with Dissolve(0.8)
        Kiara "If i still don't make it.. then that's on me but i won't give up , even if i have to do it all on my own"
        scene keisukedateyes29 with Dissolve(0.8)
        Keisuke "( I am on your side.. , i won't let it happ-)"
        scene keisukedateyes30 with Dissolve(0.8)
        Kiara "Oh hey our food's here"
        Keisuke "Oh yeah.. ( Kiara one day i'll let you know , for now i just want to spend time with you)"
        scene keisukedateyes31 with Dissolve(0.8)
        Keisuke "These are definitely very hot , but are nice"
        Kiara "The spice is so good!"
        scene keisukedateyes32 with Dissolve(0.8)
        Keisuke "( How do you make something so silly as noodle eating look so cute?)"
        scene keisukedateyes33 with Dissolve(0.8)
        Kiara "*Slurrrrp* Haa , mamma mia these are good!"
        scene keisukedateyes34 with Dissolve(0.8)
        Kiara "Haaaa , I'm so full those were good but i beat em"
        Keisuke "You definitely showed those noodles alright"
        scene keisukedateyes35 with Dissolve(0.8)
        Kiara "So don't mind me asking this but , why did the girl say no to you anyawy? I mean was it because of your job?"
        Keisuke "Well that and i felt i wasn't good enough anyway , so not the best combo also she loved someone else.. so yeah."
        Kiara "I'm sorry for that"
        scene keisukedateyes36 with Dissolve(0.8)
        Keisuke "No you shouldn't be , If it's meant to happen it will i can't really force a bond with someone"
        Kiara "Well I'm sure you'll find someone again , you're a good guy in my opinion"
        scene keisukedateyes37 with Dissolve(0.8)
        Keisuke "what if i don't though? I mean i failed at my first so badly"
        Kiara "Well I'm the best wingman remember? So don't worry i'll help somehow"
        scene keisukedateyes38 with Dissolve(0.8)
        Keisuke "Okay then , what about you though? If i'm allowed to ask do you like anyone?"
        Kiara "Oh , um.."
        scene keisukedateyes39 with Dissolve(0.8)
        Kiara "Don't mean to sound like a bummer but i kinda never found anyone who loved me , they all just cared about the money"
        Keisuke "You're not a bummer , It's hard to find a genuine comppasioante bond nowadays so i understand."
        scene keisukedateyes40 with Dissolve(0.8)
        Kiara "Well hopefully i'll end up with someone i can grow old with , someone nice and kind"
        Keisuke "Well I wish you the best on that too , one day you'll be sucessful as well honestly , probably will forget this little driver on the side"
        scene bgkskedtdytwoscndchcaftrforty with Dissolve(0.8)
        Kiara "( On the side? Um -)"
        menu:
            "Cheer him up":
                jump .part_6
            "Respond friendly":
                jump .part_7

    label .part_6:

        scene bg rspndkskeflirt 1 with Dissolve(0.8)
        Kiara "Well you could just end up with me too"
        Keisuke "Wh- what do you mean?"
        scene bg rspndkskeflirt 2 with Dissolve(0.8)
        Kiara "Like if i'm successful you could just stick with me still , not like you're moving out"
        Keisuke "Oh uh , ye- Yeah yeah definitely i can do that"
        scene bg rspndkskeflirt 3 with Dissolve(0.8)
        Keisuke "Sorry for stuttering , I kinda got spookedfor a second"
        Kiara "It was intentional , I wanted to see what you'd say haha"
        scene bg rspndkskeflirt 4 with Dissolve(0.8)
        Keisuke "R- right , sorry i'm just silly so got scared"
        Kiara "Scared or happy? heh"
        scene bg rspndkskeflirt 5 with Dissolve(0.8)
        Keisuke "N- no comment ( Argh dmamit i'm blushing now too)"
        Kiara "( He really is a simple guy , I hope i didn't make him uncomfortable)"
        $ keisuke_rom.adjust_romance(1)
        scene keisukedateyes41 with Dissolve(0.8)
        Kiara "Well I'll go sit in the car , can you grab the juice please?"
        Keisuke "Of course , I'll get them safely too don't worry"
        jump chap_2_scene_30

    label .part_7:
        scene bg rspndkskefrnd 1 with Dissolve(0.8)
        Kiara "Of course i won't , I'm way too picky with people i trust so i'm keeping you for sure"
        Keisuke "Keeping me as the tour guide or the driver?"
        scene bg rspndkskefrnd 2 with Dissolve(0.8)
        Kiara "Keeping you as a friend i trust , always"
        Keisuke "Heh , thank you i appreciate it."
        scene keisukedateyes41 with Dissolve(0.8)
        Kiara "Well I'll go sit in the car , can you grab the juice please?"
        Keisuke "Of course , I'll get them safely too don't worry"
        jump chap_2_scene_30
    
label chap_2_scene_30:
    scene blackscreen
    show titletext "Abit later outside.." with dissolve
    pause 1.0
    window hide
    scene bg kiadytwoskool 1 with Dissolve(0.8)
    Kiara "Okay Mr. Keisuke , Let us head to school shall we?"
    Keisuke "As you say Mrs. Kiara!"
    scene bg kiadytwoskool 2 with Dissolve(0.8)
    Natsuko "Why?! , Why won't he just leave us the fuck alone??!"
    Xia "Natsuko honey , calm yourself"
    scene bg kiadytwoskool 3 with Dissolve(0.8)
    Natsuko "I cannot mother! He ruined aunt mia's life first and now kiara-"
    Xia "I understand but paining yourself will not solve this natsuko"
    scene bg kiadytwoskool 4 with Dissolve(0.8)
    Natsuko "I don't want her to go back again.."
    Xia "Natsuko it isn't in our hands , but your father and everyone is trying so please-"
    scene bg kiadytwoskool 5 with Dissolve(0.8)
    Natsuko "Trying is not enough mother , we have to figure something out"
    Xia " I understand you are frustrated , but we have to consider all things"
    Xia "Let's give her the best life we can here for now , let mia and others take care of new york"
    scene bg kiadytwoskool 6 with Dissolve(0.8)
    Natsuko "Okay.. i will go with her tommorow , let her enjoy and relax"
    Xia "Good , I will do my best too to make her capable"
    scene bg kiadytwoskool 7 with Dissolve(0.8)
    Xia "I'll go ahead and make some food that she likes , let's treat her well alright?"
    Natsuko "Okay mother , I'll get some rest. I think i need it"
    scene bg kiadytwoskool 8 with Dissolve(0.8)
    Xia "Stay strong natsuko , if we won't be she can't either"
    Natsuko "Understood mother , I will try.."
    scene bg kiadytwoskool 9 with Dissolve(0.8)
    Natsuko "( Kiara.. you-)"
    scene bg kiadytwoskool 10 with Dissolve(0.8)
    Natsuko "I need to do something.. I can't let it happen again"
    scene bg kiadytwoskool 11 with Dissolve(0.8)
    Natsuko "I should ask dad first , what the situation is"
    scene bg kiadytwoskool 12 with Dissolve(0.8)
    Natsuko "Dad? Dad hello?"
    scene bg kiadytwoskool 13 with Dissolve(0.8)
    Ichigo "Natsuko hear me out for a second"
    Natsuko "No Dad! , I want this to be over , just tell me everything"
    scene bg kiadytwoskool 14 with Dissolve(0.8)
    Ichigo "Natsu I cannot explain the entire ordeal on the phone even if i wanted to"
    Natsuko "Then promise me something"
    scene bg kiadytwoskool 15 with Dissolve(0.8)
    Ichigo "What can i do for you?"
    Natsuko "Promise me she'll come back here after going there at least"
    scene bg kiadytwoskool 16 with Dissolve(0.8)
    Ichigo "Yes she will , have faith in me natsuko i am trying to get her here permanently"
    Natsuko "Okay.. I miss you by the way when are you coming?"
    Ichigo "We'll meet on monday don't worry , take care of your mother too"
    scene bg kiadytwoskool 17 with Dissolve(0.8)
    Ichigo "( Mia.. why didn't you do this sooner)"
    scene bg kiadytwoskool 18 with Dissolve(0.8)
    Ichigo "(Everything is happening quite fast , I need to do something before he grasps the plan I've had for a while)"
    scene bg kiadytwoskool 19 with Dissolve(0.8)
    Ichigo "( Kiara , Stay strong i and mason will find a way to get you home forever.)"
    scene blackscreen
    show titletext "Shibamsura University , Osaka.." with dissolve
    pause 1.0
    window hide
    scene bg kiadytwoskool 20 with Dissolve(0.8)
    Kiara "( Just the introductory class , I got this and i was good with juniors anyway)"
    scene bg kiadytwoskool 21 with Dissolve(0.8)
    pause
    scene bg kiadytwoskool 22 with Dissolve(0.8)
    pause
    scene bg kiadytwoskool 23 with Dissolve(0.8)
    Kiara "Ahh cmon why am i getting nervous , It's just kids a bit younger than me cmon"
    scene bg kiadytwoskool 24 with Dissolve(0.8)
    Kiara "(I should probably ask azumi for tips later on too)"
    scene bg kiadytwoskool 25 with Dissolve(0.8)
    "???" "May we come in?"
    Kiara "Please yes , come in"
    scene bg kiadytwoskool 26 with Dissolve(0.8)
    "???" " Ohayō Gozaimasu"
    scene bg kiadytwoskool 27 with Dissolve(0.8)
    Kiara "They really are my juniors age it seems"
    scene bg kiadytwoskool 28 with Dissolve(0.8)
    pause
    scene bg kiadytwoskool 29 with Dissolve(0.8)
    pause
    scene bg kiadytwoskool 30 with Dissolve(0.8)
    pause
    scene bg kiadytwoskool 31 with Dissolve(0.8)
    Kiara "Um is it only four of you ? where are the rest ?"
    Hodaka "Unfortunately yes mam , for now only us"
    Kiryu "We tried bringing them but they weren't interested mam , they're also kinda bigots so yeah"
    scene bg kiadytwoskool 32 with Dissolve(0.8)
    Kiara "Well alright , Um fine sit let's get started"
    scene bg kiadytwoskool 33 with Dissolve(0.8)
    Kiara "Uh well  Hi everyone I'm kiara your new english teacher , let's get started with some introductions perhaps?"
    scene bg kiadytwoskool 34 with Dissolve(0.8)
    Kiryu "Kiryu moroshima"
    scene bg kiadytwoskool 35 with Dissolve(0.8)
    Hodaka "Hodaka Matsui"
    scene bg kiadytwoskool 36 with Dissolve(0.8)
    Uno "Uno Hasegawa"
    scene bg kiadytwoskool 37 with Dissolve(0.8)
    Chiyo "Chiyo Suzuki"
    scene bg kiadytwoskool 38 with Dissolve(0.8)
    Kiara "Lovely names all of you , so why don't people want to learn english exactly? What did you mean?"
    scene bg kiadytwoskool 39 with Dissolve(0.8)
    Chiyo "Some have a backward mindset of learning english being abandoning your roots and culture"
    Kiryu "Some like i said are bigots and lazy , they don't want to bother since they won't move out"
    Kiara "I see , well that's their loss anyway just a small question what do you all want to be?"
    scene bg kiadytwoskool 40 with Dissolve(0.8)
    Chiyo "I want to be a teacher like you!"
    Kiara "( Heh cute)"
    scene bg kiadytwoskool 41 with Dissolve(0.8)
    Hodaka "I want to be a singer or pop star!"
    Kiara "Would love to hear you sing sometime"
    scene bg kiadytwoskool 42 with Dissolve(0.8)
    Kiryu "I want to be a undercover spy , be all secretive"
    Kiara "( Someone's been watching too many movies)"
    scene bg kiadytwoskool 43 with Dissolve(0.8)
    Uno "I want to be a pilot! , commercial i mean"
    Kiara "Fly in the sky huh , good goal"
    scene bg kiadytwoskool 44 with Dissolve(0.8)
    Uno "Kiara-san , do you like being a teacher?"
    Kiara "I do , i was very good in school and liked helping everyone so yeah"
    scene bg kiadytwoskool 45 with Dissolve(0.8)
    Uno "Yes , if we all succeed together it's faster and better"
    Kiara "Precisely , you're very smart"
    scene bg kiadytwoskolchcfrst with Dissolve(0.8)
    Hodaka "Kiara- san , what do you think about our other english teacher? She's quite good in my opinion"
    Kiryu "Ahh Azumi-san is very good yeah"
    Chiyo "She's sooo pretty"
    Uno "She's verrry cute!"
    Kiara "Well  I-"
    menu:
        "Compliment":
            jump .part_1
        "Say simply":
            jump .part_2

    label .part_1:
        scene bg dytwoskoolazmicmplmnt 1 with Dissolve(0.8)
        Kiara "Azumi is.. wonderful , she's quite nice and kind in a world like this where everyone else seeks benefit"
        scene bg dytwoskoolazmicmplmnt 2 with Dissolve(0.8)
        Kiara "She helped me too , so yes she's a really good soul"
        scene bg dytwoskoolazmicmplmnt 3 with Dissolve(0.8)
        Azumi "heh.."
        scene bg dytwoskoolazmicmplmnt 4 with Dissolve(0.8)
        Azumi "I think the same about you kiara"
        jump .part_3

    label .part_2:
        scene bg dytwoskoolazmisaysmply 1 with Dissolve(0.8)
        Kiara "She's a great friend , she helped me where not many other would"
        scene bg dytwoskoolazmisaysmply 2 with Dissolve(0.8)
        Kiara "Secondly i can tell by how you all are , she's a great teacher too right?"
        scene bg dytwoskoolazmisaysmply 3 with Dissolve(0.8)
        Azumi "A great friend , a great teacher.. certainly nice to hear"
        scene bg dytwoskoolazmisaysmply 4 with Dissolve(0.8)
        Azumi "I consider you my equal too , hope we'll stay good friends kiara"
        jump .part_3

    label .part_3:
        scene bg kiadytwoskool 46 with Dissolve(0.8)
        Chiyo "Kiara-san , so will azumi-san not teach us anymore?"
        Kiara "Oh um i actually don't know , but i think it'll probably be rotational"
        scene bg kiadytwoskool 47 with Dissolve(0.8)
        Hodaka "I don't really mind it , you are american so obviously you'd do it better"
        Kiara "Thank you hodaka but teaching has its skillset , so that doesn't apply"
        scene bg kiadytwoskool 48 with Dissolve(0.8)
        Kiryu "What he probably meant was that you're going to be a great teacher as well"
        Kiara "I appreciate it , I'll do my best but please be a little patient with me guys haha"
        scene bg kiadytwoskool 49 with Dissolve(0.8)
        Chiyo "I will be! , you seem like a very good person"
        Kiara "Thank you agian , so shall we get started?"
        scene bg kiadytwoskool 50 with Dissolve(0.8)
        "*Bell rings*"
        Kiara "Ah.."
        scene bg kiadytwoskool 51 with Dissolve(0.8)
        Kiara "Suppose that's all we have for today , it's a shame would've liked a demo class at least"
        Uno "It's fine kiara- san we'll see you next week too"
        scene bg kiadytwoskool 52 with Dissolve(0.8)
        Kiara "Have a great evening all of you!"
        Kiryu "Thank you!"
        scene bg kiadytwoskool 53 with Dissolve(0.8)
        Kiara "( Alright , suppose i'll pack up for salon)"
        scene bg kiadytwoskool 54 with Dissolve(0.8)
        Kiara "Hm ?.."
        scene bg kiadytwoskool 55 with Dissolve(0.8)
        Kiara "Chiyo? Is there anything you wanted to ask?"
        scene bg kiadytwoskool 56 with Dissolve(0.8)
        Chiyo "Kiara-san can i please say something , i didn't want to in front of others"
        scene bg kiadytwoskool 57 with Dissolve(0.8)
        Kiara "Yeah go on , don't worry speak your mind"
        Chiyo "Well um- you aren't much older than us right?"
        scene bg kiadytwoskool 58 with Dissolve(0.8)
        Kiara "Um yes , roughly 4 / 5 years i suppose why?"
        Chiyo "Well you just look very beautiful so i was making sure"
        scene bg kiadytwoskool 59 with Dissolve(0.8)
        Kiara "Aha  that's very sweet of you chiyo , you look cute as well"
        scene bg kiadytwoskool 60 with Dissolve(0.8)
        Chiyo "One more thing , Can i please call you big sister after class?.. I don't have one and you seem very nice so"
        Kiara "Awe.. you can , Matter of fact let's hangout like sisters on sunday okay?"
        scene bg kiadytwoskool 61 with Dissolve(0.8)
        Chiyo "Thank you! , I'll see you later have a great rest of the day kiara-san"
        Kiara "You too ( That was quite adorable , little sister huh feels funny since i am one)"
        scene bg kiadytwoskool 62 with Dissolve(0.8)
        Kiara "Alright , I'll put these here and i should be fine"
        scene bg kiadytwoskool 63 with Dissolve(0.8)
        Azumi "Ehm ehm , may i come in mam?"
        scene bg kiadytwoskool 64 with Dissolve(0.8)
        Kiara "Aheh , Hey azumi!"
        Azumi "Hi.. I was watching your class , that was very formal"
        scene bg kiadytwoskool 65 with Dissolve(0.8)
        Kiara "Sorry haha , just wanted to know them first before i just blast them with studies you know"
        Azumi "No don't apologize  , It's what i did too so you did great"
        scene bg kiadytwoskool 66 with Dissolve(0.8)
        Kiara "If you say so , the kids are great and seems i'll fit right in"
        Azumi "They'll have more of your company than i do which is a bit unfair"
        scene bg kiadytwoskool 67 with Dissolve(0.8)
        Kiara "Well they don't get to have lunch or hangout with me , so there you go!"
        Azumi "That is fair , I've got the best exclusive company when it comes to sharing tea"
        scene bg kiadytwoskool 68 with Dissolve(0.8)
        Kiara "So anything you wanted to say? I was just packing up"
        scene bg kiadytwoskool 69 with Dissolve(0.8)
        Azumi "Oh yes actually i wanted to ask-"
        scene bg kiadytwoskool 70 with Dissolve(0.8)
        Azumi "Ah.. aw cmon"
        scene bg kiadytwoskool 71 with Dissolve(0.8)
        Azumi "Um.. sorry , I guess not today"
        Kiara "What happened?"
        scene bg kiadytwoskool 72 with Dissolve(0.8)
        Azumi "I wanted to have some ice cream with you , but i think uncle fell on stairs i have to go"
        Azumi "This sucks.. I barely get to see you anyway.."
        menu:
            "Comfort her":
                #block of code to run
                jump .part_4
            "Cheer her up":
                #block of code to run
                jump .part_5

        label .part_4:
        
            scene bg daytwoskoolazmicmfrt 1 with Dissolve(0.8)
            Kiara "Don't worry , we'll hangout tommorow anyway right?"
            Azumi "Yes i suppose so"
            scene bg daytwoskoolazmicmfrt 2 with Dissolve(0.8)
            Kiara "We'll have plenty of time don't worry , laters okay?"
            Azumi "Y-yeah laters.. ( I hope tommorow i'll have plenty of time)"
            jump chap_2_scene_31
        
        label .part_5:

            scene bg daytwoskoolazmicheerup 1 with Dissolve(0.8)
            Kiara "Azumi it's okay , actually before you go can you close your eyes real quick?"
            Azumi "My eyes?.. um okay i trust you"
            scene bg daytwoskoolazmicheerup 2 with Dissolve(0.8)
            pause
            scene bg daytwoskoolazmicheerup 3 with Dissolve(0.8)
            pause
            scene bg daytwoskoolazmicheerup 4 with Dissolve(0.8)
            Kiara "Mwwaaah.."
            Azumi "Ah! *Gasp*"
            scene bg daytwoskoolazmicheerup 5 with Dissolve(0.8)
            Kiara "Happy now?"
            Azumi "Yeah that- that'll suffice.. thanks"
            scene bg daytwoskoolazmicheerup 6 with Dissolve(0.8)
            Kiara "Bye cutie pie!"
            Azumi "Y- you too!"
            scene bg daytwoskoolazmicheerup 7 with Dissolve(0.8)
            Azumi "Cutie pie.., she kissed my forehead"
            scene bg daytwoskoolazmicheerup 8 with Dissolve(0.8)
            Azumi "Yay!!!! best start to weekend!"
            jump chap_2_scene_31


label chap_2_scene_31:
    scene blackscreen
    show titletext "Aiden's apartment , Mid noon" with dissolve
    pause 1.0
    window hide
    scene aidendaytwojpn 1 with Dissolve(0.8)
    Aiden "Christ almighty i gotta get a faster way to set this up , at least it's done"
    scene aidendaytwojpn 2 with Dissolve(0.8)
    Aiden "Now let's a look at what the assistant sent"
    scene aidendaytwojpn 3 with Dissolve(0.8)
    Aiden "Hm.. So the account john transfered this to was a btc offshore , Name says wong.."
    scene aidendaytwojpn 4 with Dissolve(0.8)
    Aiden "Secret service agent.. I wonder if she's already here or near kiara"
    scene aidendaytwojpn 5 with Dissolve(0.8)
    Aiden "If she is she's probably already operating.. I'd have to trace where these funds are being spent"
    scene aidendaytwojpn 6 with Dissolve(0.8)
    Aiden "Val?.. why is she calling at this time"
    scene aidendaytwojpn 7 with Dissolve(0.8)
    Aiden "Yeah , what is it?"
    Valentina "Sorry i just wanted to ask if you found anything else.. I'm on a dead end here"
    scene aidendaytwojpn 8 with Dissolve(0.8)
    Aiden "I did or at least some of  it , what about you? and how's nick?"
    Valentina "He's alright..I am kind of just being secretive when we text "
    Valentina "Anyway , what did you find about that agent?"
    scene aidendaytwojpn 9 with Dissolve(0.8)
    Aiden "Not much except a last name, she's apparaently special ops too only works for high paying clients , i'm guessing it's a protection job or overseeing one"
    Valentina "Protection.. of kiara? why?"
    scene aidendaytwojpn 10 with Dissolve(0.8)
    Aiden "I don't know  , but my guess is even here till case settles he doesn't want her befriending anyone or too close"
    Valentina "Okay but.. won't she come after you as well then?"
    Aiden "Probably will , but i'm just a collegue employee can just remain anon for now"
    scene aidendaytwojpn 11 with Dissolve(0.8)
    Aiden "Though yes ,  seems like there are multiple homicides right around the places wherever kiara went"
    Valentina "W-what? murders?"
    scene aidendaytwojpn 12 with Dissolve(0.8)
    Aiden "A guy outside shibamishura station , Some one around the park area , One near an office building.."
    Valentina "You think they.. they're-"
    scene aidendaytwojpn 13 with Dissolve(0.8)
    Aiden "Dead yeah .. this woman ain't playing around . I'll have to be careufl"
    scene aidendaytwojpn 14 with Dissolve(0.8)
    Valentina "Please be careful.."
    Aiden "I will , you do too catch you later."
    jump chap_2_scene_32

label chap_2_scene_32:
    scene blackscreen
    show titletext "Style like none , late noon.." with dissolve
    pause 1.0
    window hide
    scene bg kiadytwosalon 1 with Dissolve(0.8)
    Kiara "No one at work.. I wonder where the others are?"
    scene bg kiadytwosalon 2 with Dissolve(0.8)
    Asa "Hey kiara , good eve how come you're here?"
    scene bg kiadytwosalon 3 with Dissolve(0.8)
    Kiara "Hey asa , Oh i uh came to do some clients.. what's going on?"
    Asa "Oh we close early on weekends , rose is in office and others are home"
    scene bg kiadytwosalon 4 with Dissolve(0.8)
    Kiara "Aw.. I thought i'd get started or practice today."
    Asa "Um well i don't think any booking are here  for today ,  I'm sorry really"
    scene bg kiadytwosalon 5 with Dissolve(0.8)
    Asa "It's alright really , you can hangout with rose or just come with me we'll have some milkshakes"
    Kiara "Yes.. but i did want to start at least something today"
    scene bg kiadytwosalon 6 with Dissolve(0.8)
    Asa "Um well , we do have dummys if you want those"
    Kiara "No I've done those enough on internship , ah well.."
    scene bg kiadytwosalon 7 with Dissolve(0.8)
    Asa "Oh sir hello , we're closing actually"
    "Fatguy" "But i wanted a haircut only"
    scene bg kiadytwosalon 8 with Dissolve(0.8)
    "Fatguy" "No barbors at all? It's just a small cut i need"
    Asa "I'm sorry sir but we are basically just leaving so"
    Kiara "W-wait asa-"
    scene bg kiadytwosalon 9 with Dissolve(0.8)
    Kiara "Um sir , I'm new here but do you mind if i do it?"
    "Fatguy" "Yeah why not it's just just simple trimming after all"
    Asa "Um are you sure about this kiara?"
    scene bg kiadytwosalon 10 with Dissolve(0.8)
    Kiara "Yeah i'm sure i can handle it , don't worry you can go"
    Asa "If you say so , I'll see you next week then okay?"
    scene bg kiadytwosalon 11 with Dissolve(0.8)
    Asa "Bye! , have a good evening and meet rose before you leave okay?"
    Kiara "You too! , take care and yeah i will!"
    scene bg kiadytwosalon 12 with Dissolve(0.8)
    Kiara "Alright let's see what this is about"
    scene bg kiadytwosalon 13 with Dissolve(0.8)
    Kiara "Just to confirm , what would you like exactly?"
    "Fatguy" "Just an trim of sideburns and my neck area to be clear"
    scene bg kiadytwosalon 14 with Dissolve(0.8)
    Kiara "Um.. Okay (He's already balding and he wants sideburns removed?.. Whatever i guess)"
    scene bg kiadytwosalon 15 with Dissolve(0.8)
    "Fatguy" "You new here , studies in japan then?"
    Kiara "Oh no , my studies have finished i'm just here for some family matters but no working visa so yeah"
    scene bg kiadytwosalon 16 with Dissolve(0.8)
    "Fatguy" "Many people move here without any plan , I hope you got one girl"
    Kiara "I mean i guess i do have a roadmap but i'll just see where the road leads me"
    scene bg kiadytwosalon 17 with Dissolve(0.8)
    "Fatguy" "You should get japanese citizenship then , would help you alot"
    Kiara "That would help but naturalization is often quite slow so can't really do it"
    scene bg kiadytwosalon 18 with Dissolve(0.8)
    "Fatguy" "You can also marry someone , that also gives it to you automatically"
    Kiara "Hah , that's not happening anytime soon for sure"
    scene bg kiadytwosalon 19 with Dissolve(0.8)
    "fatguy" "Well I'm sure a girl like you could definitely move up ranks wherever she goes.."
    scene bg kiadytwosalon 20 with Dissolve(0.8)
    Kiara "Um.. what do you mean?"
    "Fatguy" "Oh nothing nothing , just your sharp mind.. let's get started"
    scene bg kiadytwosalon 21 with Dissolve(0.8)
    Kiara "Alrgiht , let me just put this over-"
    scene bg kiadytwosalon 22 with Dissolve(0.8)
    Kiara "*Gasp* Ah! , oh my god!"
    "Fatguy" "What the-!"
    scene bg kiadytwosalon 23 with Dissolve(0.8)
    Kiara "I got it , I got it . I'm so sorry are you okay?"
    scene bg kiadytwosalon 24 with Dissolve(0.8)
    "Fatguy" "Ugh! , my neck!"
    scene bg kiadytwosalon 25 with Dissolve(0.8)
    Kiara "Please wait ! ub hold on"
    scene bg kiadytwosalon 26 with Dissolve(0.8)
    "Fatguy" "What the hell is this? Who keeps such a weak base chair"
    scene bg kiadytwosalon 27 with Dissolve(0.8)
    Kiara "It=It's not weak i think because this is made for women and so your weight-"
    "Fatguy" "Are you calling me fat? what-"
    Kiara "No I'm not! , m-maybe it was my fault"
    scene bg kiadytwosalon 28 with Dissolve(0.8)
    "Fatguy" "Fine you stand and i'll take you as support ok?"
    Kiara "Um alright.. i suppose that's fair"
    scene bg kiadytwosalon 29 with Dissolve(0.8)
    Kiara "( Better finish this fast or my ocd will kill me)"
    "Fatguy" "( She's very squishy hehe)"
    scene bg kiadytwosalon 30 with Dissolve(0.8)
    Kiara "( Okay .. let me just try this here..)"
    "Fatguy" "(Time to have a little fun)"
    scene bg kiadytwosalon 31 with Dissolve(0.8)
    Kiara "( Why is he squeezing my waist?.. Ugh it's not even the chair's fault he's just fat)"
    scene bg kiadytwosalon 32 with Dissolve(0.8)
    "Fatguy" "( I almost want to rip her top open and milk those babies)"
    scene bg kiadytwosalon 33 with Dissolve(0.8)
    "Fatguy" "(Let's see how she reacts..)"
    scene bg kiadytwosalon 34 with Dissolve(0.8)
    Kiara "Kya ! um sir..your head.."
    "Fatguy" "Oh sorry i was just relaxed so didn't realize"
    scene bg kiadytwosalon 35 with Dissolve(0.8)
    Kiara "( He's doing this intentionally i can tell.. i should hurry up)"
    scene bg kiadytwosalon 36 with Dissolve(0.8)
    Kiara "( Great now he's grabbing my legs.. good thing i wore pants today)"
    scene bg kiadytwosalon 37 with Dissolve(0.8)
    pause
    scene bg kiadytwosalon 38 with Dissolve(0.8)
    Kiara "( Ar-Are his ahnds going up?)"
    scene bg kiadytwosalon 39 with Dissolve(0.8)
    Kiara "( Yes they are! , Okay.. this what do i do?)"
    scene bg kiadytwosalondcdfrstaftrthirtynine with Dissolve(0.8)
    menu:
        "Stop him now (Requires Strength 2)" if mc_stats.current_strength >= 2:
            #block of code to run
            jump .part_1
        "Let him continue" if mc_stats.current_corruption > 45:
            #block of code to run
            jump .part_2

    label .part_1:
        scene kiadytwosalonbeat 1 with Dissolve(0.8)
        Kiara "Okay screw this.. I'm not letting some creep do this over his fat ass"
        scene kiadytwosalonbeat 2 with Dissolve(0.8)
        Kiara "There it is.. you're done"
        scene kiadytwosalonbeat 3 with Dissolve(0.8)
        "Fatguy" "Ah.. wh-"
        scene kiadytwosalonbeat 4 with Dissolve(0.8)
        Kiara "Move your hand you cunt"
        "Fatguy" "W-what did you sa-"
        scene kiadytwosalonbeat 5 with Dissolve(0.8)
        Kiara "I said move your disgusting hands you cunt!"
        "Fatguy" "Aaaah!"
        scene kiadytwosalonbeat 6 with Dissolve(0.8)
        Kiara "What the.. did i kick that hard?"
        "fatguy" "Ugh, my head..."
        jump chap_2_scene_33


    label .part_2:
        scene bg kiadytwosalonletgrope 1 with Dissolve(0.8)
        Kiara "Ugh.. I don't want to cause a scene on first client.. It's fine i'm sure he won't go too far"
        scene bg kiadytwosalonletgrope 2 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 3 with Dissolve(0.8)
        "Fatguy" "(Either this girl isn't realizing or she's letting me.. hehe)"
        scene bg kiadytwosalonletgrope 4 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 5 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 6 with Dissolve(0.8)
        Kiara "( What the.. his hands are on my ass?)"
        "Fatguy" "( You're mine now baby)"
        scene bg kiadytwosalonletgrope 7 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 8 with Dissolve(0.8)
        Kiara "( Just a bit longer , I can endure this)"
        scene bg kiadytwosalonletgrope 9 with Dissolve(0.8)
        "Fatguy" "( Oh you wanna act innocent huh?.. Let's see)"
        scene bg kiadytwosalonletgrope 10 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 11 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 12 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 13 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 14 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 15 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 16 with Dissolve(0.8)
        Kiara "( He-He's groping my ass! , what the hell?!)"
        scene bg kiadytwosalonletgrope 17 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 18 with Dissolve(0.8)
        "Fatguy" "You let everyone do this to you hun?"
        scene bg kiadytwosalonletgrope 19 with Dissolve(0.8)
        Kiara "No- no! , don't get the wrong idea I just don't want my first client to have a compalain on me.. could you please stop?"
        scene bg kiadytwosalonletgrope 20 with Dissolve(0.8)
        "Fatguy" "Stop?.. baby i'm gonna take advantage of this opportunity instead.."
        scene bg kiadytwosalonletgrope 21 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 22 with Dissolve(0.8)
        Kiara "Ah.. ( His hands are inside my shirt?)"
        scene bg kiadytwosalonletgrope 23 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 24 with Dissolve(0.8)
        Kiara "( M-my pants?.. what is he thinking?)"
        scene bg kiadytwosalonletgrope 25 with Dissolve(0.8)
        "Fatguy" "( Let's see this bitch's ass)"
        scene bg kiadytwosalonletgrope 26 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 27 with Dissolve(0.8)
        Kiara "( N-no! , what the.. what is he)"
        scene bg kiadytwosalonletgrope 28 with Dissolve(0.8)
        "Fatguy" "Now these panties.."
        scene bg kiadytwosalonletgrope 29 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 30 with Dissolve(0.8)
        "Fatguy" "Hehe.. soft skin"
        Kiara "(No! , I gotta stop this.. he's not)"
        scene bg kiadytwosalonletgrope 31 with Dissolve(0.8)
        "Fatguy" "( Ah it won't slide any down further cuz her ass is so big.. that's alright)"
        scene bg kiadytwosalonletgrope 32 with Dissolve(0.8)
        "Fatguy" "Hey baby.. I'm gonna finger your asshole now.. let's see how tight it is"
        Kiara "(No ! , enough of this)"
        scene bg kiadytwosalonletgrope 33 with Dissolve(0.8)
        Kiara "Move! , what the fuck are you doing!"
        scene bg kiadytwosalonletgrope 34 with Dissolve(0.8)
        pause
        scene bg kiadytwosalonletgrope 35 with Dissolve(0.8)
        "Fatguy" "Ugh.."
        Kiara "I did it.. but why did i let him go that far?.."
        $ mc_stats.adjust_corruption(5)
        jump chap_2_scene_33

label chap_2_scene_33:
    scene bg kiadytwosalon 40 with Dissolve(0.8)
    "Fatguy" "Hey! , Why did you do that what the fuck!"
    Kiara "You were fucking groping me! The hell is wrong with you?!"
    scene bg kiadaytworosermnc 1 with Dissolve(0.8)
    "Fatguy" "I was taking support , you were the one who said it!"
    Kiara "Support doesn't mean squeezng my body you twisted fuck!"
    scene bg kiadaytworosermnc 2 with Dissolve(0.8)
    Rose "What on earth is going on here ?"
    scene bg kiadaytworosermnc 3 with Dissolve(0.8)
    Kiara "R-rose , he this guy was-"
    scene bg kiadaytworosermnc 4 with Dissolve(0.8)
    "Fatguy" "I guess you're the owner , what the hell is this she just hit me!"
    Kiara "I didn't ! , you were doing it first I just-"
    scene bg kiadaytworosermnc 5 with Dissolve(0.8)
    "Fatguy" "Shut up lying bitch , you hit me i didn't do anything"
    scene bg kiadaytworosermnc 6 with Dissolve(0.8)
    "Fatguy" "Argh! , ouch!"
    Rose "Who the fuck are you calling slurs you fat pig!"
    scene bg kiadaytworosermnc 7 with Dissolve(0.8)
    Rose "Get out of my salon you fucking incel"
    "Fatguy" "Ugh.. uh , I'll get you both!"
    scene bg kiadaytworosermnc 8 with Dissolve(0.8)
    Rose "Out now or the next thing that hits your face will be my shoe!"
    scene bg kiadaytworosermnc 9 with Dissolve(0.8)
    "Fatguy" "Urgh! , Fuck this salon!"
    Rose "Screw off fat pig"
    scene bg kiadaytworosermnc 10 with Dissolve(0.8)
    Rose "Kiara?.. are you okay?"
    scene bg kiadaytworosermnc 11 with Dissolve(0.8)
    Kiara "I didn't mean to , he was groping me and i just-"
    Rose "Hey hey-!"
    scene bg kiadaytworosermnc 12 with Dissolve(0.8)
    Rose "You don't have to explain yourslef.. It's okay , please come sit"
    scene bg kiadaytworosermnc 13 with Dissolve(0.8)
    Rose "Kiara , don't look so down.. everyone's first clients can be assholes.."
    Kiara "But i really wanted to practice today.. ugh why does this happen to me"
    scene bg kiadaytworosermnc 14 with Dissolve(0.8)
    Rose "It's not your fault sweety , you did the right thing despite off hours"
    Kiara "Yeah.. but now i have to wait till next week just to start.. this sucks"
    scene bg kiadaytworosermnc 15 with Dissolve(0.8)
    Kiara "I just have terrible luck don't i?.. It just sucks"
    Rose "( I Should cheer her up)"
    scene bg kiadaytworosermnc 16 with Dissolve(0.8)
    Rose "Why don't you try on me?"
    scene bg kiadaytworosermnc 17 with Dissolve(0.8)
    Kiara "W-what? .. No I don't wanna ruin your hair"
    Rose "You won't kiara , come on let's give this a try"
    pause
    menu:
        "Um.."
        "Cut Rose's hair":
            #block of code to run
            jump .part_1
        "Suggest otherwise":
            #block of code to run
            jump .part_2

    label .part_2:
        scene bg kiadytwosalonroseno 1 with Dissolve(0.8)
        Kiara "Um.. can i do it next week? .. Please i don't want to ruin anything more today"
        Rose "Ah okay , I undertand.. I'll await you then oki?"
        scene bg kiadytwosalonroseno 2 with Dissolve(0.8)
        Kiara "Thanks for.. being kind , I need it nowadays"
        Rose "You can always have it , have a great evening okay?"
        scene bg kiadytwosalonroseno 3 with Dissolve(0.8)
        Rose "(Heh.. bit shy isn't she , that's alright we'l have plenty of time.)"
        jump chap_2_scene_34

    label .part_1:

        scene bg kiadytwosalonroseyes 1 with Dissolve(0.8)
        Kiara "Um alright , I'll do my best"
        Rose "You can go on the pace you like , Don't worry too much"
        scene bg kiadytwosalonroseyes 2 with Dissolve(0.8)
        Kiara "Are you really sure about this?.. I don't know if i-"
        Rose "I am sure , and i have faith you'll give me a better one than my current"
        scene bg kiadytwosalonroseyes 3 with Dissolve(0.8)
        Kiara "Okay let's start.. I think i have something"
        Rose "I can't wait ! , Let your hands run!"
        scene bg kiadytwosalonroseyes 4 with Dissolve(0.8)
        Kiara "You're already beautiful but i'll try"
        scene bg kiadytwosalonroseyes 5 with Dissolve(0.8)
        Rose "You cut very well by the way , I can almost sleep"
        Kiara "Kindly don't , it's almost done"
        scene bg kiadytwosalonroseyes 6 with Dissolve(0.8)
        Kiara "So.. what do you think?"
        Rose "Kiara.. I"
        scene bg kiadytwosalonroseyes 7 with Dissolve(0.8)
        Kiara "D-do you not like it? I'm sorry i , i think i just"
        Rose "No you goof , what are you saying? Like?"
        scene bg kiadytwosalonroseyes 8 with Dissolve(0.8)
        Rose "I love it!"
        Kiara "Wait , really?"
        scene bg kiadytwosalonroseyes 9 with Dissolve(0.8)
        Kiara "Um , I kinda mixed my cousin and mw own style so itd suit you well"
        scene bg kiadytwosalonroseyes 10 with Dissolve(0.8)
        Rose "Well i got the best of both worlds then , this looks exquisite"
        Kiara "Thanks rose , I'm glad you like it"
        scene bg kiadytwosalonroseyes 11 with Dissolve(0.8)
        Rose "I never thought id look good in short ones but here you are proving me wrong"
        Kiara "Well i think you look great , I mean very beautiful"
        $ rose_rom.adjust_romance(1)
        scene bg kiadytwosalonroseyes 12 with Dissolve(0.8)
        Rose "Mind if we play with your hair a bit? No cutting just some styles"
        Kiara "Oh um.. I mean-"
        menu:
            
            "Accept Rose's offer":
                #block of code to run
                jump .part_3
            "Don't":
                #block of code to run
                jump .part_4
            
        label .part_3:
            scene bg kiarmncdaytworoseyes 1 with Dissolve(0.8)
            Kiara "Um okay i have to go soon but why not"
            scene bg kiarmncdaytworoseyes 2 with Dissolve(0.8)
            Kiara "So what are we trying?"
            Rose "Let's try your hair flipped , sometimes side changes can do wonders"
            scene bg kiarmncdaytworoseyes 3 with Dissolve(0.8)
            Rose "By the way your hair is so smooth"
            Kiara "I just shampoo it daily , and i think yours is smoother"
            scene bg kiarmncdaytworoseyes 4 with Dissolve(0.8)
            Rose "See looks different but good right?"
            Kiara "Yea.. i might go for it tommorow , seems kinda cool"
            scene bg kiarmncdaytworoseyes 5 with Dissolve(0.8)
            Rose "Let's try this as well.."
            scene bg kiarmncdaytworoseyes 6 with Dissolve(0.8)
            Kiara "Wait no don't lean in!"
            Rose "Ah!"
            scene bg kiarmncdaytworoseyes 7 with Dissolve(0.8)
            Kiara "Aah.. i'm falling wa-"
            Rose "No no , wait! I got you!"
            scene bg kiarmncdaytworoseyes 8 with Dissolve(0.8)
            Rose "that was close.. sorry for that"
            Kiara "Not your fault.. I think it happens on backside pressure"
            scene bg kiarmncdaytworoseyes 9 with Dissolve(0.8)
            Kiara "I guess that guy was right about it being a little loose.."
            Rose "Heh.."
            scene bg kiarmncdaytworoseyes 10 with Dissolve(0.8)
            Rose "If what i'm seeing now is the sight that i get for having broken seats , then i'm never changing them"
            Kiara "Oh.. uhm I-"
            scene bg kiarmncdaytworoseyes 11 with Dissolve(0.8)
            Rose "Are you blushing? How cute are you gonna get?"
            Kiara "No i just.. i mean- i have to go"
            scene bg kiarmncdaytworoseyes 12 with Dissolve(0.8)
            Rose "As your boss i almost want some overtime.. but hey we got enough time.. so lets get you up"
            Kiara "(I'm looking away because her eyes are so pretty.. ah gosh)"
            scene bg kiarmncdaytworoseyes 13 with Dissolve(0.8)
            Kiara "Thanks again.. for standing up earlier for me.. I appreciate it"
            Rose "Don't be , that guy was a loser you're my new stylist hehe"
            Rose "Have a good evening okay? Laters"
            scene bg kiarmncdaytworoseyes 14 with Dissolve(0.8)
            Kiara "Bye! , see ya"
            Rose "Shy aren't you.. that's alright we'll have enough time"
            $ rose_rom.adjust_romance(1)
            jump chap_2_scene_34

        label .part_4:

            scene bg kiarmncdaytworoseno 1 with Dissolve(0.8)
            Kiara "Um , i actually need to go soon since my aunt's gonna get mad otherwise.. can we do it later?"
            Rose "Oh yeah no problem , thanks again for the haircut!"
            scene bg kiarmncdaytworoseno 2 with Dissolve(0.8)
            Kiara "Your welcome , and thanks agian for earlier.. i appreciate it"
            Rose "Dont be , I know you're amazing that fat guy can burn in fire for all i care"
            Rose "You take care okay? Have a great evening"
            scene bg kiarmncdaytworoseno 3 with Dissolve(0.8)
            Rose "A bit shy i suppose , We'll continue some other time kiara"
            jump chap_2_scene_34

label chap_2_scene_34:
    scene blackscreen
    show titletext "Side market street , Osaka.." with dissolve
    pause 1.0
    window hide
    scene bg daytwoassinscn 1 with Dissolve(0.8)
    "Fatguy" "Fuckin bitches.. next time i'll strip both of them nude"
    scene bg daytwoassinscn 2 with Dissolve(0.8)
    "???" "Psst.. come here"
    scene bg daytwoassinscn 3 with Dissolve(0.8)
    "Fatguy" "Huh?.. who?"
    scene bg daytwoassinscn 4 with Dissolve(0.8)
    AgentWong "Come over here.. I got something fun to show you"
    scene bg daytwoassinscn 5 with Dissolve(0.8)
    "Fatguy" "You gonna let me cum in your ass?"
    AgentWong "Anything you want hun.."
    scene bg daytwoassinscn 6 with Dissolve(0.8)
    "Fatguy" "Wh- hey ! what are you doing hey!"
    scene bg daytwoassinscn 7 with Dissolve(0.8)
    AgentWong "Like touching women huh? these hands.."
    "Fatguy" "Wait no , I won't ever , I'm gay uh please!"
    scene bg daytwoassinscn 8 with Dissolve(0.8)
    "fatguy" "Arrghghgh!!!  MY ARM!"
    scene bg daytwoassinscn 9 with Dissolve(0.8)
    "Fatguy" "Someone! , Someone help!"
    scene bg daytwoassinscn 10 with Dissolve(0.8)
    AgentWong "Nuh uh .. you aren't going anywhere.."
    "Fatguy" "Wait , WAit! , please stop !"
    scene bg daytwoassinscn 11 with Dissolve(0.8)
    AgentWong "Quiet.. , shhh"
    "fatguy" "MMMMPGH , HE... MMPPH!"
    scene bg daytwoassinscn 12 with Dissolve(0.8)
    AgentWong "I said... quiet!"
    "Fatguy" "Ulgh!..."
    scene bg daytwoassinscn 13 with Dissolve(0.8)
    AgentWong "Would've left at a broken arm and a leg but he had to shout didn't he.."
    scene bg daytwoassinscn 14 with Dissolve(0.8)
    AgentWong "Whatever.. One less filth from this planet"
    scene bg daytwoassinscn 15 with Dissolve(0.8)
    pause
    scene bg daytwoassinscn 16 with Dissolve(0.8)
    AgentWong "(Now for that cab driver.. , Let's see who you are)"
    jump chap_2_scene_35

label chap_2_scene_35:
    scene bg daytwoygajoinin 1 with Dissolve(0.8)
    Kiara "After this we can go home , I hope you're not tired"
    Keisuke "Not at all , also yoga club is a great idea"
    scene bg daytwoygajoinin 2 with Dissolve(0.8)
    Kiara "By the way are you free tommorow ? I wanted to explore the city abit and who better than you"
    Keisuke "Heh , sure why not I'll show you some nice places too"
    scene bg daytwoygajoinin 3 with Dissolve(0.8)
    Keisuke "( Hm?.. Ayane's phone?)"
    scene bg daytwoygajoinin 4 with Dissolve(0.8)
    pause
    scene bg daytwoygajoinin 5 with Dissolve(0.8)
    Keisuke "( Why could she be calling ?)"
    scene bg daytwoygajoinin 6 with Dissolve(0.8)
    Keisuke "( Another one?.. ah i can't attend it now.)"
    scene bg daytwoygajoinin 7 with Dissolve(0.8)
    pause
    scene bg daytwoygajoinin 8 with Dissolve(0.8)
    Kiara "Who is it?.. do you need to talk to someone but can't because of privacy?"
    scene bg daytwoygajoinin 9 with Dissolve(0.8)
    Keisuke "No no , It's just my little sister , I kinda promised her a gift and i'm kinda short on money right now"
    scene bg daytwoygajoinin 10 with Dissolve(0.8)
    Kiara "Um.. how short? what was the gift?"
    Keisuke "It's just a teddy bear that has her name in it , but don't worry i'll handle it"
    scene bg daytwoygajoinin 11 with Dissolve(0.8)
    Keisuke "She'll be a little angry by a day delay but it's alright haha , I can manage it"
    scene bg daytwoygajoinin 12 with Dissolve(0.8)
    Kiara "( Hm..) Alright i understand"
    scene blackscreen
    show titletext "Value self yoga , Home street" with dissolve
    pause 1.0
    window hide
    scene bg daytwoygajoinin 13 with Dissolve(0.8)
    Kiara "Alright the last stop , I got this"
    scene bg daytwoygajoinin 14 with Dissolve(0.8)
    Kiara "This place is close too , just what i needed"
    scene bg daytwoygajoinin 15 with Dissolve(0.8)
    Kiara "Excuse me , I'd like to register for a membership"
    scene bg daytwoygajoinin 16 with Dissolve(0.8)
    "Reception girl" "Of course, Please provide us an ID and documentation"
    scene bg daytwoygajoinin 17 with Dissolve(0.8)
    "Reception girl" "While i submit everything , my collegue here will guide you to the instructor rooms"
    scene bg daytwoygajoinin 18 with Dissolve(0.8)
    Kiara "Alright sure , Lets get going"
    "Reception guy" "Certainly , please follow me"
    scene bg daytwoygajoinin 19 with Dissolve(0.8)
    "Reception guy" "We are one of the safest and most hygenic centers in osaka , Quality will to be your liking"
    Kiara "Thanks , I have OCD so trust me that is a relief"
    scene bg daytwoygajoinin 20 with Dissolve(0.8)
    "Reception guy" "Understandable , please go left from here and on the straight path you shall find the room with your trainer"
    Kiara "Alright thank you again"
    scene bg daytwoygajoinin 21 with Dissolve(0.8)
    Kiara "From here to left corridor , okay so that one"
    scene bg daytwoygajoinin 22 with Dissolve(0.8)
    pause
    scene bg daytwoygajoinin 23 with Dissolve(0.8)
    Kiara "Wow , talk about a palette change , at least it's better than yamazaki's office"
    scene bg daytwoygajoinin 24 with Dissolve(0.8)
    pause
    scene bg daytwoygajoinin 25 with Dissolve(0.8)
    Kiara "I suppose this room is for the guys , so the one next to it is my side"
    scene bg daytwoygajoinin 26 with Dissolve(0.8)
    "???" "Keep stretching! , You got this , try to maintain balance"
    scene bg daytwoygajoinin 27 with Dissolve(0.8)
    Kiara "(Oh wow , they are fit alright)"
    scene bg daytwoygajoinin 28 with Dissolve(0.8)
    "???" "(Well well , new yoga mate it seems)"
    scene bg daytwoygajoinin 29 with Dissolve(0.8)
    "???" "Oh my , quite easy on the eyes"
    scene bg daytwoygajoinin 30 with Dissolve(0.8)
    "???" "Hmm.. that face and that body"
    scene bg daytwoygajoinin 31 with Dissolve(0.8)
    "???" "I definitely wouldn't mind sharing a shower"
    scene bg daytwoygajoinin 32 with Dissolve(0.8)
    "???" "What are you all distracted by? Hello?"
    "???" "Look behind you saya , we've got a new guest"
    scene bg daytwoygajoinin 33 with Dissolve(0.8)
    Saya "New guest? Who are you refe-"
    scene bg daytwoygajoinin 34 with Dissolve(0.8)
    Saya "Oh , hello there! sorry we were just focused so didn't notice you"
    Kiara "I apologize , I'm new so thought i'd just meet everyone"
    scene bg daytwoygajoinin 35 with Dissolve(0.8)
    Kiara "Hi to all , I'm kiara , Um I kind of want to get into a toned physique so thought i'd go for this"
    Saya "You're definitely at the right place , We can certainly get you to it"
    scene bg daytwoygajoinin 36 with Dissolve(0.8)
    Kiara "Could you please introduce others? .. I kind of feel odd now"
    Saya "Oh! sorry , Um I am saya  , the trainer as you can see"
    scene bg daytwoygajoinin 37 with Dissolve(0.8)
    Saya "Behind me are , Jinshi and alicia"
    Alicia "Hello!"
    Jinshi "Hey cutie"
    scene bg daytwoygajoinin 38 with Dissolve(0.8)
    Saya "The lady in gray is-"
    Olivia "Olivia , nice to meet you kiara"
    scene bg daytwoygajoinin 39 with Dissolve(0.8)
    Saya "There we go , now how do you want to get started?"
    Kiara "Well I'd like to get an outfit firstly , am i allowed to bring mine or?"
    scene bg daytwoygajoinin 40 with Dissolve(0.8)
    Saya "Actually we'd recommend the ones we use , since they're all elastic but you can bring yours too"
    scene bg daytwoygajoinin 41 with Dissolve(0.8)
    Kiara "But in case you do want to pick ours , just go with any of the girls and they'll get you your gear"
    scene bg kiadaytwoygadcd with Dissolve(0.8)
    Kiara "Um well i prefer to-"
    menu:
        
        "Go with saya":
            #block of code to run
            jump .part_1
        "Go with Alicia and jinshi" if mc_stats.current_corruption >= 45:
            #block of code to run
            jump .part_2
        "Go with Olivia" if mc_stats.current_corruption >= 50:
            jump .part_3

    label .part_1:
        scene bg dytwoyogasaya 1 with Dissolve(0.8)
        Kiara "Actually i like your outfit alot , can i please go for that one?"
        scene bg dytwoyogasaya 2 with Dissolve(0.8)
        Saya "S-sure! , please come with me we'll get it sorted for you"
        scene bg dytwoyogasaya 3 with Dissolve(0.8)
        Kiara "Is this area usually empty?"
        Saya "Mostly yes , it's staff only but i'm bringing you here since i didn't want you to change in the stalls"
        scene bg dytwoyogasaya 4 with Dissolve(0.8)
        Kiara "Well thank you , I appreciate that alot actually"
        Saya "Don't mention it , It's something i know is comfortable anyway so"
        scene bg dytwoyogasaya 5 with Dissolve(0.8)
        Kiara "Wow this is fancy"
        Saya "Yeah it's very nice and we have temperature control here so it's never bad regardless of season"
        scene bg dytwoyogasaya 6 with Dissolve(0.8)
        Saya "Anyway though you go ahead and take a shower , your clothes are on the left isle on there"
        Kiara "Alright um can i ask for a favor?"
        scene bg dytwoyogasaya 7 with Dissolve(0.8)
        Saya "Sure , what is it?"
        Kiara "Could you please wait outside or watch over so no one comes?"
        scene bg dytwoyogasaya 8 with Dissolve(0.8)
        Saya "Oh yeah no problem , I can do that feel free"
        Kiara "Thank you"
        scene bg dytwoyogasaya 9 with Dissolve(0.8)
        pause
        scene bg dytwoyogasaya 10 with Dissolve(0.8)
        Saya "She's very beautiful , hope the other girls treat her well"
        scene bg dytwoyogasaya 11 with Dissolve(0.8)
        pause
        scene bg dytwoyogasaya 12 with Dissolve(0.8)
        Kiara "This water is almost as clean as home , quite surprising for a public one"
        scene bg dytwoyogasaya 13 with Dissolve(0.8)
        Kiara "Hey , I'm ready"
        Saya "Let's take a look"
        scene bg dytwoyogasaya 14 with Dissolve(0.8)
        Saya "Well look at that , we vibe check pretty nicely"
        scene bg dytwoyogasaya 15 with Dissolve(0.8)
        Kiara "What are those!"
        Saya "Haha , well do you like it?"
        scene bg dytwoyogasaya 16 with Dissolve(0.8)
        Kiara "It's very comfortable , thank you for this"
        Saya "Well let's get going then"
        scene bg dytwoyogasaya 17 with Dissolve(0.8)
        Saya "Now we just need to do small dips and you can go then"
        Kiara "Alright sure!"
        scene bg dytwoyogasaya 18 with Dissolve(0.8)
        Saya "By the way , this suits you better than it does me"
        Kiara "Not really true , i picked it after looking at you in it haha"
        jump chap_2_scene_36

    label .part_2:
        scene bg dytwoygaaliciandjinshi 1 with Dissolve(0.8)
        Kiara "Um Alicia's outfit seems nice , Jinshi too.. could you guys get me one of a different color?"
        scene bg dytwoygaaliciandjinshi 2 with Dissolve(0.8)
        Jinshi "Sure the lockers have all schemes , but you'd have to come with us"
        Alicia "Are you comfortable with that?"
        Kiara "Of course , let's go"
        scene bg dytwoygaaliciandjinshi 3 with Dissolve(0.8)
        pause
        scene bg dytwoygaaliciandjinshi 4 with Dissolve(0.8)
        Jinshi "So you wanted red and black right?"
        Kiara "Yes , they're my favorite colors"
        Alicia "Good choice kiara , it'll suit your skin alot"
        scene bg dytwoygaaliciandjinshi 5 with Dissolve(0.8)
        pause
        scene bg dytwoygaaliciandjinshi 6 with Dissolve(0.8)
        Kiara "Um.. why are we in the showers?"
        Jinshi "Oh shower time is for us , you just need to grab it from the lockers"
        scene bg dytwoygaaliciandjinshi 7 with Dissolve(0.8)
        Kiara "Oh.. I thought you'd ask me to shower with-"
        scene bg dytwoygaaliciandjinshi 8 with Dissolve(0.8)
        Alicia "Do you want to?"
        Jinshi "I certainly won't complain about it"
        scene bg dytwoygaaliciandjinshi 9 with Dissolve(0.8)
        Kiara "Uhm no i meant like , I thought you guys wanted me to do it"
        scene bg dytwoygaaliciandjinshi 10 with Dissolve(0.8)
        Jinshi "So if we wanted you to do it , you'd get here with us?"
        Kiara "Um.."
        Alicia "Well kiara?.."
        scene bg dytwoygaaliciandjinshi 11 with Dissolve(0.8)
        Alicia "Does that make you comfortable?"
        Jinshi "I think she needs more motivation"
        Kiara "Um guys.. I-"
        scene bg dytwoygaaliciandjinshi 12 with Dissolve(0.8)
        Jinshi "You're bisexual?"
        Kiara "How did you?-.."
        Alicia "Oh cmon kiara , i caught you staring at my ass hehe"
        scene bg dytwoygaaliciandjinshi 13 with Dissolve(0.8)
        Kiara "Uhm.. it's jsut because you have a toned body so i just-"
        scene bg dytwoygaaliciandjinshi 14 with Dissolve(0.8)
        Alicia "No need to justify sweetheart , we're staring at you too aren't we?"
        Jinshi "Yeah ask her , my nipples are hard too.."
        Kiara "( What the hell , am i dreaming or something)"
        scene bg dytwoygaaliciandjinshi 15 with Dissolve(0.8)
        Alicia "You wanna squeeze em? they're super soft"
        Jinshi "I bet her's are softer"
        scene bg dytwoygaaliciandjinshi 16 with Dissolve(0.8)
        Alicia "Do you wanna perhaps skip the formality?.."
        Kiara "Is she... uh"
        scene bg dytwoygaaliciandjinshi 17 with Dissolve(0.8)
        pause
        scene bg dytwoygaaliciandjinshi 18 with Dissolve(0.8)
        Kiara "I , I don't know what to-"
        Alicia "You're still staring by the way hehe"
        scene bg dytwoygaaliciandjinshi 19 with Dissolve(0.8)
        Jinshi "Just give her the full show"
        Kiara "Oh my god.."
        scene bg dytwoygaaliciandjinshi 20 with Dissolve(0.8)
        Alicia "Cmon Kiara , a little shower never hurt anybody"
        scene bg dytwoygaaliciandjinshi 21 with Dissolve(0.8)
        Kiara "No um i'm good you guys.. carry on.. (What the fuck.. i couldn't take my eyes off of them)"
        scene bg dytwoygaaliciandjinshi 22 with Dissolve(0.8)
        Kiara "Okay it's fine.. maybe open relationships are this way whatever"
        scene bg dytwoygaaliciandjinshi 23 with Dissolve(0.8)
        Kiara "Hm.. I see the red and black , is this it?"
        scene bg dytwoygaaliciandjinshi 24 with Dissolve(0.8)
        pause
        scene bg dytwoygaaliciandjinshi 25 with Dissolve(0.8)
        Kiara "It's a bit tight"
        scene bg dytwoygaaliciandjinshi 26 with Dissolve(0.8)
        pause
        scene bg dytwoygaaliciandjinshi 27 with Dissolve(0.8)
        Kiara "But i definitely love it , plus the sleeves are great too why weren't they wearing them?"
        scene bg dytwoygaaliciandjinshi 28 with Dissolve(0.8)
        Kiara "I guess i'll just say bye and leave.."
        scene bg dytwoygaaliciandjinshi 29 with Dissolve(0.8)
        pause
        scene bg dytwoygaaliciandjinshi 30 with Dissolve(0.8)
        Kiara "Oh my-.."
        scene bg dytwoygaaliciandjinshi 31 with Dissolve(0.8)
        Kiara "This can't be happening for real"
        scene bg dytwoygaaliciandjinshi 32 with Dissolve(0.8)
        Jinshi "You saw her right? I bet she's yummy"
        Alicia "I think we should go a little slow for starters"
        scene bg dytwoygaaliciandjinshi 33 with Dissolve(0.8)
        Jinshi "Bit late for that don't you think"
        Alicia "Well she seems shy but i think she's secretly way hornier than even me"
        scene bg dytwoygaaliciandjinshi 34 with Dissolve(0.8)
        Jinshi "If she is then i'm definitely not letting a single drop of her pussy go to waste"
        Alicia "Oh yeah , you wanna just keep her naked don't you?"
        scene bg dytwoygaaliciandjinshi 35 with Dissolve(0.8)
        Jinshi "Hehe , how can you tell?"
        Alicia "Your dripping cunt kinda is like a open book right now"
        scene bg dytwoygaaliciandjinshi 36 with Dissolve(0.8)
        Jinshi "I think she'd love your chocolaty body too"
        Alicia "Maybe so , some white ones do like some brown"
        scene bg dytwoygaaliciandjinshi 37 with Dissolve(0.8)
        Jinshi "Gimme those lips , I am hella horny now"
        Jinshi "Sure but one thing before that.."
        scene bg dytwoygaaliciandjinshi 38 with Dissolve(0.8)
        Alicia "You know staring at us makes you the pervert babe?"
        Jinshi "Why stare when you can join love?"
        scene bg dytwoygaaliciandjinshi 39 with Dissolve(0.8)
        Jinshi "I promise i'll make you squirt"
        Alicia "Jinshii i said slowww"
        scene bg dytwoygaaliciandjinshi 40 with Dissolve(0.8)
        Kiara " I- uh ,  no i was just- I gotta go!"
        Alicia "Hey wait! haha"
        scene bg dytwoygaaliciandjinshi 41 with Dissolve(0.8)
        Kiara "No , no!  I'm sorry i wasn't in the best state of mind sorry guys!"
        scene bg dytwoygaaliciandjinshi 42 with Dissolve(0.8)
        Kiara "Best state of mind?.. I was totally staring at them agh"
        $ mc_stats.adjust_corruption(5)
        jump chap_2_scene_36

    label .part_3:
    
        scene bg dayywoygaolivia 1 with Dissolve(0.8)
        Kiara "I like olivia's , do you mind helping me get it?"
        scene bg dayywoygaolivia 2 with Dissolve(0.8)
        Olivia "Not at all , come along"
        scene bg dayywoygaolivia 3 with Dissolve(0.8)
        Kiara "So this area is seperate from the main one?"
        Olivia "It's a female only one , the other one is mixed"
        scene bg dayywoygaolivia 4 with Dissolve(0.8)
        Kiara "I Like your hair by the way , not many can nail the bobby classic style"
        Olivia "Thanks , I've been trying way too many and finally settled with this"
        scene bg dayywoygaolivia 5 with Dissolve(0.8)
        Kiara "How long have you been here by the way? , I mean japan"
        Olivia "Roughly 3 years , I go back home occassionaly though"
        scene bg dayywoygaolivia 6 with Dissolve(0.8)
        Olivia "We've reached!"
        Kiara "Um-.. this is open?"
        scene bg dayywoygaolivia 7 with Dissolve(0.8)
        Kiara "I thouught we'd have privacy or individual slots"
        Olivia "It's just female only , why privacy then?"
        scene bg dayywoygaolivia 8 with Dissolve(0.8)
        Kiara "Uh , I don't wanna make this weird but actually I'm bi-sexual so.."
        Olivia "Oh , I understand well um you go ahead and shower and i'll keep an eye out"
        scene bg dayywoygaolivia 9 with Dissolve(0.8)
        Kiara "Alright thanks , I'll get started then"
        Olivia "No worries , I'll go get your gear"
        scene bg dayywoygaolivia 10 with Dissolve(0.8)
        Olivia "Bi-sexual huh.. , I wonder if she's a wild or a soft one"
        scene bg dayywoygaolivia 11 with Dissolve(0.8)
        Olivia "Although she seemed uncomfortable , I think there's a side in her inside that wants to get out"
        scene bg dayywoygaolivia 12 with Dissolve(0.8)
        Olivia "Maybe I should intiate to see her response"
        scene bg dayywoygaolivia 13 with Dissolve(0.8)
        pause
        scene bg dayywoygaolivia 14 with Dissolve(0.8)
        Olivia "I'll place these here i suppose"
        scene bg dayywoygaolivia 15 with Dissolve(0.8)
        Olivia "Kiara I've put your clothes here!"
        scene bg dayywoygaolivia 16 with Dissolve(0.8)
        Kiara "Okay! , I'll get out soon just give me few minutes"
        scene bg dayywoygaolivia 17 with Dissolve(0.8)
        pause
        scene bg dayywoygaolivia 18 with Dissolve(0.8)
        Kiara "Hmm.. cold water can be nice after workout too"
        scene bg dayywoygaolivia 19 with Dissolve(0.8)
        pause
        scene bg dayywoygaolivia 20 with Dissolve(0.8)
        Olivia "Heh even through the glass , i can tell she's a lovely sight to look at"
        scene bg dayywoygaolivia 21 with Dissolve(0.8)
        Olivia "Why is she wearing a bra though?.. She should be comfortbale here"
        scene bg dayywoygaolivia 22 with Dissolve(0.8)
        Olivia "Hmm.. Maybe she-"
        scene bg dayywoygaolivia 23 with Dissolve(0.8)
        Olivia "Maybe i can help her open up.."
        scene bg dayywoygaolivia 24 with Dissolve(0.8)
        Kiara "I should come here in evening only , don't want to share the shower with too many people"
        scene bg dayywoygaolivia 25 with Dissolve(0.8)
        Olivia "Yeah you should , so only you and me can have this time"
        scene bg dayywoygaolivia 26 with Dissolve(0.8)
        Kiara "Uh.. um olivia , I was just getting out actually ."
        Olivia "Oh no i got in here to have you stay a bit longer actually"
        scene bg dayywoygaolivia 27 with Dissolve(0.8)
        Kiara "Um i don't really get what you mea-"
        Olivia "Kiara , the reason you're afraid of girls in company isn't if someone sees you"
        scene bg dayywoygaolivia 28 with Dissolve(0.8)
        Olivia "It's so if someone discovers a hidden side of you"
        Kiara "I um , well I'm just a bit shy.. is that wrong?"
        scene bg dayywoygaolivia 29 with Dissolve(0.8)
        Olivia "Shy? Or secretly explorative?"
        Kiara "Um olivia I-"
        scene bg dayywoygaolivia 30 with Dissolve(0.8)
        Kiara "Ah.. what are you doing"
        Olivia "You'd have stopped me if you wanted to kiara"
        scene bg dayywoygaolivia 31 with Dissolve(0.8)
        Olivia "You're fit enough already , joining yoga is just an excuse to have a little appreciation from others isn't it?"
        Kiara "I guess so but .. not this kind , I mean-"
        scene bg dayywoygaolivia 32 with Dissolve(0.8)
        Olivia "Then this kind?.. do you enjoy our bodies colliding together in this shower?"
        Kiara "I think , i don't know how to - it's just so sudden"
        scene bg dayywoygaolivia 33 with Dissolve(0.8)
        Olivia "Just let it happen.. you and i both want it"
        Kiara "But i can't get into relationships olivia.. not this way"
        scene bg dayywoygaolivia 34 with Dissolve(0.8)
        Olivia "Who said anything about relationships? Me and you can just explore.. that's what you want right"
        Kiara "Explore?.. what do you mean?"
        scene bg dayywoygaolivia 35 with Dissolve(0.8)
        Olivia "No strings attached , we can just workout and have fun here"
        Kiara "Do- do you mean friends with beneifits?"
        scene bg dayywoygaolivia 36 with Dissolve(0.8)
        Olivia "Exactly , No one else has to know really . It'll just be the two of us"
        Kiara "Um , I've never done it.. I just don't know if you'd"
        scene bg dayywoygaolivia 37 with Dissolve(0.8)
        Olivia "Just tell me.. do you want it?"
        Kiara "Um , Abit but nothing extreme"
        scene bg dayywoygaolivia 38 with Dissolve(0.8)
        Olivia "Ligthen up kiara , It's just a bit of fun"
        Kiara "So.. what do you want me to do?"
        Olivia "I want you to stop worrying and just grab this.."
        scene bg dayywoygaolivia 39 with Dissolve(0.8)
        Kiara "Ah.. what is-"
        Olivia "Do you like it?"
        scene bg dayywoygaolivia 40 with Dissolve(0.8)
        Kiara "Yeah , I'ts actually very soft.."
        Olivia "Well go on grab em both love"
        scene bg dayywoygaolivia 41 with Dissolve(0.8)
        Kiara "( She has very nice breasts , I really want to just)"
        Olivia "Your hands are very soft by the way , I like them too"
        scene bg dayywoygaolivia 42 with Dissolve(0.8)
        Kiara "Can i squeeze them?.. abit?"
        Olivia "They're all yours , feel free sweetheart"
        scene bg dayywoygaolivia 43 with Dissolve(0.8)
        pause
        scene bg dayywoygaolivia 44 with Dissolve(0.8)
        Kiara "Wow , they fit so firmly in my palms"
        Olivia "I guess you should be my bra then hehe"
        scene bg dayywoygaolivia 45 with Dissolve(0.8)
        Kiara "Hehe , Um wow.. what is this feeling"
        Olivia "It's what you've been supressing , worried about judgements"
        scene bg dayywoygaolivia 46 with Dissolve(0.8)
        Olivia "I won't judge you , like i said only between us"
        Kiara "Yeah , only between us.. god these are so nice to grasp"
        scene bg dayywoygaolivia 47 with Dissolve(0.8)
        Olivia "You really are a cutie , let's move abit further shall we"
        Kiara "Um further?"
        scene bg dayywoygaolivia 48 with Dissolve(0.8)
        Olivia "Let me make you feel good too"
        Kiara "Ah!.. I um-"
        scene bg dayywoygaolivia 49 with Dissolve(0.8)
        Olivia "That's alright , I can use my leg too"
        Kiara "I really have never expirienced this feeling before"
        scene bg dayywoygaolivia 50 with Dissolve(0.8)
        Olivia "How about now?"
        Kiara "I-.. i really want this"
        scene bg dayywoygaolivia 51 with Dissolve(0.8)
        Olivia "I know you do love"
        scene bg dayywoygaolivia 52 with Dissolve(0.8)
        Olivia "I do too , just hadn't found the right one yet"
        scene bg dayywoygaolivia 53 with Dissolve(0.8)
        Olivia "Let's get these off.. i want to feel your skin"
        Kiara "( Wow I've always wanted someone dominating she's so good at this)"
        scene bg dayywoygaolivia 54 with Dissolve(0.8)
        pause
        scene bg dayywoygaolivia 55 with Dissolve(0.8)
        Olivia "Much better now heh , how do you feel?"
        Kiara "I feel.. free"
        scene bg dayywoygaolivia 56 with Dissolve(0.8)
        Kiara "Um.. wait i'ma  bit sensitive there please"
        Olivia "Don't worry i won't touch there yet , I just want you to be comfortable first"
        scene bg dayywoygaolivia 57 with Dissolve(0.8)
        Olivia "What i'm interested in first is that pretty face of yours"
        Kiara "You - You're pretty too"
        scene bg dayywoygaolivia 58 with Dissolve(0.8)
        Kiara "I'm claiming you here , let me taste your body a little"
        Kiara "Ha.. this feels so good"
        scene bg dayywoygaolivia 59 with Dissolve(0.8)
        Olivia "It does , your body is just perfect you know that?"
        Kiara "Thanks , you're lovely to look at too"
        scene bg dayywoygaolivia 60 with Dissolve(0.8)
        Olivia "Feel the wartmh between our legs kiara , despite the cold water it's obvious"
        Kiara "I feel it.. I want this"
        scene bg dayywoygaolivia 61 with Dissolve(0.8)
        Kiara "No strings attached , just exploring.."
        Olivia "That's right , no judgements.. just some fun"
        scene bg dayywoygaolivia 62 with Dissolve(0.8)
        Olivia "Give me those lips now.."
        Kiara "Um.."
        scene bg dayywoygaolivia 63 with Dissolve(0.8)
        Kiara "Olivia , please wait.."
        scene bg dayywoygaolivia 64 with Dissolve(0.8)
        Kiara "I can't , I'can't do a kiss.. sorry"
        scene bg dayywoygaolivia 65 with Dissolve(0.8)
        Olivia "Why so? , what's wrong?"
        scene bg dayywoygaolivia 66 with Dissolve(0.8)
        Kiara "I'm sorry , i love this but i really don't want to share a kiss with someone i don't love.. Please"
        Olivia "Heh you're one funny girl , gonna let me take your panties off but not kiss you"
        scene bg dayywoygaolivia 67 with Dissolve(0.8)
        Kiara "I know.. I'm sorry it's just personal"
        Olivia "Hey no worries , I got plenty of other places to appreciate.. besides we can take it step by step"
        scene bg dayywoygaolivia 68 with Dissolve(0.8)
        Kiara "You're okay with this then?.. I'd love to explore a little butt i am afraid of others"
        Olivia "You can trust me , like i said before really . No strings , just abit of fun"
        scene blackscreen
        show titletext "Few minutes later.. , Changing rooms" with dissolve
        pause 1.0
        window hide
        scene bg dayywoygaolivia 69 with Dissolve(0.8)
        $ mc_stats.adjust_corruption(5)
        Olivia "So what do you think?"
        Kiara "It looks great, although after what we did i doubt i care about clothes much"
        scene bg dayywoygaolivia 70 with Dissolve(0.8)
        Kiara "Though , I do like it. I think the colors are perfect"
        scene bg dayywoygaolivia 71 with Dissolve(0.8)
        Olivia "You look good with or without , hehe so don't worry everything suits you"
        Kiara "Heh , i guess you're right about that"
        scene bg dayywoygaolivia 72 with Dissolve(0.8)
        Olivia "There we go , finally confident in your sexuality a little"
        Kiara "Helps when someone so exquisite is complimenting it"
        scene bg dayywoygaolivia 73 with Dissolve(0.8)
        Olivia "Well get used ot it , anyway shall we go then?"
        Kiara "Yeah , let's get going"
        jump chap_2_scene_36

label chap_2_scene_36:
    scene blackscreen
    show titletext "Outside yoga center, late evening.." with dissolve
    pause 1.0
    window hide
    scene bg daytwohedinhome 1 with Dissolve(0.8)
    Keisuke "( She didn't pick up , I wonder what it was?)"
    scene bg daytwohedinhome 2 with Dissolve(0.8)
    Keisuke "(I can't hide this forever from her , I should just tell her)"
    Kiara "Hey! I'm back!"
    scene bg daytwohedinhome 3 with Dissolve(0.8)
    Keisuke "Come on in! , Let's head home"
    scene bg daytwohedinhome 4 with Dissolve(0.8)
    Kiara "I guess we'll reach abit late still , I'm sorrya gain"
    Keisuke "Don't worry , at least all of it got done relatively quickly"
    scene bg daytwohedinhome 5 with Dissolve(0.8)
    Kiara "Let's head home!"
    Keisuke "Off we go!"
    scene bg daytwohedinhome 6 with Dissolve(0.8)
    Kiara "I made new friends today too"
    Keisuke "That's great , the more the better when you're new here"
    scene bg daytwohedinhome 7 with Dissolve(0.8)
    Keisuke "Here we are , message me tommorow when you want to go okay?"
    Kiara "I will , but i do have something to tell you hold on"
    scene bg daytwohedinhome 8 with Dissolve(0.8)
    Kiara "So before i do , I want you to close your eyes"
    Keisuke "Close my eyes?.. why?"
    scene bg daytwohedinhome 9 with Dissolve(0.8)
    Kiara "Please? , It'll be quick i promise"
    Keisuke "But , alright sure let's see what you have"
    scene bg daytwohedinhome 10 with Dissolve(0.8)
    pause
    scene bg daytwohedinhome 11 with Dissolve(0.8)
    Kiara "Here you go.."
    Keisuke "Hm?.."
    scene bg daytwohedinhome 12 with Dissolve(0.8)
    Keisuke "W-what is this?"
    Kiara "I sold my pendent that my dad got me  , this is 1000$ , I hope you can buy that teddy now"
    scene bg daytwohedinhome 13 with Dissolve(0.8)
    Keisuke "Kiara , I - I can't take this no-"
    Kiara "You can and you will , It's your little sister cmon treat her better and make her happy"
    scene bg daytwohedinhome 14 with Dissolve(0.8)
    Kiara "Oh also I'd lvoe to meet her if you don't mind"
    Keisuke "No- not at all.. I'll get you to meet her soon"
    scene bg daytwohedinhome 15 with Dissolve(0.8)
    Kiara "Thanks! , Let me know how she reacted to it okay?"
    Keisuke "I will.."
    scene bg daytwohedinhome 16 with Dissolve(0.8)
    Kiara "Bye! , goodnight keisuke!"
    Keisuke "Goodnight.. sleep well"
    scene bg daytwohedinhome 17 with Dissolve(0.8)
    Keisuke "Did she just-.."
    scene bg daytwohedinhome 18 with Dissolve(0.8)
    Keisuke "( She just proved everything i've ever thought of her as)"
    scene bg daytwohedinhome 19 with Dissolve(0.8)
    Keisuke "I don't deserve you kiara .. I don't"
    scene bg daytwohedinhome 20 with Dissolve(0.8)
    Keisuke "She just did that selflessly , and for who? someone that she thinks is a taxi driver?"
    scene bg daytwohedinhome 21 with Dissolve(0.8)
    Keisuke "Kiara , I will be good enough one day.. maybe not as much as you deserve but i'll try my best"
    scene bg daytwohedinhome 22 with Dissolve(0.8)
    Kiara "Everyone , I'm home!"
    scene bg daytwohedinhome 23 with Dissolve(0.8)
    Natsuko "Kiara! .. I'm coming"
    scene bg daytwohedinhome 24 with Dissolve(0.8)
    Xia "Kiara.. i should go"
    scene bg daytwohedinhome 25 with Dissolve(0.8)
    pause
    scene bg daytwohedinhome 26 with Dissolve(0.8)
    Kiara "Grandfather , I am doing my best don't you worry"
    scene bg daytwohedinhome 27 with Dissolve(0.8)
    pause
    scene bg daytwohedinhome 28 with Dissolve(0.8)
    Kiara "Ah! .. natsu?"
    Natsuko "I'm so glad you're back.."
    scene bg daytwohedinhome 29 with Dissolve(0.8)
    Kiara "I was only gone for 6 hours silly , what's wrong"
    scene bg daytwohedinhome 30 with Dissolve(0.8)
    Natsuko "Nothing is wrong , I just missed you.. 6 hours without you is still 6 hours alone"
    Kiara "Well I'm here now , so don't worry"
    scene bg daytwohedinhome 31 with Dissolve(0.8)
    Xia "I agree with her , home without you in it now feels a little empty"
    scene bg daytwohedinhome 32 with Dissolve(0.8)
    Kiara "Thank you auntie , I feel way more home here than i ever did back in NY"
    Xia "Glad to hear that , your food is ready by the way"
    scene bg daytwohedinhome 33 with Dissolve(0.8)
    Kiara "Could you please send it to natsuko's room? I need to just start a stream and login for work"
    Natsuko "Do you need any help?"
    scene bg daytwohedinhome 34 with Dissolve(0.8)
    Kiara "No  , I'll be fine don't worry you guys have dinner okay"
    Natsuko "Alright i'll send it along with nobi"
    scene bg daytwohedinhome 35 with Dissolve(0.8)
    pause
    scene bg daytwohedinhome 36 with Dissolve(0.8)
    Natsuko "When do we tell her?"
    Xia "Not yet, let her relax for a week.. then we can try to"
    jump chap_2_scene_37

label chap_2_scene_37:
    scene blackscreen
    show titletext "Hotel room , Osaka central.." with dissolve
    pause 1.0
    window hide
    scene bg daytwodmianscn 1 with Dissolve(0.8)
    Lana "Thank you so much for helping with the bags damian"
    scene bg daytwodmianscn 2 with Dissolve(0.8)
    Damian "Don't mention it , It was the least i could do for you improving my hair haha"
    Lana "It looks great on you trust me , Let it dry for a bit"
    scene bg daytwodmianscn 3 with Dissolve(0.8)
    pause
    scene bg daytwodmianscn 4 with Dissolve(0.8)
    pause
    scene bg daytwodmianscn 5 with Dissolve(0.8)
    Rin "That was fun , you going tommorow too right?"
    scene bg daytwodmianscn 6 with Dissolve(0.8)
    Lana "Yeah but that'll just be me , need to meet my mom's friends here actually"
    scene bg daytwodmianscn 7 with Dissolve(0.8)
    Rin "You're gonna go meet some boomers while a cutie like this is in your hotel room?"
    Lana "There you go again.. can you not?"
    Rin "Speaking of bags , hey damain i wouldn't mind you unpacking me"
    scene bg daytwodmianscn 8 with Dissolve(0.8)
    Damian "Um.."
    Lana "Rin! , stop that!"
    scene bg daytwodmianscn 9 with Dissolve(0.8)
    Rin "I'm just saying what i feel , I would love to sit on his face if he let me"
    Damian "Christ you really are something"
    Lana "Rin stop! do you want him out of here or something?"
    scene bg daytwodmianscn 10 with Dissolve(0.8)
    Rin "I don't! , Rather the opposite actually since I want him in me"
    Lana "Okay enough of that , you go shower and take care of your mood there"
    scene bg daytwodmianscn 11 with Dissolve(0.8)
    Rin "By the way i'm keeping the shower door open , if any of you feel like coming in feel free"
    scene bg daytwodmianscn 12 with Dissolve(0.8)
    Damian "Your friend really just says what's in her mind doesn't she , quite direct"
    Lana "She's.. yeah one of a kind, anyway come let's chat for a bit"
    scene bg daytwodmianscn 13 with Dissolve(0.8)
    Lana "So you enjoyed hanging today i hope?"
    Damian "Yeah thanks , probably did need that as a breather"
    scene bg daytwodmianscn 14 with Dissolve(0.8)
    Lana "I'm glad , look i know you're here to meet natsuko regarding something but please let's have a bit fun too here"
    Damian "Alright i'll stay with you guys as long as it's comfortable"
    scene bg daytwodmianscn 15 with Dissolve(0.8)
    Lana "Oh it's comfortable , I mean you and I always had trips during uni days "
    Damian "That was fun yeah , but a different time really and a different me"
    scene bg daytwodmianscn 16 with Dissolve(0.8)
    Lana "Do- do you still miss her?.. I mean kiara-"
    scene bg daytwodmianscn 17 with Dissolve(0.8)
    Damian "Of course i do , I'll never forget her lana , She made me better .. she healed me"
    Lana "I didn't mean it that way I just-"
    scene bg daytwodmianscn 18 with Dissolve(0.8)
    Lana "I'm here for you.. and i want you to know that"
    Damian "I know you are lana , I need friends around me and i appreciate one i know from long ago"
    scene bg daytwodmianscn 19 with Dissolve(0.8)
    Lana "Can i ask you something?.. Why not try the things you did with kiara with someone else? Maybe you just-"
    scene bg daytwodmianscn 20 with Dissolve(0.8)
    Damian "That's what you all don't get lana.."
    scene bg daytwodmianscn 21 with Dissolve(0.8)
    Lana "What do you mean?.. I mean a new-"
    scene bg daytwodmianscn 22 with Dissolve(0.8)
    Damian "Mom , friends, everyone else.. you guys don't get it"
    scene bg daytwodmianscn 23 with Dissolve(0.8)
    Damian "I don't miss doing things with kiara.."
    scene bg daytwodmianscn 24 with Dissolve(0.8)
    Damian "I miss doing nothing with her , I didn't have to try.. I could just be happy."
    scene bg daytwodmianscn 25 with Dissolve(0.8)
    Damian "It's not easy.. It never will be and i have to accept that but it's so hard"
    scene bg daytwodmianscn 26 with Dissolve(0.8)
    Lana "Please getup.. for once"
    Damian "Um okay , What is it?"
    scene bg daytwodmianscn 27 with Dissolve(0.8)
    Lana "I know what you mean to say damian I do , but you don't deserve to be sad all the time either"
    Damian "I'm trying lana , it's just not easy.."
    scene bg daytwodmianscn 28 with Dissolve(0.8)
    Lana "Can you please let me do this one thing?"
    Damian "What is it?"
    scene bg daytwodmianscn 29 with Dissolve(0.8)
    Damian "Ah.. Lana."
    Lana "I hate this , you are a great guy and you don't deserve this"
    scene bg daytwodmianscn 30 with Dissolve(0.8)
    Lana "I've been there since the start ,I know what you feel and i'm sorry but i hate seeing you sad"
    scene bg daytwodmianscn 31 with Dissolve(0.8)
    Damian "It's okay lana , I know you don't like it.. hence i try my best to just be cheerful around you"
    scene bg daytwodmianscn 32 with Dissolve(0.8)
    Lana "But you have to fake it for me and i don't like that.. I want you to be happy truly"
    Damian "It's not all fake lana .. and i have to say sadly that truly happy will take time."
    scene bg daytwodmianscn 33 with Dissolve(0.8)
    Lana  "Do you promise me you'll try at least ?"
    Damian "I will , once i meet up with natsuko then i'll try to open up more"
    scene bg daytwodmianscn 34 with Dissolve(0.8)
    Lana "No i mean..you can try with.. us"
    Damian "Lana I-.. You're"
    scene bg daytwodmianscn 35 with Dissolve(0.8)
    pause
    scene bg daytwodmianscn 36 with Dissolve(0.8)
    Lana "We were once together too.. maybe some of still exists?"
    Damian "Lana that was long ago-"
    Lana "Just one kiss.. please"
    scene bg daytwodmianscn 37 with Dissolve(0.8)
    Damian "I can't do this lana , I'm sorry.. I promised myself never again after kiara"
    Lana "But We.. Okay I understand."
    scene bg daytwodmianscn 38 with Dissolve(0.8)
    Damian "I'm sorry lana , you're very beautiful and a great person but i can't replace her , I just can't"
    Lana "I know.. Can i at least hug you again?"
    scene bg daytwodmianscn 39 with Dissolve(0.8)
    Lana "I'm sorry for everything , you will find purpose again damian. IF not with me then i hope someone at least"
    scene bg daytwodmianscn 40 with Dissolve(0.8)
    Damian "I appreciate it lana but i think enough time has passed to be sure that i'll never be the same again"
    scene bg daytwodmianscn 41 with Dissolve(0.8)
    Damian "I will try but i can't promise you or anyone anything"
    Lana "It's okay.. ( I hate lying to him so much..)"
    scene bg daytwodmianscn 42 with Dissolve(0.8)
    Damian "( Kiara , i'll never break my promise.. I'll wait for you till the next life)"
    jump chap_2_scene_38

label chap_2_scene_38:
    scene blackscreen
    show titletext "Natsuko's room , Late night.." with dissolve
    pause 1.0
    window hide
    scene bg kiadaytwostrmrsgmnt 1 with Dissolve(0.8)
    Kiara "Okay this is on , what else do i need to do?"
    Yamazaki "Simply just input the stream key in the tab above there"
    scene bg kiadaytwostrmrsgmnt 2 with Dissolve(0.8)
    Kiara "Alright so now it's asking me to setup a gamertag, what's that?"
    Yamazaki "A gamer tag is like your name but online , Kind of username on how people would find you"
    scene bg kiadaytwostrmrsgmnt 3 with Dissolve(0.8)
    Kiara "Okay alright um , I want to mix my favorites.. so since i'm catholic i'll take saint"
    Yamazaki "Okay saaint for intial , what color do you like?"
    scene bg kiadaytwostrmrsgmnt 4 with Dissolve(0.8)
    Kiara "Saintblack then!"
    Yamazaki "PRetty good but something is missing , you ever had any pets?"
    scene bg kiadaytwostrmrsgmnt 5 with Dissolve(0.8)
    Kiara "I haven't had any , but if i ever get a cat i'd like to name it moor"
    Yamazaki "Saintblackmoor then?"
    scene bg kiadaytwostrmrsgmnt 6 with Dissolve(0.8)
    Kiara "Perfect!"
    Yamazaki "Doesn't really sound very girly though"
    scene bg kiadaytwostrmrsgmnt 7 with Dissolve(0.8)
    Kiara "Girly? Did i come into your office wearing a pink skirt?"
    Yamazaki "Ahaah , I suppose that's fair alright."
    Yamazaki "SaintBlackmoor it is, then. Okay, now turn on the webcam, and let's get started."
    scene bg kiadaytwostrmrsgmnt 8 with Dissolve(0.8)
    Kiara "W-webcam? why?"
    Yamazaki "How else will people see you? Kiara you need to make sure you have an idendity"
    scene bg kiadaytwostrmrsgmnt 9 with Dissolve(0.8)
    Yamazaki "I mean, we do have VTubers as well, but I don't think it would fit your style."
    Kiara "Yeah thankss alright but - (This tank top is pretty exposing and loose , Should i change?)"
    menu:
        "It's fine" if mc_stats.current_corruption >= 50:
            #block of code to run
            jump .part_1
        "No, I should change":
            #block of code to run
            jump .part_2

    label .part_1:
        
        scene bg kiadaystrmintank 1 with Dissolve(0.8)
        Kiara "Um , alright let's get started then"
        scene bg kiadaystrmintank 2 with Dissolve(0.8)
        Kiara "So i just click on cam icon?"
        Yamazaki "Yeah click is enough , no need to hold it"
        scene bg kiadaystrmintank 3 with Dissolve(0.8)
        Yamazaki "Y-yeah i see you"
        Kiara "Oh nothing you just look great"
        scene bg kiadaystrmintank 4 with Dissolve(0.8)
        Yamazaki "Is the green light on your camrea blinking or constant?"
        Kiara "It's constant"
        scene bg kiadaystrmintank 5 with Dissolve(0.8)
        Kiara "So is quality fine?"
        Yamazaki "Yeah yeah.. it's fine (Holy shit she looks like a dream girl)"
        scene bg kiadaystrmintank 6 with Dissolve(0.8)
        Nobi "Kiara-san , Dinner"
        Kiara "Oh hi nobi , please put that over there"
        scene bg kiadaystrmintank 7 with Dissolve(0.8)
        Nobi "Anything else you requiore?"
        Kiara "No please get some rest , I'll be late"
        scene bg kiadaystrmintank 8 with Dissolve(0.8)
        Yamazaki "Wow , your boyfriend cooks for you? Damn"
        Kiara "B-boyfriend? No.. He's just a servant"
        scene bg kiadaystrmintank 9 with Dissolve(0.8)
        Yamazaki "Wait.. you're single?"
        Kiara "Yeah , why? haha"
        Yamazaki "Oh , no nothing just a bit surprised"
        scene bg kiadaystrmintank 10 with Dissolve(0.8)
        Kiara "Surprised? I'm not that pretty"
        Yamazaki "Easy to say good genes amigo ( What is she talking about? She's a fucking godess)"
        scene bg kiadaystrmintank 11 with Dissolve(0.8)
        Kiara "Oh cmon , It's alright besides dating is a commitment so i prefer long term"
        Yamazaki "That i true ( She's not wrong , way too hot for anyone in osaka)"
        scene bg kiadaystrmintank 12 with Dissolve(0.8)
        Yamazaki "So let's set up the games now"
        Kiara "I'm on it , which one do i start?"
        scene bg kiadaystrmintank 13 with Dissolve(0.8)
        "Chat member" "Hey , cool hair!"
        Kiara "Hello there , thank you"
        scene bg kiadaystrmintank 14 with Dissolve(0.8)
        "Chat member 2" "You should try Butcher 3 , really good rpg"
        Yamazaki "Oh yeah that's a good one kiara"
        Kiara "Okay if you guys say so"
        scene bg kiadaystrmintank 15 with Dissolve(0.8)
        Kiara "I hope the quality is okay for you guys"
        "Chat member 1" "All good here!"
        "Chat member 2" "Bit stuttery but not too bad"
        "Chat member 3" "Crystal clear saint! , keep playing"
        Yamazaki "Don't worry about quality it'll balance eventually"
        scene bg kiadaystrmintank 16 with Dissolve(0.8)
        Natsuko "Kiara! , I'm sleeping in you room okay?"
        Kiara "Oh! okay sure! that's fine"
        Natsuko "You look lovely Cousin!"
        scene bg kiadaystrmintank 17 with Dissolve(0.8)
        Kiara "Thank you! you look better!"
        "Chat member 2 " "Cousin?"
        Yamazaki "Cousin?.. "
        scene bg kiadaystrmintank 18 with Dissolve(0.8)
        Kiara "Goodnight natsu , see you tommorow"
        scene bg kiadaystrmintank 19 with Dissolve(0.8)
        Yamazaki "(Man she's got such nice skin)"
        scene bg kiadaystrmintank 20 with Dissolve(0.8)
        Yamazaki "(God i wish that top showed more cleavage)"
        scene bg kiadaystrmintank 21 with Dissolve(0.8)
        Yamazaki "(What the?.. Did it slide down a bit when she moved?)"
        scene bg kiadaystrmintank 22 with Dissolve(0.8)
        Kiara "Sorry guys just my cousin , let's continue"
        Yamazaki "( Holy shit.. it did! , I gotta make her move more..)"
        scene bg kiadaystrmintank 23 with Dissolve(0.8)
        Kiara "Hmm i wonder where i can find the quest marker here"
        scene bg kiadaystrmintank 24 with Dissolve(0.8)
        Kiara "What do you guys think?"
        "Chat member 2" "Go to the right side corner!"
        Yamazaki "( I have an idea)"
        scene bg kiadaystrmintank 25 with Dissolve(0.8)
        Kiara "(Ah! , sorry wait-)"
        Yamazaki "Whoa is the cam okay? ( Bless these remote controls)"
        scene bg kiadaystrmintank 26 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 27 with Dissolve(0.8)
        Kiara "I'm fixing it hold on"
        "Chatmember" "Wow.."
        Yamazaki "(Cmon cmon..)"
        scene bg kiadaystrmintank 28 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 29 with Dissolve(0.8)
        Yamazaki "(Yes! , it is! okay.. nice)"
        scene bg kiadaystrmintank 30 with Dissolve(0.8)
        Kiara "Is it fixed now?"
        "Chatmember 2 " "Um no it's not a bit more down we can't see your face"
        Yamazaki "( This fucker really had to say it , dammit)"
        scene bg kiadaystrmintank 31 with Dissolve(0.8)
        Kiara "Thanks guys , I am sorry it fell suddenly"
        scene bg kiadaystrmintank 32 with Dissolve(0.8)
        "Anon donated 50 $ !"
        Kiara "What?.. 50 bucks?"
        Yamazaki "Kiara , congrats on your first ever donation!"
        scene bg kiadaystrmintank 33 with Dissolve(0.8)
        Kiara "Hey thanks anon , much appreciated"
        Yamazaki "Anon just means anonynmus kiara"
        scene bg kiadaystrmintank 34 with Dissolve(0.8)
        Kiara "Oh okay , let's keep going"
        "Anon donated 100 $ stretch!"
        scene bg kiadaystrmintank 35 with Dissolve(0.8)
        Yamazaki "Someone redeemed 100 $ for a stretch kiara! It's like a simple yawn pose"
        Kiara "Why would someone-.. Well okay sure"
        scene bg kiadaystrmintank 36 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 37 with Dissolve(0.8)
        Kiara "How much longer?"
        Yamazaki "I think it's about 10 seconds"
        scene bg kiadaystrmintank 38 with Dissolve(0.8)
        Kiara "Okay!"
        Yamazaki "( Mamma mia , look at that waist i could ride a f1 on those curves)"
        scene bg kiadaystrmintank 39 with Dissolve(0.8)
        Kiara "( I don't get why would someone pay to just see me stretch)"
        Yamazaki "( Man i would jsut kiss that belly all day)"
        scene bg kiadaystrmintank 40 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 41 with Dissolve(0.8)
        Yamazaki "( Hehe yes.. It's working , this money is worth every penny spent)"
        scene bg kiadaystrmintank 42 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 43 with Dissolve(0.8)
        Kiara "Alrgiht that's done , now let's continue"
        Yamazaki "Oh look kiara your viewers have increased!"
        scene bg kiadaystrmintank 44 with Dissolve(0.8)
        Kiara "Oh yeah, hi everyone! New here, I'm Kiara, in case the user name is hard to remember."
        "Several chat members" "Wow you look beautiful! , cool new streamer! , You look very nice! , Good hair!"
        scene bg kiadaystrmintank 45 with Dissolve(0.8)
        Kiara "Um, well, thanks, guys. I'm new, actually, so sorry I'm slow at replying. (They're awfully sweet for no reason.)"
        scene bg kiadaystrmintank 46 with Dissolve(0.8)
        "Anon donated 120 $!"
        Yamazaki "It's a redeem for an uWu pose kiara!"
        Kiara "What the hell is that?"
        scene bg kiadaystrmintank 47 with Dissolve(0.8)
        Yamazaki "Just follow my instructions"
        scene bg kiadaystrmintank 48 with Dissolve(0.8)
        Yamazaki "Get your arms in front of you with fists clenched"
        Kiara "Alright , afrer that?"
        scene bg kiadaystrmintank 49 with Dissolve(0.8)
        Yamazaki "Thumbs up"
        Kiara "Okay.."
        "Chat member 16" "She's really doing it!"
        scene bg kiadaystrmintank 50 with Dissolve(0.8)
        Yamazaki "(Fall a bit more damn you..)"
        Kiara "Yama?"
        scene bg kiadaystrmintank 51 with Dissolve(0.8)
        Yamazaki "(Oh yess..)"
        Kiara "Yama?? Hello?"
        scene bg kiadaystrmintank 52 with Dissolve(0.8)
        Kiara "Hurry up i don't want to waste the entire stream on it"
        Yamazaki "Yeah yeah uh , just join your index finger and then say uwu"
        scene bg kiadaystrmintank 53 with Dissolve(0.8)
        Kiara "Like this?"
        Yamazaki "No no , uh like joining as if they're both touching their tips"
        scene bg kiadaystrmintank 54 with Dissolve(0.8)
        Yamazaki "Perfect!"
        scene bg kiadaystrmintank 55 with Dissolve(0.8)
        Yamazaki "Yes.. now say it (God look at those titties)"
        scene bg kiadaystrmintank 56 with Dissolve(0.8)
        Kiara "Okay so.. here we go"
        scene bg kiadaystrmintank 57 with Dissolve(0.8)
        "Chat member 11" "Don't point it out anyone , let her be.."
        Yamazaki "( Damn chat is filling with perverts too , can't blame em though that is a good sight . I'ma grab a lotion)"
        scene bg kiadaystrmintank 58 with Dissolve(0.8)
        Kiara "UwU"
        scene bg kiadaystrmintank 59 with Dissolve(0.8)
        "Chat member 1" "Donated 10$!"
        "Chat member 2" "Donated 25$!"
        "Anon donated 50$!"
        "Chat member 5 donated 35$!"
        Kiara "( Is uwu something bad? I hope not)"
        scene bg kiadaystrmintank 60 with Dissolve(0.8)
        "Chat member 5" "Don't talk about it"
        "Chat member 2" "We should tell her it's not good"
        "Chat membeer 9" "Shhh!"
        Kiara "(What are they talking about?)"
        scene bg kiadaystrmintank 61 with Dissolve(0.8)
        "Chat member 8 " "But they look so good!"
        "Chat member 14 " "Shut up!"
        Kiara "They? look good?.. wh-"
        "Chat member 2" "Hey loko down!"
        scene bg kiadaystrmintank 62 with Dissolve(0.8)
        Kiara "Down?"
        "Chat member 14 " "This fucking white knight"
        "Chat member 5" "Dude cmon!"
        scene bg kiadaystrmintank 63 with Dissolve(0.8)
        Kiara "What the!-- hey i"
        scene bg kiadaystrmintank 64 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 65 with Dissolve(0.8)
        Kiara "No! - how did it get so loose?"
        scene bg kiadaystrmintank 66 with Dissolve(0.8)
        Kiara "OKay fuck this , what one earth"
        "Chat member 11" "Aw man i almost saw her cleavage properly!"
        "Chat member 6" "Fuck you dude!"
        "Chat member 2" "Glad she noticed"
        scene bg kiadaystrmintank 67 with Dissolve(0.8)
        pause
        scene bg kiadaystrmintank 68 with Dissolve(0.8)
        Yamazaki "Wait kiara! I didn't know!"
        Kiara "What the hell do you mean you didn't know?"
        scene bg kiadaystrmintank 69 with Dissolve(0.8)
        Yamazaki "I was afk , and i just didn't notice!"
        Kiara "Do you have any idea what impression that gave for my first stream?"
        scene bg kiadaystrmintank 70 with Dissolve(0.8)
        Yamazaki "I understand , but look so many people were there and they paid!"
        Kiara "You think that makes it okay for me to almost flash strangers? And they were just discussing my body. What were you doing?"
        scene bg kiadaystrmintank 71 with Dissolve(0.8)
        Yamazaki "No! that's not what i meant , look i'm sorry really"
        Kiara "I don't wanna do this anymore.. you can take your computer back"
        scene bg kiadaystrmintank 72 with Dissolve(0.8)
        Yamazaki "No! look kiara as an apology just keep the computer.. I paid for it anyway"
        Kiara "You paid for it?.. Why?"
        scene bg kiadaystrmintank 73 with Dissolve(0.8)
        Yamazaki "Well taka told me you wanted to start new and i wanted to help anyway i could"
        Kiara "Um.. alright I'm sorry"
        Yamazaki "No! don't be... look we'll try again okay? next time i'll moderate it properly"
        scene bg kiadaystrmintank 74 with Dissolve(0.8)
        Kiara "Well i'm only free next weeek then.. "
        Yamazaki "That's okay! , I'll wait for you and i promise it won't happen again"
        scene bg kiadaystrmintank 75 with Dissolve(0.8)
        Yamazaki "Look, I'm really sorry, alright? If you want, I'll just go and get someone you're comfortable with to moderate."
        Kiara "(I shouldn't be so hard on him , it wasn't his fault)"
        scene bg kiadaystrmintank 76 with Dissolve(0.8)
        Kiara "Okay.. I'll do it , thanks again.. goodnight"
        Yamazaki "Thank you so much and you did great today okay? , goodnight!"
        scene bg kiadaystrmintank 77 with Dissolve(0.8)
        Kiara "I should've just been careful about my top. He's right, though. I did get a lot of viewers."
        scene bg kiadaystrmintank 78 with Dissolve(0.8)
        Kiara "Uhm, what am I thinking? No, I won't do that again... I should just rest."
        scene bg kiadaystrmintank 79 with Dissolve(0.8)
        pause
        $ mc_stats.adjust_corruption(5)
        scene bg kiadaystrmintank 80 with Dissolve(0.8)
        pause
        jump chap_2_scene_39

    label .part_2:
        scene bg kiadaytwostrmcloth 1 with Dissolve(0.8)
        Kiara "Uhm can you give me a moment? I need to change actually"
        Yamazaki "Oh yeah um, are you not dressed properly? I'm sorry I didn't know"
        scene bg kiadaytwostrmcloth 2 with Dissolve(0.8)
        Kiara "No, it's just a tank top,  but I'd rather not let people have the wrong impression."
        Yamazaki "That's totally fine , take your time"
        scene bg kiadaytwostrmcloth 3 with Dissolve(0.8)
        Kiara "I'll be quick just a sec"
        scene bg kiadaytwostrmcloth 4 with Dissolve(0.8)
        Kiara "Back!"
        Yamazaki "Okay! , start it up now"
        scene bg kiadaytwostrmcloth 5 with Dissolve(0.8)
        Yamazaki "Wow the sweater looks great!"
        Kiara "Thank you , Um.. is it on?"
        Yamazaki "Yeah i see you clear and fine , let's start"
        scene bg kiadaytwostrmcloth 6 with Dissolve(0.8)
        Nobi "Kiara-san , Dinner"
        Kiara "Oh hi nobi , please put that over there"
        scene bg kiadaytwostrmcloth 7 with Dissolve(0.8)
        Nobi "Anything else you requiore?"
        Kiara "No please get some rest , I'll be late"
        scene bg kiadaytwostrmcloth 8 with Dissolve(0.8)
        Yamazaki "Wow , your boyfriend cooks for you? Damn"
        Kiara "B-boyfriend? No.. He's just a servant"
        scene bg kiadaytwostrmcloth 9 with Dissolve(0.8)
        Yamazaki "Wait.. you're single?"
        Kiara "Yeah , why? haha"
        Yamazaki "Oh , no nothing just a bit surprised"
        scene bg kiadaytwostrmcloth 10 with Dissolve(0.8)
        Kiara "Surprised? I'm not that pretty"
        Yamazaki "Easy to say good genes amigo"
        scene bg kiadaytwostrmcloth 11 with Dissolve(0.8)
        Kiara "Oh, come on. It's alright. Besides, dating is a commitment, so I prefer long-term."
        Yamazaki "That is true. If you're going to find one, better find a permanent one."
        scene bg kiadaytwostrmcloth 12 with Dissolve(0.8)
        Yamazaki "So let's set up the games now"
        Kiara "I'm on it , which one do i start?"
        scene bg kiadaytwostrmcloth 13 with Dissolve(0.8)
        "Chat member" "Hey , cool hair!"
        Kiara "Hello there , thank you"
        scene bg kiadaytwostrmcloth 14 with Dissolve(0.8)
        Kiara "Umm.. wait what is this"
        scene bg kiadaytwostrmcloth 15 with Dissolve(0.8)
        Kiara "I hope the quality is okay for you guys"
        "Chat member 1" "All good here!"
        "Chat member 2" "Bit stuttery but not too bad"
        "Chat member 3" "Crystal clear saint! , keep playing"
        Yamazaki "Don't worry about quality it'll balance eventually"
        scene bg kiadaytwostrmcloth 16 with Dissolve(0.8)
        Natsuko "Kiara! , I'm sleeping in you room okay?"
        Kiara "Oh! okay sure! that's fine"
        Natsuko "You look lovely by the way sweet Cousin!"
        scene bg kiadaytwostrmcloth 17 with Dissolve(0.8)
        Kiara "Aheh , are you gonna make me blush on stream? thank you!"
        "Chat member 2 " "Cousin?"
        Yamazaki "Cousin?.. "
        scene bg kiadaytwostrmcloth 18 with Dissolve(0.8)
        Kiara "You look better! , goodnight okay?"
        Natsuko "Goodnight! , I love you!"
        Kiara "Love you too! , Sleep well!"
        scene bg kiadaytwostrmcloth 19 with Dissolve(0.8)
        Kiara "Sorry guys "
        Yamazaki "(Maybe i can ask her cousin about something? Taka did say she's very beautiful too)"
        "Chat member 1" "Is she your cousin?"
        "Chat member 3" "She has a nice name"
        scene bg kiadaytwostrmcloth 20 with Dissolve(0.8)
        Kiara "Yes, she's my cousin. She let me use her room for this stream too."
        "Chat member 3" "Next stream lets bring her on camera!"
        Yamazaki "If you're comfortable onyl then kiara"
        scene bg kiadaytwostrmcloth 21 with Dissolve(0.8)
        Kiara "I'll have to ask her..-  wait someone donated?"
        Yamazaki "Oh wow your first donation 35 $ !"
        scene bg kiadaytwostrmcloth 22 with Dissolve(0.8)
        Yamazaki "Second donation 50 $!"
        Kiara "Wh.. why? I've barely played the game"
        scene bg kiadaytwostrmcloth 23 with Dissolve(0.8)
        "Chat member 2 " "We just like your vibe!"
        Yamazaki "Sometimes that's enough too kiara"
        Kiara "Thank you so much guys"
        scene bg kiadaytwostrmcloth 24 with Dissolve(0.8)
        Yamazaki "Someone just donated 80 $ more!"
        Kiara "What on earth who was that..?"
        scene bg kiadaytwostrmcloth 25 with Dissolve(0.8)
        Kiara "Who was that? it says anon?"
        Yamazaki "Oh that refers to anonymus kiara , they want to stay hidden"
        Kiara "Well thanks anon"
        scene bg kiadaytwostrmcloth 26 with Dissolve(0.8)
        Kiara "Okay guys um.. thanks again i need to get some rest though"
        "Chat member 3" "See you later kiara-san!"
        "Chat member 2" "Bye goodnight!"
        Yamazaki " ( That anon donation was me.. good thing she dind't ask too many details)"
        scene bg kiadaytwostrmcloth 27 with Dissolve(0.8)
        pause
        scene bg kiadaytwostrmcloth 28 with Dissolve(0.8)
        Kiara "Okay , lets get some shut eye"
        scene bg kiadaytwostrmcloth 29 with Dissolve(0.8)
        Kiara "This streaming thing is nice.. but i don't want to just stay home either"
        scene bg kiadaytwostrmcloth 30 with Dissolve(0.8)
        Kiara "At least I have options now. No more being locked to just getting carried on a peddle"
        scene bg kiadaytwostrmcloth 31 with Dissolve(0.8)
        Kiara "I hope you're alright mom.. , I miss you"
        scene bg kiadaytwostrmcloth 32 with Dissolve(0.8)
        pause
        scene bg kiadaytwostrmcloth 33 with Dissolve(0.8)
        pause
        jump chap_2_scene_39

label chap_2_scene_39:
    scene blackscreen
    show titletext "Takahashi Estate , Osaka downtown.." with dissolve
    pause 1.0
    window hide
    scene bg keisukereturdhomedytwo 1 with Dissolve(0.8)
    Keisuke "Tommorow she'll have plenty of her friends and day with me.. I hope i can fit in"
    scene bg keisukereturdhomedytwo 2 with Dissolve(0.8)
    Keisuke "Why isn't ayane picking up?"
    scene bg keisukereturdhomedytwo 3 with Dissolve(0.8)
    pause
    scene bg keisukereturdhomedytwo 4 with Dissolve(0.8)
    pause
    scene bg keisukereturdhomedytwo 5 with Dissolve(0.8)
    Keisuke "I should just go and check up"
    scene bg keisukereturdhomedytwo 6 with Dissolve(0.8)
    Keisuke "Ayane? hello?"
    scene bg keisukereturdhomedytwo 7 with Dissolve(0.8)
    Keisuke "Not here either?.. where is she?"
    scene bg keisukereturdhomedytwo 8 with Dissolve(0.8)
    Keisuke "Ayane! , are you in the basement?"
    scene bg keisukereturdhomedytwo 9 with Dissolve(0.8)
    Keisuke "Ayane?! , are you here I-"
    scene bg keisukereturdhomedytwo 10 with Dissolve(0.8)
    Keisuke "Where is she?.. She's mostly in ktichen around this time"
    scene bg keisukereturdhomedytwo 11 with Dissolve(0.8)
    Keisuke "AYANE! , can you hear me? hello?"
    scene bg keisukereturdhomedytwo 12 with Dissolve(0.8)
    Keisuke "(What on earth.. where is the chef?)"
    scene bg keisukereturdhomedytwo 13 with Dissolve(0.8)
    Keisuke "Not even at pool , Where is she?"
    scene bg keisukereturdhomedytwo 14 with Dissolve(0.8)
    Keisuke "Aya-... what the-"
    "???" "Took your time big brother , she was worried"
    scene bg keisukereturdhomedytwo 15 with Dissolve(0.8)
    Ayane "MMhhmph , mmhph"
    "???" "I really don't like to be kept waiting , you're lucky she had no weapons"
    Keisuke "W-what is this.. who are you?"
    scene bg keisukereturdhomedytwo 16 with Dissolve(0.8)
    AgentWong "The luxury of questions is up to me, Mr. Keisuke Takahashi."
    scene bg keisukereturdhomedytwo 17 with Dissolve(0.8)
    AgentWong "Come sit Keisuke , Let us have a little chat"
    Keisuke "Okay.. okay just just please don't hurt her"
    scene bg keisukereturdhomedytwo 18 with Dissolve(0.8)
    Keisuke "Ayane.. It- It's going to be alright okay? I'm here"
    Ayane "MMpph? mmmmmmmmmm! , mmmph!"
    AgentWong "Making promises you can't keep huh?"
    scene bg keisukereturdhomedytwo 19 with Dissolve(0.8)
    Keisuke "Look, please just don't hurt her. I'll do whatever you want. Whoever is paying you, I'll double it—no, triple it."
    scene bg keisukereturdhomedytwo 20 with Dissolve(0.8)
    AgentWong "Stop testing my patience and come here. Or you won't have a sister to save."
    Keisuke "Okay! okay! , fine.. fine I'm coming."
    scene bg keisukereturdhomedytwo 21 with Dissolve(0.8)
    Ayane "MMhh... mhhph *Crying*"
    Keisuke "Ayane.. just relax.. I'm here"
    AgentWong "Cmon cmon , nice and slow"
    scene bg keisukereturdhomedytwo 22 with Dissolve(0.8)
    Keisuke "What do you want?.. who  are you?"
    AgentWong "Did i not make myself clear smartass?"
    scene bg keisukereturdhomedytwo 23 with Dissolve(0.8)
    AgentWong "I'm the one asking questions!"
    Ayane "MMppph! mmmmmmmmmmphh! mmmph!"
    Keisuke "Okay, okay! I'm sorry, alright. Just ask"
    scene bg keisukereturdhomedytwo 24 with Dissolve(0.8)
    "*Thud*"
    Keisuke "What did you do!?"
    scene bg keisukereturdhomedytwo 25 with Dissolve(0.8)
    AgentWong "Giving her a good nap. Don't worry, by the time she wakes up, I'll be long gone."
    scene bg keisukereturdhomedytwo 26 with Dissolve(0.8)
    AgentWong "However whether she'll find you alive or not is upto your answers"
    Keisuke "I really don't know what you're talking about.."
    scene bg keisukereturdhomedytwo 27 with Dissolve(0.8)
    AgentWong "Of course, you don't. It's regarding your new occupation and your customer, Kiara Hall. Let's head upstairs. Let's have that chat"
    Keisuke "Fine.. Okay"
    scene bg keisukereturdhomedytwo 28 with Dissolve(0.8)
    AgentWong "Tell me everything, try not to be smart. I'm trigger-happy today."
    Keisuke "I met Kiara when we were kids. I met her in Hokaido. She stayed there for two years, and in that time, I just..."
    AgentWong "Just.. what?"
    scene bg keisukereturdhomedytwo 29 with Dissolve(0.8)
    Keisuke "I fell for her. There was no one like her. It was as if she could sense every little thing I'd be sad about and make me happy immediately."
    AgentWong "Hm Continue.."
    scene bg keisukereturdhomedytwo 30 with Dissolve(0.8)
    Keisuke "When she was leaving Japan, she said she'd come back after her studies finished... and then I found out-"
    AgentWong "That her memories got erased.."
    scene bg keisukereturdhomedytwo 31 with Dissolve(0.8)
    Keisuke "How do you kno-"
    AgentWong "Leave that to me.. so she doesn't remember you at all?"
    scene bg keisukereturdhomedytwo 32 with Dissolve(0.8)
    Keisuke "No.. no she doesn't"
    AgentWong "I see , how do you feel about that?"
    scene bg keisukereturdhomedytwo 33 with Dissolve(0.8)
    Keisuke "It hurts so fucking much because I remember everything. Every little bit of her, every moment we spent together. Even now, meeting her again, she's the same."
    scene bg keisukereturdhomedytwo 34 with Dissolve(0.8)
    Keisuke "I missed her so much. I never got to confess to her because I felt I wasn't good enough for her back then. So, I worked hard and got to where I am now."
    Keisuke "Hell, maybe I'm still not, but I can try this time."
    scene bg keisukereturdhomedytwo 35 with Dissolve(0.8)
    Keisuke "Now that she's here, all I want is to make sure she's safe and happy"
    Keisuke "If fate decides to bring us back together, then so be it. Otherwise, I'll remain the friend she needs."
    scene bg keisukereturdhomedytwo 36 with Dissolve(0.8)
    AgentWong "Do you know what happened to her in new york?"
    Keisuke "I don't know everything. All I have been told is that there was a memory erasure and her death was faked. Why? How? When? I don't know anything else."
    scene bg keisukereturdhomedytwo 37 with Dissolve(0.8)
    AgentWong "Well.. so why this taxi driver facade? why not come out and say who you are?"
    Keisuke "I don't know... it might affect her in some way, and I don't want to risk it.. "
    scene bg keisukereturdhomedytwo 38 with Dissolve(0.8)
    Keisuke "Also at least this way, I get to meet the same person I did years ago. To her, I'm just a normal guy, and to me, she's that rich girl who has the humblest of heart. It's just like our past. "
    AgentWong "So you're recreating what you had once.."
    scene bg keisukereturdhomedytwo 39 with Dissolve(0.8)
    AgentWong "I'm hired to kill anyone trying to get too close to her or harm her. So, I'll ask you this... What if she doesn't want to be with you again"
    Keisuke " Then I'll respect that, but I'm not leaving. I won't let her be alone again."
    scene bg keisukereturdhomedytwo 40 with Dissolve(0.8)
    AgentWong "Ah! Hey-"
    Keisuke "I love her, and I always will. I don't care who or what gets in the way. I'll never abandon her."
    scene bg keisukereturdhomedytwo 41 with Dissolve(0.8)
    Keisuke "So, if what you want is for me to be outside of her life now, I'm afraid you're going to have to pull this trigger."
    AgentWong "( He's..)"
    scene bg keisukereturdhomedytwo 42 with Dissolve(0.8)
    AgentWong "You're willing to die for this?"
    Keisuke "Without her I'm mostly dead anyway.. and truthfully-"
    scene bg keisukereturdhomedytwo 43 with Dissolve(0.8)
    Keisuke "Perhaps i need her in my life more than you need that money in your account"
    AgentWong "Sigh.."
    scene bg keisukereturdhomedytwo 44 with Dissolve(0.8)
    Keisuke "W-what.."
    scene bg keisukereturdhomedytwo 45 with Dissolve(0.8)
    pause
    scene bg keisukereturdhomedytwo 46 with Dissolve(0.8)
    AgentWong "Can i have some water please?"
    Keisuke "O-uh Okay.. sure"
    scene bg keisukereturdhomedytwo 47 with Dissolve(0.8)
    Keisuke "Why did she throw the gun?.. who is this girl?"
    scene bg keisukereturdhomedytwo 48 with Dissolve(0.8)
    "Keisuke's words" "I love her, and I won't abandon her this time. I won't let her be alone anymore, not again.."
    scene bg keisukereturdhomedytwo 49 with Dissolve(0.8)
    AgentWong "I can't do this.. Dammit"
    scene bg keisukereturdhomedytwo 50 with Dissolve(0.8)
    pause
    scene bg keisukereturdhomedytwo 51 with Dissolve(0.8)
    Keisuke "Hey your wa-"
    scene bg keisukereturdhomedytwo 52 with Dissolve(0.8)
    Keisuke "She's gone.. Wh- did she spare me?"
    scene bg keisukereturdhomedytwo 53 with Dissolve(0.8)
    Keisuke "Kiara.. I hope you're sleeping peacefully"
    #ADD NY LOADING
    jump chap_2_scene_40

label chap_2_scene_40:
    scene blackscreen
    show titletext "Veronica's house , Early morning.." with dissolve
    pause 1.0
    window hide
    scene bg dytwoveroevestrt 1 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 2 with Dissolve(0.8)
    Veronica "Hmm mhm  *Humming music* , I hope she'll like this i haven't made pie in a while"
    scene bg dytwoveroevestrt 3 with Dissolve(0.8)
    Veronica "Though she'll probably go easy on me, I still want her to have a good breakfast."
    scene bg dytwoveroevestrt 4 with Dissolve(0.8)
    Veronica "Hmm mhm *Humming music*"
    scene bg dytwoveroevestrt 5 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 6 with Dissolve(0.8)
    Evelyn "( There you are..)"
    scene bg dytwoveroevestrt 7 with Dissolve(0.8)
    Evelyn "( She's cooking for me i think)"
    scene bg dytwoveroevestrt 8 with Dissolve(0.8)
    Evelyn "( Okay .. quiet and slow)"
    scene bg dytwoveroevestrt 9 with Dissolve(0.8)
    Veronica "It looks good enough, just a bit more -"
    scene bg dytwoveroevestrt 10 with Dissolve(0.8)
    Veronica "Aha hey-"
    Evelyn "Guess who and you get a prize?"
    scene bg dytwoveroevestrt 11 with Dissolve(0.8)
    Veronica "The most beautiful person on this planet?"
    Evelyn "Well, you're half right. You're the winner of that, actually, but I'll take the second spot"
    scene bg dytwoveroevestrt 12 with Dissolve(0.8)
    Evelyn "Though I'm feeling quite forgiving this morning, so... what prize would you like?"
    Veronica "Oh, it's standing in front of me right now."
    scene bg dytwoveroevestrt 13 with Dissolve(0.8)
    Evelyn "Well go on.. claim it then"
    Veronica "I mean if you insis on it then-"
    scene bg dytwoveroevestrt 14 with Dissolve(0.8)
    Evelyn "mm.."
    Veronica "Mmm.."
    "*Bell rings*"
    scene bg dytwoveroevestrt 15 with Dissolve(0.8)
    Veronica "Ah, that must be the mail. I'll go grab it before it runs away again."
    Evelyn "Awe.. did he really have to come now? What a douche"
    scene bg dytwoveroevestrt 16 with Dissolve(0.8)
    Evelyn "( Heh.. I'm so glad last night happened )"
    scene bg dytwoveroevestrt 17 with Dissolve(0.8)
    Evelyn "( I love you so much, V. I can't wait for us to move on to the next step.)"
    scene bg dytwoveroevestrt 18 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 19 with Dissolve(0.8)
    Veronica "What's this- A gift?"
    scene bg dytwoveroevestrt 20 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 21 with Dissolve(0.8)
    Veronica "Not even the post guy is here.. man they run away so fast seriously"
    scene bg dytwoveroevestrt 22 with Dissolve(0.8)
    Evelyn "Hey , what is it?"
    Veronica "Oh eve.. It's gifts actually , says chocolate cake on top "
    scene bg dytwoveroevestrt 23 with Dissolve(0.8)
    Evelyn "Chocolate cake? who could be sending that?"
    Veronica "I don't know but everything i get does get taste checked so i doubt it's anything bad"
    scene bg dytwoveroevestrt 24 with Dissolve(0.8)
    Veronica "Oh wait no , it says here it's from my friend's at the work"
    Evelyn "Well let's not waste them anymore then , cmon let's eat"
    scene bg dytwoveroevestrt 25 with Dissolve(0.8)
    Evelyn "These are really nice"
    Veronica "I'm surprised she sent these , she doesn't know what my faovrite is but good guess i suppose"
    scene bg dytwoveroevestrt 26 with Dissolve(0.8)
    Veronica "Well i love em for sure hope they are also to your liking eve"
    Evelyn "Yeah they are.."
    scene bg dytwoveroevestrt 27 with Dissolve(0.8)
    Veronica "Honestly i love the little waffle chocolate on it as well"
    Evelyn "Yeah i suppose it's nice.."
    scene bg dytwoveroevestrt 28 with Dissolve(0.8)
    Veronica "What's up? something bugging you love?"
    Evelyn "Yeah.. Kiara and I used to eat chocolate cakes and share them. It's been so long since I've even seen her"
    scene bg dytwoveroevestrt 29 with Dissolve(0.8)
    Veronica "I'm sorry , I didn't mean to-"
    Evelyn "It's okay um-"
    scene bg dytwoveroevestrt 30 with Dissolve(0.8)
    Evelyn "V , I have some questions.."
    Veronica "Um sure , what about?"
    scene bg dytwoveroevestrt 31 with Dissolve(0.8)
    Evelyn "This case , I understand the divorce hearing, but why is Kiara's custody in question? Why can't she just move out? I mean, she's an adult she-"
    Veronica "Ah i suppose i should explain it since you're also involved now"
    scene bg dytwoveroevestrt 32 with Dissolve(0.8)
    Veronica "Eve, when Kiara got her memories erased, she wasn't stable or... rather, she was normal. She was suicidal and a risk to others around her."
    Evelyn "W-what do you mean?"
    scene bg dytwoveroevestrt 33 with Dissolve(0.8)
    Veronica "She would wield knives, attack others, and attempt to jump off the roof. The multiple procedures John had done on her were taking a toll."
    Evelyn "( Kiara.. my sweet litte sis )"
    Veronica "It was all intentional. He recorded everything and made sure to portray Kiara as mentally unstable in order to gain custody and be alone. Consequently, the court granted him guardianship custody as well."
    scene bg dytwoveroevestrt 34 with Dissolve(0.8)
    Evelyn "So there is no way for us to save her from him?"
    Veronica "Kiara's a lot better now, so we can challenge that custody when the next hearing comes. Till then, though, not much on our hands."
    scene bg dytwoveroevestrt 35 with Dissolve(0.8)
    Veronica "Look, I'll be there with her. He planned all of this very specifically to keep Kiara to himself."
    Evelyn "I know, I just don't want her to suffer anymore. That's about it."
    scene bg dytwoveroevestrt 36 with Dissolve(0.8)
    Evelyn "I genuinely feel so useless as a big sister. I abandoned her when she needed me the most"
    Veronica "You had your demons to fight too. Besides, she still misses you. So when you go there, make up for lost time, okay?"
    scene bg dytwoveroevestrt 37 with Dissolve(0.8)
    Veronica "C'mon now, don't let anything ruin that pretty smile of yours. Don't worry, I'll be right alongside you guys."
    Evelyn "I don't care about myself anymore. I care about my little sister who deserves to be happy"
    scene bg dytwoveroevestrt 38 with Dissolve(0.8)
    Veronica "Well, I care about you too, and I always will. You're not getting rid of that anytime soon."
    Evelyn "Heh.. Alright then"
    scene bg dytwoveroevestrt 39 with Dissolve(0.8)
    Veronica "There's that smile.. now how about we finish what we were intrupted on?"
    scene bg dytwoveroevestrt 40 with Dissolve(0.8)
    Evelyn "Sounds like a splendid idea"
    Veronica "Don't mind me geting closer then"
    scene bg dytwoveroevestrt 41 with Dissolve(0.8)
    Veronica "I love you eve"
    Evelyn "I love you more"
    scene bg dytwoveroevestrt 42 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 43 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 44 with Dissolve(0.8)
    pause
    scene bg dytwoveroevestrt 45 with Dissolve(0.8)
    "Investigator" "Package delivered , keeping an eye on target"
    jump chap_2_scene_41

label chap_2_scene_41:
    scene blackscreen
    show titletext "The hall mansion , Outside brooklyn" with dissolve
    pause 1.0
    window hide
    scene johndytwonypwr 1 with Dissolve(0.8)
    John "Did she recieve them?"
    Patricia "Yes sir , your daughter is there as well , Evelyn i mean"
    scene johndytwonypwr 2 with Dissolve(0.8)
    John "Very well , keep sending as her family members or relatives"
    Patricia "Um.. alright sir"
    scene johndytwonypwr 3 with Dissolve(0.8)
    Patricia "Sir may i ask why are you doing this? I mean wouldn't she-"
    John "I believe that's none of your concern patricia."
    scene johndytwonypwr 4 with Dissolve(0.8)
    Patricia "My apologies , I was just wondering so-"
    John "It's to sweeten the lamb before you have it for yourself , I'm going to treat her until i get my hands on her"
    scene johndytwonypwr 5 with Dissolve(0.8)
    John "Is the meeting with those arabs confirmed?"
    Patricia "Yes sir , it'll happen next week"
    scene johndytwonypwr 6 with Dissolve(0.8)
    John "Perefct timing , evelyn will be gone by then too"
    Patricia "Sir , I have one more question if you don't mind"
    scene johndytwonypwr 7 with Dissolve(0.8)
    John "What is it?"
    scene johndytwonypwr 8 with Dissolve(0.8)
    Patricia "You wear the most expensive clothing and suits , however you never wear a tie.. why?"
    scene johndytwonypwr 9 with Dissolve(0.8)
    John "Glad you asked , It's something i get asked often so you should know too"
    scene johndytwonypwr 10 with Dissolve(0.8)
    John "Those who wear a tie are beneath someone, having to follow orders and answer to someone higher than them.."
    scene johndytwonypwr 11 with Dissolve(0.8)
    John "I answer to no one. I am at the top of this city, and soon, this country too."
    scene johndytwonypwr 12 with Dissolve(0.8)
    Patricia "You're really going to run for it?"
    John "I will , hell veronica will help me do it"
    scene johndytwonypwr 13 with Dissolve(0.8)
    John "Now then, let's get going. We have a long day ahead of us. Is everything ready?"
    Patricia "Yes sir , driver is waiting outside"
    scene johndytwonypwr 14 with Dissolve(0.8)
    John "( This is just the beginning )"
    scene johndytwonypwr 15 with Dissolve(0.8)
    "Security discom" "Alpha target is moving , Z security inbound"
    scene johndytwonypwr 16 with Dissolve(0.8)
    pause
    scene johndytwonypwr 17 with Dissolve(0.8)
    Patricia "(This much money..)"
    scene johndytwonypwr 18 with Dissolve(0.8)
    pause
    scene johndytwonypwr 19 with Dissolve(0.8)
    Patricia "(This much power)"
    scene johndytwonypwr 20 with Dissolve(0.8)
    Patricia "(Kiara.. , be safe)"
    John "Something bothering you patricia?"
    scene johndytwonypwr 21 with Dissolve(0.8)
    Patricia "No nothing sir , just.. i can't ever get used to this"
    scene johndytwonypwr 22 with Dissolve(0.8)
    John "You should , we only get higher from here."
    jump chap_2_scene_42


label chap_2_scene_42:
    scene blackscreen
    show titletext "Serkis house , Queens , NY" with dissolve
    pause 1.0
    window hide
    scene bg jennifrhmdytwo 1 with Dissolve(0.8)
    pause
    scene bg jennifrhmdytwo 2 with Dissolve(0.8)
    Jennifer "( Didn't want you to be lead on.. )"
    scene bg jennifrhmdytwo 3 with Dissolve(0.8)
    Jennifer "( You and i weren't meant to be..)"
    scene bg jennifrhmdytwo 4 with Dissolve(0.8)
    Jennifer "( How could he say those things.. I waited 5 years for him)"
    scene bg jennifrhmdytwo 5 with Dissolve(0.8)
    Jennifer "( Ah , i should just give up on love at this point.. it clearly isn't for me.)"
    scene bg jennifrhmdytwo 6 with Dissolve(0.8)
    Jennifer "I should just take a vacation after this case ends , maybe start something new"
    scene bg jennifrhmdytwo 7 with Dissolve(0.8)
    pause
    scene bg jennifrhmdytwo 8 with Dissolve(0.8)
    Jennifer "Hawaii , might be a nice break spot"
    scene bg jennifrhmdytwo 9 with Dissolve(0.8)
    Jennifer "At least I'm fit , I'm sure i can find someone that'd appreciate me better "
    scene bg jennifrhmdytwo 10 with Dissolve(0.8)
    Jennifer "Of course they will , I have a beautiful body after all"
    scene bg jennifrhmdytwo 11 with Dissolve(0.8)
    Jennifer "I wonder how it feels when a guy squeezes these.. , It feels so good on my own already"
    scene bg jennifrhmdytwo 12 with Dissolve(0.8)
    Jennifer "Wonder how it feels to have a tongue around these nipples"
    scene bg jennifrhmdytwo 13 with Dissolve(0.8)
    Jennifer "I'm definitely going to hook up with someone on that vacation.."
    scene bg jennifrhmdytwo 14 with Dissolve(0.8)
    Jennifer "Ah those bathroom pictures of mason don't really help.. , I wonder how big he is as well"
    scene bg jennifrhmdytwo 15 with Dissolve(0.8)
    Jennifer "I'd love to just ride  a big dick.. , It's been so long"
    scene bg jennifrhmdytwo 16 with Dissolve(0.8)
    Jennifer "(Fuck i am horny again..)"
    scene bg jennifrhmdytwo 17 with Dissolve(0.8)
    Jennifer "(Umf.. mason , don't you want to fuck me?)"
    scene bg jennifrhmdytwo 18 with Dissolve(0.8)
    "Servant" "Ms. Jennifer! , a guests has arrived"
    Jennifer "Tell them i'm busy!"
    scene bg jennifrhmdytwo 19 with Dissolve(0.8)
    "Servant" "Uh , mam it's a woman i don't recognize her , she said she's a previous client!"
    Jennifer "Ah cmon.. I was just getting started, Okay! i'm coming!"
    scene bg jennifrhmdytwo 20 with Dissolve(0.8)
    Jennifer "Previous client? Who could it even be? pretty sure i won all cases"
    scene bg jennifrhmdytwo 21 with Dissolve(0.8)
    Jennifer "Oh.. It's you"
    scene bg jennifrhmdytwo 22 with Dissolve(0.8)
    Jennifer "Sachiko.. , What brings you here?"
    scene bg jennifrhmdytwo 23 with Dissolve(0.8)
    Sachiko "What? Am i not allowed to visit?"
    Jennifer "I didn't mean it that way , I mean i didn't expect you to after-"
    scene bg jennifrhmdytwo 24 with Dissolve(0.8)
    Sachiko "After you gave me 50 million to stay quiet about that man?"
    Jennifer "Sachiko i helped you despite fighting a case for him , maybe-"
    scene bg jennifrhmdytwo 25 with Dissolve(0.8)
    Sachiko "Maybe what?"
    Jennifer "Maybe you should be thankful , you even have your kids custody"
    scene bg jennifrhmdytwo 26 with Dissolve(0.8)
    Sachiko "Kids that barely are attached to me since he just corrupted their minds , should i thank you for that as well?"
    Jennifer "That isn't my fault , look i did what i was asked to and you know it wasn't personal"
    scene bg jennifrhmdytwo 27 with Dissolve(0.8)
    Sachiko "Okay fine , then was what you did in court yesterday , was that personal?"
    Jennifer "Ugh.."
    scene bg jennifrhmdytwo 28 with Dissolve(0.8)
    Sachiko "Don't ugh me , you humiliated mia and mason for what? Nothing but personal gain"
    Jennifer "I didn't do it for personal gain , I was my client's lawyer"
    scene bg jennifrhmdytwo 29 with Dissolve(0.8)
    Sachiko "How long are you going to pretend and be in denial jennifer?"
    Jennifer "I'm not in denial sachiko , my past doesn't concern what i do in the court"
    scene bg jennifrhmdytwo 30 with Dissolve(0.8)
    Jennifer "Also i would appreciate if you-"
    Sachiko "Stop this! , you know what you're doing is wrong. There's still time, that man you're fighting the case of doesn't need you!"
    scene bg jennifrhmdytwo 31 with Dissolve(0.8)
    Jennifer "I don't need him either , look i don't want to rude to you."
    Sachiko "Being rude is fine , being in denial isn't Jen"
    scene bg jennifrhmdytwo 32 with Dissolve(0.8)
    Jennifer "I don't know what you're talking about , Sorry but i think if you're here to lecture me , you should go"
    Sachiko "I'm not here to lecture you , I am here to meet my friend jenny"
    scene bg jennifrhmdytwo 33 with Dissolve(0.8)
    Sachiko "The person who i used to hang out with , to see if she's still somewhat alive"
    scene bg jennifrhmdytwo 34 with Dissolve(0.8)
    Sachiko "Talk to me , you have enough money now.. why do this? Does the person i remember even exist anymore?"
    Jennifer "I'm afraid she died long ago sachi , Sorry."
    scene bg jennifrhmdytwo 35 with Dissolve(0.8)
    Jennifer "After dad passed away , I killed that weak version of me"
    Sachiko "It wasn't weak , It was what your father was proud of . Jen please make the right choice"
    scene bg jennifrhmdytwo 36 with Dissolve(0.8)
    Jennifer "Mason could've made the right choice too , what did he do?"
    Sachiko "Mason didn't love you , it was one sided and you know that deepdown"
    scene bg jennifrhmdytwo 37 with Dissolve(0.8)
    Sachiko "I made the same mistake thinking john loved me , but i know now it was just a waste of time"
    Jennifer "I'm sorry you felt that sachiko , but i've made my choice , you can leave now."
    scene bg jennifrhmdytwo 38 with Dissolve(0.8)
    Sachiko "Fine , I will.. but one last thing."
    Sachiko "One day , when all this has ended . You'll be sitting alone someplace hating yourself for all that happened"
    scene bg jennifrhmdytwo 39 with Dissolve(0.8)
    Sachiko "At that time , you might consider an escape that might seem beneficial to you.."
    scene bg jennifrhmdytwo 40 with Dissolve(0.8)
    Sachiko "So just know , instead of that escape.. I'll be there for you as well. You're not alone okay? I-"
    Jennifer "I need to go to court.. Bye sachiko"
    scene bg jennifrhmdytwo 41 with Dissolve(0.8)
    Sachiko "( Mia.. , I hope you can find yourself again at least.)"
    jump chap_2_scene_43


label chap_2_scene_43:
    scene blackscreen
    show titletext "Sofia's House , Harlem , NY" with dissolve
    pause 1.0
    window hide
    scene bg miasofiatlkny 1 with Dissolve(0.8)
    Sofia "I'm glad you visited , It's about time we talk about this"
    scene bg miasofiatlkny 2 with Dissolve(0.8)
    Sofia "Forgive me if you can mia , I didn't consider he'd do something so extreme"
    scene bg miasofiatlkny 3 with Dissolve(0.8)
    Mia "You don't have to , I was never angry with you and honestly I should've expected it from him."
    scene bg miasofiatlkny 4 with Dissolve(0.8)
    Mia "What i want to know is what happened that day?.. All i remember was signing and then.. nothing"
    Sofia "I remember everything , It haunts to me this day because i failed as a friend and as a doctor"
    scene bg miasofiatlkny 5 with Dissolve(0.8)
    Mia "Just calm down , and tell me... what happened?"
    Sofia "Okay , 2 years ago when kiara and him came.."
    scene bg miasofiatlkny 6 with Dissolve(0.8)
    Kiara "Please just get rid of it , It hurts every second remembering it."
    Sofia "Kiara listen i understand you're-"
    scene bg miasofiatlkny 7 with Dissolve(0.8)
    Kiara "No you don't , I am never giving my heart to anyone again.. how could he? sigh"
    scene bg miasofiatlkny 8 with Dissolve(0.8)
    Sofia "Kiara , perhaps we can just once get him here and-"
    Kiara "No , I don't want to meet him or anyone. I trust you , just please help me."
    scene bg miasofiatlkny 9 with Dissolve(0.8)
    Sofia "Kiara I understand your situation currently but lets at least consider-"
    Kiara "There's nothing to consider , he knew what he was doing sofia."
    scene bg miasofiatlkny 10 with Dissolve(0.8)
    Kiara "He knew how much it'd hurt me , I hate him."
    Sofia "Kiara , damian isn't-"
    scene bg miasofiatlkny 11 with Dissolve(0.8)
    John "Can you not hear what she is saying? We don't want his or your opinion , just get it done"
    Sofia "Mr. Jonathan I am just trying to help"
    scene bg miasofiatlkny 12 with Dissolve(0.8)
    Sofia "Kiara , are you certain of this?.. You don't have to do anything , let me just talk to him and-"
    scene bg miasofiatlkny 13 with Dissolve(0.8)
    John "Keep your trap shut! , If you can't do it then I'll buy this fucking hospital and get it done"
    Sofia "Kindly sit down and don't yell , I'm doing my job"
    scene bg miasofiatlkny 14 with Dissolve(0.8)
    John "Your job is exactly what you aren't doing! , Get to it now!"
    Sofia "She's my fri-.. my patient too! , I have the right to make sure if it's what she wants!"
    scene bg miasofiatlkny 15 with Dissolve(0.8)
    John "She's my daughter! & I want what's the best for her! So do it!"
    Sofia "Don't threaten me! , I'll call security otherwise! So just sit down and let me-"
    scene bg miasofiatlkny 16 with Dissolve(0.8)
    Kiara "Two years.. , All those memories and he just threw them all for pleasure , How could he?"
    scene bg miasofiatlkny 17 with Dissolve(0.8)
    John "Look at how hurt she is! Do you still need any more evaluation?"
    Sofia "Kiara , Sigh.. Fine i'll do it."
    scene blackscreen
    show titletext "Two hours later.." with dissolve
    pause 1.0
    window hide
    scene bg miasofiatlkny 18 with Dissolve(0.8)
    Doctor "You go get the signature from the mother , I'll give her the anesthisia "
    Sofia "Alright , please don't start till i come. I want to be here for her"
    scene bg miasofiatlkny 19 with Dissolve(0.8)
    Doctor "Rest assured , Go on ahead. I'll set everything up"
    Sofia "(Kiara , I'm only doing this for you..)"
    scene bg miasofiatlkny 20 with Dissolve(0.8)
    Sofia "Mia , are you sure about this?"
    Mia "I just want my baby to be happy , do whatever it takes."
    scene bg miasofiatlkny 21 with Dissolve(0.8)
    Sofia "I will make sure she's stable and in good hands , have faith in me"
    Mia "Thank you , please go be with her.. My head hurts."
    scene bg miasofiatlkny 22 with Dissolve(0.8)
    Sofia "Alright , time to beign"
    scene bg miasofiatlkny 23 with Dissolve(0.8)
    Sofia "Huh?.. why won't the door open?"
    scene bg miasofiatlkny 24 with Dissolve(0.8)
    Sofia "What?.. those maps?!"
    scene bg miasofiatlkny 25 with Dissolve(0.8)
    Sofia "Sir! , the- the maps! , They're extended! The door won't open , could you just?-"
    Doctor "I'm sorry sofia"
    scene bg miasofiatlkny 26 with Dissolve(0.8)
    Sofia "W-what?"
    Doctor "It is too much money to decline , forgive me."
    scene bg miasofiatlkny 27 with Dissolve(0.8)
    Sofia "What?! , No! hey open the door!"
    scene bg miasofiatlkny 28 with Dissolve(0.8)
    Sofia "Mia! , look what they're doing they-"
    scene bg miasofiatlkny 29 with Dissolve(0.8)
    Sofia "No.. , what the hell is happening?"
    scene bg miasofiatlkny 30 with Dissolve(0.8)
    John "Having any problems , Doctor sofia?"
    Sofia "You.. , you planned this."
    scene bg miasofiatlkny 31 with Dissolve(0.8)
    Sofia "Sir! , please open the door! She's my friend!!"
    Doctor "Sorry sofia , I'm afraid I cannot."
    scene bg miasofiatlkny 32 with Dissolve(0.8)
    Sofia "Open the fucking door! , You bastard!"
    John "Such words do not suit a doctor's mouth Ms. Sofia , perhaps you should get some fresh air."
    scene bg miasofiatlkny 33 with Dissolve(0.8)
    John "I raised her and she's mine , no way some fucking southern twink loser can have her"
    Sofia "Damian?.. you-"
    scene bg miasofiatlkny 34 with Dissolve(0.8)
    John "Take her! , I don't need more distractions."
    Sofia "Open the door , Kiara! hey!"
    scene bg miasofiatlkny 35 with Dissolve(0.8)
    "Guard" "Please come mam , don't make this any harder than it has to be"
    Sofia "No , I can't let this happen."
    scene bg miasofiatlkny 36 with Dissolve(0.8)
    "Guard" "C'mon now , let us take a trip outside"
    Sofia "*Bites*"
    scene bg miasofiatlkny 37 with Dissolve(0.8)
    "Guard" "Ow! you fucking bitch!"
    Sofia "Kiara! , Get up! Listen to me!"
    scene bg miasofiatlkny 38 with Dissolve(0.8)
    Kiara "Ah.. who-?"
    John "Make her unconscious, you idiot!"
    scene bg miasofiatlkny 39 with Dissolve(0.8)
    Doctor "Giving more anesthisia , starting erasure now!."
    Kiara "Uh.. I can't move"
    scene bg miasofiatlkny 40 with Dissolve(0.8)
    Sofia "You can't do this!! , Stop!"
    Doctor "It's too late ! , I'm sorry sofia!"
    scene bg miasofiatlkny 41 with Dissolve(0.8)
    Sofia "Kiara! , Please getup!.."
    John "Faster , keep going"
    scene bg miasofiatlkny 42 with Dissolve(0.8)
    Sofia "That was the last time i saw her , the day i failed"
    Mia "I'm sorry sofia , I hope they didn't hurt you."
    scene bg miasofiatlkny 43 with Dissolve(0.8)
    Sofia "I got out somehow , but it was too late."
    Sofia "The director who took the bribe got disbarred , but john had just imported all he needed by then"
    Mia "So that's how he erased everything before that as well"
    scene bg miasofiatlkny 44 with Dissolve(0.8)
    Sofia "He kept doing it , I don't know how many times without stopping for breaks even. God knows what it did to kiara"
    Mia "Sofia , I am blame for this too... stop hating yourself so much for something you couldn't stop."
    scene bg miasofiatlkny 45 with Dissolve(0.8)
    Sofia "I know , but she trusted me mia and if i had never accepted maybe she'd be still be fine."
    Mia "That boy.. Damian , do you really believe he did it?"
    scene bg miasofiatlkny 46 with Dissolve(0.8)
    Sofia "OF course not! , I don't know.. he never talks to me either now about it  but I don't think damian could do such a thing , he loved her."
    Mia "I know he did , he treated kiara better than anyone and i saw that with my eyes"
    scene bg miasofiatlkny 47 with Dissolve(0.8)
    Sofia "I want to help her badly. I want to make this right. You have to win this case, Mia."
    Mia "I- I  don't know if i can after what happened."
    scene bg miasofiatlkny 48 with Dissolve(0.8)
    Sofia "Then there is another way. It's risky, but it's worth a shot."
    scene bg miasofiatlkny 49 with Dissolve(0.8)
    Mia "what is it? I can take any risk for her.."
    Sofia "No , not you. I have to do it. I have to go into his house and get those map files"
    scene bg miasofiatlkny 50 with Dissolve(0.8)
    Mia "That's too risky sofia , you don't know the kind of man he is"
    Sofia "I know exactly the kind of man he is , don't worry.. I'll be cautious"
    scene bg miasofiatlkny 51 with Dissolve(0.8)
    Mia "Is there really no other way?"
    Sofia "There is , but that would be too complicated to do"
    Sofia "She would have to expirience the same things she got erased , food , clothes , things , events.. that can also trigger it."
    scene bg miasofiatlkny 52 with Dissolve(0.8)
    Sofia "We can't wait or rely on that though , so i have to go get the files"
    Mia "Okay i'll help you anyway i can then , Let's do this"
    scene bg miasofiatlkny 53 with Dissolve(0.8)
    Sofia "Yeah , we're gonna get the kiara we knew back."
    jump chap_2_scene_44

label chap_2_scene_44:
    scene blackscreen
    show titletext "State hospital , Brooklyn" with dissolve
    pause 1.0
    window hide
    scene bg nyjakendevehsptl 1 with Dissolve(0.8)
    Bailey "Thank you so much for coming , It is great to see you finally"
    Jake "As soon as I said it's to meet you, she immediately booked the cab."
    scene bg nyjakendevehsptl 2 with Dissolve(0.8)
    Bailey "That's very nice of you  evelyn , thank you so much"
    Evelyn "Please don't thank me , after hearing the things jake said about you. I had to meet you"
    scene bg nyjakendevehsptl 3 with Dissolve(0.8)
    Evelyn "Aside that though , how are you doing Ms. watson? I mean is it getting better?"
    Bailey "Yes! , I've gotten alot better and the tumor is slowly going away as well , All i need to do is-"
    scene bg nyjakendevehsptl 4 with Dissolve(0.8)
    Jake "Is to rest well and eat fresh fruits and juice"
    Bailey "Well that and good soap operas to watch"
    scene bg nyjakendevehsptl 5 with Dissolve(0.8)
    Evelyn "Please take care of yourself , I'm glad it's getting better but i would love for you to be out of this room one day too."
    Bailey "I certainly will , after all my biggest worry is taken care of. Finally my boy has someone alongside his life journey"
    scene bg nyjakendevehsptl 6 with Dissolve(0.8)
    Jake "( Ah dammit , Mom..)"
    scene bg nyjakendevehsptl 7 with Dissolve(0.8)
    Evelyn "Um ( Partner?.. Ah i see )"
    scene bg nyjakendevehsptl 8 with Dissolve(0.8)
    Evelyn "Yes , you don't need to worry about that at all , he's lovely."
    scene bg nyjakendevehsptl 9 with Dissolve(0.8)
    Bailey "I hope he doesn't bother you too much , if he acts tough just tell me . I'll take care of him"
    Evelyn "Haha thank you , but honestly i'm just as happy too , he's great company"
    scene bg nyjakendevehsptl 10 with Dissolve(0.8)
    Bailey "You hear that jake? Better keep her happy or I'll pull your ear in front of her"
    Jake "Got it mom , but don't worry. I'll make sure she's always smiling."
    scene bg nyjakendevehsptl 11 with Dissolve(0.8)
    Bailey "There was one more thing i needed evelyn if it's alright with you"
    Evelyn "Sure , please ask for anything"
    scene bg nyjakendevehsptl 12 with Dissolve(0.8)
    Bailey "Could you please help jake pick better clothing? All of his outfits are so bad"
    Jake "What? No it isn't haha"
    scene bg nyjakendevehsptl 13 with Dissolve(0.8)
    Evelyn "It actually is , you wear the same clothes but i didn't wanna point it out"
    Bailey "Exactly! see? Even she agrees"
    scene bg nyjakendevehsptl 14 with Dissolve(0.8)
    Jake "But mom they're fashion!"
    Bailey "Honey that is the opposite of fashion"
    scene bg nyjakendevehsptl 15 with Dissolve(0.8)
    Evelyn "Fashion? More like stash them in trash bin"
    Bailey "Hahahaa! , that was a good one evelyn!"
    scene bg nyjakendevehsptl 16 with Dissolve(0.8)
    Jake "( Man , I never thought i'd see mom smile again..)"
    scene bg nyjakendevehsptl 17 with Dissolve(0.8)
    Bailey "I am confident you are the one person who can take care of him when I can't. Thank you, Evelyn."
    Evelyn "We'll both take care of him. For now don't worry, just focus on getting better, Ms. Watson."
    scene bg nyjakendevehsptl 18 with Dissolve(0.8)
    Bailey "Your mother must be proud of having such a insightful and amazing daughter"
    Evelyn "She-.. She is , and I'm proud of having her as my mother too"
    scene bg nyjakendevehsptl 19 with Dissolve(0.8)
    Bailey "Well anyway , My nurse will arrive soon. You kids go on ahead and have a good evening"
    Evelyn "As you wish Ms. Watson"
    scene bg nyjakendevehsptl 20 with Dissolve(0.8)
    Bailey "Take her somewhere nice please jake?"
    Jake "I will , you just rest well okay?"
    scene bg nyjakendevehsptl 21 with Dissolve(0.8)
    Jake "See you later ma!"
    Bailey "Have a lovely evening you both"
    Evelyn "Thanks Ms. Watson , get well soon"
    scene bg nyjakendevehsptl 22 with Dissolve(0.8)
    Evelyn "You weren't wrong , she really is a bit like me"
    Jake "Evelyn , I-"
    scene bg nyjakendevehsptl 23 with Dissolve(0.8)
    Jake "Thank you for.. you know , Lying there."
    Evelyn "Hey if a little pretend act makes her feel better , then i'm all for it"
    scene bg nyjakendevehsptl 24 with Dissolve(0.8)
    Jake "I appreciate it really , I'm sorry if it made you uncomfortable"
    Evelyn "Why would it? Besides, I only lied about the first part. You are great company still, you know?"
    scene bg nyjakendevehsptl 25 with Dissolve(0.8)
    Jake "Thanks , you are too."
    Evelyn "C'mon now , let's go get some ice cream okay?"
    jump chap_2_scene_45

label chap_2_scene_45:
    scene blackscreen
    show titletext "Boyd Hosusehold , Queens" with dissolve
    pause 1.0
    window hide
    scene bg eugnsxscn 1 with Dissolve(0.8)
    Luke "Do you need anything else son?"
    Damian "No i'm fine dad , hope you guys are too"
    Eugine "Why are you up so late sweety? get some rest"
    scene bg eugnsxscn 2 with Dissolve(0.8)
    Eugine "Try some warm milk without sugar , should help you"
    Damian "Yeah I'll go for that , thanks.. mom"
    scene bg eugnsxscn 3 with Dissolve(0.8)
    Luke "When are you coming back then son?"
    Damian "Will take me roughly an week or two , Don't worry i really am alright dad."
    scene bg eugnsxscn 4 with Dissolve(0.8)
    Luke "I am not worried , I am confident in you. She however is quite concerned"
    Eugine "Please just keep us updated , that's all."
    scene bg eugnsxscn 5 with Dissolve(0.8)
    Luke "I'll go get changed , talk to you later damian"
    Damian "Yeah , bye dad."
    scene bg eugnsxscn 6 with Dissolve(0.8)
    Eugine "Do you have money and everything there? Please let me know if you need anything else"
    Damian "I will eugine , right now though i don't need anything"
    scene bg eugnsxscn 7 with Dissolve(0.8)
    Eugine "Why don't you call me mother more often?"
    Damian "You know exactly why i can't , Sorry if it makes you upset"
    scene bg eugnsxscn 8 with Dissolve(0.8)
    Eugine "Damian i am not telling you to forget her , I just want you to give me a try"
    Damian "I did give you that chance , we both know where it ended eugine."
    scene bg eugnsxscn 9 with Dissolve(0.8)
    Eugine "Damian that was a one time mistke , I just wanted you to feel better."
    Damian "What i needed was a hug , not.. what you did."
    scene bg eugnsxscn 10 with Dissolve(0.8)
    Eugine "I just thought it would help since you were stressed"
    Damian "Well you were wrong , Look.. i don't hate you or have anything against you"
    scene bg eugnsxscn 11 with Dissolve(0.8)
    Damian "I just can't forget my mother like that , sorry but you won't replace her eugine"
    Eugine "I know i can't , but we can try at least?"
    Damian "I'll try but i can't promise anything , Bye."
    scene bg eugnsxscn 12 with Dissolve(0.8)
    Eugine "Why does he push me away so much , I only want him to be happy"
    scene bg eugnsxscn 13 with Dissolve(0.8)
    Luke "Hey hun , all good?"
    Eugine "Yes , everything is fine"
    scene bg eugnsxscn 14 with Dissolve(0.8)
    Eugine "I wish he would accept me more"
    Luke "It'll take some time , don't fret over it."
    scene bg eugnsxscn 15 with Dissolve(0.8)
    Luke "How about we relieve a little stress?"
    Eugine "Hm?"
    scene bg eugnsxscn 16 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 17 with Dissolve(0.8)
    Luke "You wore this for me it seems"
    scene bg eugnsxscn 18 with Dissolve(0.8)
    Luke "Love how you never wear a bra you know?"
    menu:
        "Skip scene?"
            
        "Yes":
            jump chap_2_scene_46
        "No":
            pass
    scene bg eugnsxscn 19 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 20 with Dissolve(0.8)
    Luke "It's so much easier to just have some action then"
    scene bg eugnsxscn 21 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 22 with Dissolve(0.8)
    Luke "Look at those babies"
    scene bg eugnsxscn 23 with Dissolve(0.8)
    Eugine "Hm , I wonder if.."
    scene bg eugnsxscn 24 with Dissolve(0.8)
    Eugine "Damian.."
    scene bg eugnsxscn 25 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 26 with Dissolve(0.8)
    Eugine "Hello son , I've been waiting for you"
    Damian "I've been waiting for you as well , let's start mom"
    scene bg eugnsxscn 27 with Dissolve(0.8)
    Eugine "Do you like how they feel?"
    Damian "They're so lovely and fit perfectly in my hands"
    scene bg eugnsxscn 28 with Dissolve(0.8)
    Eugine "Mmm... , your lips are so soft damian"
    scene bg eugnsxscn 29 with Dissolve(0.8)
    Eugine "Come here , I want to taste them"
    scene bg eugnsxscn 30 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 31 with Dissolve(0.8)
    Eugine "Once more.."
    scene bg eugnsxscn 32 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 33 with Dissolve(0.8)
    Eugine "Mmm.. you are mine"
    scene bg eugnsxscn 34 with Dissolve(0.8)
    Eugine "I'm all yours too"
    scene bg eugnsxscn 35 with Dissolve(0.8)
    Eugine "Let mommy make you happy.."
    Damian "Yes, please"
    scene bg eugnsxscn 36 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 37 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 38 with Dissolve(0.8)
    Eugine "Such a nice cock and it is all mine."
    scene bg eugnsxscn 39 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 40 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 41 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 42 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 43 with Dissolve(0.8)
    Eugine "You liking this honey?"
    Damian "I love it , please wrap your lips around it too."
    scene bg eugnsxscn 44 with Dissolve(0.8)
    Damian "Fuck.. those lips feel so good."
    scene bg eugnsxscn 45 with Dissolve(0.8)
    Damian "Look at me while you do it"
    scene bg eugnsxscn 46 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 47 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 48 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 49 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 50 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 51 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 52 with Dissolve(0.8)
    Damian "Ohh.. fuck such a good mouth"
    scene bg eugnsxscn 53 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 54 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 55 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 56 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 57 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 58 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 59 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 60 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 61 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 62 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 63 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 64 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 65 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 66 with Dissolve(0.8)
    Eugine "Hard finally , look at it.. my damian's hard cock"
    Damian "Lick it a bit mommy."
    scene bg eugnsxscn 67 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 68 with Dissolve(0.8)
    Eugine "*Slurrp* , such a nice dick"
    Damian "Oh your tongue is so soft"
    scene bg eugnsxscn 69 with Dissolve(0.8)
    Damian "Mom , I want to make you happy too"
    scene bg eugnsxscn 70 with Dissolve(0.8)
    Eugine "Of course baby , mommy wants it too"
    scene bg eugnsxscn 71 with Dissolve(0.8)
    Damian "Mom , I want this"
    Eugine "Take it , you can have anything you want baby"
    scene bg eugnsxscn 72 with Dissolve(0.8)
    Damian "Let's get you naked"
    Eugine "Yes , no more shame.. strip your mother"
    scene bg eugnsxscn 73 with Dissolve(0.8)
    pause
    scene bg eugnsxscn 74 with Dissolve(0.8)
    Damian "Your ass is better than anyone i've dated mom."
    Eugine "Told you you didn't need anyone else baby"
    scene bg eugnsxscn 75 with Dissolve(0.8)
    Damian "Wow , you smell so nice"
    Eugine "I clean it daily for you"
    scene bg eugnsxscn 76 with Dissolve(0.8)
    Eugine "What are you looking at honey? hehe"
    scene bg eugnsxscn 77 with Dissolve(0.8)
    Damian "Such a soft nice ass , I'm gonna spread it"
    scene bg eugnsxscn 78 with Dissolve(0.8)
    Damian "Oh , what a cute asshole."
    Eugine "Oh my  , you like it?"
    scene bg eugnsxscn 79 with Dissolve(0.8)
    Damian "I wanna eat it , you're so fucking sexy"
    Eugine "Everyhing there is yours , take me how you want to."
    scene bg eugnsxscn 80 with Dissolve(0.8)
    Damian "What a beautiful pussy , It's begging to be fucked "
    Eugine "Don't just stare now , eat it baby"
    scene bg eugnsxscn 81 with Dissolve(0.8)
    Eugine "Mmm... yes , go on keep eating it."
    Damian "*Licking* , It's so wet , you're so fucking wet"
    scene bg eugnsxscn 82 with Dissolve(0.8)
    Damian "*Smooch* Such a soft ass , I love it mom"
    Eugine "I love your lips on it too , those cheeks are ready for you"
    scene bg eugnsxscn 83 with Dissolve(0.8)
    Damian "*Smooch* , I love how you smell mom such a lovely pussy too"
    scene bg eugnsxscn 84 with Dissolve(0.8)
    Eugine "Stop teasing mommy now baby , let's start already"
    scene bg eugnsxscn 85 with Dissolve(0.8)
    Damian "Mom.. I wanna fuck you"
    Eugine "Go for it baby."
    scene bg eugnsxscn 86 with Dissolve(0.8)
    Damian "Oh yeah , I'm gonna fuck you.."
    Eugine "Yes , do it son. I want you inside me."
    scene bg eugnsxscn 87 with Dissolve(0.8)
    Damian "Fuckk , I love how your pussy is wrapping around my tip"
    Eugine "It wants you in.. , don't stop anymore"
    scene bg eugnsxscn 88 with Dissolve(0.8)
    Damian "Ohh fuck , your pussy feels so warm"
    Eugine "Mmm.. yes , It's warm because of you baby."
    scene bg eugnsxscn 89 with Dissolve(0.8)
    Eugine "Awwhh... , Yes pound me.. I love that dick of yours"
    Damian "You want this badly don't you?.. Fuck yeah."
    Eugine "Get faster honey , destroy my cunt"
    scene bg eugnsxscn 90 with Dissolve(0.8)
    Damian "Oh fuck , you're such a slut i love it."
    Eugine "Ohh yes.. fuck mommy baby , Fuck this slutty pussy"
    scene bg eugnsxscn 91 with Dissolve(0.8)
    Eugine "( He feels so good inside me)"
    scene bg eugnsxscn 92 with Dissolve(0.8)
    Eugine " ( Ohh yes baby )"
    scene bg eugnsxscn 93 with Dissolve(0.8)
    Eugine "( Damian fuck me..)"
    scene bg eugnsxscn 94 with Dissolve(0.8)
    Eugine "( Another dream.. what would i not give to make it a reality)"
    scene bg eugnsxscn 95 with Dissolve(0.8)
    Eugine "Honey , can we not do this today? I am not in the mood after talking to him"
    Luke "I understand , that's perfectly fine"
    scene bg eugnsxscn 96 with Dissolve(0.8)
    Eugine "( One day , I won't have to imagine any of that damain.)"
    jump chap_2_scene_46



label chap_2_scene_46:
    scene blackscreen
    show titletext "Valentina's apartment , Harlem" with dissolve
    pause 1.0
    window hide
    scene bg vlntndytwony 1 with Dissolve(0.8)
    Valentina "Ugh , Where could he be? why isn't he picking up?"
    scene bg vlntndytwony 2 with Dissolve(0.8)
    Valentina "C'mon damian , just pick up the phone for once."
    scene bg vlntndytwony 3 with Dissolve(0.8)
    Valentina "For fuck's sake , I can't locate them either.. this sucks"
    scene bg vlntndytwony 4 with Dissolve(0.8)
    Valentina "Ah great, aiden isn't picking up either. What a nuisance"
    Nick "She seems stressed.."
    scene bg vlntndytwony 5 with Dissolve(0.8)
    Valentina "I feel so useless not being able to do anything from here"
    Nick "Babe , you alright?"
    scene bg vlntndytwony 6 with Dissolve(0.8)
    Valentina "Oh.. hi boo , sorry just stressed about you know-"
    Nick "I do.. , what is it that's bothering you?"
    scene bg vlntndytwony 7 with Dissolve(0.8)
    Valentina "I tried to call Damian, but his number is mostly off. Aiden is staying underground, and I can't find Kiara's contact details at all."
    Nick "You're doing what you can from here. Besides, if Aiden is there, I'm sure he'll figure something out."
    scene bg vlntndytwony 8 with Dissolve(0.8)
    Nick "Did you try calling lana?"
    Valentina "I did but she is ignoring me i think , something tells me she's hiding something too"
    scene bg vlntndytwony 9 with Dissolve(0.8)
    Nick "Can't do much from here , she's too far for you to do anything for now"
    Valentina "If only there was a way i could just know where everyone is"
    scene bg vlntndytwony 10 with Dissolve(0.8)
    Nick "Look you've done all you can , leave the rest to aiden. Until you get acess to anything worrying about it won't really solve it"
    Valentina "Yeah i suppose you're right , I should stop thinking so much"
    scene bg vlntndytwony 11 with Dissolve(0.8)
    Nick "Exactly , now what do i get for being right?"
    Valentina "Heh what would you like?"
    Nick "I think you know already"
    scene bg vlntndytwony 12 with Dissolve(0.8)
    Valentina "Mwwah"
    scene bg vlntndytwony 13 with Dissolve(0.8)
    pause
    scene bg vlntndytwony 14 with Dissolve(0.8)
    Nick "I love you okay? Don't worry we'll fix everything eventually."
    Valentina "I love you too boo , alright i'll stop for now"
    scene bg vlntndytwony 15 with Dissolve(0.8)
    Nick "I'm making some pasta , which ones would you like?"
    Valentina "Some pink sauce would be great"
    scene bg vlntndytwony 16 with Dissolve(0.8)
    "Tablet ringing"
    Valentina "Hm?.. who could it be at this time?"
    scene bg vlntndytwony 17 with Dissolve(0.8)
    pause
    scene bg vlntndytwony 18 with Dissolve(0.8)
    "Morphed voice" "What a cute couple you both are,  too bad he'll just be watching while i take you"
    scene bg vlntndytwony 19 with Dissolve(0.8)
    Valentina "You again.. Hey-"
    "Morphed voice" "Imagine it , him tied up to a chair while i spread that pussy of yours with my dick"
    scene bg vlntndytwony 20 with Dissolve(0.8)
    "Morphed voice" "Those boobs too , I am gonna play with them till they're fucking red"
    scene bg vlntndytwony 21 with Dissolve(0.8)
    Valentina "How dare you call agai-"
    "Morphed voice" "That dress and no panties hehe , you dressed for me today didn't you?"
    scene bg vlntndytwony 22 with Dissolve(0.8)
    pause
    scene bg vlntndytwony 23 with Dissolve(0.8)
    "Morphed voice" "Those ass cheeks deserve to be clapped , god you have the body of a fucking pornstar"
    scene bg vlntndytwony 24 with Dissolve(0.8)
    Valentina "You fucking cunt , who are you?!"
    "Morphed voice" "You don't need to know baby."
    scene bg vlntndytwony 25 with Dissolve(0.8)
    Valentina "Answer and talk with your real voice you fucking dipshit! , Who the fuck are you?"
    Nick "what the..?"
    scene bg vlntndytwony 26 with Dissolve(0.8)
    "Morphed voice" "Want me that bad hehe?"
    Valentina "Oh yeah i fucking do , I'm going to gut you like a fucking fish you bitch"
    Nick "Babe! hey!"
    scene bg vlntndytwony 27 with Dissolve(0.8)
    Nick "What's wrong?.. who was that?"
    Valentina "I..uh , It's nothing babe just a fucking troll"
    scene bg vlntndytwony 28 with Dissolve(0.8)
    Nick "Didn't sound like nothing , look.. how about we take a little break?"
    Valentina "Um?"
    scene bg vlntndytwony 29 with Dissolve(0.8)
    Nick "Let's take a vacation , me and you just like old times"
    Valentina "I would love that.. , where to?"
    scene bg vlntndytwony 30 with Dissolve(0.8)
    Nick "Exactly where you need to be , Let's head to osaka"
    Nick "Yes.. that would be great but let's just cuddle for a bit now"
    scene bg vlntndytwony 31 with Dissolve(0.8)
    Nick "I can make all the time in world for that if it's with you val"
    Valentina "Thank you.."
    scene bg vlntndytwony 32 with Dissolve(0.8)
    Nick "( Kiara , we'll save you stay strong till then. )"
    jump chap_2_scene_47

label chap_2_scene_47:

#masonmeetsjin
    scene blackscreen
    show titletext "Somewhere in downtown.." with dissolve
    pause 1.0
    window hide
    scene bg masonmeetsjin 1 with Dissolve(0.8)
    pause
    scene bg masonmeetsjin 2 with Dissolve(0.8)
    pause
    scene bg masonmeetsjin 3 with Dissolve(0.8)
    pause
    scene bg masonmeetsjin 4 with Dissolve(0.8)
    pause
    scene bg masonmeetsjin 5 with Dissolve(0.8)
    pause
    scene bg masonmeetsjin 6 with Dissolve(0.8)
    "???" "Here it is.."
    scene bg masonmeetsjin 7 with Dissolve(0.8)
    "???" "Thanks for closing the door , people often forget to"
    "???" "It's most likely the distance mate , had to walk 10 miles on foot here"
    scene bg masonmeetsjin 8 with Dissolve(0.8)
    "???" "Extra safety never hurt anyone"
    "???" "Suppose you're right about that"
    scene bg masonmeetsjin 9 with Dissolve(0.8)
    Mason "Now then , shall we start?"
    "???" "Look at the irony though , protector of law needing help from a nobody like me "
    scene bg masonmeetsjin 10 with Dissolve(0.8)
    Mason "Law takes time , What i need to get done is priority."
    "???" "That is true , no doubt on it"
    scene bg masonmeetsjin 11 with Dissolve(0.8)
    "???" "So , did you bring everything i asked for?"
    Mason "Yeah , everyhing is in a file."
    scene bg masonmeetsjin 12 with Dissolve(0.8)
    Mason "When are you leaving then?"
    "???" "Once I've read it."
    scene bg masonmeetsjin 13 with Dissolve(0.8)
    Mason "Look , this is important i hope you-"
    "???" "I undertand quite clearly , you want anything to drink Mr. mason?"
    scene bg masonmeetsjin 14 with Dissolve(0.8)
    Mason "No i'm good , just water would be nice"
    "???" "Bring a glass of water for our client kevin."
    scene bg masonmeetsjin 15 with Dissolve(0.8)
    "???" "So this is kiara , Alright then."

    ##DREAM SCENE 1
    scene blackscreen
    show titletext "2 years ago , central park." with dissolve
    pause 1.0
    window hide
    scene bg dreamscnone 1 with Dissolve(0.8)
    Damian "Do you like it?"
    Kiara "It's quite lovely , but I'm just glad we're spending time together."
    scene bg dreamscnone 2 with Dissolve(0.8)
    Damian "Ditto to that."
    scene bg dreamscnone 3 with Dissolve(0.8)
    Damian "I wanted to bring you here since you said you love gardens"
    scene bg dreamscnone 4 with Dissolve(0.8)
    Kiara "It's actually because of my older sister , she loves nature and it reminds me of her everytime i'm surrounded by it."
    Damian "I'm glad i can make you feel a bit better"
    scene bg dreamscnone 5 with Dissolve(0.8)
    Kiara "you make me feel alot better always , no need for a garden for that"
    Damian "Well there was one more reason i brought you here."
    scene bg dreamscnone 6 with Dissolve(0.8)
    Damian "Don't laugh, but... I wrote a poem for you. I didn't want to embarrass myself, so I thought I'd read it to you alone."
    Kiara "Aheh , damian.. why would i laugh?"
    scene bg dreamscnone 7 with Dissolve(0.8)
    Kiara "However i am curious what kinda poem it is for you to get me all the way here"
    Damian "Okay um , I'll go for it then but don't laugh okay?"
    scene bg dreamscnone 8 with Dissolve(0.8)
    Kiara "PInky promise i won't , now cmon.. say it."
    scene bg dreamscnone 9 with Dissolve(0.8)
    Damian "Time will make the ugly lovely , Time will make the lovely ugly"
    scene bg dreamscnone 10 with Dissolve(0.8)
    Damian "Time will turn.. me into somethng , then time will turn me into nothing."
    scene bg dreamscnone 11 with Dissolve(0.8)
    Damian "So I'll be gone one day either way , will you be with me till that day?"
    Kiara "Damian.."
    scene bg dreamscnone 12 with Dissolve(0.8)
    Damian "You don't like it?"
    scene bg dreamscnone 13 with Dissolve(0.8)
    Kiara "I'll make sure such a time never comes in our space"
    scene bg dreamscnone 14 with Dissolve(0.8)
    Kiara "So you can stop worrying and keep a lovely smile on that face"
    Damian "Heh.. wow."
    scene bg dreamscnone 15 with Dissolve(0.8)
    Damian "Took me 2 weeks to write that , and you just.. said the best follow up to it"
    scene bg dreamscnone 16 with Dissolve(0.8)
    Kiara "It's because i want you to know that i'm happy with you , so if you try two times , I'll do four."
    scene bg dreamscnone 17 with Dissolve(0.8)
    Damian "I love you , more than anything in this world."
    Kiara "Prove it.. Kiss me."
    scene bg dreamscnone 18 with Dissolve(0.8)
    Damian "Yeah.. Of course."
    scene bg dreamscnone 19 with Dissolve(0.8)
    pause
    scene bg dreamscnone 20 with Dissolve(0.8)
    Damian "Wh.. no , not again."
    scene bg dreamscnone 21 with Dissolve(0.8)
    Damian "No.. not again , Kiara.."
    scene bg dreamscnone 22 with Dissolve(0.8)
    Damian "Kiara?.. Where'd you go? Comeback!"
    scene bg dreamscnone 23 with Dissolve(0.8)
    show titletext "Present.." with dissolve
    pause 1.0
    window hide
    Damian "KIARA!! DON'T LEAVE ME!"
    scene bg dreamscnone 24 with Dissolve(0.8)
    Damian "Another nightmare.. Kiara."
    scene bg dreamscnone 25 with Dissolve(0.8)
    Damian "Every dream , every memory.. ends this way."
    scene bg dreamscnone 26 with Dissolve(0.8)
    Rin "Um.. lana he-"
    Lana "Rin go get some water"
    scene bg dreamscnone 27 with Dissolve(0.8)
    Rin "Is he?-"
    Lana "Rin just shut up and get some water, go."
    Rin "O-um okay , alright."
    scene bg dreamscnone 28 with Dissolve(0.8)
    Damian "Why? , Why don't they ever stop?"
    Lana "Damian?.. are you okay?"
    scene bg dreamscnone 29 with Dissolve(0.8)
    Damian "I'm not okay , I don't think i ever will be"
    Lana "Hey.. look don't say that , tell me what happened?"
    scene bg dreamscnone 30 with Dissolve(0.8)
    Lana "Was it another nightmare? Kiara?.."
    Lana "Damian?"
    scene bg dreamscnone 31 with Dissolve(0.8)
    Damian "I killed her lana , It was me.."
    Lana "Hey .. no you did no such thing , don't say that."
    scene bg dreamscnone 32 with Dissolve(0.8)
    Damian "If i didn't go to the hotel that day , she wouldn't have-"
    Lana " it wasnt your fault , you know that.. please stop blaming yourself"
    Damian "But Lana i-"
    scene bg dreamscnone 33 with Dissolve(0.8)
    Lana "Not one more word , she would want you to be happy wouldn't she?.. Let's try that okay?"
    scene bg dreamscnone 34 with Dissolve(0.8)
    Damian "Right.. sorry for waking you guys up"
    Lana "It's alright , here drink some water."


    jump chap_2_scene_48

label chap_2_scene_48:
    scene blackscreen
    show titletext "Natsuko's bedroom , Osaka" with dissolve
    pause 1.0
    window hide
    scene bg kiadaythreestrt 1 with Dissolve(0.8)
    pause
    scene bg kiadaythreestrt 2 with Dissolve(0.8)
    pause
    scene bg kiadaythreestrt 3 with Dissolve(0.8)
    Kiara "Ah.. did i leave the lights on?"
    scene bg kiadaythreestrt 4 with Dissolve(0.8)
    Kiara "At least the bed is comfy"
    scene bg kiadaythreestrt 5 with Dissolve(0.8)
    Kiara "Welp , forgot to turn the pc off too.. just great."
    scene bg kiadaythreestrt 6 with Dissolve(0.8)
    "Knock knock"
    Kiara "Hm?"
    scene bg kiadaythreestrt 7 with Dissolve(0.8)
    "Knock knock"
    Kiara "Uhm , coming!.. just a sec"
    scene bg kiadaythreestrt 8 with Dissolve(0.8)
    pause
    scene bg kiadaythreestrt 9 with Dissolve(0.8)
    Kiara "Oh..uhm hey auntie."
    Xia "Sorry , did i wake you up?"
    scene bg kiadaythreestrt 10 with Dissolve(0.8)
    Kiara "No just didn't sleep that well so a bit tired , good morning to you though"
    Xia "I see , well would you like some refreshing tea then?"
    scene bg kiadaythreestrt 11 with Dissolve(0.8)
    Kiara "That's a great idea! , I'll go make some"
    Xia "No need for that honey"
    scene bg kiadaythreestrt 12 with Dissolve(0.8)
    Xia "I made it for you already , Come.. let's have a little breakfast too"
    Kiara "Awesome! , let's get going"
    scene bg kiadaythreestrt 13 with Dissolve(0.8)
    Kiara "Auntie I love how your house captures everything so properly about japan"
    Xia "It's your house too , I decided today for breakfast here so you can enjoy some natural air"
    scene bg kiadaythreestrt 14 with Dissolve(0.8)
    Xia "Besides you look better in a kimono then i do , so i have some clothing for you today that you might like"
    Kiara "I'll definitely wear it , thanks again for all this."
    scene bg kiadaythreestrt 15 with Dissolve(0.8)
    Kiara "So that's the tea?"
    Xia "Well it's a little bit more than just tea , It's herbal sake"
    scene bg kiadaythreestrt 16 with Dissolve(0.8)
    Kiara "There's a little bit of fish too ! , Thanks auntie had been a while"
    Xia "I'm glad you like it."
    scene bg kiadaythreestrt 17 with Dissolve(0.8)
    Xia "So shall we dig in?"
    Kiara "Certainly!"
    scene bg kiadaythreestrt 18 with Dissolve(0.8)
    Xia "Take a small sip , and then just breath in"
    scene bg kiadaythreestrt 19 with Dissolve(0.8)
    Kiara "( Mm... this is so refreshing )"
    scene bg kiadaythreestrt 20 with Dissolve(0.8)
    Xia "( Seems she likes it after all )"
    scene bg kiadaythreestrt 21 with Dissolve(0.8)
    Xia "Here eat some too sweetheart"
    Kiara "Yes , please you have some too"
    scene bg kiadaythreestrt 22 with Dissolve(0.8)
    Kiara "This is so good auntie , You gotta teach me how to make these dishes"
    Xia "Plenty of time for us to learn , for now you enjoy the food"
    scene bg kiadaythreestrt 23 with Dissolve(0.8)
    Xia "Would you like some more tea?"
    Kiara "Yes!"
    scene bg kiadaythreestrt 24 with Dissolve(0.8)
    Kiara "Please you take some too , otherwise i'll feel fat haha"
    Xia "As you wish so , I believe you're very fit though "
    scene bg kiadaythreestrt 25 with Dissolve(0.8)
    Kiara "(Why can't life just be like this?..)"
    scene bg kiadaythreestrt 26 with Dissolve(0.8)
    Xia "Did you say anything? also more tea?"
    Kiara "Oh nothing , just.. wish i was here sooner."
    scene bg kiadaythreestrt 27 with Dissolve(0.8)
    Kiara "Oh, and no, no more tea, Auntie. I'm full. Haha, that was great though.."
    scene bg kiadaythreestrt 28 with Dissolve(0.8)
    Xia "You're here now , that's all that matters"
    Kiara "I wish mom was here too"
    scene bg kiadaythreestrt 29 with Dissolve(0.8)
    Kiara "I also wish my sister was here , Its been so long since i met her"
    Xia "That time will come too sweetheart"
    scene bg kiadaythreestrt 30 with Dissolve(0.8)
    Kiara "That garden looks so nice , I would honestly just live in this room for that view "
    scene bg kiadaythreestrt 31 with Dissolve(0.8)
    Xia "Well why just see it then? Come let's bask in some fresh air"
    scene bg kiadaythreestrt 32 with Dissolve(0.8)
    Kiara "Oh you were defintely right about fresh air , I can smell the grass"
    Xia "I've grown up in this garden , I'm glad you like it too."
    scene bg kiadaythreestrt 33 with Dissolve(0.8)
    Kiara "Is that where you?-"
    Xia "Yes , I still bath there when i can."
    scene bg kiadaythreestrt 34 with Dissolve(0.8)
    Xia "Father used to walk your mom and me on this path , this is where we took our first steps"
    Kiara "That is fascinating.. so that's why you kept some of the house old japanese style too"
    scene bg kiadaythreestrt 35 with Dissolve(0.8)
    Xia "Exactly , I never want to miss any of it so i've kept it how it was"
    Kiara "I don't miss much from home there.. except mom's lap"
    scene bg kiadaythreestrt 36 with Dissolve(0.8)
    Kiara "Resting my head in it felt great , I could just stop worrying about things easily"
    Xia "(Kiara..)"
    scene bg kiadaythreestrt 37 with Dissolve(0.8)
    Xia "You miss mia alot don't you?"
    Kiara "I'd be lying if i said no , but i know she can't come right now"
    scene bg kiadaythreestrt 38 with Dissolve(0.8)
    Xia "She'll come soon , don't trouble yourself over it"
    scene bg kiadaythreestrt 39 with Dissolve(0.8)
    Kiara "I know , but it'd be kinda nice to just not worry about things again for a bit"
    scene bg kiadaythreestrt 40 with Dissolve(0.8)
    Xia "Well i don't know if i can replace it , but i have a lap too if you'd like it"
    Kiara "Really? can i?"
    Xia "Of course you can"
    scene bg kiadaythreestrt 41 with Dissolve(0.8)
    Kiara "Ahh... , Okay this is nice"
    scene bg kiadaythreestrt 42 with Dissolve(0.8)
    Xia "Do you find it comfortable?"
    Kiara "Comfortable?"
    scene bg kiadaythreestrt 43 with Dissolve(0.8)
    Kiara "This is better than any pillow in the house"
    Xia "Ahehe , thank you I'm happy to be of service "
    scene bg kiadaythreestrt 44 with Dissolve(0.8)
    Xia "You know , I'm very happy you're here too."
    scene bg kiadaythreestrt 45 with Dissolve(0.8)
    Xia "To me you're one of the most best things that happened to our family"
    scene bg kiadaythreestrt 46 with Dissolve(0.8)
    Xia "There's nothing else i would want then for our entire family to be here again"
    scene bg kiadaythreestrt 47 with Dissolve(0.8)
    Xia "That plate over there , It's what your grandfather used to eat in"
    scene bg kiadaythreestrt 48 with Dissolve(0.8)
    Xia "Those little statues in corner , your mother made those"
    scene bg kiadaythreestrt 49 with Dissolve(0.8)
    Xia "That tree there was a little seed when i planted it"
    scene bg kiadaythreestrt 50 with Dissolve(0.8)
    Xia "All of these things , they stay with me.. I try my best to keep them intact always"
    scene bg kiadaythreestrt 51 with Dissolve(0.8)
    Xia "Everything was going so well till father left us.. , then everything changed"
    scene bg kiadaythreestrt 52 with Dissolve(0.8)
    Xia "Without family there is no value in life , wouldn't you agree kiara?"
    scene bg kiadaythreestrt 53 with Dissolve(0.8)
    Xia "Kiara?.."
    scene bg kiadaythreestrt 54 with Dissolve(0.8)
    Xia "Heh .. fell asleep like a baby."
    scene bg kiadaythreestrt 55 with Dissolve(0.8)
    Xia "( This is what john took from mia ... I'll make him pay one day)"
    scene bg kiadaythreestrt 56 with Dissolve(0.8)
    Xia "Look at her, smiling so peacefully. How could someone ever take this away?"
    scene bg kiadaythreestrt 57 with Dissolve(0.8)
    Xia "I don't want to wake you up.. but i know you have plans today."
    scene bg kiadaythreestrt 58 with Dissolve(0.8)
    Xia "Mia , don't you worry I'm taking care of her here.."
    scene bg kiadaythreestrt 59 with Dissolve(0.8)
    Xia "Kiara?..honey?"
    scene bg kiadaythreestrt 60 with Dissolve(0.8)
    Xia "Sweetheart ? Get up ?"
    scene bg kiadaythreestrt 61 with Dissolve(0.8)
    Xia "Get up little bean , you have plans today"
    Kiara "Uhm.. ah"
    scene bg kiadaythreestrtdcd with Dissolve(0.8)
    menu:
        "Get up":
            jump .part_1
        "Open your eyes":
            jump .part_2
    
    label .part_2:
        scene bg kiawakeupsee 1 with Dissolve(0.8)
        Xia "There you go , come on up."
        scene bg kiawakeupsee 2 with Dissolve(0.8)
        Kiara "Ah.."
        Xia "C'mon , C'mon slow and easy"
        scene bg kiawakeupsee 3 with Dissolve(0.8)
        pause
        scene bg kiawakeupsee 4 with Dissolve(0.8)
        Xia "Slow and easy , there we go"
        jump chap_2_scene_49

    label .part_1:

        scene bg wakewithoutseeing 1 with Dissolve(0.8)
        Xia "There you go , come on up."
        scene bg wakewithoutseeing 2 with Dissolve(0.8)
        Xia "C'mon , C'mon slow and easy"
        scene bg wakewithoutseeing 3 with Dissolve(0.8)
        pause
        scene bg wakewithoutseeing 4 with Dissolve(0.8)
        Kiara "Uahm.."
        scene bg wakewithoutseeing 5 with Dissolve(0.8)
        Xia "Ah!.. um"
        scene bg wakewithoutseeing 6 with Dissolve(0.8)
        Kiara "Hm?"
        scene bg wakewithoutseeing 7 with Dissolve(0.8)
        Kiara "Oh no.."
        scene bg wakewithoutseeing 8 with Dissolve(0.8)
        Kiara "Um.. auntie , I didn't mean to do that."
        scene bg wakewithoutseeing 9 with Dissolve(0.8)
        Kiara "I should've been careful sorry-"
        scene bg wakewithoutseeing 10 with Dissolve(0.8)
        Xia "Hey , It's completely fine."
        Kiara "Are you sure?"
        scene bg wakewithoutseeing 11 with Dissolve(0.8)
        Xia "Yes , besides your lips are quite soft so it almost felt like nothing"
        scene bg wakewithoutseeing 12 with Dissolve(0.8)
        Xia "Look at that , now you're blushing too. How much more pink are you gonna get?"
        scene bg wakewithoutseeing 13 with Dissolve(0.8)
        Kiara "I just blush easily i think"
        Xia "That's good , because you look lovely when doing it"
        scene bg wakewithoutseeing 14 with Dissolve(0.8)
        Kiara "Okay. let's get up now"
        Xia "Slow and easy , there we go"
        jump chap_2_scene_49

label chap_2_scene_49:

    scene bg kiaaftrwake 1 with Dissolve(0.8)
    Xia "Did you sleep well this time?"
    Kiara "Yeah.. I did , thank you"
    scene bg kiaaftrwake 2 with Dissolve(0.8)
    Xia "We should do this more often then?"
    Kiara "I would love to"
    scene bg kiaaftrwake 3 with Dissolve(0.8)
    Xia "I would love to accompany you too"
    Kiara "You're the best auntie , this helps alot thank you really."
    scene bg kiaaftrwake 4 with Dissolve(0.8)
    Xia "Most welcome , so anything else you wanted to say? Or should we start our day?"
    scene bg kiaaftrwake dcd with Dissolve(0.8)
    Kiara "Well I guess I-"
    menu:
        "Suggest to train":
            jump .part_1
        "Go get ready":
            jump .part_2

    label .part_1:

        scene bg traindaythreeyes 1 with Dissolve(0.8)
        Kiara "Um , well there's still time so i was thinking we could train again?"
        Xia "Would yo like to? I would love to accompany you if so."
        scene bg traindaythreeyes 2 with Dissolve(0.8)
        Kiara "Of course , I think i'm getting used to it as well now so"
        Xia "Alright , Let's move above basics today then"
        scene blackscreen
        show titletext "30 Minutes later.." with dissolve
        pause 1.0
        window hide
        scene bg traindaythreeyes 3 with Dissolve(0.8)
        Xia "You're starting to get speed kiara , but what you need is more power"
        Kiara "Um I think I'm quite strong"
        scene bg traindaythreeyes 4 with Dissolve(0.8)
        Xia "Quite isn't enough , we either reach the top or no start at all."
        Kiara "I see , so how do we get started"
        scene bg traindaythreeyes 5 with Dissolve(0.8)
        Xia "This would require alot more than one session"
        Kiara "Okay that's perfectly fine , I am sure i can reach it."
        scene bg traindaythreeyes 6 with Dissolve(0.8)
        Xia "Confidence is good kiara , but what you also need is focus"
        scene bg traindaythreeyes 7 with Dissolve(0.8)
        Xia "If you don't have focus , It's a mere waste time of time leaving you weak"
        scene bg traindaythreeyes 8 with Dissolve(0.8)
        Xia "Tell me do you want to remain weak?"
        scene bg traindaythreeyes 9 with Dissolve(0.8)
        Kiara "No , I don't . Let's begin"
        scene bg traindaythreeyes 10 with Dissolve(0.8)
        Xia "So today won't be movement , I want you to just do one thing only."
        Xia "Get in your stance"
        Kiara "Alright , I have it."
        scene bg traindaythreeyes 11 with Dissolve(0.8)
        Xia "See carefully , your stronger arm is the right one , So we'll go with that"
        Kiara "Um okay.. Sure."
        scene bg traindaythreeyes 12 with Dissolve(0.8)
        Xia "So what i want you to do is do a punch"
        Kiara "Um.. a punch? Auntie i don't want to-"
        scene bg traindaythreeyes 13 with Dissolve(0.8)
        Xia "Not me , this palm.. if you can move it with your punch , we end training today."
        Kiara "But why the palm? uh okay.. sure."
        scene bg traindaythreeyes 14 with Dissolve(0.8)
        Xia "Remmeber , Don't hold back."
        scene bg traindaythreeyes 15 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 16 with Dissolve(0.8)
        Kiara "Haaa!"
        scene bg traindaythreeyes 17 with Dissolve(0.8)
        Kiara "What the.."
        scene bg traindaythreeyes 18 with Dissolve(0.8)
        Kiara "It didn't even flinch?"
        scene bg traindaythreeyes 19 with Dissolve(0.8)
        Kiara "How did you-"
        Xia "Again!"
        scene bg traindaythreeyes 20 with Dissolve(0.8)
        Kiara "Um?"
        Xia "Throw another , keep doing it till it moves."
        scene bg traindaythreeyes 21 with Dissolve(0.8)
        Kiara "Alright , I can do this."
        scene bg traindaythreeyes 22 with Dissolve(0.8)
        Xia "Kiara , don't be weak"
        Kiara "I'm not weak.. I just need to focus"
        scene bg traindaythreeyes 23 with Dissolve(0.8)
        Kiara "Okay , here goes nothing"
        scene bg traindaythreeyes 24 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 25 with Dissolve(0.8)
        Kiara "Ha!"
        scene bg traindaythreeyes 26 with Dissolve(0.8)
        Kiara "Seriously?.."
        scene bg traindaythreeyes 27 with Dissolve(0.8)
        Kiara "How can you just-?"
        Xia "I can do it because you're not focused"
        scene bg traindaythreeyes 28 with Dissolve(0.8)
        Kiara "I'm putting all my power in it!"
        Xia "You're using what you used to have , what you need is more from inside that's hidden."
        scene bg traindaythreeyes 29 with Dissolve(0.8)
        Kiara "How?"
        Xia "Channel it , you have it within you like i said"
        scene bg traindaythreeyes 30 with Dissolve(0.8)
        Kiara "But i can't feel any of it"
        Xia "Kiara , focus.. you can't lie to yourself"
        scene bg traindaythreeyes 31 with Dissolve(0.8)
        Xia "I'm not always going to be here , don't you want to protect the ones you care about"
        Kiara "I do , of course i do."
        scene bg traindaythreeyes 32 with Dissolve(0.8)
        Xia "Again then.. now when you throw punch , focus on my words."
        scene bg traindaythreeyes 33 with Dissolve(0.8)
        Xia "Come , remember full power."
        Kiara "Okay."
        scene bg traindaythreeyes 34 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 35 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 36 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 37 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 38 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 39 with Dissolve(0.8)
        Kiara "Ha!"
        scene bg traindaythreeyes 40 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 41 with Dissolve(0.8)
        Xia "Remember the one who took your sister away from you"
        scene bg traindaythreeyes 42 with Dissolve(0.8)
        Kiara "(Tsk..)"
        scene bg traindaythreeyes 43 with Dissolve(0.8)
        Kiara "Hmph!"
        scene bg traindaythreeyes 44 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 45 with Dissolve(0.8)
        Xia "(There it is..)"
        scene bg traindaythreeyes 46 with Dissolve(0.8)
        Xia "Again.."
        Kiara "Okay."
        scene bg traindaythreeyes 47 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 48 with Dissolve(0.8)
        Xia "Left hand now"
        scene bg traindaythreeyes 49 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 50 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 51 with Dissolve(0.8)
        Xia "Remmeber the one , who's the reason behind your mother's suffering"
        scene bg traindaythreeyes 52 with Dissolve(0.8)
        Kiara "Ugh.."
        scene bg traindaythreeyes 53 with Dissolve(0.8)
        Kiara "Hmph!"
        Xia "(So her strength is hatred)"
        scene bg traindaythreeyes 54 with Dissolve(0.8)
        Xia "Good , you did it..Let's-"
        Kiara "No , we keep going."
        scene bg traindaythreeyes 55 with Dissolve(0.8)
        Xia "Okay , again then."
        scene bg traindaythreeyes 56 with Dissolve(0.8)
        Kiara "Strike."
        scene bg traindaythreeyes 57 with Dissolve(0.8)
        Xia "Remmeber the one who broke our family apart"
        scene bg traindaythreeyes 58 with Dissolve(0.8)
        Kiara "HaGh!"
        Xia "Remmeber the one that took your chance of having a normal life away"
        scene bg traindaythreeyes 59 with Dissolve(0.8)
        Kiara "Augh!"
        scene bg traindaythreeyes 60 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 61 with Dissolve(0.8)
        Xia "Remmeber the one you were supposed to look upto kiara"
        scene bg traindaythreeyes 62 with Dissolve(0.8)
        Xia "Remmeber your father"
        scene bg traindaythreeyes 63 with Dissolve(0.8)
        pause
        scene bg traindaythreeyes 64 with Dissolve(0.8)
        Kiara "He's not my father!"
        scene bg traindaythreeyes 65 with Dissolve(0.8)
        Kiara "Hu-?"
        scene bg traindaythreeyes 66 with Dissolve(0.8)
        Kiara "Ah! I can't balance"
        scene bg traindaythreeyes 67 with Dissolve(0.8)
        Xia "Come here.."
        scene bg traindaythreeyes 68 with Dissolve(0.8)
        Kiara "Aunty i don't know what just-"
        scene bg traindaythreeyes 69 with Dissolve(0.8)
        Xia "Kiara hatred is a tool , not what defines you , don't let it control you"
        scene bg traindaythreeyes 70 with Dissolve(0.8)
        Kiara "I'm sorry.. I-"
        Xia "It's okay , anger is a human trait it isn't your fault , I'm sorry for agitating you."
        scene bg traindaythreeyes 71 with Dissolve(0.8)
        Xia "You are better than all of us kiara , you don't need hatred to protect others , your hope is enough."
        scene bg traindaythreeyes 72 with Dissolve(0.8)
        Kiara "How do i channel hope and power then?"
        Xia "You stay you , It'll come from within when you have to protect those you care about."
        scene bg traindaythreeyes 73 with Dissolve(0.8)
        Kiara "Thanks auntie.."
        Xia "I love you , always remember that."
        scene bg traindaythreeyes 74 with Dissolve(0.8)
        Kiara "I love you too , thank you for giving me a life again."
        scene bg traindaythreeyes 75 with Dissolve(0.8)
        Xia "It's my pleasure , c'mon now.. let us go"
        Kiara "(I'll become strong , that's a promise to myself)"
        jump chap_2_scene_50

    label .part_2:
        scene bg traindaythreeno 1 with Dissolve(0.8)
        Kiara "Well i guess nothing really , I should get ready i suppose"
        Xia "Alright then , I'll go get some chores done"
        scene bg traindaythreeno 2 with Dissolve(0.8)
        Kiara "See ya auntie!"
        Xia "Have a great day!"
        scene bg traindaythreeno 3 with Dissolve(0.8)
        Xia "It's like having a second daughter , I definitely don't mind it."
        jump chap_2_scene_50


label chap_2_scene_50:
    scene blackscreen
    show titletext "An hour later.." with dissolve
    pause 1.0
    window hide

    scene bg kiadaythreebathsegmnt 1 with Dissolve(0.8)
    pause
    scene bg kiadaythreebathsegmnt 2 with Dissolve(0.8)
    pause
    scene bg kiadaythreebathsegmnt 3 with Dissolve(0.8)
    Kiara "Alright , bathtime."
    scene bg kiadaythreebathsegmnt 4 with Dissolve(0.8)
    pause
    scene bg kiadaythreebathsegmnt 5 with Dissolve(0.8)
    Kiara "Shit.. i forgot"
    scene bg kiadaythreebathsegmnt 6 with Dissolve(0.8)
    Kiara "God she's-"
    scene bg kiadaythreebathsegmnt 7 with Dissolve(0.8)
    Kiara "She is naked.. what-"
    scene bg kiadaythreebathsegmnt 8 with Dissolve(0.8)
    Kiara "Natsuko! I'm really sorry."
    scene bg kiadaythreebathsegmnt 9 with Dissolve(0.8)
    Natsuko "Aah!, um.. kiara. Shit.. did i leave bathroom unlocked?"
    scene bg kiadaythreebathsegmnt 10 with Dissolve(0.8)
    Kiara "Um yeah but i'm sorry i forgot you slept here last night , so"
    Natsuko "Oh , um.. it's okay."
    scene bg kiadaythreebathsegmnt 11 with Dissolve(0.8)
    Kiara "I'll get going then , enjoy the bath."
    scene bg kiadaythreebathsegmnt 12 with Dissolve(0.8)
    Kiara "Is it fine if i use your bathroom?"
    Natsuko "Yeah sure , um-"
    scene bg kiadaythreebathsegmnt 13 with Dissolve(0.8)
    Natsuko "Kiara! , can you help me a little?"
    Kiara "Sure , what is it?"
    scene bg kiadaythreebathsegmnt 14 with Dissolve(0.8)
    Natsuko "Actually my shoulders hurt alot.. can you help me clean my back? I forgot the brush outside actually so"
    Kiara "Oh.. uh , well where is the brush?"
    scene bg kiadaythreebathsegmnt 15 with Dissolve(0.8)
    Natsuko "I've got no idea , if it's okay can you help? I'm just really sore today"
    scene bg kiadaythreebathsegmnt dcd with Dissolve(0.8)
    Kiara "Well I-"
    pause

    menu:
        "Suggest an alternative":
            jump .part_1
        "Massage Natsuko" if natsuko_fond.current_fondness >= 1:
            jump .part_2

    label .part_1:

        scene bg baththirddayno 1 with Dissolve(0.8)
        Kiara "How about i get you my brush? I have it in the bag"
        scene bg baththirddayno 2 with Dissolve(0.8)
        Natsuko "That'd be great too! , thanks!"
        scene bg baththirddayno 3 with Dissolve(0.8)
        Kiara "Don't mention it , I'll bring it hold on"
        scene bg baththirddayno 4 with Dissolve(0.8)
        Natsuko "(Why was so shy?)"
        scene bg baththirddayno 5 with Dissolve(0.8)
        Natsuko "Ah.. I see"
        scene bg baththirddayno 6 with Dissolve(0.8)
        Natsuko "(Bisexual still after all , Sorry if i made you uncomfortable kia)"
        jump chap_2_scene_51

    label .part_2:


        scene bg baththirddayyes 1 with Dissolve(0.8)
        Kiara "Sure if you're comfortable , I'm too."
        scene bg baththirddayyes 2 with Dissolve(0.8)
        Natsuko "Great! come , I'll sit with my back facing."
        scene bg baththirddayyes 3 with Dissolve(0.8)
        Kiara "Are you comfortable sitting wise?"
        Natsuko "Yeah all good , you can start"
        scene bg baththirddayyes 4 with Dissolve(0.8)
        Kiara "So , why are you sore? what happened?"
        Kiara "Oh nothing , didn't get enough sleep and then during morning walk had a stupid cramp"
        scene bg baththirddayyes 5 with Dissolve(0.8)
        Kiara "Oh , well i hope you feel better. If you can't hang out today it's alright"
        Natsuko "No no! I'm good walking wise just a little pain that's all."
        scene bg baththirddayyes 6 with Dissolve(0.8)
        Kiara "So natsuko , I've been a little curious to ask something"
        Natsuko "About what? I mean sure ask ahead."
        scene bg baththirddayyes 7 with Dissolve(0.8)
        Kiara "What do you think about nobi?"
        Natsuko "Um do you mean? Like as a person?"
        scene bg baththirddayyes 8 with Dissolve(0.8)
        Kiara "Well you know, like as a guy do you find his company good?"
        Natsuko "Heh , um.. he's nice. Like our grocery trip was good , he was quite sweet to me."
        scene bg baththirddayyes 9 with Dissolve(0.8)
        Kiara "He likes you , you know that right?"
        Natsuko "I've known that since we were kids"
        scene bg baththirddayyes 10 with Dissolve(0.8)
        Natsuko "I don't know really.. He's a good guy but right now we're just friends really."
        Kiara "Well he asked me to figure how to have a tea with you  , so i thought i'd tell you"
        scene bg baththirddayyes 11 with Dissolve(0.8)
        Natsuko "Tea with me?.. Heh he could've just asked me directly"
        Kiara "Like you said , grew up together so he's probably just shy"
        scene bg baththirddayyes 12 with Dissolve(0.8)
        Kiara "Well i better get going then"
        Natsuko "Thanks for massage too.. your hands feel really nice by the way"
        scene bg baththirddayyes dcd with Dissolve(0.8)
        Kiara "( Heh , hands feel nice?.. should i continue? )"
        menu:
            "Play with [Natsuko]" if mc_stats.current_corruption >= 40:
                jump .part_3
            "Let it be":
                jump .part_4

        label .part_4:
            scene bg daythreebathmsgnatsuno 1 with Dissolve(0.8)
            Kiara "Well your welcome , I'ma go get ready see you outside soon."
            Natsuko "Okay! , mum dropped the dress on the desk in my room , feel free to wear it!"
            scene bg daythreebathmsgnatsuno 2 with Dissolve(0.8)
            Kiara "Will do , see you soon."
        jump chap_2_scene_51

        label .part_3:

            scene bg daythreebathmsgnatsu 1 with Dissolve(0.8)
            Natsuko "Ahm , kiara?"
            scene bg daythreebathmsgnatsu 2 with Dissolve(0.8)
            Natsuko "What are you doing? I thought you had to go"
            Kiara "Well you said my hands felt nice , i figured a extended massage wouldn't hurt"
            scene bg daythreebathmsgnatsu 3 with Dissolve(0.8)
            Natsuko "Oh , well great then. Please do"
            Kiara "Let me just eh , sit properly."
            scene bg daythreebathmsgnatsu 4 with Dissolve(0.8)
            Kiara "Alright , now what do you want to massage?"
            Natsuko "Um , anything really. My whole body is sore so the more relaxation i get is better"
            scene bg daythreebathmsgnatsu 5 with Dissolve(0.8)
            Kiara "I think i know just the place then"
            scene bg daythreebathmsgnatsu 6 with Dissolve(0.8)
            pause
            scene bg daythreebathmsgnatsu 7 with Dissolve(0.8)
            Natsuko "Um.."
            scene bg daythreebathmsgnatsu 8 with Dissolve(0.8)
            Natsuko "Ah.."
            scene bg daythreebathmsgnatsu 9 with Dissolve(0.8)
            Kiara "what's wrong?"
            Natsuko "N-nothing i'm just a little sensitive."
            scene bg daythreebathmsgnatsu 10 with Dissolve(0.8)
            Kiara "Sensitive where?"
            Natsuko "Just you know..my-"
            scene bg daythreebathmsgnatsu 11 with Dissolve(0.8)
            Kiara "Here?"
            Natsuko "Uhm! , ah yeah.."
            scene bg daythreebathmsgnatsu 12 with Dissolve(0.8)
            Kiara "Are you getting a little turned on?"
            Natsuko "Nu- no , I mean yeah , no of course not."
            scene bg daythreebathmsgnatsu 13 with Dissolve(0.8)
            Kiara "You don' thave to explain , It's natural you know."
            Natsuko "um.. but i'm not really-"
            scene bg daythreebathmsgnatsu 14 with Dissolve(0.8)
            Kiara "How about we play a little game? I'll massge you and if i hear a moan you owe me a ice cream or vice versa"
            Natsuko "S-sure okay."
            scene bg daythreebathmsgnatsu 15 with Dissolve(0.8)
            Kiara "Don't worry , just a little game between us , no harm done here."
            scene bg daythreebathmsgnatsu 16 with Dissolve(0.8)
            Natsuko "Okay.. Let's start I'm sure i can handle it."
            scene bg daythreebathmsgnatsu 17 with Dissolve(0.8)
            pause
            scene bg daythreebathmsgnatsu 18 with Dissolve(0.8)
            Kiara "Handle it huh?.. let's see"
            scene bg daythreebathmsgnatsu 19 with Dissolve(0.8)
            Natsuko "(Um.. why do her fingers feel so good against my skin)"
            scene bg daythreebathmsgnatsu 20 with Dissolve(0.8)
            Natsuko "(She's rotating her fingers around them now too..)"
            scene bg daythreebathmsgnatsu 21 with Dissolve(0.8)
            Kiara "(It's not the breasts.. I wonder if-)"
            scene bg daythreebathmsgnatsu 22 with Dissolve(0.8)
            pause
            scene bg daythreebathmsgnatsu 23 with Dissolve(0.8)
            pause
            scene bg daythreebathmsgnatsu 24 with Dissolve(0.8)
            pause
            scene bg daythreebathmsgnatsu 25 with Dissolve(0.8)
            Natsuko "(Ah!)"
            scene bg daythreebathmsgnatsu 26 with Dissolve(0.8)
            Kiara "(Ahan , so her nipples are the weak spot)"
            scene bg daythreebathmsgnatsu 27 with Dissolve(0.8)
            Natsuko "Uhm.. I'm fine yeah.."
            scene bg daythreebathmsgnatsu 28 with Dissolve(0.8)
            Kiara "Are you?"
            scene bg daythreebathmsgnatsu 29 with Dissolve(0.8)
            Kiara "That' smile says otherwise you know?"
            scene bg daythreebathmsgnatsu 30 with Dissolve(0.8)
            Kiara "These definitely never lie you know?"
            Natsuko "Ah.. fuck."
            scene bg daythreebathmsgnatsu 31 with Dissolve(0.8)
            Kiara "Oh we're biting lips already? huh"
            Natsuko "Aahhh.. , shit."
            scene bg daythreebathmsgnatsu 32 with Dissolve(0.8)
            Kiara "God your nipples are sensitive as hell , one touch and they're hard"
            Natsuko "N-no! , I mean it's just because it's cold."
            scene bg daythreebathmsgnatsu 33 with Dissolve(0.8)
            Kiara "Oh it's cold.. well then-"
            scene bg daythreebathmsgnatsu 34 with Dissolve(0.8)
            Natsuko "Han..."
            scene bg daythreebathmsgnatsu 35 with Dissolve(0.8)
            Kiara "Still cold?.."
            Natsuko "Unf.. um.."
            scene bg daythreebathmsgnatsu 36 with Dissolve(0.8)
            Natsuko "Han.. god."
            Kiara "Hehe wow you are really liking my fingers huh"
            scene bg daythreebathmsgnatsu 37 with Dissolve(0.8)
            Natsuko "Ah?! hm?"
            Kiara "There we go"
            scene bg daythreebathmsgnatsu 38 with Dissolve(0.8)
            Natsuko "Um?.. what?"
            Kiara "I won hehe , your nipples are rock hard natsu"
            scene bg daythreebathmsgnatsu 39 with Dissolve(0.8)
            Kiara "Someone owes me an ice cream heh"
            scene bg daythreebathmsgnatsu 40 with Dissolve(0.8)
            Natsuko "Uhm.. yeah i do i guess."
            scene bg daythreebathmsgnatsu 41 with Dissolve(0.8)
            Kiara "Now , I'm gonna go. You can take care of the rest I'm sure. "
            scene bg daythreebathmsgnatsu 42 with Dissolve(0.8)
            Natsuko "Um? what do you mean by rest?"
            Kiara "Perhaps if you open up that leg space you'll know."
            scene bg daythreebathmsgnatsu 43 with Dissolve(0.8)
            Natsuko "Well uhm , your dress is in my room.. mum left it on the desk"
            Kiara "I'll wear it then , have fun okay?"
            scene bg daythreebathmsgnatsu 44 with Dissolve(0.8)
            Natsuko "Fun?..Oh wow."
            scene bg daythreebathmsgnatsu 45 with Dissolve(0.8)
            Natsuko "I'm actually horny. Fuck i hope she didn't notice."
            scene bg daythreebathmsgnatsu 46 with Dissolve(0.8)
            Kiara "I guess i wouldn't mind helping her open up a little."
            jump chap_2_scene_51

label chap_2_scene_51:

    ##KIA MEETS ICHIGO
    scene blackscreen
    show titletext "20 minutes later.." with dissolve
    pause 1.0
    window hide
    scene bg kiameetsichigo 1 with Dissolve(0.8)
    Kiara "This outfit has such a good fabric"
    scene bg kiameetsichigo 2 with Dissolve(0.8)
    Kiara "Shouldn't be surprised though , it's auntie's choice after all"
    scene bg kiameetsichigo 3 with Dissolve(0.8)
    pause
    scene bg kiameetsichigo 4 with Dissolve(0.8)
    Kiara "It suits me nicely too , much better than a kimono personally."
    scene bg kiameetsichigo 5 with Dissolve(0.8)
    Kiara "( Oki , let's enjoy the sunday. )"
    scene bg kiameetsichigo 6 with Dissolve(0.8)
    Kiara "I wonder what natsuko is gonna wear"
    scene bg kiameetsichigo 7 with Dissolve(0.8)
    "*Bell sound*"
    Kiara "Hm?.. I should go check."
    scene bg kiameetsichigo 8 with Dissolve(0.8)
    pause
    scene bg kiameetsichigo 9 with Dissolve(0.8)
    Kiara "I should probably call Keisuke and others."
    scene bg kiameetsichigo 10 with Dissolve(0.8)
    pause
    scene bg kiameetsichigo 11 with Dissolve(0.8)
    Kiara "Morning grandpa"
    scene bg kiameetsichigo 12 with Dissolve(0.8)
    pause
    scene bg kiameetsichigo 13 with Dissolve(0.8)
    Ichigo "Tadaima!"
    scene bg kiameetsichigo 14 with Dissolve(0.8)
    pause
    scene bg kiameetsichigo 15 with Dissolve(0.8)
    Ichigo "Where is everyone?"
    scene bg kiameetsichigo 16 with Dissolve(0.8)
    Kiara "Excuse me , can i help you?"
    Ichigo "Wh-- Kiara"
    scene bg kiameetsichigo 17 with Dissolve(0.8)
    Ichigo "Um.. sorry who are you?"
    scene bg kiameetsichigo 18 with Dissolve(0.8)
    Ichigo "Kiara it-It's me.. Ichigo"
    scene bg kiameetsichigo 19 with Dissolve(0.8)
    Kiara "Ichigo?.. ( Why does that name sound familiar? )"
    scene bg kiameetsichigo 20 with Dissolve(0.8)
    Ichigo "It's me.. do you remember?"
    scene bg kiameetsichigo 21 with Dissolve(0.8)
    Kiara "I- I don't , how do you know my name?"
    Ichigo "(He erased everything..)"
    scene bg kiameetsichigo 22 with Dissolve(0.8)
    Kiara "Okay , no sad faces allowed, you guys have to cheese okay?"
    scene bg kiameetsichigo 23 with Dissolve(0.8)
    Kiara "Uncle looks great,  Mom and auntie you guys have to smile okay?"
    scene bg kiameetsichigo 24 with Dissolve(0.8)
    Kiara "There you go mom!"
    scene bg kiameetsichigo 25 with Dissolve(0.8)
    Kiara "Ahan , uncle a bit wider more please"
    scene bg kiameetsichigo 26 with Dissolve(0.8)
    Kiara "Aunty yuo never smile! , please for me just smile?"
    scene bg kiameetsichigo 27 with Dissolve(0.8)
    Xia "Okay honey , for you i will."
    Kiara "Thank you!"
    scene bg kiameetsichigo 28 with Dissolve(0.8)
    Ichigo "Our family.."
    scene bg kiameetsichigo 29 with Dissolve(0.8)
    Ichigo "Xia!.. Hey I'm back."
    scene bg kiameetsichigo 30 with Dissolve(0.8)
    Xia "Hello love , i see you met her already"
    Kiara "Aunty , who is this- ?"
    scene bg kiameetsichigo 31 with Dissolve(0.8)
    pause
    scene bg kiameetsichigo 32 with Dissolve(0.8)
    Xia "I have missed you my love"
    Ichigo "I have missed you more."
    scene bg kiameetsichigo 33 with Dissolve(0.8)
    Xia "Only her presence stops me from kissing you right now"
    Ichigo "We have plenty of time to do that."
    scene bg kiameetsichigo 34 with Dissolve(0.8)
    Xia "Say hi to your uncle , Kiara"
    Kiara "Oh! (Ichigo! that's right how could i forget)"
    Ichigo "Hi kiara"
    scene bg kiameetsichigo 35 with Dissolve(0.8)
    Kiara "I'm so sorry , I had so much on my mind"
    Ichigo "It's fine.. very happy to meet you finally by the way."
    scene bg kiameetsichigo 36 with Dissolve(0.8)
    Xia "Trust me , soon you'll always remember him , he's the one who named you when you were born"
    Kiara "Really? Heh wow."
    scene bg kiameetsichigo 37 with Dissolve(0.8)
    Kiara "Hi uncle , I made the worst first impression but.. it's nice to meet you too"
    Ichigo "Don't worry about it , come let's have some lunch?"
    Xia "Yes , come kiara"
    scene bg kiameetsichigo 38 with Dissolve(0.8)
    Kiara "I'll be with you both shortly , just gotta make calls first"
    Xia "Okay we'll wait for you then"
    scene bg kiameetsichigo 39 with Dissolve(0.8)
    Ichigo "I'm dying to eat some homemade food love"
    Xia "I've made plenty , You'll love it."
    Kiara "( Look at them.. married for years and still meeting as if a college date )"
    scene bg kiameetsichigo 40 with Dissolve(0.8)
    Kiara "I hope i find someone like this too.."
    jump chap_2_scene_52

label chap_2_scene_52:

    scene bg kiacallscn 1 with Dissolve(0.8)
    Kiara "Okay , time to let everyone know."
    scene bg kiacallscn 2 with Dissolve(0.8)
    Ayane "Kei?! , Keiiiii , Get ready fast!"
    scene bg kiacallscn 3 with Dissolve(0.8)
    Keisuke "I'm done , I'm done! , Just getting clothes on"
    Ayane "Don't  be late okay??"
    scene bg kiacallscn 4 with Dissolve(0.8)
    Keisuke "I won't! , Don't worry."
    scene bg kiacallscn 5 with Dissolve(0.8)
    Keisuke "What should i wear , can't be too fancy.. but has to look decent."
    scene bg kiacallscn 6 with Dissolve(0.8)
    Keisuke "Oh , It's kiara.."
    Kiara "Keisuke! , Hope you're ready soon, my cousin and i will be waiting for you!"
    scene bg kiacallscn 7 with Dissolve(0.8)
    Keisuke "( Cousin?.. natsuko? ) Um.. Okay sure i'll be there in half an hour."
    scene bg kiacallscn 8 with Dissolve(0.8)
    Kiara "Thanks! , see you soon"
    Keisuke "Yeah.. see ya."
    scene bg kiacallscn 9 with Dissolve(0.8)
    Keisuke "It's been a while but, Ah dammit i hope natsuko doesn't recognize me"
    scene bg kiacallscn 10 with Dissolve(0.8)
    Kiara "Azumi , I'll see you at the temple okay?"
    Azumi "Okay! , I'll be outisde by afternoon!"
    scene bg kiacallscn 11 with Dissolve(0.8)
    Azumi "This is what wore when we met , I hope she'll like it"
    scene bg kiacallscn 12 with Dissolve(0.8)
    Azumi "( Kiara , we finally have some alone time again.. I can't wait)"
    scene bg kiacallscn 13 with Dissolve(0.8)
    Kiara "Hello? Daichi-san , If you aren't too occupied at the shop I'd love to meet"
    Daichi "Of course kiara -san , I will be pleased to-"
    scene bg kiacallscn 14 with Dissolve(0.8)
    AgentWong "Teashop huh.. , Seems i'll hang out a bit with you too kiara"
    scene bg kiacallscn 15 with Dissolve(0.8)
    Kiara "Okay daichi-san , see you at evening then!"
    AgentWong "I should get going.. better have a heads up"
    scene bg kiacallscn 16 with Dissolve(0.8)
    AgentWong "Wong out , Helena back in.."
    scene bg kiacallscn 17 with Dissolve(0.8)
    Kiara "Lana , where do i come to pick you up?"
    Lana "I'll meet you at the park , we'll decide from there then"
    scene bg kiacallscn 18 with Dissolve(0.8)
    Kiara "Okay , I've been waiting to see the dress you got too"
    Lana "You'd love it , I think it looks lovely."
    Kiara "Heh , alright bye!"
    scene bg kiacallscn 19 with Dissolve(0.8)
    Lana "Hm.. I have to make sure he doesn't leave the hotel till i'm back."
    scene bg kiacallscn 20 with Dissolve(0.8)
    Lana "Rin! , could you come for a second?"
    scene bg kiacallscn 21 with Dissolve(0.8)
    pause
    scene bg kiacallscn 22 with Dissolve(0.8)
    Rin "Yeah ? What is it?"
    Lana "You know everything i do too now , can you take care of him?"
    scene bg kiacallscn 23 with Dissolve(0.8)
    Rin "I can try but can't promise anything"
    Lana "Just please don't try to be on him , He's not well."
    scene bg kiacallscn 24 with Dissolve(0.8)
    Rin "You can't lie to him forever you know? , he's gonna know eventually."
    Lana "I'll decide what to do at that time then."
    scene bg kiacallscn 25 with Dissolve(0.8)
    Rose "Mhmhm.. *Humming music*"
    scene bg kiacallscn 26 with Dissolve(0.8)
    pause
    scene bg kiacallscn 27 with Dissolve(0.8)
    Rose "( Now that's what i call a great latte )"
    scene bg kiacallscn 28 with Dissolve(0.8)
    Kiara "Hello? rose? Kiara here , I was thinking we could meet up in evening?"
    Rose "We certainly can , i definitely can for you"
    scene bg kiacallscn 29 with Dissolve(0.8)
    Kiara "Heh , Okay that's quite sweet of you but only if it's not too far for you"
    Rose "I'll manage just fine , don't worry. See you at eve"
    scene bg kiacallscn 30 with Dissolve(0.8)
    Kiara "That takes care of that , now let's have some lunch"
    scene bg kiacallscn 31 with Dissolve(0.8)
    Kiara "I wonder when these swords were last used"
    scene bg kiacallscn 32 with Dissolve(0.8)
    Xia "Kiara! come food is getting old"
    Ichigo "Welcome kiara, free to take any seat"

    "0.4 end"

    $ renpy.quit()

