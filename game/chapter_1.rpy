label epilouge:
    #TODO change name here
    play music "/audio/elogue.ogg"
    show bg epilogue 1 with Dissolve(0.8)
    "" "We hope you liked the game , here's what to expect in chapter 2!"
    show bg epilogue 1pt1 with Dissolve(0.8)
    "" "More cosplays & cool choices!"
    show bg epilogue 2 with Dissolve(0.8)
    "" "Mia and john's Trial"
    show bg epilogue 3 with Dissolve(0.8)
    "" ""
    show bg epilogue 4 with Dissolve(0.8)
    "" ""
    show bg epilogue 5 with Dissolve(0.8)
    "" "Lana's time in japan"
    show bg epilogue 6 with Dissolve(0.8)
    "" ""
    show bg epilogue 7 with Dissolve(0.8)
    "" "Who will get kiara? Keisuke or Damian? It's up to you!"
    show bg epilogue 8 with Dissolve(0.8)
    "" "Kiara's various opportunities begin!"
    show bg epilogue 9 with Dissolve(0.8)
    "" "Will she take the advantages this time and succeed?"
    show bg epilogue 10 with Dissolve(0.8)
    "" "Or will the city"
    show bg epilogue 11 with Dissolve(0.8)
    "" "Take advantage of her?"
    show bg epilogue 12 with Dissolve(0.8)
    "" ""
    show bg epilogue 13 with Dissolve(0.8)
    "" ""
    show bg epilogue 14 with Dissolve(0.8)
    "" "Lastly..."
    show bg epilogue 15 with Dissolve(0.8)
    "" "The doctor behind it all..."
    "" "See you all in chapter 2 ~"
    jump chap_2_scene_1




label azumiportbathroom:
    stop music
    play music "/audio/azmibthscn.ogg"
    show bg azumibathport 1 with Dissolve(0.8)
    ""
    show bg azumibathport 2 with Dissolve(0.8)
    Azumi "Kiara , what a lovely name. "
    show bg azumibathport 3 with Dissolve(0.8)
    Azumi "I hope we become great friends if nothing more. "
    show bg azumibathport 4 with Dissolve(0.8)
    Azumi "Although I would hope for the latter"
    show bg azumibathport 5 with Dissolve(0.8)
    Azumi "I'll help her out anyway I can , she deserves it. "
    show bg azumibathport 6 with Dissolve(0.8)
    Azumi "Ok , careful around the edges. "
    show bg azumibathport 7 with Dissolve(0.8)
    ""
    show bg azumibathport 8 with Dissolve(0.8)
    Azumi "Haa , much better... "
    show bg azumibathport 9 with Dissolve(0.8)
    Azumi "*Whistling* "
    show bg azumibathport 10 with Dissolve(0.8)
    "Sounds in background""Ahh... Uffh , god! "
    show bg azumibathport 11 with Dissolve(0.8)
    Azumi "What's that sound? are you, okay? "
    show bg azumibathport 12 with Dissolve(0.8)
    Azumi "Excuse me? are you alright? "
    "Sounds in background""Ahh...  "
    stop music
    play music "/audio/choicmusic.ogg"
    show bg azumibathport dcd with Dissolve(0.8)
    menu:
        "I should investigate , could be serious":
            #TODO add kiara corruption by 1
            $ mc_stats.adjust_corruption(1)
            jump azumiportbathroomchoice1 
        "I'll just call security from outside to check it.":
            jump azumiportbathroomchoice2 
    ""
    stop music
    jump airport

label azumiportbathroomchoice1:
    stop music
    play music "/audio/azmibthc1.ogg"
    show azumiinvstgt 1 with Dissolve(0.8)
    Azumi "Excuse me , is everything okay? do you need help? "
    show azumiinvstgt 2 with Dissolve(0.8)
    Azumi "Hello? Daijobu desu ka? "
    show azumiinvstgt 3 with Dissolve(0.8)
    Azumi "Ehm , let me look from here. "
    show azumiinvstgt 4 with Dissolve(0.8)
    ""
    show azumiinvstgt 5 with Dissolve(0.8)
    Azumi "Are you alri-- "
    show azumiinvstgt 6 with Dissolve(0.8)
    "Girls" "Ohh.... ahh yeah , eat it well mm... "
    show azumiinvstgt 7 with Dissolve(0.8)
    Azumi "Oh my kami... "
    show azumiinvstgt 8 with Dissolve(0.8)
    "Girls" "Mmm... that's right , get that tongue swirling in there. "
    show azumiinvstgt 9 with Dissolve(0.8)
    "Girls" "Haaa.... yes babe , you're so good at it. "
    show azumiinvstgt 10 with Dissolve(0.8)
    ""
    show azumiinvstgt 11 with Dissolve(0.8)
    "Girls" "Ohh... fuck , yes eat it "
    show azumiinvstgt 12 with Dissolve(0.8)
    "Blonde" "Aaaaaahhhh , yes... "
    show azumiinvstgt 13 with Dissolve(0.8)
    "Blonde" "Ha.... huh?... "
    show azumiinvstgt 14 with Dissolve(0.8)
    Azumi "Shit... she saw me. "
    show azumiinvstgt 15 with Dissolve(0.8)
    "Blonde" "Babe , we got a peeker heh. "
    show azumiinvstgt 16 with Dissolve(0.8)
    "Asian girl" "That so huh? where? "
    Azumi "I'm sorry! "
    show azumiinvstgt 17 with Dissolve(0.8)
    "Blonde" "Hiding doesn't do much when you're the pervert too you know cutie? "
    show azumiinvstgt 18 with Dissolve(0.8)
    Azumi "No... I'm not , I'm sorry I checked to see if you were alright and I was shocked... so I couldn't mov- "
    show azumiinvstgt 19 with Dissolve(0.8)
    "Asian girl" "Honey , we're not asking for a explanation. It's all good... how about you join us for more fun? "
    Azumi "No... I can't- sorry. "
    show azumiinvstgt 20 with Dissolve(0.8)
    Azumi "I... I already like someone , I apologize I didn't intend to do that , I just froze. "
    "Girls" "Aw , that's okay you can go then you're really cute by the way. "
    show azumiinvstgt 21 with Dissolve(0.8)
    Azumi "Did...that just happen? "
    show azumiinvstgt 22 with Dissolve(0.8)
    stop music
    ""
    jump airport

label azumiportbathroomchoice2:
    show bg azumidntbthr 1 with Dissolve(0.8)
    Azumi "I'll just tell security outside , need to get home soon anyway. "
    show bg azumidntbthr 2 with Dissolve(0.8)
    Azumi "Can't wait to see you again kiara , hope you reach home safe. "

    jump airport

label endingofchaptr1final:
    play music "/audio/endingscn.ogg"
    show bg endingchpt 36 with Dissolve(0.8)
    "Zzzzzzzz...."
    show bg endingchpt 37 with Dissolve(0.8)
    Kiara "Good morning to me...Let's start a new life. "

    stop music
    jump veronicaevidencedel

label veronicaevidencedel:
    show bg veronicaevidencedel 1 with Dissolve(0.8)
    play music "/audio/verondingsc.ogg"
    "" "Hungry Due club"
    "*Footsteps*"
    show bg veronicaevidencedel 2 with Dissolve(0.8)

    Veronica "Let's take care of this loose end. "

    show bg veronicaevidencedel 3 with Dissolve(0.8)

    Veronica "Hello there , excuse me."

    Bartender "Bit late for a drink. "

    Veronica "As if you care... listen. "

    show bg veronicaevidencedel 4 with Dissolve(0.8)

    Veronica "I need you to hear me , stay quiet, and follow... "

    show bg veronicaevidencedel 5 with Dissolve(0.8)

    Veronica "Check your counter below, my coworker earlier dropped 10K for you... you don't need to know how , when, or why , just delete all of your CCTV footage since last week and remember... I wasn't here. "

    show bg veronicaevidencedel 6 with Dissolve(0.8)

    Bartender "What the... she's not bluffing. "

    show bg veronicaevidencedel 7 with Dissolve(0.8)

    Bartender "I don't know what footage you're talking about, but I remembered I had something to do with the computer. "

    show bg veronicaevidencedel 8 with Dissolve(0.8)

    Veronica "Smart man... good , I'm waiting. "

    show bg veronicaevidencedel 9 with Dissolve(0.8)

    Jake "Yo john... she's here like you said... what do I do? "

    show bg veronicaevidencedel 10 with Dissolve(0.8)

    John "Record everything , and trail her , I got special plans. "

    Jake "Wouldn't this footage help you in case, though? "

    John "Don't worry about it , as I said, I got plans for her. Just keep an eye out. "

    show bg veronicaevidencedel 11 with Dissolve(0.8)

    Jake  "Sure... alright. "
    ""
    stop music
    jump chap_2_scene_1
    return


label endingofchaptrpart2:
    show bg endingchpt 18 with Dissolve(0.8)
    ""
    play music "/audio/ndngscnmain.ogg"
    show bg endingchpt 19 with Dissolve(0.8)
    Lana "D-Damian?... "
    show bg endingchpt 20 with Dissolve(0.8)
    Damian "Lana! , heh wow hi. "
    Lana "Oh my god Damian! its nice to see you , how come you're here? "
    Damian "Natsuko asked me to come to Osaka, seemed serious so I'm going. "
    show bg endingchpt 21 with Dissolve(0.8)
    Lana "Natsuko told him?... Could she be? no... I shouldn't jump to conclusions. "
    show bg endingchpt 22 with Dissolve(0.8)
    Rin "Hello? how do you know him? "
    Lana "Rin , he's... he's Damian he's an old friend from college , really nice guy. "
    show bg endingchpt 23 with Dissolve(0.8)
    Rin "Um... Remember the basketball tourney I told you about? he was the one who won it. "
    show bg endingchpt 24 with Dissolve(0.8)
    Rin "Did you fuck him? "
    show bg endingchpt 25 with Dissolve(0.8)
    Damian "Ah no, we were just friends- "
    Lana "Rin, shut up, will you , christ's sake. "
    show bg endingchpt 26 with Dissolve(0.8)
    Damian "Hey Lana, cool outfit by the way. "
    Lana "You think so? I wanted to try something new. "
    show bg endingchpt 27 with Dissolve(0.8)
    Rin "She looks better without it , trust me. "
    Lana "Rin! ZIP IT! "
    show bg endingchpt 28 with Dissolve(0.8)
    Rin "Issa. Jokes, calm down. "
    Damian "She reminds me of you in the first year, Lana. "
    Lana "Aheheh , I guess that's why she's my friend."
    show bg endingchpt 29 with Dissolve(0.8)
    "Announcement""{i}Attention all passengers , flight to Osaka will leave in 30 minutes , please board the plane immediately. {/i}"
    "Lana , Rin , Damian""Come on Damian , let's go... Nice name, by the way... Thanks. "
    stop music
    show bg endingchpt 30 with Dissolve(0.8)
    play music "/audio/dmnlanaairpot.ogg"
    Lana "Damain, did you know Osaka is one of the oldest cities? "
    show bg endingchpt 31 with Dissolve(0.8)
    Lana "Damian?... you okay? "
    show bg endingchpt 32 with Dissolve(0.8)
    Lana "Hm? what's this? "
    Damian "Take a look... "
    show bg endingchpt 33 with Dissolve(0.8)
    Lana "Look at this world and its people , they're just words , while you ... poetry. ( that's Kiara's lips... I can't tell him) "
    show bg endingchpt 34 with Dissolve(0.8)
    Lana "Damian, you'll be okay... I promise , give yourself a break , you deserve to be happy too. "
    Damian "I hope so, Lana, because the last 3 years, all I've done is try and fail. "
    Lana "(Damian... no , I can't tell him. Natsuko I don't know what you're doing but be careful) "
    show bg endingchpt 35 with Dissolve(0.8)
    Damian "( Kiara , you were right... I really never found anyone like you again) "
    ""
    stop music
    jump endingofchaptr1final


label endingofchaptr1:
    show bg endingchpt 1 with Dissolve(0.8)
    play music "/audio/ndngscnmain.ogg"
    ""
    show bg endingchpt 2 with Dissolve(0.8)
    Rin "Should've cut the nails properly. "
    show bg endingchpt 3 with Dissolve(0.8)
    Rin "Laanaaa , hurry up. We'll be late otherwise! "
    Lana "I'm coming! I'm sorry okay I didn't get time to fit it properly! "
    show bg endingchpt 4 with Dissolve(0.8)
    Rin "Jesus this girl , how hard can it be to put on a dress? "
    show bg endingchpt 5 with Dissolve(0.8)
    Natsukoontext "Just come please , I can't say why but it's urgent. I need your help, and mom wanted to meet you too. "
    "???""I will , the flight is booked, don't worry, talk to you in a bit. "
    show bg endingchpt 6 with Dissolve(0.8)
    Rin "Hey fuckface , do you not see the big woman outside, or are you just a massive pervert , either way, get the hell- "
    show bg endingchpt 7 with Dissolve(0.8)
    "???""Ah... shit, I'm so sorry , I was reading my friend's text, and I- "
    show bg endingchpt 8 with Dissolve(0.8)
    Rin "Oh my... he's easy on the eyes. "
    show bg endingchpt 9 with Dissolve(0.8)
    "???""I'm truly sorry  , I didn't mean to- "
    Rin "It's all good... go on, finish your business. "
    "???""Uh... what? I'm sorry, I think I misheard."
    show bg endingchpt 10 with Dissolve(0.8)
    Damian "Uh... I don't want any trouble. Look, I apologize. "
    Rin "Trouble? "
    show bg endingchpt 11 with Dissolve(0.8)
    Rin "I'm just asking you to take a piss , that's why you entered, right? "
    Damian "Uh, no, I'm good... I'ma go, actually. Sorry again. "
    show bg endingchpt 12 with Dissolve(0.8)
    show bg endingchpt 13 with Dissolve(0.8)
    Rin "Hey, wait! you dropped your wallet, look. "
    Damian "Oh, thanks I- "
    show bg endingchpt 14 with Dissolve(0.8)
    Damian "What the-... "
    Rin "Like what you see, big boy? "
    show bg endingchpt 15 with Dissolve(0.8)
    Damian "Uh no , I mean, I am sorry you're okay, but I actually- "
    show bg endingchpt 16 with Dissolve(0.8)
    Rin "C'mon , come closer... I know you want this you, pervert. "
    Damian "Hey, I'm sorry for real I don't want any trouble, please. "
    stop music
    show bg endingchpt 17 with Dissolve(0.8)
    play music "/audio/choicmusic.ogg"
    Rin "Oh c'mon don't be shy let's have some fun... "
    
    jump endingofchaptr1choice2
    # menu:
    #     "Kiara... No , I can't do this":
    #         jump endingofchaptr1choice2 
    #     "Her hands are so tender... once wouldn't hurt.":
    #         jump endingofchaptr1choice1 
    ""
    return
label endingofchaptr1choice2:
    show bg endingchptdcd with Dissolve(0.8)
    stop music
    play music "/audio/ndngscnmain.ogg"
    "Kiara... No , I can't do this"
    show bg endingrjctrin 1 with Dissolve(0.8)
    Damian "Ugh, sorry for pushing you look , I- "
    Rin "Hey what's your deal? what am I not pretty enough for you? "
    show bg endingrjctrin 2 with Dissolve(0.8)
    Damian "No , Please I don't mean that... I have someone in my life. "
    show bg endingrjctrin 3 with Dissolve(0.8)
    Rin "Ahh, you're one of the lover types... alright , care to tell me why? "
    Damian "I will , but please do that first. "
    show bg endingrjctrin 4 with Dissolve(0.8)
    Rin "Do what? "
    show bg endingrjctrin 5 with Dissolve(0.8)
    Damian "Uh your top... could you please... fix it? "
    show bg endingrjctrin 6 with Dissolve(0.8)
    Rin "Heh , this?... Jesus how long has it been since you saw tits, dude? "
    Damian "Uh... I haven't in a while yeah , thanks. "
    show bg endingrjctrin 7 with Dissolve(0.8)
    Rin "With that handsome face , kinda hard to believe. "
    show bg endingrjctrin 8 with Dissolve(0.8)
    Damian "Can I open, my eyes? "
    Rin "Yes, yes you, can. "
    show bg endingrjctrin 9 with Dissolve(0.8)
    Damian "Uh... I don't know if that's actually covered. "
    Rin "Well maybe you shouldn't stare then. "
    Damian "Right... sorry. "
    show bg endingrjctrin 10 with Dissolve(0.8)
    Rin "So , care to tell me who the lucky girl is?m "
    Damian "Oh, actually she- "
    show bg endingrjctrin 11 with Dissolve(0.8)
    Lana "I'm ready! ugh, This stupid fucking lock. "
    ""
    stop music
    jump endingofchaptrpart2
label endingofchaptr1choice1:
    show bg endingchptdcd with Dissolve(0.8)
    play music "/audio/damiccpt.ogg"
    ""
    show bg endingacctprin 1 with Dissolve(0.8)
    Damian "Wow... they're so soft. "
    Rin "Same goes for your hands. "
    show bg endingacctprin 2 with Dissolve(0.8)
    Damian "Take this thing off... let me feel these properly. "
    Rin "Oh my , you just needed a bit of motivation. "
    show bg endingacctprin 3 with Dissolve(0.8)
    Damian "Wow, you take good care of them ... I like squeezing them. "
    Rin "Gosh, you're cute , shame it's a bathroom, not a bed. "
    show bg endingacctprin 4 with Dissolve(0.8)
    Rin "Gimme your hand."
    show bg endingacctprin 5 with Dissolve(0.8)
    Rin "Feel how wet I am."
    show bg endingacctprin 6 with Dissolve(0.8)
    Damian "Wow... "
    Rin "Oh yea... that's all you. "
    show bg endingacctprin 7 with Dissolve(0.8)
    Rin "Bring it here. "
    Damian "What are you- ?"
    show bg endingacctprin 8 with Dissolve(0.8)
    Rin "*Slurp* Mmmm. "
    Damian "Holy shit, you're good at this. "
    show bg endingacctprin 9 with Dissolve(0.8)
    Rin "You're not half bad , come here. "
    show bg endingacctprin 10 with Dissolve(0.8)
    show bg endingacctprin 11 with Dissolve(0.8)
    Rin "Bring me those lips... "
    Damian "I can't control... sorry kia- "
    show bg endingacctprin 12 with Dissolve(0.8)
    Lana "I'm ready! ugh, This stupid fucking lock. "
    show bg endingacctprin 13 with Dissolve(0.8)
    Rin "Shit! Act normal... okay. "
    stop music

    jump endingofchaptrpart2



label wongandjohn:
    play music "/audio/Intomain2.ogg"
    show bg wongjohn 1 with Dissolve(0.8)
    John "Hmm... one week huh , I guess this side is covered. "
    show bg wongjohn 2 with Dissolve(0.8)
    "" "*sound of door opening*"
    show bg wongjohn 3 with Dissolve(0.8)
    John "Ms. Wong! Welcome, welcome , so glad to have you. "
    show bg wongjohn 4 with Dissolve(0.8)
    John "Here please , let's have some drinks! "
    AgentWong "No thanks , you enjoy yourself."
    John "Well, it is great to have your company regardless! "
    show bg wongjohn 5 with Dissolve(0.8)
    AgentWong "You don't have my company Mr.Jonathan only my services. "
    show bg wongjohn 6 with Dissolve(0.8)
    John "That's fair , so I suppose you know what the job details already? "
    AgentWong "Oversee your daughter's life in japan and intervene if anyone tries to get too close. "
    John "Yes and- "
    show bg wongjohn 7 with Dissolve(0.8)
    AgentWong "Eliminate any target if any signs of danger towards kiara. "
    show bg wongjohn 8 with Dissolve(0.8)
    John "You truly amaze me, Mrs. Wong , an amazing practitioner of deduction indeed. "
    AgentWong "I'm not practicing, john. "
    show bg wongjohn 9 with Dissolve(0.8)
    AgentWong "I've perfected it. "
    John "Classy response! "
    show bg wongjohn 10 with Dissolve(0.8)
    AgentWong "So I believe the financials will be taken care of by you? "
    show bg wongjohn 11 with Dissolve(0.8)
    John "Of course , 30,000 $ has been transferred to your account, and if anything is needed, contact my assistant, please. "
    AgentWong "Alright, will do. "
    show bg wongjohn 12 with Dissolve(0.8)
    AgentWong "Before I go , one question Mr. Johnathan if you don't mind. "
    show bg wongjohn 13 with Dissolve(0.8)
    John "Of course , ask away. "
    show bg wongjohn 14 with Dissolve(0.8)
    AgentWong "Why do you want her so bad?... No offense but it's not like she's miss universe or the best looker. "
    John "Ms. Wong , I've slept with celebrities. Looks aren't the reason here at all. "
    show bg wongjohn 15 with Dissolve(0.8)
    AgentWong "Well, what is it then? You can get any model you want with your money, so why her? Your daughter specifically. "
    John "I'm glad you asked actually , let me explain. "
    show bg wongjohn 16 with Dissolve(0.8)
    John "You see, ever since my older daughter Evelyn resisted my advances years ago . The sensation I felt was ... amazing. "
    John "During the day , I want to treat someone like a princess... give them everything they want and for them to rely on me. "
    show bg wongjohn 17 with Dissolve(0.8)
    John "Then at night or suddenly ... take it all way... treat them like a cum dump , a whore... and then pound that puss- "
    show bg wongjohn 18 with Dissolve(0.8)
    AgentWong "Enough... you're disgusting. "
    show bg wongjohn 19 with Dissolve(0.8)
    AgentWong "I'm not here to listen to your trash version of 50 shades... "
    John "Oh well... my bad. "
    show bg wongjohn 20 with Dissolve(0.8)
    AgentWong "I'm leaving , have the jet ready . I want to say one more thing, Mr. Jonathan. "
    John "Which is? "
    show bg wongjohn 21 with Dissolve(0.8)
    AgentWong "I didn't drink because I knew it was drugged... Mia only broke your balls , I'll cut em off and feed em to dogs if you try this shit with me again. "
    show bg wongjohn 22 with Dissolve(0.8)
    John "Aha hah, Ms. Wong, it was. Merely a test of your awareness skills, you know... "
    AgentWong "Whatever, keep your bullshit. "
    show bg wongjohn 23 with Dissolve(0.8)
    AgentWong "I'll report when I land in Osaka, bye. "
    show bg wongjohn 24 with Dissolve(0.8)
    John "Fucking bitch... I'll make you gobble on my dick one day, for now... I have another plan, one much sweeter. "
    show bg wongjohn 25 with Dissolve(0.8)
    John "Ain't that right...? Lovely Veronica. "
    ""
    stop music
    jump veronicaevidencedel

label aidenrevealscene:
    play music "/audio/aidnrevl.ogg"
    scene bg aidenvalconvo 1 with Dissolve(0.8)
    "???""C'mon, pickup... "
    show bg aidenvalconvo 2 with Dissolve(0.8)
    "???""Val... c'mon on already. "
    show bg aidenvalconvo 3 with Dissolve(0.8)
    Valentinaonphone "Hello? who's this? "
    "???""Your lifesaver, dumbass. "
    Valentinaonphone "Aiden! Oh my god, hi, I'm sorry I was ...just getting home. "
    show bg aidenvalconvo 4 with Dissolve(0.8)
    Aiden "Yeah, that's great pick up faster next time please , so... did you tell him? "
    Valentinaonphone "I... Couldn't , Something happened, he was out for groceries. I'll just go tomorrow, it's okay. "
    Aiden "What are you talking about? He's off to Japan."
    show bg aidenvalconvo 5 with Dissolve(0.8)
    Valentinaonphone "Wait, what? the maid said he went out for- "
    Aiden "No shit, he lied , I just saw his ticket being booked , why japan now? "
    Valentinaonphone "Are you thinking what I'm thinking? "
    show bg aidenvalconvo 6 with Dissolve(0.8)
    Aiden "I am , but uncertain still... anyway, the guy who called you yesterday, be careful of him, Val. "
    Valentinaonphone "Oh... why? Is he a troll? "
    Aiden "Far from it. As I said, be careful. "
    show bg aidenvalconvo 7 with Dissolve(0.8)
    Valentinaonphone "Alright... so what are you doing? "
    Aiden "John's account has suspiciously high transfers into a BTC account. I'm trying to find to whom. "
    Valentinaonphone "Okay, let me know later , you take care, okay! *call cuts* "
    show bg aidenvalconvo 8 with Dissolve(0.8)
    Aiden "Old man... what are you planning. "
    ""
    stop music
    jump investigatevng


label valntdamimomscn:
    play music "/audio/vlnthmscne1.ogg"
    show valntdamimomscn 1 with Dissolve(0.8)
    "" "Arundel Household"
    show valntdamimomscn 2 with Dissolve(0.8)
    Valentina "Once I'm done here, I'll get on tracking whoever it was last night. "
    show valntdamimomscn 3 with Dissolve(0.8)
    Valentina "Who could it be? He threatened me with nick as well , how does he know? "
    show valntdamimomscn 4 with Dissolve(0.8)
    Valentina "I don't want nick to be hurt, especially because of me. "
    show valntdamimomscn 5 with Dissolve(0.8)
    MaidAna "Welcome, ms. valentina , how may I be of service? "
    show valntdamimomscn 6 with Dissolve(0.8)
    Valentina "Oh, Ana , no, it's alright. I just wanted to talk to Damian. Is he home? "
    show valntdamimomscn 7 with Dissolve(0.8)
    Valentina "Master Damian left about an hour ago for groceries. However, the mistress is in her room. Do you think I should call her? "
    show valntdamimomscn 8 with Dissolve(0.8)
    Valentina "No, it's fine , I'll meet her myself , thanks, Ana. "
    show valntdamimomscn 9 with Dissolve(0.8)
    ""
    show valntdamimomscn 10 with Dissolve(0.8)
    MaidAna "Mrs. Valentina always has been kind to master Damian , I wonder why they never got together. "
    show valntdamimomscn 11 with Dissolve(0.8)
    Valentina "Mrs. Arundel? It's me. When will Damian will be ba- "
    show valntdamimomscn 12 with Dissolve(0.8)
    Eugine "Hmm hmm *music humming* "
    show valntdamimomscn 13 with Dissolve(0.8)
    Valentina "Shit! I forgot they had an open bathroom... she didn't notice me, right? "
    show valntdamimomscn 14 with Dissolve(0.8)
    ""
    stop music
    show valntdamimomscn 15 with Dissolve(0.8)
    Valentina "I- This was a mistake , what do I do? "
    play music "/audio/choicmusic.ogg"
    menu:
        "Leave! the last thing you need is this stuff right now.":
            jump valntdamimomscn1 
        "I should wait , maybe she's done.":
            $ mc_stats.adjust_corruption(1)
            jump valntdamimomscn2 
    ""
    return

label valntdamimomscn1:

    show valntdamimomscn 15 with Dissolve(0.8)
    Valentina "I'll just tell him later by call... This is too embarrassing! "
    ""
    stop music
    #loading
    jump veromeetsevlyn

label valntdamimomscn2:
    stop music
    show valntdamimomscn 16 with Dissolve(0.8)
    play music "/audio/vlnmummstrbt.ogg"
    Valentina "I'll just call to her when she gets out in the towel... "
    show valntdamimomscn 17 with Dissolve(0.8)
    Valentina "She's got such an amazing body for a mother... , wait why am I staring ? "
    show valntdamimomscn 18 with Dissolve(0.8)
    Valentina "Why is she turning the water off ?... "
    show valntdamimomscn 19 with Dissolve(0.8)
    ""
    show valntdamimomscn 20 with Dissolve(0.8)
    Valentina "Wow... that's a sight I didn't think I'd see today. "
    show valntdamimomscn 21 with Dissolve(0.8)
    ""
    show valntdamimomscn 22 with Dissolve(0.8)
    ""
    show valntdamimomscn 23 with Dissolve(0.8)
    Valentina "Uh... what is she doing?...I can't stop looking. "
    show valntdamimomscn 24 with Dissolve(0.8)
    Eugine "Mmm... they've gotten so big since my marriage , luke's usually busy but I've been craving and my son being so hot doesn't help. "
    Valentina "What the? is she talking about Damian? "
    show valntdamimomscn 25 with Dissolve(0.8)
    Eugine "Haa... Damian I wonder if you think about me as well. "
    show valntdamimomscn 26 with Dissolve(0.8)
    ""
    show valntdamimomscn 27 with Dissolve(0.8)
    Valentina "I can't believe it... she's thinking of her son while masturbating? "
    show valntdamimomscn 28 with Dissolve(0.8)
    Valentina "It's wrong on so many levels but... it's so hot I don't know why. "
    show valntdamimomscn 29 with Dissolve(0.8)
    ""
    show valntdamimomscn 30 with Dissolve(0.8)
    Eugine "Mmm... Damian mommy will take care of you. "
    show valntdamimomscn 31 with Dissolve(0.8)
    Valentina "God... I used to do this too, thinking about Damian, this is so wrong. "
    show valntdamimomscn 32 with Dissolve(0.8)
    Valentina "What am I doing?... I like nick and yet... "
    show valntdamimomscn 33 with Dissolve(0.8)
    Eugine "Aaaahh , fuck me... I want you so bad. "
    show valntdamimomscn 34 with Dissolve(0.8)
    Valentina "Mmm... god she's so hot too. "
    show valntdamimomscn 35 with Dissolve(0.8)
    Eugine "Ahh! yess "
    show valntdamimomscn 36 with Dissolve(0.8)
    Eugine "Aaahhh... so good. "
    Valentina "I wanna share the shower now... "
    show valntdamimomscn 37 with Dissolve(0.8)
    Valentina "Umph... I am about to cum too... "
    show valntdamimomscn 38 with Dissolve(0.8)
    Luke "Honey I'm home! "
    Eugine "Perfect timing. "
    Valentina "Oh my gosh, no !  "
    show valntdamimomscn 39 with Dissolve(0.8)
    Valentina "I can't let uncle luke see me this way! I'll just call him later. "
    ""
    stop music
    jump veromeetsevlyn

label jakemeetsevelyn:
    play music "/audio/jkeveone.ogg"
    show bg eveandjakepark 1 with Dissolve(0.8)
    Jake "Mom , just a few more months then I'll get a good job and leave all this behind. "
    show bg eveandjakepark 2 with Dissolve(0.8)
    Jake "Okay, gotta cheer me up a bit , these tacos should do the trick. "
    show bg eveandjakepark 3 with Dissolve(0.8)
    Jake "Nice , seems like he did all the fillings. "
    show bg eveandjakepark 4 with Dissolve(0.8)
    Jake "Alright, let's open it up. "
    show bg eveandjakepark 5 with Dissolve(0.8)
    Jake "Muchos gracias , this looks nice! "
    show bg eveandjakepark 6 with Dissolve(0.8)
    ""
    show bg eveandjakepark 7 with Dissolve(0.8)
    Jake "WHAT THE FUCK! "
    show bg eveandjakepark 8 with Dissolve(0.8)
    Jake "AAAAHHHHHHHHHH THE FUCK IS THAT SPICE , WATER! "
    show bg eveandjakepark 9 with Dissolve(0.8)
    Jake "Urgh ah , water yes, good... "
    show bg eveandjakepark 10 with Dissolve(0.8)
    Jake "Urgh ah , huh...huh.huu"
    show bg eveandjakepark 11 with Dissolve(0.8)
    Jake "Blugh, what the fuck is this ocean water salty as shit. "
    show bg eveandjakepark 12 with Dissolve(0.8)
    ""
    show bg eveandjakepark 13 with Dissolve(0.8)
    Jake "AAH ITS IN MY EYES NOW ! SOMEONE HELP? "
    stop music
    show bg eveandjakepark 14 with Dissolve(0.8)
    play music "/audio/jakeevetwo.ogg"
    "AHHHHHHHHHHHH!"
    show bg eveandjakepark 15 with Dissolve(0.8)
    "???""Hey here , have some water. "
    show bg eveandjakepark 16 with Dissolve(0.8)
    Jake "URgh... fuck that taco guy , ruined my taste buds for life. "
    "???""Heh , it's why I always make my own food. "
    show bg eveandjakepark 17 with Dissolve(0.8)
    Jake "Arugh yeah , I am shit at cooking. Oh boy, thanks again. "
    Evelyn "You're welcome , are you alright? "
    show bg eveandjakepark 18 with Dissolve(0.8)
    Jake "(What the...) "
    show bg eveandjakepark 18pt2 with Dissolve(0.8)
    Jake "(Holy shit , she's beautiful...) "
    Evelyn "Hello? did the spice make you deaf as well? "
    show bg eveandjakepark 19 with Dissolve(0.8)
    Jake "Oh yeah, sorry , needed a moment. Are you new in town? never seen you here. "
    Evelyn "Uhh well... "
    show bg eveandjakepark 20 with Dissolve(0.8)
    Evelyn "You're not entirely wrong , but new and old both. Get it? "
    Jake "I don't, but it's fine , I suck at expressing myself too."
    show bg eveandjakepark 21 with Dissolve(0.8)
    Evelyn "So this your usual hang out spot? seems lonely. "
    Jake "Well, not hangout, isolation rather, lonely, yes, but peaceful too. "
    show bg eveandjakepark 22 with Dissolve(0.8)
    Evelyn "Peaceful it is , no doubt about that. "
    show bg eveandjakepark 23 with Dissolve(0.8)
    Jake "Hey, I'm sorry again for wasting your entire water , it was burning my eyes , hell, my mouth is still a mess. "
    Evelyn "Heh, it's alright. I can afford more. "
    show bg eveandjakepark 24 with Dissolve(0.8)
    Evelyn "Here, by the way , this candy will help calm the mouth a bit. "
    show bg eveandjakepark 25 with Dissolve(0.8)
    Jake "Am I hallucinating due to the spice, or are you actually real? "
    Evelyn "What? why would you think that? "
    Jake "Well , you're so kind... it's pretty rare in today's world. "
    show bg eveandjakepark 26 with Dissolve(0.8)
    Evelyn "It's not rare , it should be the norm. Being kind isn't hard. It just takes a little bit of effort, but because people are afraid of getting attached to people or things and losing them."
    show bg eveandjakepark 27 with Dissolve(0.8)
    Evelyn "Sure, there are exceptions, but I think everyone should be kind to each other , especially after us surviving a pandemic. "
    Jake "Hm... ( these are mom's words... man, she's not just pretty outside but inside too) "
    show bg eveandjakepark 28 with Dissolve(0.8)
    Jake "(Mom...!) "
    show bg eveandjakepark 29 with Dissolve(0.8)
    Evelyn "Hey ? you alright? sorry if I said something that upset you. "
    show bg eveandjakepark 30 with Dissolve(0.8)
    Jake "No, you're good , sorry anyway, I'm Jake , I'm a- "
    show bg eveandjakepark 31 with Dissolve(0.8)
    Jake "Ah shit... gotta go. "
    Evelyn "No worries , also I'm Evelyn. "
    show bg eveandjakepark 32 with Dissolve(0.8)
    Jake "Cool name ! , Uh, meet me this weekend, I'll bring ice cream! "
    Evelyn "Oh , okay, uhh... "
    show bg eveandjakepark 33 with Dissolve(0.8)
    Evelyn "I like BUTTERSCOTCH! "
    Jake "Gotcha! Will bring a family size. "
    show bg eveandjakepark 34 with Dissolve(0.8)
    Evelyn "That wasn't so bad... I suppose people have changed with time. "
    show bg eveandjakepark 35 with Dissolve(0.8)
    Jake "Mom... I think I found the girl you were talking about , I'll do my best to be a better person. "
    ""
    stop music
    jump wongandjohn

label assistantevngscn:
    play music "/audio/asstntscn2.ogg"
    show bg assistantevng 1 with Dissolve(0.8)
    "" "{i}Patricia's House {/i}"
    Patricia "Alright that takes care of the meetings. "
    show bg assistantevng 2 with Dissolve(0.8)
    Patricia "All trips are delayed as well. "
    show bg assistantevng 3 with Dissolve(0.8)
    Patricia "Should be all, for now, work wise , I'm sure the manager can handle the rest. "
    show bg assistantevng 4 with Dissolve(0.8)
    Patricia "Okay , I should get some food now. "
    show bg assistantevng 5 with Dissolve(0.8)
    Patricia "I hope he took his medication , or it'll be another headache. "
    show bg assistantevng 6 with Dissolve(0.8)
    Patricia "He must've, right? It was for his own good, after all. "
    show bg assistantevng 7 with Dissolve(0.8)
    Patricia "I'll just make sure anyway. I don't want to argue with the doctor later. "
    show bg assistantevng 8 with Dissolve(0.8)
    Patricia "Hello? Sir? can you hear me? "
    John "Hey Patricia , yes I hear you just fine. What's up? "
    show bg assistantevng 9 with Dissolve(0.8)
    Patricia "Sir, I've moved your meetings and trips to next month , you shouldn't have any problems also, how's your health? "
    John "Oh, thanks Patricia , you didn't have to, but I appreciate it. "
    show bg assistantevng 10 with Dissolve(0.8)
    Patricia "Sir , Don't ignore my question. How's your health? Did you take the meds? "
    John "Uh, okay, I'm sorry, I forgot. "
    show bg assistantevng 11 with Dissolve(0.8)
    Patricia "Sir, I told you to take them on time, didn't I? please take them now. "
    John "Yes , right away. I'm sorry I forgot due to a friend's party. "
    Patricia "Good , thank you. "
    show bg assistantevng 12 with Dissolve(0.8)
    John "Ulgh, these are sour anyway , you okay with being at the hearing next week? "
    Patricia "Sure, I'll be there, sir. Please take your medication on time. "
    show bg assistantevng 13 with Dissolve(0.8)
    Devin "He's better off dead anyway , why do you care? "
    Patricia "Ugh! ( for fucks sake , he had to come now, didn't he) "
    show bg assistantevng 14 with Dissolve(0.8)
    Patricia "Sir, I have to go now. I'll make sure to call you later, is that okay? "
    John "No worries, and it's okay. Enjoy your break, patty. "
    show bg assistantevng 15 with Dissolve(0.8)
    Devin "Are you not ashamed to work for someone like that? It's immoral, and you know it. "
    show bg assistantevng 16 with Dissolve(0.8)
    Patricia "I can be either a morally rich but poor girl or the opposite , go ahead, choose. "
    Devin "Money isn't everything, Patricia. "
    show bg assistantevng 17 with Dissolve(0.8)
    Devin "You have to realize , you're working for a guy who has been in multiple sexual harassment cases and yesterday tried to do it to his daughter! "
    show bg assistantevng 18 with Dissolve(0.8)
    Patricia "One, he never got convicted on them, and, 2 In the 3 years I've worked for him , he hasn't done anything to me, and he pays me well , So I don't care. "
    Devin "How can you not care? is money so important to you that you're just gonna let other innocent people suffer? you should be ashamed as a woman.  "
    show bg assistantevng 19 with Dissolve(0.8)
    Patricia "Should I be ashamed of making a living, then you should be ashamed as a man for not earning one , no wonder Valentina left you as well. "
    show bg assistantevng 20 with Dissolve(0.8)
    Devin "Don't you fucking dare bring her into this conversation , I had health issues and was a recovering addict. "
    show bg assistantevng 21 with Dissolve(0.8)
    Patricia "I don't mean it that way, and yes, I know it's exactly why I am working, so you and mom don't have to. "
    Devin "Don't call my mother yours , there's no way someone who whores herself for money could be my sister! "
    show bg assistantevng 22 with Dissolve(0.8)
    Patricia "Are you serious? We've been a family for 12 years , you're still going to do this step shit? "
    Devin "It's the truth , you're nothing but a slut anyway if you're working for a rapist! "
    show bg assistantevng 23 with Dissolve(0.8)
    Caroline "DEVIN! Mind your language! She's the reason you were able to even recover. "
    Devin "Mom, I- "
    show bg assistantevng 24 with Dissolve(0.8)
    Caroline "I don't want to hear it , Go downstairs. I need to talk to your sister. "
    Devin "Ugh, fine... "
    show bg assistantevng 25 with Dissolve(0.8)
    Devin "You can counsel me all you want mom... , but she'll never be my sister. "
    show bg assistantevng 26 with Dissolve(0.8)
    Caroline "Patricia, I'm sorry for what he sa- "
    Devin "It's fine mom , He's not wrong in the end... I'll eat dinner in a bit, don't worry. "
    show bg assistantevng 27 with Dissolve(0.8)
    Caroline "Okay, honey. ( Devin really should watch his words , The passing of Ben hurt them both, but words like these only make it worse) "
    ""
    jump jakemeetsevelyn


label natsunightbathroom:
    show bg natsunight 1 with Dissolve(0.8)
    Natsuko "I guess they are asleep now... I should as well. "
    show bg natsunight 2 with Dissolve(0.8)
    Natsuko "One side of me agrees that the memory thing was good for kiara. "
    show bg natsunight 3 with Dissolve(0.8)
    Natsuko "But other wants to tell kiara everything , she didn't deserve to get her love stolen that way... what should I do? "
    show bg natsunight 4 with Dissolve(0.8)
    Natsuko "I have an idea... I don't know how risky it will be, but it's better than letting it all out and overwhelming her. "
    show bg natsunight 5 with Dissolve(0.8)
    Natsuko "Alright , I'll text him... this is the only way to do it. "
    show bg natsunight 6 with Dissolve(0.8)
    Natsuko "Finally, I feel a bit clean... ugh, I'll make sure that molester suffers next time. "
    ""
    stop music
    jump miamasonnighttalk


label azuminighttext:
    play music "/audio/azmihmscn.ogg"
    show bg azuminighttext 1 with Dissolve(0.8)
    Azumi "One call... I need one call or message. "
    show bg azuminighttext 2 with Dissolve(0.8)
    Azumi "Even if we don't talk...  I hope she's safe. "
    show bg azuminighttext 3 with Dissolve(0.8)
    Azumi "All I can do is wait and pray , Kiara, please be alright. "
    show bg azuminighttext 4 with Dissolve(0.8)
    Azumi "Huh? * phone ring* please be her , please be her. "
    stop music
    show bg azuminighttext 5 with Dissolve(0.8)
    play music "/audio/azminttxtfull.ogg"
    Kiaraonphone "Azumi! I just saw your texts. I'm so sorry , I lost my phone, and then it died... I'll explain, I promise. "
    Azumi "No, it's completely fine , I was just worried. Sorry for the spam... So are you okay now? "
    show bg azuminighttext 6 with Dissolve(0.8)
    Kiaraonphone "Yes, I'm perfect , I really should've taken your offer of the ride instead of a cab tho, haha. "
    Azumi "Told you , but it's okay... so are you coming tomorrow to school? "
    Kiaraonphone "Yes, definitely! "
    show bg azuminighttext 7 with Dissolve(0.8)
    Azumi "Okay, sleep nice and let me know before you get there. I'll be waiting. "
    Kiaraonphone "Yes, I will , gonna get some rest now, okay? Goodnight. "
    Azumi "Goodnight ,  I'll miss you. "
    show bg azuminighttext 8 with Dissolve(0.8)
    Azumi "Mmmm, that felt good , I can sleep peacefully now ... see you tomorrow, Kiara. "
    stop music
    show bg azuminighttext 9 with Dissolve(0.8)
    play music "/audio/hmnitscn.ogg"
    Kiara "Miss me? she is a cutie. "
    show bg azuminighttext 10 with Dissolve(0.8)
    Kiara "Alright, time for bed. "
    show bg azuminighttext 11 with Dissolve(0.8)
    Xia "While Ichi is right about not being harsh, I have to teach her to defend herself. "
    show bg azuminighttext 12 with Dissolve(0.8)
    Xia "Perhaps I'll talk to her tomorrow about it, self defense is a necessity nowadays. "
    show bg azuminighttext 13 with Dissolve(0.8)
    Xia "Same goes for Natsuko , she's old enough now for preying eyes... should probably sleep now though. "
    ""
    jump natsunightbathroom


label Keisukereveal:
    play music "/audio/ksuke.ogg"
    show bg keisukereveal 1 with Dissolve(0.8)
    Ayane "Kei? Kei!? "
    show bg keisukereveal 2 with Dissolve(0.8)
    Ayane "Here you are...? I've something important to tell you."
    show bg keisukereveal 3 with Dissolve(0.8)
    Ayane "Kiara , She's back here in jap- "
    Keisuke "I'm aware of it. "
    show bg keisukereveal 3 with Dissolve(0.8)
    Ayane "So... what are you going to? Are you going tomorrow? "
    show bg keisukereveal 4 with Dissolve(0.8)
    Keisuke "I don't know , Ayane. "
    show bg keisukereveal 5 with Dissolve(0.8)
    Ayane "What do you mean you don't know? You've waited 4 years for this. "
    show bg keisukereveal 6 with Dissolve(0.8)
    Keisuke "She made her choice long ago, Ayane , I have no right to step in and take that away. "
    Ayane "What are you talking about? "
    show bg keisukereveal 7 with Dissolve(0.8)
    Ayane "You and I both know she lost her memories , she couldn't come back even if she wanted to. "
    show bg keisukereveal 8 with Dissolve(0.8)
    Ayane "Kei , you told me she was someone you could never replace , someone you felt your soul attach to. "
    show bg keisukereveal 9 with Dissolve(0.8)
    Ayane "You told me you loved her. Why give up now? "
    show bg keisukereveal 10 with Dissolve(0.8)
    Keisuke "I'll never give up on her , nor stop loving her. "
    Ayane "That's what I am saying , don't waste away this beautiful thing you had over an assumption. "
    show bg keisukereveal 11 with Dissolve(0.8)
    Keisuke "It isn't that easy, Ayane."
    Ayane "It is! , sit down for a moment. "
    Keisuke "Fine "
    show bg keisukereveal 12 with Dissolve(0.8)
    Ayane "Kei, what if she made the wrong choice? You told me you were happy together, but you never confessed. "
    Keisuke "I wanted to take it slow , I fucked up... I didn't want her to hate me. "
    show bg keisukereveal 13 with Dissolve(0.8)
    Ayane "Kei , even if you feel you fucked up, which I don't think you did , you can fix it now.  "
    show bg keisukereveal 14 with Dissolve(0.8)
    Ayane "Think about what I said, okay?... My brother's a great guy, and I'm sure she'd think the same.  "
    show bg keisukereveal 15 with Dissolve(0.8)
    Keisuke "If what Ayane says is true, then I may have a chance. "
    show bg keisukereveal 16 with Dissolve(0.8)
    Keisuke "A chance to fix things , appreciate her even better, and perhaps confess... "
    show bg keisukereveal 17 with Dissolve(0.8)
    Keisuke "This time , I'll be good enough, kiara, I swear. "
    show bg keisukereveal 18 with Dissolve(0.8)
    Keisuke "I hope you're sleeping with a smile. It always suits you. "
    ""
    stop music
    jump azuminighttext

label investigatevng:
    play music "/audio/invstaftrjke2.ogg"
    show bg jakeinvestaftrevng 1 with Dissolve(0.8)
    Jake "He told me he'd be here , of course, he's late. "
    show bg jakeinvestaftrevng 2 with Dissolve(0.8)
    John "Hellooo there , Looking for a ride, buddy? "
    Jake "I like how you told me to keep it under cover and you come in a limo. "
    show bg jakeinvestaftrevng 3 with Dissolve(0.8)
    John "This instance calls for it , hop on in. I got something to tell you."
    show bg jakeinvestaftrevng 4 with Dissolve(0.8)
    John "Thanks to your evidence, my lawyer said the case could be in our favor eventually. "
    Jake "I don't understand the law, but great for you. "
    show bg jakeinvestaftrevng 5 with Dissolve(0.8)
    Jake "I wanted to know though , what's the deal with you exactly? Can't you buy her lawyer out? "
    John "I would've, but the bitch hired Mason instead , and he's like her slave since college days. "
    show bg jakeinvestaftrevng 6 with Dissolve(0.8)
    John "I tried to get the judge, but it seems he's a tough ass as well , so a legal battle is my only option here. "
    show bg investigatoraftermiamason 7 with Dissolve(0.8)
    Jake "So you're gonna more than a million to avoid paying a couple hundred thousand? "
    John "It ain't about the money here Jake , no one touches me in New York."
    show bg investigatoraftermiamason 8 with Dissolve(0.8)
    John "Mia not only hurt me but also took my girl, who I've made sure remains a virgin for myself. I ain't letting this shit go. I want to see Mia humiliated. "
    Jake "Right , of course. "
    show bg investigatoraftermiamason 9 with Dissolve(0.8)
    John "So why did you wanna go to the hospital? "
    Jake "Been feeling a bit of a throat problem , nothing major. "
    John "Do not get sick, and I will have a big party for you to post your hearing on social media. "
    stop music
    show bg investigatoraftermiamason 10 with Dissolve(0.8)
    John "How does a billionare act like such a child is beyond me. "
    show bg investigatoraftermiamason 11 with Dissolve(0.8)
    Jake "Alright , this is it. "
    show bg investigatoraftermiamason 12 with Dissolve(0.8)
    play music "/audio/jkemumscn.ogg"
    Bailey "Who's there? is that you Dr.? "
    show bg investigatoraftermiamason 13 with Dissolve(0.8)
    Jake "It's me mom , how are you feeling? "
    Bailey "My wonderful son , I'm fine come sit here. "
    show bg investigatoraftermiamason 14 with Dissolve(0.8)
    Jake "Did you eat lunch on time? Is the doctor checking in on you? "
    Bailey "Yes yes , I did and Dr. is great... tell me about you , you said you had good news? "
    show bg investigatoraftermiamason 15 with Dissolve(0.8)
    Jake "Yes , I'm gonna get a huge paycheck soon and we can move you to fortis and they will get chemo started as well. "
    Bailey "You shouldn't be wasting so much money on me Jake , save it for yourself. "
    show bg investigatoraftermiamason 16 with Dissolve(0.8)
    Jake "Mom, I've told you not to say that... its never a waste if its to keep you healthy and well , no matter what amount. "
    Bailey "I'm sorry Jake, but I want you to find a girl and get married before I die. I want a grandson before I go... "
    show bg investigatoraftermiamason 17 with Dissolve(0.8)
    Jake "You won't go anywhere , I'll make sure of that... besides I doubt any girl would like a guy that's barely even social. "
    Bailey "That's untrue and you know it , my son is very handsome too after all I'm sure you'll find a kind person. "
    show bg investigatoraftermiamason 18 with Dissolve(0.8)
    Bailey "As long as you're doing something that's morally right ,I'm proud of you and someone who shares those morals will find you as well. "
    Jake "Yeah mom , I'll try my best. "
    show bg investigatoraftermiamason 19 with Dissolve(0.8)
    Jake "Okay mom , I'll get back to work you take your meds on time okay? I'll see you tomorrow. "
    Bailey "Take care okay? and don't worry too much about me. "
    show bg investigatoraftermiamason 20 with Dissolve(0.8)
    Jake "Mom I don't know if what I do is morally right , but I'll do whatever it takes to save you. "
    ""
    stop music
    jump Lanaliz


label miaveroeve:
    play music "/audio/miaveroevescn.ogg"
    show bg miaveroeve 1 with Dissolve(0.8)
    Mia "Sachi? sachi? hello? "
    show bg miaveroeve 2 with Dissolve(0.8)
    Mia "Did she just cut the call?... She yelled at something as well. "
    show bg miaveroeve 3 with Dissolve(0.8)
    Mia "Should I call her again?... Maybe not, she didn't seem in the mood to talk. "
    show bg miaveroeve 4 with Dissolve(0.8)
    Mia "*Door open* Mason? is that you? "
    show bg miaveroeve 5 with Dissolve(0.8)
    Veronica "Sorry to dissappoint you but issa me. "
    show bg miaveroeve 6 with Dissolve(0.8)
    Mia "How could it ever be dissappointing to have your company veronica? "
    Veronica "Ooo smooth , trying to get in both cousins pants are you? "
    Mia "Aheh no , you're cooler. "
    show bg miaveroeve 7 with Dissolve(0.8)
    Veronica "Sounds about right , so did you get the child care papers from john's ex? "
    Mia "Yeah I've got the soft copies , um... did you talk to Evelyn? "
    show bg miaveroeve 8 with Dissolve(0.8)
    Veronica "I did Mia , but she needs a little bit of thinking time , She will meet us tomorrow, I hope you understand. "
    Mia "Oh... does she still hate me? "
    show bg miaveroeve 9 with Dissolve(0.8)
    Veronica "If she did, she wouldn't have agreed to come , you need to realize, Mia your decision to stay with john in the past did affect her deeply. "
    Mia "I know... I was naive and stupid, thinking he'd change , I want to embrace my daughter once again I'm sorry. "
    show bg miaveroeve 10 with Dissolve(0.8)
    Veronica "That's the past, Mia. The future is now. Stop hurting yourself; everything will be okay, and I promise I'll be the first guest at your and Mason's marriage. "
    Mia "Do you think that the future is possible? I wonder if I am good enough for him. "
    Veronica "Of course it is, and you're right. You're not just good. "
    show bg miaveroeve 11 with Dissolve(0.8)
    Veronica "You're perrrfect, I gotta go, but I'll make you smile this way from now on if you're sad. "
    Mia "Thank you... ( I wish I were as positive as her ) "
    ""
    stop music
    jump miamasonmiday

label sachikohome:
    play music "/audio/schikobthscn.ogg"
    show bg sachikohome 1 with Dissolve(0.8)
    "" "{i}Tada Household{/i}"
    Sachiko "I sure hope Rin didn't feel bad about me not going to drop her off. "
    show bg sachikohome 2 with Dissolve(0.8)
    Sachiko "She needed some freedom anyway , it's fine. "
    show bg sachikohome 3 with Dissolve(0.8)
    Sachiko "What I need right now is some rest and alone time. "
    show bg sachikohome 4 with Dissolve(0.8)
    Sachiko "Let me get into something comfortable first. "
    show bg sachikohome 5 with Dissolve(0.8)
    ""
    show bg sachikohome 6 with Dissolve(0.8)
    Liu "Why's the door open? I bet it was Rin. "
    show bg sachikohome 7 with Dissolve(0.8)
    Liu "Mom? I'm home, and I'm hungry. "
    show bg sachikohome 8 with Dissolve(0.8)
    Liu "Darn it, this is all sweet stuff , I wanted something spicy. "
    show bg sachikohome 9 with Dissolve(0.8)
    Liu "I'll just go ask mom to make some noodles."
    show bg sachikohome 10 with Dissolve(0.8)
    "*Phone rings* "
    show bg sachikohome 11 with Dissolve(0.8)
    Sachiko "I had my favorite movie loaded. Alright, let's see who this is. "
    show bg sachikohome 12 with Dissolve(0.8)
    ""
    show bg sachikohome 13 with Dissolve(0.8)
    Sachiko "Mia?... let me pick this up. "
    show bg sachikohome 14 with Dissolve(0.8)
    Miaonphone "Sachiko! This is Mia... I need your help. "
    Sachiko "Oh, hi Mia , yes, tell me what I can help you with. "
    Miaonphone "I need some documents you have on john and the child support ... I'm sorry, but it can help my case. "
    show bg sachikohome 15 with Dissolve(0.8)
    Sachiko "No, I understand , of course, please give me a moment. I have the soft copies in my laptop, I think."
    Miaonphone "Thank you so much. Take your time. "
    show bg sachikohome 16 with Dissolve(0.8)
    Sachiko "Okay, okay... it was here, I think. "
    show bg sachikohome 17 with Dissolve(0.8)
    Liu "Mom, could you make me some noo- "
    show bg sachikohome 18 with Dissolve(0.8)
    Liu "Whoa , is that... mom. "
    show bg sachikohome 19 with Dissolve(0.8)
    Liu "Her ass is so big... "
    show bg sachikohome 20 with Dissolve(0.8)
    ""
    show bg sachikohome 21 with Dissolve(0.8)
    Sachiko "So Mia I'll archive these and send you on mail , is there anything else? "
    Miaonphone "Well not really , how are you though? how are the kids? "
    show bg sachikohome 22 with Dissolve(0.8)
    Sachiko "Well the usual , When's the hearing? I hope you get rid of john soon. "
    show bg sachikohome 23 with Dissolve(0.8)
    Miaonphone "The hearing is 3 days from now , I wanted to also ask you who was the lawyer who fought for john in your case? "
    Sachiko "Oh it was this girl her- "
    show bg sachikohome 24 with Dissolve(0.8)
    Sachiko "*Gasp* What the f- "
    Miaonphone "What happened Sachi? you there? "
    show bg sachikohome 25 with Dissolve(0.8)
    Sachiko "I-uh yes I'm here , her name was Jennifer... Mia can I call you in a bit? "
    Miaonphone "Why? what happened? I hope john's not bothering you is he? "
    show bg sachikohome 26 with Dissolve(0.8)
    Sachiko "No no its just... something sudden. "
    Miaonphone "Look I know being a single mother has been rough on you , I'm sorry for reminding you of him today. "
    show bg sachikohome 27 with Dissolve(0.8)
    Sachiko "Ahh no its okay , Mia I actually. "
    Mia "Yes I know you have anxiety issues as well , look I'm here for you too okay. "
    show bg sachikohome 28 with Dissolve(0.8)
    Sachiko "Mia I know what you mean , but can we talk in a bit I uh... I gotta pee. "
    Mia "Uh what? did you drink too much water or something haha? "
    show bg sachikohome 29 with Dissolve(0.8)
    Sachiko "Ye... yeah I just. "
    Miaonphone "Look I understand talking to me may feel weird because we're both victims here. "
    show bg sachikohome 30 with Dissolve(0.8)
    Miaonphone "But once I'm through this I hope we can meet and talk and - "
    Sachiko "MIA I'LL TALK TO YOU LATER OKAY I PROMISE BYE. "
    show bg sachikohome 31 with Dissolve(0.8)
    Sachiko "Back off ! "
    Liu "Woah *thud* "
    show bg sachikohome 32 with Dissolve(0.8)
    Sachiko "What do you think you're doing young man? "
    Liu "Mom I'm sorry I couldn't control- "
    show bg sachikohome 33 with Dissolve(0.8)
    Sachiko "Not one word more! Out of the room now and we're gonna have a talk about this. "
    show bg sachikohome 34 with Dissolve(0.8)
    Liu "Sorry mom... "
    Sachiko "He's been this way ever since his 18th birthday ,  what am I gonna do with this kid. "
    ""
    stop music
    jump miaveroeve


label auntdinner:
    play music "/audio/kiaanttlkscn.ogg"
    show bg jpndinnerkiaxia 1 with Dissolve(0.8)
    "" "Bit later , dinning room"
    Kiara "I should talk to mom tomorrow, get her informed and stuff. "
    show bg jpndinnerkiaxia 2 with Dissolve(0.8)
    Xia "Kiara , come sit. Let's have dinner. "
    show bg jpndinnerkiaxia 3 with Dissolve(0.8)
    Kiara "Auntie , where's natsuko? She's not hungry? "
    Xia "She wanted to eat in her room , so I let her probably be tired. "
    show bg jpndinnerkiaxia 4 with Dissolve(0.8)
    Kiara "Are these rice cakes?... they look wonderful. "
    Xia "(I knew she'd love em) "
    show bg jpndinnerkiaxia 5 with Dissolve(0.8)
    Kiara "Aunty, I wanted to apologize for the kimono , it got so dirty I'll clean it up. "
    Xia "What are you talking about? It's fine.  "
    show bg jpndinnerkiaxia 6 with Dissolve(0.8)
    Kiara "Are you sure? "
    Xia "Kiara seeing you in it alone was worth its price. "
    show bg jpndinnerkiaxia 7 with Dissolve(0.8)
    Kiara "Alright, let's dig in then. "
    Xia "Speaking of which... kiara, are you unhappy here? "
    show bg jpndinnerkiaxia 8 with Dissolve(0.8)
    Kiara "No, aunty , I'm happy to be here. "
    Xia "Well... "
    show bg jpndinnerkiaxia 9 with Dissolve(0.8)
    Xia "Natsuko told me you're looking for a job tomorrow ... why so? "
    Kiara "Auntie, I just am tired of not being independent. "
    show bg jpndinnerkiaxia 10 with Dissolve(0.8)
    Kiara "I don't want to burden anyone , I want to have my place in the world. "
    show bg jpndinnerkiaxia 11 with Dissolve(0.8)
    Xia "But kiara, you aren't a burden to me , just because you're mia's daughter doesn't mean you're any less , this is your home too. "
    Kiara "Auntie, I don't mean it that way , I know you care, and it's my home, but I want to separate myself too , I want people to know that I can live in the real world too. "
    show bg jpndinnerkiaxia 12 with Dissolve(0.8)
    Xia "But honey, you've been through enough already , you can take this step later too , rest for now. "
    Kiara "Auntie, time doesn't stop , it'll keep moving, and if I delay this now , it'll just be another procrastinated event in my life. I'm sorry, I don't mean to be rude , I want to be confident in myself too. "
    show bg jpndinnerkiaxia 13 with Dissolve(0.8)
    Xia "Alright, honey , but will you at least let me know if you're ever in trouble? "
    Kiara "Yes , I promise. "
    show bg jpndinnerkiaxia 14 with Dissolve(0.8)
    Xia "Come give your aunt a hug then? "
    show bg jpndinnerkiaxia 15 with Dissolve(0.8)
    Kiara "Thank you for understanding auntie , I'm glad I can open up to you. "
    Xia "You always can , I'll be here for you. "
    ""
    stop music
    jump Keisukereveal

label backhomenight:
    play music "/audio/bkhome.ogg"
    show bg backhomenight 1 with Dissolve(0.8)
    Natsuko "Scared? "
    show bg backhomenight 2 with Dissolve(0.8)
    Kiara "Abit... "
    show bg backhomenight 3 with Dissolve(0.8)
    Natsuko "Don't worry, just be behind me, okay , we'll handle this. "
    Kiara "Okay. "
    show bg backhomenight 4 with Dissolve(0.8)
    Xia "Father , I miss you. If you were here, maybe things would be easier."
    show bg backhomenight 5 with Dissolve(0.8)
    Natsuko "M-Mom... I'm home. "
    show bg backhomenight 6 with Dissolve(0.8)
    Xia "Natsuko , Kiara come here please. "
    show bg backhomenight 7 with Dissolve(0.8)
    NatsukoKiara "Mom, I can explain , it got dark, and then we took- aunty, it's my fault. I promise it won't happ- "
    show bg backhomenight 8 with Dissolve(0.8)
    NatsukoKiara "Hu? um? "
    Xia "What are you two saying? I'm glad your home, I was so worried. "
    show bg backhomenight 9 with Dissolve(0.8)
    Natsuko "So you're not angry? "
    Xia "What? I've never been that way to you, have I? Please, you two must be tired , get freshened up, and let's eat dinner, alright? "
    NatsukoKiara "Yes, mom , Yes, aunty. "
    show bg backhomenight 10 with Dissolve(0.8)
    Xia "Look at her , looks lovely in the kimono, doesn't she natsu? "
    show bg backhomenight 11 with Dissolve(0.8)
    Xia "Natsuko? Honey? "
    show bg backhomenight 12 with Dissolve(0.8)
    Natsuko "(I should just talk to Kiara maybe she'll-) "
    show bg backhomenight 13 with Dissolve(0.8)
    Xia "Natsuko? are you alright? "
    Natsuko "I- yes, mom, just a bit tired , I'll take my dinner to my room, is that okay? "
    Xia "Of course, rest well , I love you. "
    show bg backhomenight 14 with Dissolve(0.8)
    Natsuko "Love you to mom, Goodnight. "
    Xia "Hm... ( Is she okay?... I'll ask her tomorrow. She needs some space now, it seems) "
    ""
    stop music
    jump auntdinner

label aftersubway2:
    play music "/audio/ntsuaftrsbwy.ogg"
    show bg kianatsuaftrsbway 5 with Dissolve(0.8)
    "" "{i}Home Street {/i}"
    Kiara "I think we're close right? natsu? "
    show bg kianatsuaftrsbway 5 with Dissolve(0.8)
    Natsuko "( What do I do , I want to tell her...) "
    show bg kianatsuaftrsbway 6 with Dissolve(0.8)
    Natsuko "She's gonna live here , city is great but predators exist too. "
    Kiara "Natsu? "
    show bg kianatsuaftrsbway 7 with Dissolve(0.8)
    Natsuko "And her past... it feels just so wrong to hide it even if mom told me to. "
    show bg kianatsuaftrsbway 8 with Dissolve(0.8)
    Natsuko "What if aunt Mia loses the case? I don't want her to go back."
    Kiara "Natsuko!! "
    Natsuko "Wha-! "
    show bg kianatsuaftrsbway 9 with Dissolve(0.8)
    Kiara "What's wrong? You haven't talked since we left subway. Are you alright? "
    Natsuko "Um , no kiara I'm fine just- "
    show bg kianatsuaftrsbway 10 with Dissolve(0.8)
    Natsuko "I'm just exhausted... I walked a lot today. "
    Kiara "Oh... we're close, right? "
    show bg kianatsuaftrsbway 11 with Dissolve(0.8)
    Natsuko "Yes , the house is to the left."
    show bg kianatsuaftrsbway 12 with Dissolve(0.8)
    Kiara "I'm sorry again. I- "
    Natsuko "No - no, it's not because of you , don't worry. "
    ""
    stop music
    jump backhomenight

label introsachikorin:
    play music "/audio/schikobthscn.ogg"
    show bg sachikandrinintro 1 with Dissolve(0.8)
    "" "{i}Sachiko's Home{/i}"
    Sachiko "What on earth is taking her so long. "
    show bg sachikandrinintro 2 with Dissolve(0.8)
    Sachiko "Rin , You'll be late sweetheart , ms beth just called me as well."
    Rin "Give me a few minutes, mom, just getting my boots on. "
    show bg sachikandrinintro 3 with Dissolve(0.8)
    Sachiko "Okay , I'll be in the living room! "
    show bg sachikandrinintro 4 with Dissolve(0.8)
    Sachiko "Good grief, this girl , how will she manage herself in japan? "
    show bg sachikandrinintro 5 with Dissolve(0.8)
    Rin "Being with Lana will be fun. I hope to open up more in japan. "
    Sachiko "Rin... hurry up, please. "
    show bg sachikandrinintro 6 with Dissolve(0.8)
    Rin "Yes, mom, I'm coming! "
    show bg sachikandrinintro 7 with Dissolve(0.8)
    Rin "Alright, enough decor , time to go. "
    show bg sachikandrinintro 8 with Dissolve(0.8)
    Rin "What's with Lana's obsession with ancient dress anyway. "
    show bg sachikandrinintro 9 with Dissolve(0.8)
    Sachiko "Why am I feeling such a bad omen today?... "
    show bg sachikandrinintro 10 with Dissolve(0.8)
    Rin "Mom , I'm ready lets go? "
    show bg sachikandrinintro 11 with Dissolve(0.8)
    Sachiko "Oh, Rin , the keys are next to the garage door. Feel free. "
    Rin "Um... what "
    show bg sachikandrinintro 12 with Dissolve(0.8)
    Rin "I thought we were going together to drop me off. "
    Sachiko "I feel very anxious suddenly. I'm going to take some meds and rest, okay? I'm sorry, sweety. I'm sure you'll be fine, you're a big girl. "
    Rin "Well yes but... "
    show bg sachikandrinintro 13 with Dissolve(0.8)
    Sachiko "Please let me know when you reach your distination, okay? Love you lots. "
    Rin "Um ( Is she angry at me because I'm moving?... I doubt it , I hope mom's okay) "
    show bg sachikandrinintro 14 with Dissolve(0.8)
    Rin "Ahh *stretch* Well , I'll be back in a month , I think she's staying for liu as well. "
    show bg sachikandrinintro 15 with Dissolve(0.8)
    Rin "I hope I meet someone cute at least , tired of try hard fuckboys. "
    show bg sachikandrinintro 16 with Dissolve(0.8)
    Rin "Plus, I wonder what Lana's deal is. Her travel plans are more random than her mood swings. "
    show bg sachikandrinintro 17 with Dissolve(0.8)
    ""
    jump valntdamimomscn

label Lanaliz:
    play music "/audio/clthnshop.ogg"
    show bg lanaandlizatshop 1 with Dissolve(0.8)
    Lana "Karl you fucking idiot , I knew you'd mess it up. "
    Karl "Ms. Lana, please, I misunderstood. "
    show bg lanaandlizatshop 2 with Dissolve(0.8)
    Lana "How do you mess something up that's just so simple to do? "
    Karl "Please Ms. Lana at least hear me out, you said Japanese dress, and I-{w=1.5}{nw}"
    show bg lanaandlizatshop 3 with Dissolve(0.8)
    Lana "Karl, stop being delusional."
    show bg lanaandlizatshop 4 with Dissolve(0.8)
    Lana "I told you , ancient Japanese dress. "
    Karl "Yes, mam and it is Japane- "
    show bg lanaandlizatshop 5 with Dissolve(0.8)
    Lana "In what world is this ancient, you daft cunt? "
    Karl "Forgive me, mam , I'll get it for you tommor- "
    show bg lanaandlizatshop 6 with Dissolve(0.8)
    Lana "I have a flight in 4 hours, you muppet! "
    Karl "Argh, my jaw! "
    show bg lanaandlizatshop 7 with Dissolve(0.8)
    Elizabeth "What's happening here? Lana, behave and get in the car. "
    show bg lanaandlizatshop 8 with Dissolve(0.8)
    Lana "But momm... "
    Elizabeth "No buts , I understand you're angry but behave , I've talked to Sachiko. Rin will help you with your dress. "
    show bg lanaandlizatshop 9 with Dissolve(0.8)
    Lana "Ugh , okay, mom."
    Karl "*grumbling*Augh , my face. "
    Elizabeth "Karl , Get up, please. "
    show bg lanaandlizatshop 10 with Dissolve(0.8)
    Elizabeth "Are you alright? I'm sorry on behalf of Lana. "
    Karl "No, it's okay, ms Elizabeth, it was my fault too , it only hurts a bit. "
    show bg lanaandlizatshop 10pt2 with Dissolve(0.8)
    Elizabeth "*Smooch* , There I hope that helps , and we'll buy the dress regardless. "
    Karl "Urm... ( Wow, her lips are so soft) "
    show bg lanaandlizatshop 11 with Dissolve(0.8)
    Elizabeth "Take good care, okay? And feel free to visit home if you need some tea. "
    Karl "Yes... of course, Ms. Elizabeth. "
    show bg lanaandlizatshop 12 with Dissolve(0.8)
    Karl "Man, how does an elegant lady like her share genes with that brat Lana... I'd get hurt 100 times a day if I could get that. "
    show bg lanaandlizatshop 13 with Dissolve(0.8)
    Lana "Mommm , I'll be late, c'mon."
    show bg lanaandlizatshop 14 with Dissolve(0.8)
    Elizabeth "Lana , that wasn't very nice of you , please call him later and apologize, okay? "
    Lana "I'm sorry mom , I lost my cool, but yes, I will , shall we go? "
    show bg lanaandlizatshop 15 with Dissolve(0.8)
    Elizabeth "Yes & don't worry, you'll get your dress on time, honey. "
    Lana "Okay, mom , off we go. "
    ""
    stop music
    jump assistantevngscn

label miamasonmiday:
    show bg miamasonnoon 1 with Dissolve(0.8)
    play music "/audio/miamsnntlk.ogg"
    News "Signs of a heavy storm in japan in the upcoming days , homeless shelters are advised to be evacuated. "
    Mia "This primarily will affect Tokyo, I think , but I hope kiara doesn't go out in the rain much. "
    show bg miamasonnoon 2 with Dissolve(0.8)
    Mason "Hm? *Silently* Oh, it's her. "
    News "In other news , a Florida man bites his jaguar back. "
    show bg miamasonnoon 3 with Dissolve(0.8)
    ""
    show bg miamasonnoon 4 with Dissolve(0.8)
    Mason "Surpriseee , guess who? "
    Mia "Ahh... someone handsome? "
    show bg miamasonnoon 5 with Dissolve(0.8)
    Mason "Hmm, wrong guess , c'mon guess right, and you get a gift. "
    Mia "My future husband? "
    show bg miamasonnoon 6 with Dissolve(0.8)
    Mason "Right guess, you win a forehead kiss. "
    Mia "I prefer a lip one, though. "
    show bg miamasonnoon 7 with Dissolve(0.8)
    Mason "Your wish is my command. "
    MiaMason "*Kissing each other* "
    stop music
    jump Investigationafter

label Investigationafter:
    play music "/audio/invstaftrjke2.ogg"
    show bg investigatoraftermiamason 1 with Dissolve(0.8)
    Jake "Ah, I doubt they're gonna do anything anymore. "
    show bg investigatoraftermiamason 2 with Dissolve(0.8)
    Jake "Ah man, I feel jealous almost , good for them, I guess. "
    show bg investigatoraftermiamason 3 with Dissolve(0.8)
    Jake "I need a break dude , tracking all this shit and then fucking my sleep schedule as well. "
    show bg investigatoraftermiamason 4 with Dissolve(0.8)
    Jake "I should probably check on veronica as well , god knows what that girl is doing. "
    show bg investigatoraftermiamason 5 with Dissolve(0.8)
    Jake "Alright, c'mon Jake , just a bit more. "
    show bg investigatoraftermiamason 6 with Dissolve(0.8)
    Jake "Hm, alright, john told me to be outside his office , suppose I'll go there. "
    ""
    stop music
    jump sachikohome

label aftersubway:
    show bg kianatsuaftrsbway 1 with Dissolve(0.8)
    play music "/audio/ntsuaftrsbwy.ogg"
    "" "Outside station"
    Natsuko "I can't let something like that happen to kia... I'll tell her to be careful or save her. "
    show bg kianatsuaftrsbway 2 with Dissolve(0.8)
    Kiara "Hello slowpoke , took you a while? "
    Natsuko "Oh... yea bit crowded. "
    show bg kianatsuaftrsbway 3 with Dissolve(0.8)
    Kiara "So up then left right? "
    Natsuko "Hm yeah , come lets go. "
    show bg kianatsuaftrsbway 4 with Dissolve(0.8)
    Kiara "You were right about the cabs being clean , really hygenic. "
    Natsuko "Yeah I know right , it's pretty clean. "
    ""
    stop music
    jump aftersubway2

label natsugrop:
    show bg natsugropedecd
    Molester "Don't worry I'll just play with you a little baby. "
    Natsuko "I've got to be quick here , what do I do? "
    play music "/audio/choicmusic.ogg"
    menu:
        "I'm not letting this happen , he can't do this.":
            call natsugroprjct from _call_natsugroprjct
        "I can't make a scene... Kiara and I need to go home.":
            $ mc_stats.adjust_corruption(1)
            call natsugropaccpt from _call_natsugropaccpt

    ""


label natsugroprjct:
    stop music
    show bg natsugroperjct 1 with Dissolve(0.8)
    play music "/audio/chiknrjct.ogg"
    Natsuko "Alright , I have a grip on the top... "
    show bg natsugroperjct 2 with Dissolve(0.8)
    Natsuko "SOMEONE HELP PLEASE ! THERE'S A MOLESTER HERE! "
    Molester "What the - I'll get you next time bitch "
    show bg natsugroperjct 3 with Dissolve(0.8)
    "Crowd background""Hello? miss are you okay? , Hey someone catch that bald fuck , Poor girl , Hey let me help you with your top I'm a woman. "
    show bg natsugroperjct 4 with Dissolve(0.8)
    Natsuko "It was risky but I did it... god knows what he would've done. "
    ""
    stop music
    jump aftersubway

label natsugropaccpt:
    stop music
    show bg natsugropedecd with Dissolve(0.8)
    play music "/audio/ntsuchiknacpt.ogg"
    Natsuko "I have to endure , can't make a scene he won't do anything extreme in public right? "
    show bg natsugropaccpt 1 with Dissolve(0.8)
    Molester "Good girl , Lets cope a feel of these shall we? "
    show bg natsugropaccpt 2 with Dissolve(0.8)
    Molester "Oooh , these are nice , you oil them daily it seems. "
    Natsuko "Shut up... "
    show bg natsugropaccpt 3 with Dissolve(0.8)
    Molester "Hate it? you're the one letting me do it baby , don't my hands feel nice? "
    Natsuko "Ugh "
    show bg natsugropaccpt 4 with Dissolve(0.8)
    Natsuko "(Just a bit more... ignore whatever he says) "
    show bg natsugropaccpt 5 with Dissolve(0.8)
    Natsuko "This is so gross , how can you do this? "
    Molester "Oh cmon sweetheart , you're gonna tell me you haven't fantasized about it ? "
    Natsuko "No! "
    show bg natsugropaccpt 6 with Dissolve(0.8)
    Molester "Damn these fit in my hand so well... you know I was gonna go for the american but- "
    show bg natsugropaccpt 7 with Dissolve(0.8)
    Natsuko "*gasp* Kya! "
    Molester "You sure are a babe too , I mean look at these tits... "
    show bg natsugropaccpt 8 with Dissolve(0.8)
    Molester "Let's see down below... "
    Natsuko "Huh?... hey wh- "
    show bg natsugropaccpt 9 with Dissolve(0.8)
    Natsuko "Hey! stop, you can't do this. We're in public."
    Molester "I'm the only thing covering you right now, so how about you shut up? "
    Molester "Besides, you say you hate it , but your body says otherwise."
    show bg natsugropaccpt 10 with Dissolve(0.8)
    Molester "These nipples are rock hard... you're even turned on, I bet. "
    Natsuko "Screw you... "
    show bg natsugropaccpt 11 with Dissolve(0.8)
    Molester "We'll do that too , I'll feel every it of you with my fingers and lips, baby. "
    show bg natsugropaccpt 12 with Dissolve(0.8)
    Molester "I'll taste you too , such a yummy girl after all. "
    Natsuko "Please stop... I don't. "
    show bg natsugropaccpt 13 with Dissolve(0.8)
    Natsuko "No! he's actually taking them off , hey! "
    show bg natsugropaccpt 14 with Dissolve(0.8)
    Natsuko "Hey, stop... I'll... I'll shout. "
    Molester "Oh yea?... what's that gonna do? "
    show bg natsugropaccpt 15 with Dissolve(0.8)
    Molester "Half the train will see your tits and your pants down , what do you think the guys will do? "
    show bg natsugropaccpt 16 with Dissolve(0.8)
    Molester "I bet they'd strip you naked and fuck you right here even , so stay quiet and let me have a little fun. "
    Natsuko "Okay... *sniff* "
    show bg natsugropaccpt 17 with Dissolve(0.8)
    Molester "Mm... cotton very soft , I like the texture. "
    Natsuko "Just stop talking... please."
    show bg natsugropaccpt 18 with Dissolve(0.8)
    Molester "That's half the fun though , making you realize you're a slut that's letting me do this is fun, babe. "
    Natsuko ".... "
    Molester "Let's see this ass first."
    show bg natsugropaccpt 19 with Dissolve(0.8)
    Molester "So big and soft , I bet you never got fucked anally, huh? "
    Natsuko "*sniff* I'm- "
    show bg natsugropaccpt 20 with Dissolve(0.8)
    Molester "Yea yea, whatever, let's slide these down... you're the softest slut I've met, you know that? "
    Natsuko "Please stop , I'm sens- "
    Molester "Shhh, stay quiet. *kisses Natsu's cheek* "
    show bg natsugropaccpt 21 with Dissolve(0.8)
    Molester "I love the trim , did you do it for me, baby? "
    Natsuko ".... "
    show bg natsugropaccpt 22 with Dissolve(0.8)
    Molester "Let's feel your insides, hehe... "
    Natsuko "No... please someone... "
    show bg natsugropaccpt 23 with Dissolve(0.8)
    "Announcement""Train station has been reached , please stay away from the doors. "
    Molester "Shit...saved by the bell, babe. "
    Natsuko "*sniff* Thank god... "
    show bg natsugropaccpt 24 with Dissolve(0.8)
    Molester "Wear a skirt next time... we'll have more fun... hehe *buttslap* "
    Natsuko "I...why didn't I stop him... "
    show bg natsugropaccpt 25 with Dissolve(0.8)
    Natsuko "I should dress up , I can't let anyone see me like this. "
    ""
    stop music
    jump aftersubway



label returninghome:
    play music "/audio/kiaenvg.ogg"
    show bg kiaraandnatsugohome 1 with Dissolve(0.8)
    Kiara "I hope you don't mind , my cousin will be here soon. "
    Ino "Not at all , please feel free to be comfortable here. "
    show bg kiaraandnatsugohome 2 with Dissolve(0.8)
    Kiara "So you said you live alone here because your kids left? Why not go with them? "
    Ino "It's because I've been disappointed by them and didn't want to again. "
    show bg kiaraandnatsugohome 3 with Dissolve(0.8)
    Kiara "But don't you feel alone? No family here , no one to talk to? "
    Ino "I've learned not to mind it. "
    show bg kiaraandnatsugohome 4 with Dissolve(0.8)
    Ino "Being independent has its perks Kiara, you learn not to care about what others think. "
    Kiara "I see , I suppose in a way it's peaceful... but anyway I- *Knock knock* "
    show bg kiaraandnatsugohome 5 with Dissolve(0.8)
    Kiara "Ah, that must be my cousin ... I've got to go, Ms. Ino; I hope we meet again. "
    show bg kiaraandnatsugohome 6 with Dissolve(0.8)
    Ino "I'll be here , feel free to visit. "
    Kiara "Coming natsu! "
    show bg kiaraandnatsugohome 7 with Dissolve(0.8)
    Natsuko "Well, well , if it's kiara the explorer. "
    Kiara "I'm sorry , I didn't mean to upset you or aunty , I apologize seriously. "
    show bg kiaraandnatsugohome 8 with Dissolve(0.8)
    Natsuko "Hey, hey it's okay. I was teasing you, silly. "
    Kiara "I know, but I should be more careful , auntie's mad at me probably... "
    show bg kiaraandnatsugohome 9 with Dissolve(0.8)
    Kiara "I'll do my best from now, I promise... I just got lost and - "
    Natsuko "Hey shush... we care about you , you can explore all you want. You're not trapped here, okay? Now, please smile for me. "
    show bg kiaraandnatsugohome 10 with Dissolve(0.8)
    Kiara "Okay... "
    Natsuko "That's such an awful smile, but you're adorable so I'll allow it, "
    stop music
    #loading


    pass
label returninghome2:
    play music "/audio/ntsukianitwlk.ogg"
    show bg kiaraandnatsugohome 11 with Dissolve(0.8)
    Natsuko "Ahh, my feet hurt. "
    Kiara "I can't believe I walked this far. How did I not notice it? "
    show bg kiaraandnatsugohome 11pt1 with Dissolve(0.8)
    Natsuko "Worse thing is my phone's dead too. Mom will kill me.  "
    Kiara "I feel bad , I hope you're not mad at me. "
    Natsuko "Of course, I'm not , don't be silly. "
    show bg kiaraandnatsugohome 11pt2 with Dissolve(0.8)
    Kiara "My phone's dead too... it's dark as well , should we walk back? "
    Natsuko "You're right , okay, follow me. Let's take the subway. "
    show bg kiaraandnatsugohome 12 with Dissolve(0.8)
    "???""Hehehe, subway , that'll be fun. "
    stop music
    show bg kiaraandnatsugohome 13 with Dissolve(0.8)
    play music "/audio/subwy.ogg"
    Kiara "Are the subways here good? Back in NY, it's an unhygienic mess. "
    Natsuko "Oh no, they're spotless here. It's how my friends travel as well. "
    show bg kiaraandnatsugohome 14 with Dissolve(0.8)
    Natsuko "Plus, our home is near 4 stations, so wherever you go, you'll be home in 25 minutes or less. "
    Kiara "(I suppose subways are good for now till I get proper transport.)."
    show bg kiaraandnatsugohome 15 with Dissolve(0.8)
    Kiara "Is it usually this crowded even at night? "
    Natsuko "This is less than half of Osaka uses subways since it's also very cheap. "
    show bg kiaraandnatsugohome 16 with Dissolve(0.8)
    Natsuko "The only downside is if you have OCD then forget it, and another issue being chi- "
    show bg kiaraandnatsugohome 17 with Dissolve(0.8)
    "Announcement""{i}Attention all passengers , the cab is at the station. Please get inside.{/i} "
    show bg kiaraandnatsugohome 18 with Dissolve(0.8)
    Kiara "Natsu! "
    Natsuko "Aaah , they don't push what the. "
    show bg kiaraandnatsugohome 19 with Dissolve(0.8)
    Natsuko "Well, this is what I get for standing in front of the gate crowd. "
    show bg kiaraandnatsugohome 20 with Dissolve(0.8)
    Kiara "I hope she got in... last thing I'd want is her to be more delayed cuz of me...wh- *looks down* "
    show bg kiaraandnatsugohome 21 with Dissolve(0.8)
    Natsuko "Don't worry, I'm in the other cab , we'll meet in like 15 minutes. "
    show bg kiaraandnatsugohome 22 with Dissolve(0.8)
    Kiara "Are you alright? I hope you found a place to sit. "
    Natsuko "Far from it , but don't worry, I'm good to see you in a bit. "
    show bg kiaraandnatsugohome 23 with Dissolve(0.8)
    Natsuko "Alright then , music time it is. "
    show bg kiaraandnatsugohome 24 with Dissolve(0.8)
    stop music
    show bg kiaraandnatsugohome 25 with Dissolve(0.8)
    play music "/audio/ntsuchikn.ogg"
    "???""Start with a soft touch... "
    show bg kiaraandnatsugohome 26 with Dissolve(0.8)
    "???""Doesn't seem to notice... let's go further, then. "
    show bg kiaraandnatsugohome 27 with Dissolve(0.8)
    ""
    show bg kiaraandnatsugohome 28 with Dissolve(0.8)
    ""
    show bg kiaraandnatsugohome 29 with Dissolve(0.8)
    ""
    show bg kiaraandnatsugohome 30 with Dissolve(0.8)
    Natsuko "Is that someone's hand? it is crowded... "
    show bg kiaraandnatsugohome 31 with Dissolve(0.8)
    Natsuko "*Gasp* Ah! Hey, what are you-... "
    show bg kiaraandnatsugohome 32 with Dissolve(0.8)
    Molester "You might want to stay quiet, sweetheart. "
    Natsuko "Hey who are yo- "
    show bg kiaraandnatsugohome 33 with Dissolve(0.8)
    Molester "Shhh , it'll take me a minute to rip this top away and disappear into the crowd. Meanwhile, you'd be left topless in a train full of mostly guys,  you sure you want that?... "
    Natsuko "(What the hell.... he can't be serious?)"
    stop music
    jump natsugrop

label auntlateevng:
    play music "/audio/anthmevscn.ogg"
    show bg xiaevescn 1 with Dissolve(0.8)
    Xia "What should I make for dinner? I wonder what she'll like."
    show bg xiaevescn 2 with Dissolve(0.8)
    Xia "Hmm... maybe rice cakes, or tofu. I guess I'll make both."
    show bg xiaevescn 3 with Dissolve(0.8)
    Xia "I should get some sake as well , she'll like it. "
    show bg xiaevescn 4 with Dissolve(0.8)
    Xia "Hm? Ah, it must be her. "
    show bg xiaevescn 5 with Dissolve(0.8)
    Xia "Hello? Kiara? where are you?"
    show bg xiaevescn 6 with Dissolve(0.8)
    Ichigo "Oh , is she home already? Xia?"
    Xia "Ichigo! yes, she arrived early... how are you, love?"
    show bg xiaevescn 7 with Dissolve(0.8)
    Ichigo "That's good to hear, and I'm perfect. How's my lovely wife doing?"
    Xia "Well, your lovely wife misses her lovely husband."
    show bg xiaevescn 8 with Dissolve(0.8)
    Ichigo "Ahaha , I'll be home soon. I'm sorry , and I'll bring your favorite flowers as well. "
    Xia "You better , or you're not getting any of me."
    show bg xiaevescn 9 with Dissolve(0.8)
    Ichigo "Very well , speaking of which... what are you wearing, love? "
    Xia "A top half kimono.... "
    Ichigo "Oh.... and? "
    show bg xiaevescn 10 with Dissolve(0.8)
    Xia "You heard me."
    Ichigo "Wait, so... you're bottomless? "
    show bg xiaevescn 11 with Dissolve(0.8)
    Xia "Hmmm , maybe I am. "
    Ichigo "W-wow... um, can I video call? "
    show bg xiaevescn 12 with Dissolve(0.8)
    Xia "Aheh, shut  up. I have to make dinner, Ichigo."
    Ichigo "Aww, well, can I at least have a kiss? "
    show bg xiaevescn 13 with Dissolve(0.8)
    Xia "Mwwah , there. "
    Ichigo "Thank you, that should suffice for the week. "
    show bg xiaevescn 14 with Dissolve(0.8)
    Ichigo "So...where's natsuko? She grew up so fast and didn't even call me a lot. "
    Xia "No, no , she misses you too, just busy, and currently outside with kiara. "
    show bg xiaevescn 15 with Dissolve(0.8)
    Ichigo "This late? Is everything alright? "
    Xia "Yes, all is well , kiara just got lost, so she went to find her. She's in the park. They'll return home soon. "
    show bg xiaevescn 16 with Dissolve(0.8)
    Ichigo "Oh, alright , so did you talk to kiara? How is she? "
    Xia "I did. She's... not okay, but I think her being here will help, and it'll take time, Ichigo. "
    Ichigo "Ah, of course, and what about Mia? is she coming? "
    show bg xiaevescn 17 with Dissolve(0.8)
    Xia "She won't be able to till the lawsuit, it seems. I miss sis. I hope this time that man gets out of her life. "
    Ichigo "I hope so as well , Xia. I have a small request. "
    show bg xiaevescn 18 with Dissolve(0.8)
    Xia "Yes, dear? What is it? "
    Ichigo "Please go easy on her, okay? I know you want her to be strong, but she's been through a lot. "
    show bg xiaevescn 19 with Dissolve(0.8)
    Xia "Of course, I will love , like I said, it'll take time for her to heal. I'll be there with her till she can stand. "
    Ichigo "Thank you , I hope Mia gets justice as well , I'm sure she'd love to be home again too. "
    show bg xiaevescn 20 with Dissolve(0.8)
    Xia "Yes , her birthday is soon as well. We'll have a good party. "
    Ichigo "Look at you , strong and caring... anyway, I'll eat dinner now, okay? "
    show bg xiaevescn 21 with Dissolve(0.8)
    Xia "Alright, I'll get to cooking too. I nee- "
    Ichigo "Wait, wait, wait ,  one super important thing. "
    show bg xiaevescn 22 with Dissolve(0.8)
    Xia "Yes, dear? Tell me. "
    Ichigo "Aishiteru Xia "
    show bg xiaevescn 23 with Dissolve(0.8)
    Xia "*Blushes* I love you more ... wait before you go, I have something to show you. "
    Ichigo "Oh, sure. "
    show bg xiaevescn 24 with Dissolve(0.8)
    Xia "Happy now? "
    Ichigo "Oh my kami , I am the luckiest man on earth... thank you, love."
    Xia "You're welcome *mwah* "
    ""
    stop music
    jump returninghome

label kiaralocal2:
    play music "/audio/kiaenvg.ogg"
    show bg kiarainlocal 9 with Dissolve(0.8)
    Natsuko "Where could she be? Mr. Daichi said she went this way but I can't find her...\n * phone rings * "
    show bg kiarainlocal 10 with Dissolve(0.8)
    Natsuko "Kon'nichiwa, koreha daredesuka? "
    Kiaraonphone "Um Natsu? is that you? "
    show bg kiarainlocal 11 with Dissolve(0.8)
    Natsuko "Kiara! Where are you? I've been trying to find you , I found your phone at taka's. "
    Kiaraonphone "I- I know I'm sorry I lost it there and I'm right now at tori gate garden , some house in the middle of it... could you come? "
    Natsuko "Yes , stay there don't move, okay? "
    show bg kiarainlocal 12 with Dissolve(0.8)
    Natsuko "C'mon, c'mon, it's close I can get there fast. "
    ""
    stop music
    jump auntlateevng


label azumiworried:
    play music "/audio/azmihmscn.ogg"
    show bg azumiworried 1 with Dissolve(0.8)
    "" "{i}Satō Household{/i}"
    Azumi "Why isn't she picking up my calls  ... or replying... Is she okay? "

    show bg azumiworried 2 with Dissolve(0.8)

    Azumi "Did I flirt too much?... Was I too direct? I really wanna talk to her. "

    show bg azumiworried 3 with Dissolve(0.8)

    Azumi "Kiara , even if any of that is true, I really hope you're okay, that's all. "

    "sato" "Azumi? did you not eat yet? "

    show bg azumiworried 4 with Dissolve(0.8)

    Azumi "Oh uncle... uh, I'm not hungry. "

    "sato" "Don't be silly , you haven't eaten since you arrived. Tell me, what's bothering you? "

    show bg azumiworried 5 with Dissolve(0.8)

    Azumi "It's just the girl I told you about uncle , she's not responding at all. It's been hours, and I'm worried. "

    "sato" "Azumi , she must be tired as well, you know. Maybe she's resting? "

    show bg azumiworried 6 with Dissolve(0.8)

    Azumi "We had a perfect vibe... She said she'll meet me as well , I hope that happens at least. "

    "sato" "I'm sure she will , so who is she anyway? "

    show bg azumiworried 7 with Dissolve(0.8)

    Azumi "This is her , She's moving from the states to here to start her life kinda , I just offered to help her, and our conversation seemed decent, really... "

    show bg azumiworried 8 with Dissolve(0.8)

    "sato" "I see ( Mmm... look at those lips, seems even I have to meet her in person now ) "

    show bg azumiworried 9 with Dissolve(0.8)

    "sato" "How about leaving the phone for a bit and eating? You need peace in your tummy first before your mind. "

    Azumi "Okay, uncle , I'll be back if she calls midway, please let me know. "

    show bg azumiworried 10 with Dissolve(0.8)

    "sato" "Don't worry , I will! "

    show bg azumiworried 11 with Dissolve(0.8)

    "sato" "I'll give her the job , bonus, and personal attention, heh. "
    ""
    stop music
    jump kiaralocal2

label veromeetsevlyn:
    play music "/audio/evlynvnca.ogg"
    scene bg veromeetsevelyn 1 with Dissolve(0.8)
    Veronica "Such a long trip , but I think it's about time. "
    show bg veromeetsevelyn 2 with Dissolve(0.8)
    Veronica "She's probably gonna be mad at me for this... "
    show bg veromeetsevelyn 3 with Dissolve(0.8)
    Veronica "Plus, it doesn't help that she's a diva as well. "
    show bg veromeetsevelyn 4 with Dissolve(0.8)
    Veronica "Though right now I have to do this , it's the only chance to fix this family. "
    show bg veromeetsevelyn 5 with Dissolve(0.8)
    Veronica "Welp , here goes nothing. "
    show bg veromeetsevelyn 6 with Dissolve(0.8)
    Veronica "Okay, deep breaths... Let's go. "
    show bg veromeetsevelyn 6pt2 with Dissolve(0.8)
    "Doorbell" "*Bell rings* "
    "???""Who could it be this early? "
    show bg veromeetsevelyn 7 with Dissolve(0.8)
    "???""I'm sure I have paid the bills for the month already.   "
    show bg veromeetsevelyn 8 with Dissolve(0.8)
    Veronica "Should I ring the bell again?... no, she hates it. I'll wait. "
    show bg veromeetsevelyn 9 with Dissolve(0.8)
    "???""Alright, I don't look homeless. At least, let's go. "
    show bg veromeetsevelyn 10 with Dissolve(0.8)
    "???""Please wait! I'm coming. "
    show bg veromeetsevelyn 11 with Dissolve(0.8)
    "???""I hope it isn't some pranking kids. "
    show bg veromeetsevelyn 12 with Dissolve(0.8)
    Veronica "There she is... Alright. "
    show bg veromeetsevelyn 13 with Dissolve(0.8)
    Veronica "Hello there , natural beauty. "
    show bg veromeetsevelyn 14 with Dissolve(0.8)
    Evelyn "Veronica?... Hey. "
    show bg veromeetsevelyn 15 with Dissolve(0.8)
    Veronica "That all I get for traveling 100 miles? hey? "
    Evelyn "Aheh, sorry, love, Just woke up. I didn't know you were coming. "
    show bg veromeetsevelyn 16 with Dissolve(0.8)
    Evelyn "Please come in , let's at least have a coffee. "
    Veronica "Ahh, your handmade coffee is worth even 1000 miles. "
    show bg veromeetsevelyn 17 with Dissolve(0.8)
    Evelyn "So what brings new york's hottest lawyer into my little shed? "
    Veronica "Look who's talking."
    show bg veromeetsevelyn 18 with Dissolve(0.8)
    Veronica "I've been trying to catch up to your beauty since we were teenagers. "
    show bg veromeetsevelyn 19 with Dissolve(0.8)
    Veronica "But... today I'm here for something serious."
    Evelyn "Hm? is everything alright, V? "
    Veronica "I-... I'm here to talk about Mia... "
    show bg veromeetsevelyn 20 with Dissolve(0.8)
    Evelyn "I don't know who that person is V , and I'd prefer you not to continue the conversation here. "
    Veronica "Eve, hear me out, please, at least. "
    show bg veromeetsevelyn 21 with Dissolve(0.8)
    Veronica "Eve , Mia needs you right now. Please understand she's not the person you remember. "
    Evelyn "Grandpa needed her too , what did she do? "
    show bg veromeetsevelyn 22 with Dissolve(0.8)
    Evelyn "I needed her too V , When I was 15 and I left that home she had the choice to save everyone but what did she do? "
    Veronica "Eve , I know what- "
    show bg veromeetsevelyn 23 with Dissolve(0.8)
    Evelyn "No you don't V , she had the choice to save grandpa , fix our lives but she chose to stay with that man instead. "
    Veronica "Eve , look... "
    show bg veromeetsevelyn 24 with Dissolve(0.8)
    Evelyn "As for that man... If I could rip my genes out I would , the fact that he's my father disgusts me. "
    Veronica "Evelyn please listen , it's not just about Mia here. "
    show bg veromeetsevelyn 25 with Dissolve(0.8)
    Evelyn "What do you mean? "
    Veronica "He tried to grope kiara , and it got very messy yesterday night. "
    show bg veromeetsevelyn 26 with Dissolve(0.8)
    Veronica "Before you lose it... Mia hit him in his junk and got kiara out and she's in japan now back at your aunt's house. "
    Evelyn "Okay... so why are you here? I mean... what can I do? "
    show bg veromeetsevelyn  27 with Dissolve(0.8)
    Veronica "I'm here for my friend , a daughter and a sister that this family desperately needs. "
    Evelyn "Do you mean Kiara?... She probably hates me V. "
    show bg veromeetsevelyn 28 with Dissolve(0.8)
    Evelyn "Even if  I go back , She'll just... not accept me or despise me and that'll break me V. "
    Veronica "Eve... "
    show bg veromeetsevelyn 29 with Dissolve(0.8)
    Veronica "Maybe it's the opposite, maybe what she needs the most now is a older sister , and what Mia needs is the piece of her heart that she's never able to hold again. "
    Evelyn "Do you really believe that?... "
    show bg veromeetsevelyn 30 with Dissolve(0.8)
    Veronica "I believe in you Evelyn , it's why I came here and I have faith you'll do the right thing. "
    Evelyn "Thank you V , you're amazing. "
    show bg veromeetsevelyn 31 with Dissolve(0.8)
    Veronica "No you're the amazing one , I just copy you hehe. "
    Evelyn "You're still the same... I'll get ready then. "
    show bg veromeetsevelyn 32 with Dissolve(0.8)
    Veronica "Be quick about it or I might join you in the shower nature beauty. Heh just kidding. "
    Evelyn "You and your silly compliments.... "
    ""
    stop music
    jump Lanaliz


label kiaralocal:
    play music "/audio/kiaenvg.ogg"
    show bg kiarainlocal 1 with Dissolve(0.8)
    Kiara "Dammit... I forgot my phone but I can't remember the way back either. "
    show bg kiarainlocal 2 with Dissolve(0.8)
    Kiara "Alright, I'll just keep going till I find someone sensible to talk to for help."
    show bg kiarainlocal 3 with Dissolve(0.8)
    Kiara "Mr. Daichi was right though , I have to become independent first and start over. "
    show bg kiarainlocal 4 with Dissolve(0.8)
    Kiara "Is that a tori garden? Someone might be there. "
    show bg kiarainlocal 5 with Dissolve(0.8)
    Kiara "I hope aunty won't be angry with me... "
    show bg kiarainlocal 6 with Dissolve(0.8)
    Kiara "Crap, It's getting late. What do I do? "
    show bg kiarainlocal 7 with Dissolve(0.8)
    Kiara "Wait, is that a hut? Can someone be inside? I can at least ask for a phone. "
    show bg kiarainlocal 8 with Dissolve(0.8)
    Kiara "Okay Kiara, don't be dumb. Just be formal and ask nicely. "
    ""
    stop music
    jump azumiworried


label natsufindingkiara2:
    play music "/audio/tkashop.ogg"
    show bg natsuandtakamid 1 with Dissolve(0.8)
    "" "{i}Taka's Shop, Osaka{/i}"
    Taka "Lookin great baby , show those curves! "
    show bg natsuandtakamid 2 with Dissolve(0.8)
    ""
    show bg natsuandtakamid 3 with Dissolve(0.8)
    ""
    show bg natsuandtakamid 4 with Dissolve(0.8)
    Taka "Keep at it. Let's get rid of the skirt, babe. "
    show bg natsuandtakamid 5 with Dissolve(0.8)
    Natsuko "Hey Taka did my cousin- Wh... "
    Taka "That's right sweety don't be shy. "
    show bg natsuandtakamid 6 with Dissolve(0.8)
    Natsuko "How on earth is that fashion? "
    Taka "Wait a sec, the babe got a guest here. "
    show bg natsuandtakamid 7 with Dissolve(0.8)
    Taka "Oh hey natsu , sup? "
    Natsuko "Sup? what are you doing shooting this lewd stuff."
    show bg natsuandtakamid 8 with Dissolve(0.8)
    Taka "You wouldn't get it , it's art. "
    Natsuko "Right... A R T , anyway I'm here to ask about kiara , did she come here? "
    show bg natsuandtakamid 9 with Dissolve(0.8)
    Taka "Oh yeah, she did , she forgot her phone here, actually. "
    show bg natsuandtakamid 10 with Dissolve(0.8)
    Natsuko "Okay.... and you did not think of informing or calling me why? "
    show bg natsuandtakamid 11 with Dissolve(0.8)
    Taka "Well, I did call you. You have my number blocked, that's all. "
    show bg natsuandtakamid 12 with Dissolve(0.8)
    Natsuko "Yeah , because you're one grade A creep. "
    Taka "Is not false but kinda harsh. "
    Natsuko "I don't care , thanks. "
    show bg natsuandtakamid 13 with Dissolve(0.8)
    Taka "So hey, you wanna get some coffee this weekend? "
    Natsuko "You ask that every time and it's the same answer always , bye taka. "
    show bg natsuandtakamid 14 with Dissolve(0.8)
    Taka "Aw man , oh well babe, let's lose the clothes altogether , let's not hide your beauty. "
    Model "Alright , I'll do a nice pose too. Just a second."
    show bg natsuandtakamid 15 with Dissolve(0.8)
    Taka "Nicely done babe , smile and gimme a good pose."
    show bg natsuandtakamid 16 with Dissolve(0.8)
    Taka "Mamma Mia! "
    ""
    stop music
    jump kiaralocal

label Johnandjake:
    play music "/audio/jnmrngscn.ogg"
    show bg johnafterintro 1 with Dissolve(0.8)
    John "Ugh my head...how long was I out for? "
    show bg johnafterintro 2 with Dissolve(0.8)
    John "Mia... Kiara... Man what a mess. "
    show bg johnafterintro 3 with Dissolve(0.8)
    John "Argh my balls still hurt , the fuck did she think I wasn't even touching kiara. "
    show bg johnafterintro 4 with Dissolve(0.8)
    John "*Bell rings*  Who the fuck is it at this time. "
    "Doorbell" "*Continous ringing* "
    show bg johnafterintro 5 with Dissolve(0.8)
    John "Coming coming dammit , if it's the mailman, I'll fucking rip his spine out. "
    show bg johnafterintro 6 with Dissolve(0.8)
    JakeInvestigator "Hey there, john! Miss me? "
    show bg johnafterintro 7 with Dissolve(0.8)
    John "Oh, for fucks sake , buzz off. "
    show bg johnafterintro 8 with Dissolve(0.8)
    JakeInvestigator "Oh, c'mon, that a way to talk to your friend? "
    John "Alright, let us get two things straight. You're not my friend. "
    show bg johnafterintro 9 with Dissolve(0.8)
    John "Two , you're someone I pay 6 figures for somewhat decent work every year , so if it's not the latter. "
    show bg johnafterintro 10 with Dissolve(0.8)
    John "I'd like you to jump the fuck out of the window there. "
    show bg johnafterintro 11 with Dissolve(0.8)
    JakeInvestigator "Well, I have something for which you might even increase my pay. "
    John "Yeah, right, don't make me laugh , can you get to the point? "
    show bg johnafterintro 12 with Dissolve(0.8)
    JakeInvestigator "Well, I heard you tried to hanky panky your daughter yesterday."
    show bg johnafterintro 13 with Dissolve(0.8)
    John "How the fuck do you kn- "
    JakeInvestigator "Woah , hear me out ... I have something that can save you from the lawsuit."
    show bg johnafterintro 14 with Dissolve(0.8)
    JakeInvestigator "Take a look , you'll be pleased, or at least your lawyer will be. "
    John "What are these? "
    show bg johnafterintro 15 with Dissolve(0.8)
    JakeInvestigator "Well, evidence legally, but in simple terms, your wife fucked someone else, john. "
    John "This is perfect... "
    JakeInvestigator "Not the ideal reaction of a man seeing his wife naked with another guy, but alright. "
    show bg johnafterintro 16 with Dissolve(0.8)
    John "Well done Jake. I'm going to have to make some calls. Your money will be wired soon. "
    JakeInvestigator "Right... Fine by me. "
    ""
    stop music
    jump lanaafterintro

label natsufindingkiara:
    play music "/audio/antntsutlksns.ogg"
    show bg natsuafterintro 1 with Dissolve(0.8)
    Xia "I hope Mr. Daichi talked to her , I used to go to him when I felt lost. Perhaps his wisdom may calm her emotions. "
    show bg natsuafterintro 2 with Dissolve(0.8)
    Natsuko "*Humming music* Hm mhm... "
    show bg natsuafterintro 3 with Dissolve(0.8)
    Xia "Natsuko , please come here."
    show bg natsuafterintro 4 with Dissolve(0.8)
    Natsuko "Yes, mother? Is everything okay? "
    show bg natsuafterintro 5 with Dissolve(0.8)
    Xia "Natsuko, kiara isn't picking up my calls. Could you please perhaps check on her? She must be either at your friend's shop or Mr. Daichi's. "
    Natsuko "Sure , mother, I'm sure it's nothing to worry about. She probably wants to see the town. "
    show bg natsuafterintro 6 with Dissolve(0.8)
    Kiara "I understand, however, but she's not picking up my calls either , so please look around, okay? "
    Natsuko "Certainly, mother , I'll go right away. "
    show bg natsuafterintro 7 with Dissolve(0.8)
    Xia "Oh, and remember Natsuko, no mentions of the past. Your room decor choice earlier was risky as well. Please don't do that again, if you don't mind. "
    show bg natsuafterintro 8 with Dissolve(0.8)
    Natsuko "I'm sorry, mother. I just really wanted her to smile. It won't happen again, so may I go? "
    Xia "I love yours too, natsuko, and yes, take care."
    ""
    stop music
    return

label kiarateashop:

    play music "audio/teashop.ogg"

    show bg kiarateashop 1 with Dissolve(0.8)



    Kiara "So this is it, huh? Alright, but it seems to be empty right now. "
    show bg kiarateashop 2 with Dissolve(0.8)
    Kiara "Oh, someone is there."
    show bg kiarateashop 3 with Dissolve(0.8)
    Kiara "Hello sir, who are you making this for? No one's outside. "
    Daichi "Welcome, and to answer your question. "
    show bg kiarateashop 4 with Dissolve(0.8)
    Daichi "You're here now, aren't you? We can call it a sixth sense. "
    Kiara "Heh, sure, why not. "
    show bg kiarateashop 5 with Dissolve(0.8)
    Kiara "Anyway... Um, I'm Kiara. Aunty xia told me about-- "
    show bg kiarateashop 6 with Dissolve(0.8)
    Daichi "Yes yes , Kiara san! Please, please come and let us talk. "
    Kiara "Oki, right behind you. "
    show bg kiarateashop 7 with Dissolve(0.8)
    Daichi "I'm happy to have you here. I hope you like Osaka. "
    Kiara "So far, great, yes."
    show bg kiarateashop 8 with Dissolve(0.8)
    Daichi "Please wait here. I'll get back to you after some food is ready. "
    Kiara "Sure, take your time. "
    show bg kiarateashop 9 with Dissolve(0.8)
    Kiara "This place is beautiful. It feels so... authentic. "
    show bg kiarateashop 10 with Dissolve(0.8)
    Daichi "She does not remember me at all. I have to be careful. "
    show bg kiarateashop 11 with Dissolve(0.8)
    Kiara "Is Mr. Daichi there? I can't see him. "
    show bg kiarateashop 12 with Dissolve(0.8)
    Daichi "Apologies for the delay. I was getting something good to eat. I hope you like shrimp. "
    show bg kiarateashop 13 with Dissolve(0.8)
    Kiara "Love them! Please, let's have at it! "
    show bg kiarateashop 14 with Dissolve(0.8)
    Daichi "So Kiara-san, what brings you to japan? "
    Kiara "Honestly, some family problems, but ... I suppose I want a new start, and I don't know where to start. "
    show bg kiarateashop 15 with Dissolve(0.8)
    Kiara "I am tired of being judged by everyone, Mr. Daichi. I can't relate to anyone... or,  I don't understand because I never lived an everyday life. "
    show bg kiarateashop 16 with Dissolve(0.8)
    Kiara "I don't mean to boast here ,  but being a billionare's daugther it feels as if I never really lived in reality and now I feel like I'm not ready. "
    Daichi "Kiara-san , you need to remember no matter what your past maybe ,  it does not define the future you. In fact it hasn't don't you see? "
    show bg kiarateashop 17 with Dissolve(0.8)
    Kiara "Um... I don't understand, what do you mean? "
    Daichi "While what you say is true , you need to realize despite all that fortune you turned out an humble and kind person that accepts they have flaws , many kings even in past couldn't do this. "
    Kiara "But Mr. Daichi, I don't know what will I do... How do I stop worrying myself so much when no one wants to see the real me , all they see is the my father's name or my past. "
    show bg kiarateashop 18 with Dissolve(0.8)
    Daichi "Kiara-san , you have to accept that we can't please everyone, so the first thing would be to stop doing that, second would be starting over."
    Kiara "So what do I do? where do I initiate this? "
    show bg kiarateashop 19 with Dissolve(0.8)
    Daichi "Before any of it , you've got to stop hating yourself first, kiara-san. To do that, you have to become independent and strong from within. "
    show bg kiarateashop 20 with Dissolve(0.8)
    Kiara "But... I'm not confident I can. All I have is regrets about not being able to do things or take control of actions when I should've. "
    Daichi "Kiara san , regrets stay forever in our heads. They never go away , all you can do to suppress them. "
    show bg kiarateashop 21 with Dissolve(0.8)
    Daichi "You have to first try to accept that the people who, despite your efforts, don't recognize the real you , are not worth sacrificing your sanity. "
    Kiara "So, move on? Forget everything?... Is it that easy? "
    show bg kiarateashop 22 with Dissolve(0.8)
    Daichi "It's never easy, kiara-san , even though I have regrets, can I reverse them ? No... but I can make up for that lost time by improving myself and being happy. "
    show bg kiarateashop 23 with Dissolve(0.8)
    Kiara "Yes... exactly... how do I be happy? I wish the things never occurred, I wish none of it had happened."
    Daichi "So do all who live to see through such times , but that's not for us to decide. All we have to decide is what to do with the time given to us."
    show bg kiarateashop 24 with Dissolve(0.8)
    Daichi "I believe your time is worth getting a better life than wasting away over people who fade away , so go out there, explore , try new things , and become who you've wanted to be."
    show bg kiarateashop 25 with Dissolve(0.8)
    Daichi "Once you've done it and you're on the path where you feel you've accomplished something truly , that is when you're happy & that day, I promise you'll thank yourself."
    Kiara "I see.... starting a new beginning then. "
    show bg kiarateashop 26 with Dissolve(0.8)
    Daichi "Kiara- san, I apologize if I was harsh in words, but what I mean to say is you can do everything you think you can't. All it requires is a start. Failure or success are worries of the future."
    Kiara "Thank you, Daichi san , no, you weren't rude. I'll try to implement what you said... it might take time, but I know what to do now. "
    show bg kiarateashop 27 with Dissolve(0.8)
    Kiara "I hope we talk again , nice to meet you, Daichi-san , Let's share tea next time. "
    Daichi "Tea or not, you are always welcome here. Nice to meet you too. "
    show bg kiarateashop 28 with Dissolve(0.8)
    Kiara "I need to take all of that in... let me find somewhere peaceful. "
    stop music
    jump natsufindingkiara2

label miafterintro:
    play music "/audio/miamsnntlk.ogg"
    show bg lawafterintro 1 with Dissolve(0.8)
    Veronica "Mason, you here? "
    show bg lawafterintro 2 with Dissolve(0.8)
    "Maso&Mia" "You're even more beautiful when you smile. "
    Veronica "*quietly* What do we have here? "
    show bg lawafterintro 3 with Dissolve(0.8)
    Mia "You're pretty handsome when you kiss too. "
    show bg lawafterintro 4 with Dissolve(0.8)
    Mason "Well, would you help me be more handsome then? "
    show bg lawafterintro 5 with Dissolve(0.8)
    "Mason&Mia" "*leaning for a kiss* "
    show bg lawafterintro 6 with Dissolve(0.8)
    Veronica "Ehm ehm, Enjoying ourselves, are we? "
    "Mason&Mia" "Ah shit , V , * Gasp* Veronica I- "
    show bg lawafterintro 7 with Dissolve(0.8)
    Veronica "So what's happening? "
    Mia "Veronica, I can explain... "
    show bg lawafterintro 8 with Dissolve(0.8)
    Veronica "Heh, Explain what exactly, Mia. With you wearing his shirt and him in his boxers only a little left to interpret here. "
    Mason "V, She means to say. "
    show bg lawafterintro 9 with Dissolve(0.8)
    Veronica "Relax, guys, it's not like I walked in on you fucking. Calm down. "
    show bg lawafterintro 9pt2 with Dissolve(0.8)
    Veronica "Was just here to wake my cousin up but friendly to see you here, I guess. "
    show bg lawafterintro 10 with Dissolve(0.8)
    Veronica "One more thing, by the way, you two... "
    show bg lawafterintro 11 with Dissolve(0.8)
    "Mason&mia" "Hm?... What? "
    Veronica "You both look adorable together. "
    show bg lawafterintro 12 with Dissolve(0.8)
    Mason "She's the cute one."
    Mia "No you... "
    stop music

    jump Johnandjake

label lanaafterintro:
    play music "/audio/lnamrng.ogg"
    show bg lanaafterintro 1 with Dissolve(0.8)
    Lana "I wonder how she's doing. I can't wait to go there soon. "
    show bg lanaafterintro 2 with Dissolve(0.8)
    Lana "Shame mom isn't going with me. She would've liked Osaka. "
    show bg lanaafterintro 3 with Dissolve(0.8)
    Lana "Then again, I understand why. She's busy with her business as well. "
    show bg lanaafterintro 4 with Dissolve(0.8)
    Lana "*Bell rings*  I wonder who that is, most likely the shipment guy... mom isn't home though. "
    show bg lanaafterintro 5 with Dissolve(0.8)
    Lana "Should I just tell them to go or?... "
    show bg lanaafterintro 6 with Dissolve(0.8)
    Lana "Wait... how about I tease him a bit? The man's working hard and deserves a bit of eye candy. "

    #TODO add a choice like this here
    menu:
        "Tease him":
            jump .part_1
        "Don't do it":
            Lana "Yeah not worth it."
            jump introsachikorin

    label .part_1:
        show bg lanaafterintro 7 with Dissolve(0.8)
        Lana "*Yawn* Hmm, I wonder how Japanese food is. I've only had sushi. "
        show bg lanaafterintro 8 with Dissolve(0.8)
        ""
        show bg lanaafterintro 9 with Dissolve(0.8)
        Lana "I should probably get a custom dress as well. I can't go in my usual outfits. "
        show bg lanaafterintro 10 with Dissolve(0.8)
        Lana "Speaking of which, I wonder how lovely kiara looked in the one I got her. "
        show bg lanaafterintro 11 with Dissolve(0.8)
        "Deliveryguy" "Uhh, this is the shipment for movesesian industries, ms Elizabeth? "
        show bg lanaafterintro 12 with Dissolve(0.8)
        Lana "Heh, let's see how he reacts. "
        "Deliveryguy" "I would require an uh sign or a thumbprint of any receiver. "
        show bg lanaafterintro 13 with Dissolve(0.8)
        Lana "Yes , I am lana movesesian. "
        "Deliveryguy" "Ah, perfect, mam, this would be.... w- "
        show bg lanaafterintro 14 with Dissolve(0.8)
        "Deliveryguy" "What he-... uh hi mam I am from sorry if I disturbed you at the wrong time. "
        Lana "I love that surprise. Lets's tease him more."
        show bg lanaafterintro 15 with Dissolve(0.8)
        Lana "Well, go on. Where do I need to sign? "
        show bg lanaafterintro 16 with Dissolve(0.8)
        "Deliveryguy" "Er... yes, mam, this document, one sign...( wow, she's hot damn) "
        show bg lanaafterintro 17 with Dissolve(0.8)
        Lana "Well, I don't have a pen, so let me get that. "
        "Deliveryguy" "Ar... yes, mam sure take your time ( damn, I can't take my eyes off of her tits fuck) "
        show bg lanaafterintro 18 with Dissolve(0.8)
        Lana "Very well then, give me a moment, cutie. "
        show bg lanaafterintro 19 with Dissolve(0.8)
        "Deliveryguy" "Cutie? That made my confidence climb hella high. "
        show bg lanaafterintro 20 with Dissolve(0.8)
        "Deliveryguy" "Damn, look at that ass, though. I bet she's like a perfect package. "
        show bg lanaafterintro 21 with Dissolve(0.8)
        Lana "Hey, so I can't find a pen. Do you have one? "
        "Deliveryguy" "Uh yes, mam, I do, here you g-- *pen drops* "
        show bg lanaafterintro 22 with Dissolve(0.8)
        "Deliveryguy" "Shit, I'm sorry, mam, I'll- "
        Lana "That's okay, I'll pick it up. "
        show bg lanaafterintro 23 with Dissolve(0.8)
        Lana "Ah - this pen rolls around a lot. "
        "Deliveryguy" "Shall I? "
        Lana "No-no, I got it. It's here at the door. "
        show bg lanaafterintro 24 with Dissolve(0.8)
        "Deliveryguy" "Man, this girl... is she testing me or what. "
        show bg lanaafterintro 25 with Dissolve(0.8)
        "Deliveryguy" "Should I maybe touch it?... this has to be intentional. "
        show bg lanaafterintro 26 with Dissolve(0.8)
        stop music
        jump introsachikorin

    label .part_2:
        show bg lanaafterintro 27 with Dissolve(0.8)
        Lana "Hope he's enjoying the view. Only some get to. "
        show bg lanaafterintro 28 with Dissolve(0.8)
        "Deliveryguy" "Alright, just one grab... "
        show bg lanaafterintro 29 with Dissolve(0.8)
        "Deliveryguy" "Oh man, so soft... okay, I better fucking run. "
        Lana "Aha, his hands are kinda nice. "
        show bg lanaafterintro 30 with Dissolve(0.8)
        Lana "Hey, where are you going? "
        "Deliveryguy" "Mam, I'll erm send the receipt! You're her heir, so that you won't need a sign. "
        Lana "Sign not needed, huh,  cute excuse. "
        show bg lanaafterintro 31 with Dissolve(0.8)
        Lana "That was kinda fun. "
        show bg lanaafterintro 32 with Dissolve(0.8)
        Lana "Kiara, I hope you allow yourself to open up and live a little, too. See you soon, babe. "
        ""
        stop music
    jump introsachikorin

label kiarainstreets2:
    show bg kiaraandtaka 32 with Dissolve(0.8)
    Taka "Heh... way out of my league but at least she's nice. "
    show bg kiarainthestreets 14 with Dissolve(0.8)
    Kiara "So this is the locality side, hmm, reminds me of harlem in New York. "
    show bg kiarainthestreets 15 with Dissolve(0.8)
    Kiara "Say what one might, the weather here remains nice regardless. "
    show bg kiarainthestreets 16 with Dissolve(0.8)
    Kiara "I guess this is the tea shop path, let's see what its about.  "
    ""
    stop music
    jump kiarateashop


label kiaraandtaka:
    play music "/audio/tkashop.ogg"
    show bg kiaraandtaka 1 with Dissolve(0.8)
    Kiara "Impressive shop, I must say."
    Taka "Yes, I'm the biggest retailer in the locality here. "
    show bg kiaraandtaka 2 with Dissolve(0.8)
    Kiara "At such young age? How did you set this all up."
    Taka "Well, half of it is luck, and half is hard work. Let's say things work out, haha."
    show bg kiaraandtaka 3 with Dissolve(0.8)
    Taka "Please come sit. We can continue then. "
    Kiara "The fabrics look nice. "
    show bg kiaraandtaka 4 with Dissolve(0.8)
    Taka "So how can I be of help to you ms?... "
    Kiara "Name's Kiara. "
    show bg kiaraandtaka 5 with Dissolve(0.8)
    Taka "Pretty name, so what do you need help with? "
    Kiara "Well, I want to know where I can explore a bit. I'm new here, so where should I go? "
    show bg kiaraandtaka 6 with Dissolve(0.8)
    Taka "Well, to the left side, you'll have the city route, which goes to the city and posh areas. However, the right leads to the locality, so go right first. "
    Kiara "Alright... uh, aunt xia told me there's a tea shop here in the locality too? "
    show bg kiaraandtaka 7 with Dissolve(0.8)
    Taka "Precisely, do try their dumplings. They're great. "
    Kiara "I will, do you have a rough idea of where I can get started looking for work?  "
    show bg kiaraandtaka 8 with Dissolve(0.8)
    Taka "I do. I'll let you know through the agency friend... "
    Kiara "Great, anyway, how's your business doing? "
    show bg kiaraandtaka 9 with Dissolve(0.8)
    Taka "Ah, it's going okay. I'm looking for a western model for some cosplays, though... wait. "
    show bg kiaraandtaka 10 with Dissolve(0.8)
    Taka "Hey kiara , how about you become one? "
    show bg kiaraandtaka 11 with Dissolve(0.8)
    Kiara "Are you for real? I don't know anything about that besides, I don't want to make a fool of myself. "
    show bg kiaraandtaka 12 with Dissolve(0.8)
    Taka "Calm down, calm down, hear me out first. "
    show bg kiaraandtaka 13 with Dissolve(0.8)
    Taka "You needed work as well, right? I'll pay you 350 $ for it. It's an easy shoot. However, another one is for 500 but a bit modern. What do you prefer? "
    show bg kiaraandtaka 14 with Dissolve(0.8)
    stop music
    play music "/audio/choicmusic.ogg"
    Kiara "Hmm.... 350 for a simple shoot, if it's nothing stupid, doesn't sound too bad. "
    menu:
        "Okay I'll do the 350$ one.":
            jump .part_2
        "I'll do the 500$ one":
            #TODO add kiara corruption by 5
            $ mc_stats.adjust_corruption(5)
            jump .part_3

    label .part_1:
        show bg kiaraandtaka 28 with Dissolve(0.8)
        stop music
        play music "/audio/kiastrts1.ogg"
        Taka "That was great, I'm sorry again for the tight outfit. "
        Kiara "No, it wasn't that bad. "
        show bg kiaraandtaka 29 with Dissolve(0.8)
        Kiara "Thank you actually it was kinda cool, I'd love to do more! "
        show bg kiaraandtaka 30 with Dissolve(0.8)
        Taka "Well I'm glad you did, I'll let you know what the investors think of the shoot, please do come again though. "
        show bg kiaraandtaka 31 with Dissolve(0.8)
        Kiara "Sure!, Well I'll be going now see you later Mr. taka! "
        Taka "Likewise Boss kiara. "
        stop music
    jump kiarainstreets2

    label .part_2:

    
        play music "/audio/tkashop.ogg"
        show bg kiaraandtaka 15 with Dissolve(0.8)
        Kiara "Alright , When do we start? "
        Taka "Now , come follow me into the studio. "
        #show Nbijloading - Some time later...
        show bg kiaraandtaka 16 with Dissolve(0.8)
        Taka "Kiaraaa , ready when you are. "
        show bg kiaraandtaka 17 with Dissolve(0.8)
        Kiara "Yes I'm coming! I can't find the shoes! "
        Taka "They're to the left side! "
        show bg kiaraandtaka 18 with Dissolve(0.8)
        Kiara "The clothes are a bit tight "
        show bg kiaraandtaka 19 with Dissolve(0.8)
        Kiara "What is this prosthetic thing , whatever lets just wear it. "
        show bg kiaraandtaka 20 with Dissolve(0.8)
        Kiara "Where's the helm? "
        Taka "Next to the stool, looking great by the way! "
        show bg kiaraandtaka 21 with Dissolve(0.8)
        Taka "Alright looking good , gimme the poses! "
        show bg kiaraandtaka 22 with Dissolve(0.8)
        Taka "Damnn nice nailing it , now the bow! "
        show bg kiaraandtaka 23 with Dissolve(0.8)
        Taka "Beautiful , now the diva side. "
        show bg kiaraandtaka 24 with Dissolve(0.8)
        Taka "Nice , The shinobi now. "
        show bg kiaraandtaka 25 with Dissolve(0.8)
        Taka "You're nailing these , now the boss approach! "
        show bg kiaraandtaka 26 with Dissolve(0.8)
        Taka "Sweet! "
        show bg kiaraandtaka 27 with Dissolve(0.8)
        Taka "Well done , impressive indeed. "
        stop music
    jump .part_1

    label .part_3:
        

        show bg kiaraandtaka 16 with Dissolve(0.8)
        stop music
        play music "/audio/lthrcsply.ogg"
        "" "{i}A bit later{/i}"
        Taka "Kiara, ready when you are! "
        show bg photoshootleather 1 with Dissolve(0.8)
        Kiara "What is this outfit? It's so skin tight. "
        Taka "Kiara, how much longer? "
        show bg photoshootleather 2 with Dissolve(0.8)
        Kiara "Uh yeah, coming. Just give me a moment. "
        show bg photoshootleather 3 with Dissolve(0.8)
        Kiara "I feel like I'm being squeezed by it."
        show bg photoshootleather 4 with Dissolve(0.8)
        Kiara "Um... taka, I think this outfit is a bit tight. "
        Taka "It can't be that bad. I'm sure it's elastic. Let me have a lo- "
        show bg photoshootleather 5 with Dissolve(0.8)
        Taka "look.... ( Holy fuck that body) "
        show bg photoshootleather 6 with Dissolve(0.8)
        ""
        show bg photoshootleather 7 with Dissolve(0.8)
        Kiara "Are you sure? material is fine, but it's a bit small."
        Taka "Don't worry about it, besides it's a small shoot anyway so it won't be an issue. Alright, let's start, (what a beauty) "
        show bg photoshootleather 8 with Dissolve(0.8)
        Taka "Lovely pose! You're a natural, alright. Let's do a leg up back view with hair falling behind. "
        show bg photoshootleather 9 with Dissolve(0.8)
        Taka "Perfect!, next up let's get the chair (man, look at that ass) "
        show bg photoshootleather 10 with Dissolve(0.8)
        Taka "Nice, now a side pose on the chair."
        show bg photoshootleather 11 with Dissolve(0.8)
        Taka "Nice!  Give me a moment to adjust the reel. "
        show bg photoshootleather 12 with Dissolve(0.8)
        Kiara "Why's this chair so stiff."
        Taka "Alright, Kiara, spread your legs for me! "
        show bg photoshootleather 13 with Dissolve(0.8)
        Kiara "W-what did you say?! "
        Taka "Your legs! The gang style poses Kiara, spread the legs. "
        show bg photoshootleather 14 with Dissolve(0.8)
        Kiara "(This feels a bit wrong)... "
        Taka "Kiara spread em more, like you know the biker gang people."
        show bg photoshootleather 15 with Dissolve(0.8)
        Taka "(Damn, I would bury my face between those legs) Kiara, one important thing! "
        show bg photoshootleather 16 with Dissolve(0.8)
        Kiara "Yes? "
        Taka "You gotta smile! Please give me a smirking smile with the badass pose. "
        show bg photoshootleather 17 with Dissolve(0.8)
        Taka "Sweet! Perfect shot, Alright, Kiara, now pull down the zipper. "
        show bg photoshootleather 18 with Dissolve(0.8)
        Kiara "Um... what...?"
        show bg photoshootleather 19 with Dissolve(0.8)
        Taka "The zipper Kiara, down to below chest level, we gotta show the quality and fit."
        Kiara "Um, I don't know if I can do that... "
        show bg photoshootleather 20 with Dissolve(0.8)
        Taka "Hm ? what do you mean, you were in a kimono, fitting don't you have the bodysuit beneath it? "
        Kiara "There's a bodysuit to wear beneath it?... I didn't know. "
        show bg photoshootleather 21 with Dissolve(0.8)
        Taka "Well, alright, so what are you wearing? Sports gear works too. "
        Kiara "Actually, I- I'm not wearing any undergarments... could you please get me some? "
        show bg photoshootleather 22 with Dissolve(0.8)
        Taka "Oh uh- (No underwear huh... I gotta see this) "
        show bg photoshootleather 23 with Dissolve(0.8)
        Taka "I don't have any unfortunately, but you don't have to worry, kiara. I'm gay anyway, so don't think of it that way. It's just a few shots, so don't overthink. "
        show bg photoshootleather dcd with Dissolve(0.8)
        Kiara "I didn't expect this... What do I do? "


        menu:
            "I can't do this , just because he's gay doesn't mean I can be in front of him like that.":
                call photoshootleatherchoice1 from _call_photoshootleatherchoice1
            "Okay... I trust you.":
                $ mc_stats.adjust_corruption(5)
                call photoshootleatherchoice2 from _call_photoshootleatherchoice2

        jump .part_1


    label photoshootleatherchoice1:
        show bg photoshootleather rjctd1 with Dissolve(0.8)
        Kiara "Taka, I'm sorry you don't have to pay I can't do this... "
        Taka "No, it's alright I'll pay still, you okay? "
        show bg photoshootleather rjctd2 with Dissolve(0.8)
        Taka "I hope you're not mad at me sorry if that made you uncomfortable (shit... I'll have to take my time with this girl) "
        Kiara "No, it's okay... I'll meet you outside after changing, sorry if I ruined the shoot. "
        stop music

        return

    label photoshootleatherchoice2:
        Taka " (Fuck she's actually doing it) "
        show bg photoshootaccpt 2 with Dissolve(0.8)
        Taka " Kiara , you good? "
        Kiara " Yes, just a moment... ( Ughhh c'mon I can do this) "
        show bg photoshootaccpt 3 with Dissolve(0.8)
        Taka " Bravo! (Mamma Mia, look at that cleavage.) "
        show bg photoshootaccpt 4 with Dissolve(0.8)
        Taka " (They're so smooth, wish I could smell her up close.) "
        Taka " Alright, kiara, let's do a neck hold straight stand pose! "
        show bg photoshootaccpt 5 with Dissolve(0.8)
        Taka " Nice, but come on, where's the smile!, do one arm side and one arm back head with it. "
        show bg photoshootaccpt 6 with Dissolve(0.8)
        Taka " There it is!  (I thought natsuko was the hottest girl I had met, boy, was I wrong? Not only is this sweet and cute but hot as fuck too) "
        Taka " Alright, one looking left and shoulder hold."
        show bg photoshootaccpt 7 with Dissolve(0.8)
        Taka " Nice, okay, last one arm down and standing in an arch."
        show bg photoshootaccpt 8 with Dissolve(0.8)
        Taka " Alright, that's a wrap. I'll be outside the shop getting changed and stuff ( Look at those babies, I bet they're softer than cotton)"
        stop music
        return





label kiarainstreets:
    play music "/audio/kiastrts1.ogg"
    show bg kiarainthestreets 1 with Dissolve(0.8)
    Kiara "Alright, Let's go be brave, Kiara. You got this. "
    show bg kiarainthestreets 2 with Dissolve(0.8)
    Kiara "The streets are so clean compared to back home. That's nice. "
    show bg kiarainthestreets 3 with Dissolve(0.8)
    Kiara "Is that a miyaki shop? I'll try it out someday. "
    show bg kiarainthestreets 4 with Dissolve(0.8)
    Kiara "Is this a cafe? Why is it closed in the morning? "
    show bg kiarainthestreets 5 with Dissolve(0.8)
    Kiara "Ah, here it is. Natsu told me about a shop with a blue logo on the upper. "
    show bg kiarainthestreets 6 with Dissolve(0.8)
    Kiara "Why is the building so tall? I thought it was just a clothing store. "
    show bg kiarainthestreets 7 with Dissolve(0.8)
    Taka "Hey, you over there, sup? "
    Kiara "Oh, uh, hi. "
    show bg kiarainthestreets 8 with Dissolve(0.8)
    Taka "I'm glad you like the logo. I spent more on this than on my gaming setup. "
    show bg kiarainthestreets 9 with Dissolve(0.8)
    Kiara "Aheh, sorry, Natsuko told me this shop belonged to her friend, so she told me to check it out. "
    Taka "Natsuko called me a friend? Well, that's nice to hear. "
    show bg kiarainthestreets 10 with Dissolve(0.8)
    Kiara "Actually, she told me you could help me a bit with the locality. "
    Taka "Uh, I can, but what do you mean by help in it? "
    show bg kiarainthestreets 11 with Dissolve(0.8)
    Kiara "Um, just... like where to start and meeting people and stuff. "
    Taka "Oh right, okay. "
    show bg kiarainthestreets 12 with Dissolve(0.8)
    Taka "Certainly I can help you with it. I have friends at agencies & language courses. "
    show bg kiarainthestreets 13 with Dissolve(0.8)
    Taka "Please, Come in, though let's discuss this further in the office. It would be best if you didn't stand in the street. "
    Kiara "Sure. (What's that outfit he's wearing) "
    ""
    stop music
    jump kiaraandtaka



label auntevening:
    play music "/audio/mcanttlk.ogg"
    show bg auntevening 1 with Dissolve(0.8)
    Kiara "I think this is the room, Auntie? Are you here? "
    show bg auntevening 2 with Dissolve(0.8)
    Xia "Kiara... come sit, tell me what happened yesterday. "
    Kiara "Um... alright. "
    show bg auntevening 2pt2 with Dissolve(0.8)
    Kiara "I... I need to figure out where to start, auntie. I, I don't understand why dad would. "
    show bg auntevening 3 with Dissolve(0.8)
    Xia "Go slow. It's okay... tell me. "
    Kiara "It's just dad did try to grope me. I don't know how far it went, but mom intervened."
    show bg auntevening 4 with Dissolve(0.8)
    Kiara "All this combined with the accident, my anxiety, it just feels like I'm being suffocated without anywhere to breathe, it's as if I try, but the world pushes me back and puts me down. "
    show bg auntevening 5 with Dissolve(0.8)
    Xia "John, what have you done to this poor girl, first Mia and now her, was a pleasure worth this? "
    show bg auntevening 6 with Dissolve(0.8)
    Kiara "The one person I'm supposed to look up to has enough problems on her side, too, I don't want to trouble mom, but I don't want to take all this on my own either... Ugh, why me? "
    show bg auntevening 7 with Dissolve(0.8)
    Xia "Kiara , come here dear. "
    Kiara "Auntie, I- "
    show bg auntevening 8 with Dissolve(0.8)
    Kiara "I want to be happy, that's all. "
    Xia "You will be, and you're not alone either. You have your real family always. "
    show bg auntevening 9 with Dissolve(0.8)
    Kiara "Thanks, auntie, this feels real, and I'm glad for it."
    Xia "You're a wonderful person Kiara, don't let anyone make you feel otherwise. "
    show bg auntevening 10 with Dissolve(0.8)
    Xia "Besides, why ruin such a pretty smile over those that aren't even worth half of it? "
    Kiara "You're lovely, auntie... So um, Natsuko told me. "
    show bg auntevening 11 with Dissolve(0.8)
    Xia "Yes, please wait here, okay? I'll bring you something nice to wear. "
    Kiara "Okay, auntie, I'll be here. "
    show bg auntevening 12 with Dissolve(0.8)
    Kiara "I hope you're doing well too, mom. It feels good to have a family, finally. "
    stop music
    #loading screen
    show bg auntevening 13 with Dissolve(0.8)
    play music "/audio/kimonosn.ogg"
    Xia "Kiaraa , come out let me see. "
    Kiara "It doesn't look good I look silly. "
    Xia "Oh shush , come on out. "
    show bg auntevening 14 with Dissolve(0.8)
    Kiara "Auntiee I don't know if this looks good. "
    Xia "Don't think so much come on show me. "
    show bg auntevening 15 with Dissolve(0.8)
    Kiara "Does it look bad? Please don't laugh auntie. "
    Xia "Bad? Kiara you look like a flower! pun intended. "
    show bg auntevening 16 with Dissolve(0.8)
    Kiara "I knew it! you're just making fun of me. "
    Xia "Aha , No honey I'm serious you look immaculate I'd go as far as to say it looks better on you than it ever did on me. "
    show bg auntevening 17 with Dissolve(0.8)
    Xia "You look wondeful kiara , so you wanted to explore right? Go on out return before 7 okay? "
    show bg auntevening 18 with Dissolve(0.8)
    Kiara "Alright auntie , thank you so much again."
    ""
    stop music
    jump kiarainstreets

label johnandassistant:
    play music "/audio/Intomain2.ogg"
    show bg johnandassistant 1 with Dissolve(0.8)
    Patricia "Ugh, c'mon, why are you so heavy? "
    John "aguh... where am I... "
    show bg johnandassistant 2 with Dissolve(0.8)
    Patricia "Your 2nd home sir. Please don't talk much. You need rest. "
    John "uhh... who are you."
    show bg johnandassistant 3 with Dissolve(0.8)
    Patricia "Unfh, c'mon, get on it. "
    show bg johnandassistant 4 with Dissolve(0.8)
    Patricia "Ahhh, there we go. "
    show bg johnandassistant 5 with Dissolve(0.8)
    Patricia "Alright, let's get you comfortable, sir."
    John "P-Patricia, is that you? "
    show bg johnandassistant 6 with Dissolve(0.8)
    Patricia "Yes, sir, it's me. Please stay still. I'm getting you into comfortable clothing. "
    John "A-alright, what did the doctor say? "
    Patricia "Said to rest and avoided any sexual activity for a week. I'd advise you to follow, sir. "
    show bg johnandassistant 7 with Dissolve(0.8)
    John "Right... what did Kiara say? "
    Patricia "She didn't reply, sir. Her last message was to take care of dad. "
    show bg johnandassistant 8 with Dissolve(0.8)
    John "Alright... you're free for the week Patricia, I'll have to prepare some things. "
    Patricia "Fine, sir, I'll do just that. Please stay safe as well. "
    show bg johnandassistant 9 with Dissolve(0.8)
    Patricia "Is there anything else you need, sir? "
    John "Call Ms. Wong. I'll tell you the details later."
    Patricia "Alright, sir, goodnight. "
    show bg johnandassistant 10 with Dissolve(0.8)
    John "Patricia... One more thing. "
    show bg johnandassistant 11 with Dissolve(0.8)
    John "Thank you, I appreciate this. "
    show bg johnandassistant 12 with Dissolve(0.8)
    Patricia "Just doing my job, sir, have a good sleep. "
    show bg johnandassistant 13 with Dissolve(0.8)
    Patricia "I guess even billionaires feel lonely in the end. "
    show bg johnandassistant 14 with Dissolve(0.8)
    Patricia "While I may feel sorry for him, this is for the better, I hope you find a new life, Kiara and Mia. "
    ""
    stop music
    jump miafterintro

label miamasonnighttalk:
    play music "/audio/miamsnntlk.ogg"
    show bg miamasonnighttalk 1 with Dissolve(0.8)
    Mia "Kiara I hope you're alright , So much has been thrown to you , stay strong. "
    show bg miamasonnighttalk 2 with Dissolve(0.8)
    Mia "My life may be a waste and destroyed but I won't let it happen to you. "
    show bg miamasonnighttalk 3 with Dissolve(0.8)
    Mia "Ah dear , I really hope john isn't trying to be clever this time and leaves her alone "
    show bg miamasonnighttalk 4 with Dissolve(0.8)
    Mia "But what if he is? How will I even fight it? He can drag the case and keep punishing me."
    show bg miamasonnighttalk 5 with Dissolve(0.8)
    Mia "I don't want to think about a future where Kiara ends up with that man anymore. "
    show bg miamasonnighttalk 6 with Dissolve(0.8)
    Mason "I should probably get Mia something she likes... uh wait, what."
    show bg miamasonnighttalk 7 with Dissolve(0.8)
    Mason "Mia? Did you not sleep? "
    Mia "Oh. Mason, I, uh yeah, I couldn't. "
    show bg miamasonnighttalk 8 with Dissolve(0.8)
    Mia "You didn't sleep either? "
    Mason "Was reading a DUI case and then got coffee, so. "
    Mia "Oh... right yeah, okay. "
    show bg miamasonnighttalk 9 with Dissolve(0.8)
    Mason "Hey, what happened? are you okay? "
    Mia "I'm... I'm not Mason. I don't know what's going to happen. "
    show bg miamasonnighttalk 10 with Dissolve(0.8)
    Mason "Why? are you worried about the hearing? "
    Mia "It's not just that, Mason...I feel like I've failed as a daughter, sister, wife, and mother, maybe. "
    show bg miamasonnighttalk 11 with Dissolve(0.8)
    Mason "You haven't failed at anything, Mia. Look at the people around you who care. You've got a kind, wonderful daughter, friends who care, and a family that exists despite everything. "
    Mia "But, Mason, I- "
    show bg miamasonnighttalk 12 with Dissolve(0.8)
    Mason "No, buts Mia, you know it's right. Don't let one pathetic man's life make you feel you're the loser here. "
    Mia "I understand; however, what if he does something crazy again? He's a powerful man, Mason. "
    show bg miamasonnighttalk 13 with Dissolve(0.8)
    Mason "Then we'll take it on together. You're not alone in this... I'm here for you, okay? I always will be, I've waited 10 years for you, Mia, and all I need is you by my side to take on anything. "
    show bg miamasonnighttalk 14 with Dissolve(0.8)
    Mia "But why me? You could've gotten anyone... all I did was ignore you back then, so why do you care. "
    show bg miamasonnighttalk 15 with Dissolve(0.8)
    Mason "Because I don't want anyone, I want someone who knows the weakest version of me and has seen me grow here, understands what I say. "
    Mia "I'm sorry, Mason... I was terrible to you. "
    show bg miamasonnighttalk 16 with Dissolve(0.8)
    Mason "No, don't be. You and I both grew up, realized our flaws, and tried to mend them... I know what happened earlier in the bathroom may make you feel otherwise, and I'm sorry. I do care about you, Mia. "
    show bg miamasonnighttalk 17 with Dissolve(0.8)
    Mia "But going through this will be tough. I am wonder if I can do it. "
    Mason "As I said, you're not going to be alone. Yes, it's a challenging mountain to climb, but I'll be with you, and the least I can do is until you're at the top. I won't let you fall. "
    show bg miamasonnighttalk 18 with Dissolve(0.8)
    Mia "Thank you, Mason. I needed to hear that. "
    Mason "No, you need one more thing. Cmon get up. "
    show bg miamasonnighttalk 19 with Dissolve(0.8)
    Mason "There you go, feel better? "
    Mia "Yes, It does... Thank you. "
    Mason "Don't thank me for what you deserve, Mia. "
    show bg miamasonnighttalk 20 with Dissolve(0.8)
    Mia "I'm sorry, Kiara, I took this feeling from you... I hope Damian finds you again. "
    Mason "Don't worry about Kiara, okay? She's got your older sister. "
    show bg miamasonnighttalk 21 with Dissolve(0.8)
    Mason "She's the strongest woman I ever met. You know that, too, right? "
    Mia "Heh, you're right about that. "
    ""
    stop music
    jump johnandassistant

label meetingnatsuko:
    play music "/audio/mtngntsu.ogg"
    show bg daybathaftr 1 with Dissolve(0.8)
    Kiara "Mhm, alright, definitely needed that. "
    show bg daybathaftr 2 with Dissolve(0.8)
    Kiara "It's a shame my clothes aren't here yet. I wanted to explore the city a bit, and that dress could be better. "
    show bg daybathaftr 3 with Dissolve(0.8)
    Xia "Remember natsu, nothing of the past, you and she shared a good bond, I know, but that's not her anymore. "
    Natsuko "I was there when it happened, and I'll be with you even now. "
    show bg daybathaftr 4 with Dissolve(0.8)
    Natsuko "It'll be fun knowing you once again, lovely kia. "
    show bg daybathaftr 5 with Dissolve(0.8)
    Natsuko "I've always loved her hair. She loved mine. It was cute and jealous at the same time, heh. "
    show bg daybathaftr 6 with Dissolve(0.8)
    Kiara "Oh, I'm sorry I didn't notice you. "
    Natsuko "Don't mind me. I don't mind the view from the back, haha."
    show bg daybathaftr 7 with Dissolve(0.8)
    Kiara "Aheh, thanks, um, I'm so sorry but I- you. "
    Natsuko "It's ok, we haven't met. I'm Natsuko, but you can call me cousin. "
    Kiara "Oh hi! "
    show bg daybathaftr 8 with Dissolve(0.8)
    Natsuko "Well, mom wasn't lying about beauty in a garden. You got the genes, girl. "
    Kiara "Oh hush it, coming from someone I'm already jealous of over the height but thank you."
    show bg daybathaftr 9 with Dissolve(0.8)
    Natsuko "So, how was your trip? "
    Kiara "Oh, it was okay. I made one friend who I will visit tomorrow. "
    show bg daybathaftr 10 with Dissolve(0.8)
    Natsuko "Oh, that so? I saw the dress you arrived in, and if I'll say you'd get many friendly people with that on, haha."
    Kiara "Well, that's true, haha, but no, she was very kind and sweet and even gave me a blanket when I slept on a plane. "
    show bg daybathaftr 11 with Dissolve(0.8)
    Natsuko "That's good then, so what do you think about the room? I re-designed it when I heard you were coming. "
    Kiara "Oh wow, um, I love it! Green's my favorite color."
    show bg daybathaftr 12 with Dissolve(0.8)
    Kiara "How did you know? Even the lights are exactly the warm I like. "
    Natsuko "I'm an interior design student, so it wasn't too hard."
    Kiara "Oh nice, well, thank you. Seriously I love it."
    show bg daybathaftr 13 with Dissolve(0.8)
    Natsuko "Well I was mainly here to let you know mom called you to talk. She has some clothes for you, okay? "
    Kiara "Oh... yes, okay, sure! Nice meeting you, by the way. "
    Natsuko "Likewise ~ "
    ""
    stop music
    jump auntevening

label daybath:
    play music "/audio/dybthmc.ogg"
    show bg roomentr 1 with Dissolve(0.8)
    Kiara "Woah, the lights are so warm."
    Kiara "This is better than my room back home."
    show bg roomentr 2 with Dissolve(0.8)
    Kiara "Well, I prefer this one. I love it."
    Kiara "Alright, time to shower."
    show bg roomentr 3 with Dissolve(0.8)
    Kiara "Lana, I love you, sweetie, but your fashion sense is.... dangerous."
    show bg roomentr 4 with Dissolve(0.8)
    Kiara "Okay then, let's see how the shower is. "
    show bg daybath 1 with Dissolve(0.8)
    Kiara "*Gasp* uh... wow, okay. "
    show bg daybath 2 with Dissolve(0.8)
    Kiara "This is way better than the open side style. I feel like a queen! "
    show bg daybath 3 with Dissolve(0.8)
    Kiara "And there's my throne. "
    show bg daybath 4 with Dissolve(0.8)
    Kiara "Mmm, the water is so nice. "
    show bg daybath 5 with Dissolve(0.8)
    Kiara "So refreshing, nothing like a good bath after a long trip."
    ""
    stop music
    jump meetingnatsuko

label auntmeet:
    show bg auntmeet 1 with Dissolve(0.8)
    play music "/audio/athom.ogg"
    Kiara "Wow, aunt's house is so cool."
    Oldman "No wonder she's fine. This is an upper-class girl. "
    show bg auntmeet 2 with Dissolve(0.8)
    Kiara "Whew... Alright, Kiara, make a good first impression, okay. "
    show bg auntmeet 3 with Dissolve(0.8)
    Kiara "Um Kon'nichiwa? Dareka masu ka? ( God, I feel like a moron) "
    show bg auntmeet 4 with Dissolve(0.8)
    Kiara "Helloooo? "
    Xia "Is that her? Kiara, I never got to apologize for not being there for her. "
    show bg auntmeet 5 with Dissolve(0.8)
    Xia "I wonder if our past is still with her, I Doubt it. I wasn't there for her when she needed me, either. "
    show bg auntmeet 6 with Dissolve(0.8)
    Xia "Kiara, I promise I'll protect you from everything this time. "
    Kiara "Oh hey, someone's there."
    show bg auntmeet 7 with Dissolve(0.8)
    Kiara "Yooooo auntie! Cool outfit! "
    Xia "Who's there? "
    show bg auntmeet 8 with Dissolve(0.8)
    Kiara "Well shit, there goes the first impression. Uhh, okay, act normal. "
    show bg auntmeet 9 with Dissolve(0.8)
    Kiara "Er... Watashi wa , Kiara des , ohio gosaimas... Hi? "
    Xia "I can speak english just fine. Stand tall. "
    show bg auntmeet 10 with Dissolve(0.8)
    Oldman "Damn, it's a shame her dress didn't open fully. That ass is begging to get out. "
    Kiara "Um, I am Kiara, daughter of Mia Murayama, your sis-- "
    show bg auntmeet 11 with Dissolve(0.8)
    Kiara "Ah * Gasp* she just hugged me. "
    Xia "Kiara, Honey, welcome home. It is nice to have you here finally. I waited the entire morning."
    show bg auntmeet 12 with Dissolve(0.8)
    Kiara "This is what genuine appreciation feels like... It's nice. "
    Xia "How was your trip? I hope you got here easily. "
    show bg auntmeet 13 with Dissolve(0.8)
    Kiara "Yes, all good. Thankfully, I met someone who speaks english at the airport, so it was pretty easy. "
    Xia "That's great, don't worry about the luggage, okay? I'll tell the servant to take care of it. "
    show bg auntmeet 14 with Dissolve(0.8)
    Xia "Well, Mia wasn't wrong though when she said you're the most beautiful in our family. "
    Kiara "Ahan, Thank you, auntie. I doubt that's true since all of you have such good genes. "
    show bg auntmeet 15 with Dissolve(0.8)
    Xia "Haha, is this flattery perhaps an apology for your poor Japanese earlier? "
    Kiara "Of course not, auntie, you're amazingly beautiful."
    Xia "Well, thank you, honey."
    show bg auntmeet 16 with Dissolve(0.8)
    Xia "Still such a sweetheart. Memories might be gone, but you're still pure Kiara. "
    show bg auntmeet 17 with Dissolve(0.8)
    Kiara "Aunty, your house is so beautiful. I love the design. "
    show bg auntmeet 18 with Dissolve(0.8)
    Xia "You think so? Why don't you  come in and take a look? "
    Kiara "Really? Yayyyy !"
    show bg auntmeet 19 with Dissolve(0.8)
    Kiara "Oh my gosh, it's real armor? Auntie come here! "
    show bg auntmeet 20 with Dissolve(0.8)
    Xia "Coming honey, you go ahead. I'll be with you soon. "
    Kiara "Okay! Wow, that's a real sword. "
    show bg auntmeet 21 with Dissolve(0.8)
    Xia "Now then... let's attend to this. "
    show bg auntmeet 22 with Dissolve(0.8)
    stop music
    Oldman "Ain't no way I'm letting this go , Ima go help her unpack hehe. "
    show bg auntmeet 22pt2 with Dissolve(0.8)
    play music "/audio/antattck.ogg"
    Xia "Where do you think you're going mister? "
    Oldman "Uhh, to  help your daughter with luggage and stuff."
    Xia "No, thank you, We'll take care of it... besides, I caught you staring at her inappropriately."
    show bg auntmeet 23 with Dissolve(0.8)
    Xia "Is this how you treat your customers? Gawking at them like a pervert? "
    Oldman "Woah woah, lady, calm down."
    show bg auntmeet 24 with Dissolve(0.8)
    Oldman "What's with the accusations? I was ensuring she reached the right location... although the one I was staring at was you. "
    Xia "Oh, is that so? "
    show bg auntmeet 25 with Dissolve(0.8)
    Oldman "Yes dear, I mean it seems you got quite fun bags as well... let me grab a feel. "
    show bg auntmeet 26 with Dissolve(0.8)
    Oldman "Ough *growls* What the- "
    Xia "How dare you. "
    show bg auntmeet 27 with Dissolve(0.8)
    Xia "Hai! "
    Oldman "Aaaaaaaaaaagh *thud* "
    show bg auntmeet 28 with Dissolve(0.8)
    Oldman "Urgh, what the hell? How do you have so much- "
    Xia "If I see you here again, I'll make sure you go through that wall next time, and then I'll use your bones to rebuild it. "
    show bg auntmeet 28pt2 with Dissolve(0.8)
    Oldman "The fuck, you're crazy. I'm leaving. "
    Xia "Good riddance, what a pathetic man... ruined my mood. "
    stop music
    show bg auntmeet 29 with Dissolve(0.8)
    play music "/audio/athom.ogg"
    Kiara "I'd love to touch that katana, but I love my fingers more. It looks so cool, though. "
    Xia "It is real. My father's sensei crafted it. "
    show bg auntmeet 30 with Dissolve(0.8)
    Kiara "Is that so...? grandpa was a samurai? "
    Xia "Yes, among the 12 last clans, he was a legend in his prime. "
    Kiara "I wanna know more abo- "
    show bg auntmeet 31 with Dissolve(0.8)
    Xia "Kia, you must be tired from the trip. Get freshened and have some lunch. I'll personally give you a tour then. "
    Kiara "Okay, auntie, Thank you. "
    stop music
    ""
    jump daybath

label kiaraincab:
    show bg cabjpn 1 with Dissolve(0.8) 
    Oldman "That's right."
    Oldman "Hmm , I should initiate I suppose. "
    Kiara "All the other kids with the pumped up k-- "
    show bg cabjpn 2 with Dissolve(0.8)
    Oldman "So this a trip or holiday? Or just visiting? "
    Kiara "Actually, it's my first time in japan. I don't know much, so hopefully, auntie will help me get to know stuff. "
    Oldman "Right, right, well, enjoy the sightseeing. "
    show bg cabjpn 3 with Dissolve(0.8)
    Kiara "Oh my gosh, the architecture is so pretty! "
    Oldman "Okay, I've gotta find an opportunity ... that dress looks loose. "
    show bg cabjpn 4 with Dissolve(0.8)
    Kiara "There's like temples and castles, this is so cool! "
    show bg cabjpn 5 with Dissolve(0.8)
    Oldman "Hm, her jumping around is loosening her dress. "
    show bg cabjpn 6 with Dissolve(0.8)
    Kiara "Are those sakura blossoms? Sooo pretty! "
    show bg cabjpn 7 with Dissolve(0.8)
    Oldman "That's right baby, keep moving around. I know what to do soon."
    menu:
        "Pay attention to the dress":
            Oldman "Dammit she is fixing it, Oh well another day."
            jump auntmeet
        "Don't pay attention":
            $ mc_stats.adjust_corruption(2)
            pass
    show bg cabjpn 8 with Dissolve(0.8)
    Kiara "*yawn* Ahh, man, I can't wait to explore all this soon. "
    show bg cabjpn 9 with Dissolve(0.8)
    Oldman "That dress won't hold if any more if a push is given, so fucking close. "
    stop music
    show bg cabjpn 10 with Dissolve(0.8)
    Oldman "Now's my chance! "
    show bg cabjpn 11 with Dissolve(0.8)
    Kiara "AAH What the! "
    "" "The car suddenly bounces in traffic."
    show bg cabjpn 12 with Dissolve(0.8)
    Oldman "Now let's take a peek! "
    show bg cabjpn 13 with Dissolve(0.8)
    play music "/audio/mmsx.ogg"
    Oldman "Hoo hoo! what a body, so smooth, let us give it another bump."
    show bg cabjpn 14 with Dissolve(0.8)
    Kiara "Ah! I can't, ugh! "
    Oldman "Wow, what a view this bitch is fine! "
    show bg cabjpn 15 with Dissolve(0.8)
    Oldman "Those panties? Is she secretly a slut?  "
    show bg cabjpn 16 with Dissolve(0.8)
    Oldman "Either way, who cares? Damn shame she's wearing panties would've been nice to see her snatch. "
    show bg cabjpn 17 with Dissolve(0.8)
    Oldman "Even then, so worth it that body is remarkable, mmm. "
    show bg cabjpn 18 with Dissolve(0.8)
    Kiara "Ugh... hey? What the hell was that? "
    show bg cabjpn 19 with Dissolve(0.8)
    Oldman "Hey, I am so sorry. I had to overtake. Otherwise, the truck would've hit us! "
    show bg cabjpn 20 with Dissolve(0.8)
    Kiara "Ah, whatever, let me find my sho-- What the! "
    show bg cabjpn 21 with Dissolve(0.8)
    Kiara "My dress opened!... Did he see anything?... I hope not. "
    show bg cabjpn 22 with Dissolve(0.8)
    Oldman "All good back there? "
    Kiara "Uhh yea, yea, Um, let's go."
    Kiara "Better not argue. I'll get home and stay off this weirdo."
    stop music

    ""
    jump auntmeet

label kiaraairport:
    play music "/audio/oska.ogg"
    show bg arrivaljapan 1
    "" "{i}Osaka Japan - Early Morning{/i}"
    Azumi "Are you sure you're not cold? The ac was extreme in the plane. "
    Kiara "Heh, I am okay, Azumi. You worry more than my mum. "
    scene
    show bg arrivaljapan 2
    Azumi "Well, yea, because I know I won't find such a cool company again."
    Kiara "Very cute. You're smoother than the leather seats in the plane."
    show bg arrivaljapan 3
    Azumi "So you really can't come home with me? I make good cupcakes. "
    Kiara "I'll eat all of those, I promise, but right now, my aunt is probably waiting for me, so I need to go there first. "
    show bg arrivaljapan 4
    Azumi "I hope you don't get lost or something. This is a big city. "
    Kiara "I know, don't worry, I'll get home directly, and once I'm there, I'll let you know. "
    show bg arrivaljapan 5
    Kiara "Besides, I'm going to live here. Not to be rude, but I gotta learn the city a bit."
    Azumi "No, of course not, but do let me know if you need anything. "
    Kiara "You know I will ~ "
    show bg arrivaljapan 6
    Azumi "Kiara, Please call me, okay? I hope we meet again."
    Kiara "Azumi, I will, I promise. You're my first friend here, after all. "
    show bg arrival 1
    Kiara "She was cute... Alright then, here we are, time to get going."
    Crowd "Damn, that's a babe right there."
    stop music
    ""
    jump kalintro

label kalintro:
    play music "/audio/vltnc.ogg"
    show bg kaylaintro 1  with Dissolve(0.8)
    Valentina "Cmon, Cmon, this is it. "
    show bg kaylaintro 2  with Dissolve(0.8)
    Valentina "I knew it... her passport was used! "
    show bg kaylaintro 3  with Dissolve(0.8)
    Valentina "I have to be sure. I don't want this to be a hunch."
    show bg kaylaintro 4  with Dissolve(0.8)
    Valentina "I'll visit the embassy tomorrow and verify it myself. "
    show bg kaylaintro 5  with Dissolve(0.8)
    Valentina "I should call Damian to let him know. "
    show bg kaylaintro 6  with Dissolve(0.8)
    Valentina "Ah, what am I thinking... before I even mention her in front of him, I have to be entirely sure. "
    show bg kaylaintro 7  with Dissolve(0.8)
    Valentina "Either way, this can't be a coincidence. I've been following everything because I never believed that man's story. "
    show bg kaylaintro 8  with Dissolve(0.8)
    Valentina "Dammit, nothing to eat. I hope Nick brings a pizza. "
    show bg kaylaintro 9  with Dissolve(0.8)
    Valentina "Huh? was that the door? "
    show bg kaylaintro 10  with Dissolve(0.8)
    Valentina "I left it open because nick said he'd return soon. "
    show bg kaylaintro 11  with Dissolve(0.8)
    Valentina "Nick? is that you, honey? "
    show bg kaylaintro 12  with Dissolve(0.8)
    Valentina "Um... can I help you, officer? "
    Police "Mam, A call was made about someone in distress. It seems like a false alarm, but please keep the doors locked next time. "
    show bg kaylaintro 13  with Dissolve(0.8)
    Valentina "I... I'm very sorry. I was waiting for my fiance, and I had left it unlocked. "
    show bg kaylaintro 14  with Dissolve(0.8)
    Valentina "Why does he have a gun...? "
    show bg kaylaintro 15  with Dissolve(0.8)
    Police "Mam? is that clear? "
    Valentina "Um... yes, officer, I'm sorry again. "
    show bg kaylaintro 16  with Dissolve(0.8)
    Valentina "A fake distress call?... ugh kids these days."
    show bg kaylaintro 17  with Dissolve(0.8)
    Valentina "I should watch something. I need a distraction. "
    show bg kaylaintro 18  with Dissolve(0.8)
    "Phone""**Rings** "
    Valentina "Hm? who could it be this late? "
    show bg kaylaintro 19  with Dissolve(0.8)
    Valentina "This... seems like a burner number? Okay val! "
    show bg kaylaintro 20  with Dissolve(0.8)
    Valentina "Aiden , is that you? "
    show bg kaylaintro 21  with Dissolve(0.8)
    morphvoice "Hey babe , looking lovely in blue. "
    Valentina "Who the fuck is this? "
    morphvoice "Damn, why the temper? I only complimented you. "
    show bg kaylaintro 22  with Dissolve(0.8)
    Valentina "Listen asshole, this is not the time nor am I in the mood , So, go fuck yourself! "
    morphvoice "Alright I'll cut to the chase , you're snooping around things you shouldn't babe , back off, you're smart enough to know what I'm refering to here. "
    show bg kaylaintro 23  with Dissolve(0.8)
    Valentina "You fucking pig , how dare you! "
    morphvoice "**Hangs up** "
    show bg kaylaintro 26  with Dissolve(0.8)
    Valentina "Ugh... who the hell was that? I can't even trace it. "
    Valentina "I should finish everything tomorrow , I'll look into this then. "
    show bg kaylaintro 27  with Dissolve(0.8)
    Valentina "Ah... Kiara if you really are alive, you've got alot more to explain than I do to anyone... "
    stop music

    ""


    jump azumiportbathroom


label airport:
    "" "{i}Airport - Outside{/i}"
    play music "/audio/oska.ogg"
    scene bg arrival 2
    Kiara "Alright, japan, Here I come!... Ah, the air seems nice too."
    show bg arrival 3 with Dissolve(0.8)
    Kiara "Dammit... probably should've asked Azumi to book a cab. My Japanese is trash. "
    show bg arrival 4 with Dissolve(0.8)
    Kiara "Alright! I know what to do. I'll get to aunt's home by maps and then figure out the rest. "
    show bg arrival 5 with Dissolve(0.8)
    Kiara "After that, I'll try to contact mum and update everyone. "
    show bg arrival 6 with Dissolve(0.8)
    Kiara "Oh wait, there's a cab coming! Heyyyyyy! Uh... Ohiooooo. "
    show bg arrival 7 with Dissolve(0.8)
    Kiara "Teishi shite kudasai! Er...no, wait! "
    show bg arrival 8 with Dissolve(0.8)
    Oldman "Far from home, aren't you, sweetheart? "
    show bg arrival 9 with Dissolve(0.8)
    Kiara "Oh my gosh, you speak english! Hi... I'm so lucky, wow. "
    Oldman "Hahaha, I moved here 30 years ago, so where do you need to go? "
    show bg arrival 10 with Dissolve(0.8)
    Kiara "I just arrived, I'm sorry, but yeah, I need to go to my aunts! "
    show bg arrival 11 with Dissolve(0.8)
    Kiara "Here you go, this was the location on maps sent to me... will this-- "
    Oldman "Hot damn, this gal has nice tits... "
    Oldman "Ah yes, yes! Please sit, and put the bag behind you. "
    show bg arrival 12 with Dissolve(0.8)
    Kiara "Alright, Vamenos senior! "

    ""
    jump kiaraincab

    #intro segment



label intro:
    play music "audio/Intrmainscn.ogg"
    "{i}Somewhere in brooklyn{/i}"
    show bg intro 1 with Dissolve(0.8)
    Kiara "Three years I've lost , they say the accident was so horrible that it put me in coma , all of that makes sense but what of before?...Why can't I remember days of uni? Maybe-"
    show bg intro 2 with Dissolve(0.8)
    stop music
    play music "audio/Intomain2.ogg"
    John "Hey ya'll I'm home!"
    show bg intro 3 with Dissolve(0.8)
    Kiara "Shit , lost my train of thought."
    show bg intro 4 with Dissolve(0.8)
    Kiara "That must be dad... late as usual but I hope he's alright."
    show bg intro 5 with Dissolve(0.8)
    Mia  "Well look who decided to show up , the irresponsible drunktard that thinks money and alchohol solves evertything."
    show bg intro 6 with Dissolve(0.8)
    John "Money got me you didn't it? You're a fine piece that has everything heh."
    show bg intro 7 with Dissolve(0.8)
    Mia  "You're so drunk you don't even realize john , compliments won't save you here , you told me you'd stop this."
    John "Oh for christ sakes , shut up will you"
    show bg intro 8 with Dissolve(0.8)
    John "Listen Mia can we not do this today , I had a fun night hun and it was great now don't ruin my mood alright."
    show bg intro 8 with Dissolve(0.8)
    Mia  "Not today? When does it stop Jonathan? You and I agreed that we'll improve our lives after what happened with kiara , how about you start doing that by not drinking and sleeping with sluts."
    show bg intro 9 with Dissolve(0.8)
    John "Argh whatever, you just don't understand me  , though you're right about one thing , I should stop sleeping with sluts, starting from today bedroom is all yours"
    show bg intro 10 with Dissolve(0.8)
    Mia  "What the fuck did you just say?"
    show bg intro 10 with Dissolve(0.8)
    John "It was a joke!"
    show bg intro 11 with Dissolve(0.8)
    Kiara "What on earth is happening down there."
    show bg intro 12 with Dissolve(0.8)
    Mia  "You have the guts to call me that after I've left my fucking family for you? What the hell is wrong with you."
    show bg intro 12 with Dissolve(0.8)
    John "Oh please you got money for it too stop acting like a teenager , don't act all high and mighty, fuck your stupid judgements."
    show bg intro 13 with Dissolve(0.8)
    Mia  "Fuck you too!"
    show bg intro 14 with Dissolve(0.8)
    Kiara "I wish this would stop , they've been this way even after I got back home , god knows how bad it got in those 3 years."
    show bg intro 15 with Dissolve(0.8)
    Kiara "Honestly I'm too tired to even think at this point , I'll just take some pills and rest."
    show bg intro 16 with Dissolve(0.8)
    Kiara "Goodnight awful life , see you again tomorrow ."
    show bg intro 17 with Dissolve(0.8)
    John "Kiara , sorry for all the comotion down there ,  I hope you weren't asleep-"
    show bg intro 18 with Dissolve(0.8)
    John "You here ?"
    show bg intro 18 with Dissolve(0.8)
    John "The only reason I agreed to this stupid open bathroom was hoping to walk in on her and see her, hasn't happened yet what a shame."
    show bg intro 19 with Dissolve(0.8)
    John "Kiara... oh my"
    show bg intro 20 with Dissolve(0.8)
    John "There's my babygirl man what a diamond cutter she has , shame I can't cross boundries."
    show bg intro 21 with Dissolve(0.8)
    John "I wonder how her feet smell , she stays so clean after all I'm sure a little sniff wouldn't hurt."
    show bg intro 21 with Dissolve(0.8)
    John "*sniff* Oh god , she's perfect even in this department."
    show bg intro 22 with Dissolve(0.8)
    John "I guess a touch wouldn't hurt after all , I'm the reason she's in this world ."
    show bg intro 23 with Dissolve(0.8)
    John "God even through the fabric its so soft , okay... I won't do more than touch so lets see how this ass looks."
    show bg intro 24 with Dissolve(0.8)
    Mia  "What a joke this life is , ugh whatever I should check up on kiara."
    show bg intro 25 with Dissolve(0.8)
    John "Holy fuck , that ass is so fucking soft , I think she wears skinny panties let'see."
    show bg intro 26 with Dissolve(0.8)
    Mia  "My life might be a shithole but I'll make sure her is the best , soon I'll find a way."
    show bg intro 27 with Dissolve(0.8)
    John "Damn I can't touch but guess I can jerk off to it at least , she's my babygirl for sure."
    show bg intro 28 with Dissolve(0.8)
    John "Mmm god blessed me with a fine daughter"
    show bg intro 29 with Dissolve(0.8)
    Mia "Kiar- Huh?"
    show bg intro 30 with Dissolve(0.8)
    Mia "What the fuck do you think you're doing Jonathan hall"
    John "Shit! Got caught . Hey ! I can explain"
    show bg intro 31 with Dissolve(0.8)
    Mia  "How fucking dare you !"
    Kiara "Ugh... what is happening?"
    show bg intro 32 with Dissolve(0.8)
    Kiara "Wha- ? why are my pants halfway down? Did dad...?"
    show bg intro 33 with Dissolve(0.8)
    Mia  "Explain it to your fucking lawyer!"
    show bg intro 34 with Dissolve(0.8)
    Mia  "Come kiara , we're leaving!"
    show bg intro 35 with Dissolve(0.8)
    John "Fuck - ough , hey I wasn't gonna do anything!"
    show bg intro 36 with Dissolve(0.8)
    Mia  "You can shove your excuse where the sun doesn't shine ."
    show bg intro 37 with Dissolve(0.8)
    John "Wait hey you can't do this , she's my daughter too and I was only looking!"
    Mia  "Oh you think I can't? Fucking watch me you asshole."
    show bg intro 38 with Dissolve(0.8)
    John "Kiara I am sorry , I was drunk and then suddenly ju..."
    Kiara "Even if you are sorry dad I think you need some time alone after what's happened , and I mean a long time alone , take care."
    Mia "Kiara , come quick!"
    stop music



    jump hotel


label hotel:
    "" "An Hour later avenue hotel"
    play music "audio/htlscns.ogg" loop
    show bg hotel 1 with Dissolve(0.8)
    Kiara "Well I certainly didn't expect to end today this way."
    show bg hotel 2 with Dissolve(0.8)
    Kiara "And SPECIALLY not dressed like this!"
    show bg hotel 3 with Dissolve(0.8)
    Kiara "But here we are anyway , oh well how bad can it be"
    show bg hotel 4 with Dissolve(0.8)
    Kiara "Seems like a nice hotel too."
    show bg hotel 5 with Dissolve(0.8)
    Mia  "Hello there"
    show bg hotel 5 with Dissolve(0.8)
    #Reception
    "{i}Welcome to central avenue mam{/i}"
    show bg hotel 6 with Dissolve(0.8)
    Mia  "Thank you , we'd like a room for two for tonight , could you please take us we're very tired."
    Dennis "Give me a moment mam"
    show bg hotel 8 with Dissolve(0.8)
    Dennis "Damn these are some babes , that girl is trying to hide her best but her thighs alone tell me she's got a juicy pussy under those shorts ."
    show bg hotel 9 with Dissolve(0.8)
    Dennis "speaking of juicy tho the mother ain't so bad a thic asian with that cute face."
    show bg hotel 10 with Dissolve(0.8)
    Dennis "Damn can even imagine how they look like uner that top too."
    show bg hotel 7 with Dissolve(0.8)
    Dennis "Sure mam , please come  with me."
    show bg mumgrop 1 with Dissolve(0.8)
    Dennis "Lets see how she reacts to a little touch"
    show bg mumgrop 2 with Dissolve(0.8)
    Dennis "I'd love to bang em both but one should be good for dinner , here we go."
    show bg mumgrop 3 with Dissolve(0.8)
    Dennis "Here goes nothing!"
    stop music
    show bg mumgrop 4 with Dissolve(0.8)
    play music "/audio/surprisedgrop.ogg" noloop
    Mia  "That's... a hand? No , it isn't an accident he's actually groping me... what the hell last thing I need now is this."
    stop music
    show bg mumgropdecide
    play music "/audio/choicmusic.ogg"
    menu:
        "Let it be , Kiara needs less drama now":
            #TODO add kiara corruption by 1 
            $ mc_stats.adjust_corruption(1)
            call accepthotelmom from _call_accepthotelmom
        "Stop him!":
            call rejecthotelmom from _call_rejecthotelmom

    jump roomsegment


label accepthotelmom:
    stop music
    play music "/audio/htlscns.ogg"
    show bg mumacctdgrope 1 with Dissolve(0.8)
    Mia  "Ugh whatever , we're just gonna go to the room and this will end I can endure this much."
    show bg mumacctdgrope 2 with Dissolve(0.8)
    Dennis "Well well we got a submissive babe here I see , very well then I'll enjoy myself."
    show bg mumacctdgrope 3 with Dissolve(0.8)
    Kiara "Mom you comin?"
    show bg mumacctdgrope 4 with Dissolve(0.8)
    Mia  "Be there shortly hun you take some rest  need to talk to a friend."
    show bg mumacctdgrope 5 with Dissolve(0.8)
    Kiara "Alright, see you I'm too tired to stand."
    show bg mumacctdgrope 6 with Dissolve(0.8)
    Mia  "Care to explain yourself?"
    show bg mumacctdgrope 7 with Dissolve(0.8)
    Dennis "Do I? you're the one that let me squeeze , also perhaps we should continue this in a private space ."
    show bg mumacctdgrope 6 with Dissolve(0.8)
    Mia  "Why would I do that?"
    show bg mumacctdgrope 6 with Dissolve(0.8)
    Dennis "Because I know your husband and I am sure me informing him you  being here whatever the reason won't really please him"
    show bg mumacctdgrope 6 with Dissolve(0.8)
    Dennis "Tho don't worry all I want is to see you naked no touching."
    show bg gropedcde 2 with Dissolve(0.8)
    Mia  "No! if john knows about us he'll come for kiara , I can't let this happen."
    stop music

    play music "/audio/choicmusic.ogg"
    menu:
        "It's just my body , I'd give my life for her":
            #TODO kiara corruption by 1
            $ mc_stats.adjust_corruption(1)
            call accmumelv from _call_accmumelv
        "I can't do this...":
            call rejmumelv from _call_rejmumelv

    return

label accmumelv:
    stop music
    play music "/audio/htlscns.ogg" loop
    show bg gropedcde 2 with Dissolve(0.8)
    Mia  "Alright fine ... you won't tell him if I do right?"
    show bg mumelv 0 with Dissolve(0.8)
    Dennis "Cross my heart love , now lets go!"
    show bg mumelv 1 with Dissolve(0.8)
    Mia  "Hey my heels ouch!"
    show bg mumelv 2 with Dissolve(0.8)
    Mia  "Do we really have to do this?"
    show bg mumelv 3 with Dissolve(0.8)
    Dennis "That ass was soft even with  your jeans on , no way I'm skipping the chance here."
    show bg mumelv 3 with Dissolve(0.8)
    Dennis "Now then... you won't be needing this top hun ."
    show bg mumelv 4 with Dissolve(0.8)
    Dennis "Holy shit they're bigger than I thought damn"
    show bg mumelv 4 with Dissolve(0.8)
    Mia  "Please I am sensitive go easy"
    show bg mumelv 5 with Dissolve(0.8)
    Dennis "Damn you were hiding good gems these feel so great to hold"
    show bg mumelv 6 with Dissolve(0.8)
    Mia  "Um you said no touching?"
    show bg mumelv 6 with Dissolve(0.8)
    Dennis "No touching means no dicking hun , besides not like you got a choice so stay quiet before I fuck you in the hallway."
    show bg mumelv 7 with Dissolve(0.8)
    Mia  "Okay sorry , fine."
    show bg mumelv 8 with Dissolve(0.8)
    Dennis "Now lets see what we got here"
    show bg mumelv 8 with Dissolve(0.8)
    Mia  "Hey wait not there!"
    show bg mumelv 9 with Dissolve(0.8)
    Dennis "Oh my all shaved are we , I gotta see this for myself."
    show bg mumelv 10 with Dissolve(0.8)
    Mia  "A guy I don't know has stripped me naked and I'm not even resisting... am I really a slut like john said?"
    show bg mumelv 10 with Dissolve(0.8)
    Dennis "You got a soft shaved cunt babe , I like it."
    show bg mumelv 11 with Dissolve(0.8)
    Mia  "This... can't be happening"
    show bg mumelv 11 with Dissolve(0.8)
    Dennis "It is!"
    show bg mumelv 12 with Dissolve(0.8)
    Dennis "My fingers feel good don't they?"
    show bg mumelv 12 with Dissolve(0.8)
    Mia  "Sigh... just stay quiet..."
    Mia  "Look I did what you asked , you've seen me now can I go please?"
    show bg mumelv 12 with Dissolve(0.8)
    Dennis "Fair I suppose , but two things left , lets see you properly ."
    show bg mumelv 13 with Dissolve(0.8)
    Mia  "Hey wait!"
    show bg mumelv 13 with Dissolve(0.8)
    Dennis "Keep quiet babe, take a good look at yourself , biting your lip while a stranger spreads your fucking legs."
    show bg mumelv 14 with Dissolve(0.8)
    Dennis "You can say whatever but those holes are begging to be fucked babe."
    show bg mumelv 14 with Dissolve(0.8)
    Mia  "I know... Can I please go now."
    show bg mumelv 15 with Dissolve(0.8)
    Dennis "You can but last thing left , give me a good kiss hun."
    show bg mumelv 15 with Dissolve(0.8)
    Mia  "Alright..."
    show bg mumelv 16 with Dissolve(0.8)
    Dennis "*Smooch* Juicy , now you can go ."
    stop music



    return

label rejmumelv:
    stop music
    play music "/audio/mibeg.ogg"
    show bg mumrjctelevtr 1 with Dissolve(0.8)
    Mia  "Look We've had a rough night , my daughter has had a accident recently"
    show bg mumrjctelevtr 2 with Dissolve(0.8)
    Mia  "And we are very stressed please understand me that I --"
    show bg mumrjctelevtr 3 with Dissolve(0.8)
    Dennis "Oh cmon now you ruined the mood , whatever I don't need sob stories I like sluts , I'm out."
    show bg mumrjctelevtr 4 with Dissolve(0.8)
    Mia  "Thank you..."
    stop music
    return

label rejecthotelmom:
    stop music
    play music "/audio/takacton.ogg"
    show bg momgroperjctd 1 with Dissolve(0.8)
    Mia  "Alright I'm not suffering this shit , let's take care of it right now I know my room already."
    show bg momgroperjctd 2 with Dissolve(0.8)
    Dennis "aw shucks I guess not tod-"
    show bg momgroperjctd 3 with Dissolve(0.8)
    Mia  "Take this"
    show bg momgroperjctd 4 with Dissolve(0.8)
    Dennis "Hey what the-"
    show bg momgroperjctd 4 with Dissolve(0.8)
    Mia  "Oh my god are you okay? I'm so sorry ,take care"
    show bg momgroperjctd 5 with Dissolve(0.8)
    Mia  "Serves you right fucker."
    show bg momgroperjctd 4 with Dissolve(0.8)
    Dennis "- m—uh jaw."
    stop music
    return



    label roomsegment:
    play music "/audio/htlroom.ogg"
    show bg htlroom 1 with Dissolve(0.8)
    Mia "Room seems fine... god, what a headache."
    show bg htlroom 2 with Dissolve(0.8)
    Kiara "Mom... are you sure about this? This is a very big step you'll take to know."
    show bg htlroom 3 with Dissolve(0.8)
    Mia  "Of course I am. That man abused me my whole married life, which I can handle, but today he crossed the line."
    show bg htlroom 4 with Dissolve(0.8)
    Kiara "You're the boss, mom. I was trying to say what I felt."
    show bg htlroom 5 with Dissolve(0.8)
    Mia  "I'm sorry honey, I've just been having a bad day already."
    show bg htlroom 6 with Dissolve(0.8)
    Mia "I've got to go.... I'm sorry for tonight. Please rest. I'll be late."
    Kiara "I'll be okay, mom. Please take care too."
    show bg htlroom 7 with Dissolve(0.8)
    Kiara "She is not well. Why did dad do this."
    show bg htlroom 7 with Dissolve(0.8)
    Kiara "Ah, well, I might as well take a shower. I feel disgusting. I don't know why."
    show bg htlroom 9 with Dissolve(0.8)
    Kiara "God, I love a warm shower. It is like everything wrong fades away."
    show bg htlroom 11 with Dissolve(0.8)
    "Waitor""Room service, two bags for 162? "
    show bg htlroom 12 with Dissolve(0.8)
    "Waitor""Huh, I guess they must be at dinner. I'll leave these here, I guess."
    show bg htlroom 13 with Dissolve(0.8)
    "Waitor""Time to go!"
    show bg htlroom 15 with Dissolve(0.8)
    Kiara "Did I hear something? Must've been the wind."
    show bg htlroom 16 with Dissolve(0.8)
    Dennis "Stupid intern left the door open, heh, time to see that beauty , huh?"
    show bg htlroom 17 with Dissolve(0.8)
    Dennis "Aw shucks no one here damn room will be locked at night and they'll leave tomorrow, got to think of something."
    show bg htlroom 18 with Dissolve(0.8)
    Dennis "Well, what do we have here?"
    show bg htlroom 19 with Dissolve(0.8)
    Dennis "If I take one of these, one of them will have to come to the lobby, and then I'll have fun with one of them."
    show bg htlroom 20 with Dissolve(0.8)
    Dennis "I guess these are their clothes , best choice I'm so smart."
    show bg htlroom 21 with Dissolve(0.8)
    Dennis "Lifting bags now then I'll lift their cheeks, later!"
    show bg htlroom 22 with Dissolve(0.8)
    Kiara "Damn, they've grown a lot since I started uni , hopefully not much more since I like my back not in pain."
    show bg htlroom 23 with Dissolve(0.8)
    Kiara "Now then where were we."
    show bg htlroom 24 with Dissolve(0.8)
    Kiara "Hm? Who's calling now?"
    show bg htlroom 24 with Dissolve(0.8)
    Kiara "Ah, hopefully this isn't dad, I'm not in the mood."
    show bg htlroom 25 with Dissolve(0.8)
    Kiara "Hello who's this?"
    show bg htlroom 26 with Dissolve(0.8)
    Miaonphone "Hey, hun!"
    show bg htlroom 27 with Dissolve(0.8)
    Kiara "Oh hey mom , everything okay?"
    show bg htlroom 27 with Dissolve(0.8)
    Miaonphone  "It'll be okay , baby I need you to go to airport and take the flight to japan,its sudden I know but trust me this is what mason recommended."
    show bg htlroom 28 with Dissolve(0.8)
    Kiara "Oh uh... Okay mom , what do I do then?"
    show bg htlroom 28 with Dissolve(0.8)
    Miaonphone "You must have received two bags  it has your passport and ticket and stuff you need okay?"
    show bg htlroom 29 with Dissolve(0.8)
    Kiara "I see it mom , don't worry I'll handle it, you be safe okay?"
    show bg htlroom 29 with Dissolve(0.8)
    Kiara "Ah my clothes aren't here , she said two bags, she sounded stressed and I forgot to notice.... I can't go to the lobby now, the flight is soon , what do I do?"
    show bg htlroom 30 with Dissolve(0.8)
    Kiara "Oh wait yes! I can call lana to grab me one for the moment."
    show bg htlroom 31 with Dissolve(0.8)
    Kiara "Lana?.... Hello, uh,I need some help!"
    stop music
    ""
    jump lanastart

label lanastart:
    play music "/audio/lanahtlc.ogg"
    show bg lanaapt with Dissolve(0.8)
    Lana "The one and only babe , what can I help you with hun?"
    show bg lanaapt  with Dissolve(0.8)
    Kiaraonphone "I.... uh need a dress , I can't explain now but I have a flight and forgot to bring clothes and stuff could you please just lend me a dress? I'll return it."
    Lana "Of course why not , I was on the way to a party and your hotel is close, see you soon."
    Kiaraonphone "Thank you, so much!"
    show bg lanaapt2 with Dissolve(0.8)
    show bg lanaapt2 with Dissolve(0.8)
    Lana "I'll give her a nice bag so she doesn't have trouble either , lets go lana."
    jump lanahotel

label lanahotel:
    show bg lanahtl1 with Dissolve(0.8)
    Lana "Yo, anyone here?"
    show bg lanahtl2 with Dissolve(0.8)
    Dennis "My sincere apologies mam , my colleague was having stomach pain."
    show bg lanahtl3 with Dissolve(0.8)
    Lana "It's fine , sup?  I need this bag delivered to my friends room, I believe its 162."
    show bg lanahtl4 with Dissolve(0.8)
    Dennis "Of course , I'll carry it, you don't have to burden yourself at all."
    show bg lanahtl5 with Dissolve(0.8)
    Dennis "Damn I'd love to carry this bitch on my dick too, what a hot blondie."
    show bg lanahtl6 with Dissolve(0.8)
    Dennis "Upstairs mam."
    show bg lanahtl6 with Dissolve(0.8)
    Lana "Sure, lets go."
    show bg lanahtl7 with Dissolve(0.8)
    Lana "This is it?"
    show bg lanahtl7 with Dissolve(0.8)
    Dennis "Yes"
    stop music
    jump lanaelevator

label lanaelevator:
    play music "/audio/htlscns.ogg"
    show bg lanadecidegrope with Dissolve(0.8)
    Lana "**Hm mhm**"
    show bg lanalift1 with Dissolve(0.8)
    Dennis "Well then time to make my move."
    show bg lanalift2 with Dissolve(0.8)
    Dennis "Lets see how you react."
    show bg lanalift2 with Dissolve(0.8)
    Dennis "I bet this slut is smooth."
    show bg lanalifttouch with Dissolve(0.8)
    stop music
    play music "/audio/choicmusic.ogg"
    Lana "- Did he just touch my butt? What the-.... I should."

    menu:
        "Don't mind it":
            #TODO add kiara corruption by 1
            $ mc_stats.adjust_corruption(1)
            call lanaAcpt1 from _call_lanaAcpt1
        "Time to kick his ass":
            call lanaRjt1 from _call_lanaRjt1



    jump roomsegment2

label roomsegment2:
    play music "/audio/htlroom.ogg"
    show bg htlroom 32 with Dissolve(0.8)
    Kiara "Ah that must be her ."
    show bg htlroom 33 with Dissolve(0.8)
    Kiara "Ah here's the bag... where's lana though?"
    show bg htlroom 34 with Dissolve(0.8)
    Kiara "I swear I heard her voice..."
    MIB "Looking good, baby."
    show bg htlroom 35 with Dissolve(0.8)
    Kiara "*gasp* oh my god I'm so sorry, I heard my friend and I –"
    show bg htlroom 36 with Dissolve(0.8)
    MIB "Chill out what ya sorry for , I should thank you... speaking of favors tho how about we help each other take off towels heh?"
    show bg htlroom 37 with Dissolve(0.8)
    Kiara "Nope nope nope bye!"
    MIB "Aw dammit."
    show bg htlroom 38 with Dissolve(0.8)
    Kiara "Whew... close , Jesus perverted people all over."
    show bg htlroom 39 with Dissolve(0.8)
    Kiara "Now then lets see what's in the bag."
    show bg htlroom 40 with Dissolve(0.8)
    Kiara "Okay its very sweet of her to bring more food but this dress... what on earth , it'll never fit me and I can't wear it on a flight!"
    show bg htlroom 41 with Dissolve(0.8)
    Kiara "I don't have time to go to lobby, oh well , beggers can't be choosers."
    show bg htlroom 42
    Kiara "I guess its not that bad.... the top won't close fully, but its just one flight and I'll then get my clothes the next day."
    stop music

    jump Momandlawyer

label lanaAcpt1:
    play music "/audio/htlscns.ogg"
    show bg lanadecidegrope with Dissolve(0.8)
    Lana "Okay, whatever, poor guy probably hasn't seen a girl. I'll be out of the lift soon."
    show bg lanaelv 1 with Dissolve(0.8)
    Dennis "Now's my turn !"
    Lana "Hey, what the f-"
    show bg lanaelv 2 with Dissolve(0.8)
    Lana "What are you?-"
    Dennis "I know the room you're going to only has women in it, and no panties mean you are seeking fun? Speaking of which, let us see these puppies."
    show bg lanaelv 3 with Dissolve(0.8)
    Lana "*Gasp*"
    show bg lanaelv 4 with Dissolve(0.8)
    Dennis "God gave you wonderful babies for sure, hun. I wonder what god gave you down there, heh."
    Lana "Hey, cut it out. What the -"
    Lana "This is crazy. I should do something before it's too late."
    menu:
        "Try to run away...":
            call lanaRjt2 from _call_lanaRjt2
        "It's too late...":
            #TODO add kiara corruption by 1
            $ mc_stats.adjust_corruption(1)
            call lanaAcpt2 from _call_lanaAcpt2
    # show bg lanaelv 5 with Dissolve(0.8)
    # Dennis "You won't be need this either anymore"
    # show bg lanaelv 6 with Dissolve(0.8)
    # Lana ""
    # show bg lanaelv 7 with Dissolve(0.8)
    # Lana "Hey cut it out!"
    # show bg lanaelv 8 with Dissolve(0.8)
    # Dennis "Oh man this pussy is soft"
    # show bg lanaelv 9 with Dissolve(0.8)
    # Lana "This is crazy I should do something before its too late."





    return

label lanaRjt1:
    play music "/audio/takacton.ogg"
    show bg lanarjctgrp1 with Dissolve(0.8)
    Lana "Hey honey, no need to rush, let's go to a room, and we'll continue, but how about I give you a good taste on your dick first? Come on, close your eyes."
    show bg lanarjctgrp2 with Dissolve(0.8)
    Dennis "Now, you're talking, babe, alright closed, let's feel what you got."
    show bg lanarjctgrp3 with Dissolve(0.8)
    Lana "This is what I got, you fucker."
    show bg lanarjctgrp4 with Dissolve(0.8)
    Dennis "Ow! My fucking balls."
    show bg lanarjctgrp5 with Dissolve(0.8)
    Dennis "Hey, hey, calm down. It was just a touch."
    show bg lanarjctgrp5 with Dissolve(0.8)
    Lana "Calm down? You fucking pig?"
    Lana "You're lucky I'm in a good mood, or those balls would be in your mouth right now."
    show bg lanarjctgrp6 with Dissolve(0.8)
    Dennis "Hey, please don't compl-"
    show bg lanarjctgrp6 with Dissolve(0.8)
    Lana "Fuck off"
    Dennis "Ugh!"
    show bg lanarjctgrp7 with Dissolve(0.8)
    Lana "FFs, I'll meet her in japan. My mood is ruined."
    show bg lanarjctgrp8 with Dissolve(0.8)
    Lana "Your package Is here! baby~"
    stop music
    jump roomsegment2

label lanaRjt2:
    play music "/audio/lanrnawy.ogg"
    show bg lanarunaaway 1 with Dissolve(0.8)
    Lana "Um hey?"
    show bg lanarunaaway 2 with Dissolve(0.8)
    Dennis "Damn that pussy is smooth , lets slide this skirt too."
    show bg lanarunaaway 3 with Dissolve(0.8)
    Lana "Hey wait! Hear me out okay."
    show bg lanarunaaway 4 with Dissolve(0.8)
    Dennis "Alright fine what is it ? I'm playing with your tits meanwhile go on."
    show bg lanarunaaway 5 with Dissolve(0.8)
    Lana "Look my friend has a flight and she needs the bag once I give this to her we can continue this however you want."
    show bg lanarunaaway 6 with Dissolve(0.8)
    Dennis "Alright fare deal , but you'll go out topless so I know your ass won't run away."
    show bg lanarunaaway 7 with Dissolve(0.8)
    Lana "Deal!"
    Lana "I'd rather let strangers see my tits than to be touched by a waitor , okay lana lets do this *"
    show bg lanarunaaway 8 with Dissolve(0.8)
    Lana "KIARA YOUR LUGGAGE!"
    show bg lanarunaaway 9 with Dissolve(0.8)
    "Lana runs away"
    show bg lanarunaaway 10 with Dissolve(0.8)
    Dennis "Hey what the hell come back bitch."
    show bg lanarunaaway 11 with Dissolve(0.8)
    Dennis "Shit someone's coming , bitch tricked me."
    stop music
    jump roomsegment2

label lanaAcpt2:
    play music "/audio/htlscns.ogg"
    show bg lanarunaaway 1 with Dissolve(0.8)
    Lana "Ah its too late he's touching my pussy already I got no excuse."
    show bg lanaelv 5 with Dissolve(0.8)
    Dennis "Lets unwrap you."
    show bg lanaelv 6 with Dissolve(0.8)
    Lana "Jesus you can'tbe-"
    show bg lanaelv 6 with Dissolve(0.8)
    Dennis "Shut up let me show you how much of a slut you are."
    show bg lanaelv 6 with Dissolve(0.8)
    Lana "What are you hey- ?"
    show bg lanaelv 8 with Dissolve(0.8)
    Dennis "Look at that face , those nipples and that pussy 10 minutes ago you didn't knew me and here I am spreading your holes."
    show bg lanaelv 8 with Dissolve(0.8)
    Lana "God he's right I let him do this after all, but I should talk."
    show bg lanaelv 8 with Dissolve(0.8)
    Lana "Hey look I just didn't expect you to go all the way , please let me go this package is urgent."
    show bg lanaelv 9 with Dissolve(0.8)
    Dennis "Alright then."
    show bg lanaelv 9 with Dissolve(0.8)
    Lana "What are you doing?"
    show bg lanaelv 10 with Dissolve(0.8)
    Dennis "We'll deliver this to your friend and then have fun."
    show bg lanaelv 10 with Dissolve(0.8)
    Lana "Hey wtf , my clothes!"
    show bg lanaelv 11 with Dissolve(0.8)
    Dennis "You won't be needing those tonight don't worry."
    show bg lanaelv 11 with Dissolve(0.8)
    Dennis "Mam room service your package has arrived!"
    show bg lanaelv 12 with Dissolve(0.8)
    Lana "Hey you can't be serious where ya taking me I thought you'd only touch abit not go this far"
    show bg lanasex 1 with Dissolve(0.8)
    Dennis "Well you're the one who let me strip you and either way you had your fun , now I'll have mine."
    show bg lanasex 1 with Dissolve(0.8)
    Lana "You can't just do this , I have a party to attend okay so can we talk about thi-"
    show bg lanasex 2 with Dissolve(0.8)
    Dennis "Up you go"
    show bg lanasex 2 with Dissolve(0.8)
    Lana "Hey what the!"
    show bg lanasex 3 with Dissolve(0.8)
    Lana "You can't just throw me around this way , if you're gonna do this at least be nice about it"
    show bg lanasex 4 with Dissolve(0.8)
    Dennis "I am being nice about it , take a look."
    show bg lanasex 4 with Dissolve(0.8)
    Lana "There's no way thing that is real"
    show bg lanasex 5 with Dissolve(0.8)
    Dennis "More than happy to confirm heh"
    show bg lanasex 5 with Dissolve(0.8)
    Lana "Oh my god its so big no way it'll fit in me... but its been a while I enjoyed sex...so mayb -"
    show bg lanasex 6 with Dissolve(0.8)
    Dennis "Get that ass over here."
    show bg lanasex 7 with Dissolve(0.8)
    Lana "Hey look we should um... talk?"
    show bg lanasex 8 with Dissolve(0.8)
    Dennis "Sorry babe gonna talk to this cute cunt of yours now."
    show bg lanasex 9 with Dissolve(0.8)
    Dennis "Damn look at this tight pussy , lets take a closer look."
    show bg lanasex 9 with Dissolve(0.8)
    Dennis "Nice and tight , but not a virgin figures I guess."

    Lana "You're one to judge."

    show bg lanasex 10 with Dissolve(0.8)
    Dennis "Lets taste and spread these holes."
    show bg lanasex 11 with Dissolve(0.8)
    Lana "*gasps* go a bit slow will ya"
    show bg lanasex 12 with Dissolve(0.8)
    Dennis "Man you are yummy"
    show bg lanasex 13 with Dissolve(0.8)
    Lana "Gosh please go slow I'm sensitive down there"
    show bg lanasex 14 with Dissolve(0.8)
    Dennis "I'll go harder then"
    show bg lanasex 15 with Dissolve(0.8)
    Lana "fuck... please stop."
    Dennis "This pussy says otherwise babe."
    show bg lanasex 15pt2 with Dissolve(0.8)
    Lana "*moaning* - please fuck hey... go slow."
    show bg lanasex 16 with Dissolve(0.8)
    Dennis "*licking * so good."
    Lana "AAahh... couldn't hold it"
    Lana "I um..."
    show bg lanasex 16 with Dissolve(0.8)
    Dennis "It's okay babe , not gonna lie by the way sex aside you got a pretty cute face if circumstances were different I'd ask you on a date heh."
    show bg lanasex 16 with Dissolve(0.8)
    Lana "Um... stop saying such things"
    show bg lanasex 18 with Dissolve(0.8)
    Lana "Hey where are you  going?..."
    show bg lanasex 19 with Dissolve(0.8)
    Lana "When I say stop I didn't mean literally."
    show bg lanasex 20 with Dissolve(0.8)
    Dennis "Your turn now babe."
    show bg lanasex 21 with Dissolve(0.8)
    Lana "Heh could've just told me to  lets see here."
    show bg lanasex 22 with Dissolve(0.8)
    Lana "*smooch* , you've got quite a good one not gonna lie."
    show bg lanasex 23 with Dissolve(0.8)
    Lana "*glurg* *lick*"
    show bg lanasex 24 with Dissolve(0.8)
    Dennis "Fuck you're good."
    show bg lanasex 25 with Dissolve(0.8)
    Lana "heh *Slurp* I know you guys love it when a gal does it."
    show bg lanasex 26 with Dissolve(0.8)
    Dennis "Fuck yes..."
    Lana "*glurg* mmm."
    show bg lanasex 27 with Dissolve(0.8)
    Dennis "ahh damn you're so good at this."
    show bg lanasex 28 with Dissolve(0.8)
    Lana "*Spit and slurp* hehe."
    show bg lanasex 29 with Dissolve(0.8)
    Dennis "*Moans out loud* Fuck baby you're amazing."
    show bg lanasex 30 with Dissolve(0.8)
    Lana "That was pretty good but time to taste the stick too now right?"
    show bg lanasex 31 with Dissolve(0.8)
    Dennis "All yours..."
    show bg lanasex 32 with Dissolve(0.8)
    Lana "Now that shame is out of corner lets enjoy ourselves."
    show bg lanasex 32pt2 with Dissolve(0.8)
    Dennis "Fuck yeah"
    show bg lanasex 33 with Dissolve(0.8)
    Lana "Heh this night surely went  better than I expected"
    show bg lanasex 34 with Dissolve(0.8)
    Dennis "Damn you're a good girl."
    show bg lanasex 34 with Dissolve(0.8)
    Lana "Then let me do the work and hands off ."
    show bg lanasex 35 with Dissolve(0.8)
    Dennis "As you say"
    show bg lanasex 36 with Dissolve(0.8)
    Lana "*glug* Best cock I've had in a while not gonna lie."
    Dennis "Heh thank you."

    Lana "So big and warm."
    show bg lanasex 37 with Dissolve(0.8)
    Lana "Your turn now hehe."
    show bg lanasex 38 with Dissolve(0.8)
    Dennis "Oh with pleasure"
    show bg lanasex 39 with Dissolve(0.8)
    Lana "Do me dirty will you?"
    Dennis "You know it."
    show bg lanasex 40 with Dissolve(0.8)
    Lana "Fuck you're so big..."
    show bg lanasex 42 with Dissolve(0.8)
    Dennis "Yes babe , you're hella tight too."
    show bg lanasex 43
    Lana "Fuck yea, fuck me , oh yes"
    scene bg lanasex 43
    Dennis "you're so good , you're so damn hot , holy fuck so tight."
    Dennis "Blondes are the best no lies"
    show bg lanasex 44 with Dissolve(0.8)
    Dennis "I can't wait anymore."
    scene
    show bg lanasex 45 with Dissolve(0.8)
    Lana "What ya planning now boy?"
    show bg lanasex 46 with Dissolve(0.8)
    Dennis "Spreading your other hole babe."
    show bg lanasex 47 with Dissolve(0.8)
    Lana "Go on..."
    show bg lanasex 48 with Dissolve(0.8)
    Lana "Oh fuck! That hurt but so good omg."
    Dennis "Hurts me too but I can't stop fuck."
    Lana "fuck me you bastard spread that ass, oh yes."
    Dennis "Damn baby you are tight"
    Dennis "Fuck I'm cumming"
    show bg lanasex 50 with Dissolve(0.8)
    Lana "Hey lets not waste it!"
    show bg lanasex 51 with Dissolve(0.8)
    Lana "mm gimme that hot stuff you fucker."
    show bg lanasex 52 with Dissolve(0.8)
    Dennis "*moans* fuck... I can't."
    show bg lanasex 53 with Dissolve(0.8)
    Lana "heh that was fun... very hot too lemme taste this."
    Lana "mm warm and tasty just how I like it."
    show bg lanasex 54 with Dissolve(0.8)
    Dennis "Oh god you are such a slut."
    show bg lanasex 55 with Dissolve(0.8)
    Lana "*giggles* Heh ditto my stud."
    Dennis "Guess you're right , well that was fun indeed."
    Dennis "You can stay tonight , tabs on me , that pussy was worth the entire hotel."
    show bg lanasex 56 with Dissolve(0.8)
    Lana "Thank you babe, it was nice indeed."
    show bg lanasex 57 with Dissolve(0.8)
    Lana "Kinda ironic how I was gonna bring kiara clothes and I'm the one naked... oh well hope your trip to japan is as fun as this was for me kiara <3."
    stop music



    jump roomsegment2

label Momandlawyer:
    #"" "Over atMason and veronica's."
    play music "/audio/lwscn.ogg"
    show bg mumlaw 1
    Mia  "Please take care, honey, and text me when you reach Japan, okay?"
    Kiaraonphone "Don't worry, mom, I'll keep you updated. Love you, okay?"
    Mia  "Love you too."
    show bg mumlaw 2 with Dissolve(0.8)
    Mason "Is she okay?... She's not had the easiest day."
    Mia  "She's a tough girl. I don't know how to thank you for arranging all this on short notice. I'm so sorry."
    show bg mumlaw 3 with Dissolve(0.8)
    Mason "Don't be silly, Mia, you're my friend. We go way back, okay? \nI care for you, and Kiara, both don' thank me for what you deserve."
    show bg mumlaw 4 with Dissolve(0.8)
    Mia  "It is just very rare, thanks, you're very sweet.... Let's perhaps talk about the other matter now?"
    show bg mumlaw 6 with Dissolve(0.8)
    Mason "Sure."
    show bg mumlaw 7 with Dissolve(0.8)
    Mia  "What are my options here, mason? I am done with this man and don't want him in my life anymore."
    show bg mumlaw 8 with Dissolve(0.8)
    Mason "Mia, I understand your emotional state right now, but we need to consider this legally too. In that context, the truth is that he was indeed drunk and intoxicated. It'll show in court, and then he has that defense."
    show bg mumlaw 9 with Dissolve(0.8)
    Mia  "So what do we do? You said there was a way."
    show bg mumlaw 9 with Dissolve(0.8)
    Mason "Yes, and there is. What we need to do now before even filing for divorce is to make sure all proof of him being drunk is gone so the forensic doctor who tests it, I'll take care of that, and also we'll need to erase footage or any proof of him being at the bar."
    show bg mumlaw 10 with Dissolve(0.8)
    Mia  "Okay, you said veronica could help with that, so that should be fine."
    show bg mumlaw 11 with Dissolve(0.8)
    Mason "As for the grounds that you assaulted him, we'll make those an exception in self-defense."
    Mia "I'm getting a headache..."
    show bg mumlaw 12 with Dissolve(0.8)
    Mason "Mia, Calm down. I'm here for you, okay? You're not alone."
    show bg mumlaw 13 with Dissolve(0.8)
    Mason "However, you do need to understand, Mia, we're taking a big risk here... you should've done this much earlier, and we could've found a smarter way to do it."
    show bg mumlaw 14 with Dissolve(0.8)
    Mia  "I'm sorry. What are the risks, then?"
    Mason "The risks are you may not get alimony or protection you need or custody of a child could be affected; however, Kiara isn't a minor, so that can be argued in court."
    Mia  "Not only have I wasted my life and risked the future, the property, and happiness I risk losing her too in one way...."
    show bg mumlaw 15 with Dissolve(0.8)
    Mason "Don't think that way. Try to see this as a new start, and you can have hope for the future."
    Mia  "Yeah... new life, of course. I got so much ahead of me, don't I, Mason?... Sorry, ima go."
    #loading a bit later...
    show bg mumlawyer 16 with Dissolve(0.8)
    Mia  "Mason is right in one way. I need to cheer myself up, or Kiara won't have any confidence either."
    show bg mumlawyer 17 with Dissolve(0.8)
    Mia  "I need a shower... this is just too much to handle ."
    show bg mumlawyer 18 with Dissolve(0.8)
    Mia  "Well, hot water should help..."
    show bg masonvero 1 with Dissolve(0.8)
    Mason "Mia deserves so much better. I hope she doesn't think it's the end."
    show bg masonvero 2 with Dissolve(0.8)
    Mason "Although john's going to come full force, I know what I have to do."
    show bg masonvero 3 with Dissolve(0.8)
    Mason "Hm? Vero? Probably It's serious. I'll awnser it."
    show bg masonvero 4 with Dissolve(0.8)
    Mason "Hey V ? what's up?"
    Veronica "Hey.... How is she?"
    show bg masonvero 5 with Dissolve(0.8)
    Mason "Well, not great, not terrible. We talked about the case, and she left upset."
    Veronica "Okay... what did you say?"
    show bg masonvero 6 with Dissolve(0.8)
    Mason "I told her life is still ahead for her, the lawsuit can be won, but she shouldn't be negative."
    Veronica "Are you stupid, mason? She's had such a rough life, and you're telling her to be positive?"
    show bg masonvero 7 with Dissolve(0.8)
    Veronica "So many people already despise her for trying to stay faithful to john, now she might lose her daughter too."
    Mason "Shit... didn't realize that... what do I do?"
    show bg masonvero 8 with Dissolve(0.8)
    Veronica "Go talk to her, you dummy!"
    Mason "I'm Going...."
    show bg mumlawyer 19 with Dissolve(0.8)
    Mason "{i}I was too stupid with my words to her. I should at least think first, dammit.{/i}"
    show bg mumlawyer 20 with Dissolve(0.8)
    Mason "Mia, are you here? She's-"
    show bg mumlawyer 21 with Dissolve(0.8)
    Mason "I see. In the bathroom, she needs some time alone. I understand to cry, I guess..."
    show bg mumlawyer 22 with Dissolve(0.8)
    Mason "What has life come to... why did you do this, john? You had everything, even Mia... the one person I never could have but always loved."
    Mason "I've always sucked so badly, couldn't confess on to her, can't make her happy now either, what a joke."
    show bg mumlawyer 23 with Dissolve(0.8)
    Mason "She hasn't responded. I hope she's not doing something stupid."
    show bg mumlawyer 24 with Dissolve(0.8)
    Mason "I should check... – wait? Is the door open? I guess then I can go in."
    stop music
    play music "/audio/swhrmsc.ogg"
    show bg mumlawyer 25 with Dissolve(0.8)
    "" "Mia due to stress had forgot to lock the door."
    show bg mumlawyer 26 with Dissolve(0.8)
    Mia "Ah if nothing else at least warm water helps to keep head clean."
    show bg mumlawyer 29 with Dissolve(0.8)
    Mason "Fuck... that's'... that's Mia, my god she looks maginificant..."
    show bg mumlawyer 30 with Dissolve(0.8)
    Mia "Damn you john... not only do I not get love emotionally but not phsyiscally either... you ruined so much."
    show bg mumlawyer 31 with Dissolve(0.8)
    Mia "I am so horny too... I should take care of this should help a little with stress."
    show bg mumlawyer 32 with Dissolve(0.8)
    Mia "Unf , it feels so wrong to masturbate in someone else's house, but I don't wanna stop... I wonder if Mason ever thought about me this way."
    show bg mumlawyer 33 with Dissolve(0.8)
    Mason "Is she really talking about me?"
    show bg mumlawyer 34 with Dissolve(0.8)
    Mia "Mmm… I want to get railed so bad..."
    show bg mumlawyer 35 with Dissolve(0.8)
    Mason "Fuck I'm getting hard... I – I can't stop I have to go... this is my only chance."
    show bg mumlawyer 36 with Dissolve(0.8)
    Mia "This is so wrong imagining another guy than my husband but I love it..."
    show bg mumlawyer 37 with Dissolve(0.8)
    Mia "God, I'm so wet."
    show bg mumlawyer 38 with Dissolve(0.8)
    Mia "Mmm... this is risky yet so exciting."
    show bg mumlawyer 39 with Dissolve(0.8)
    Mia "I want you badly m-"
    show bg mumlawyer 40 with Dissolve(0.8)
    Mason "Hi Mia..."
    show bg mumlawyer 41 with Dissolve(0.8)
    Mia "What I uh-"
    show bg mumlawyer 42 with Dissolve(0.8)
    Mia "Mason um, what are you-"
    Mason "I know you want this... let me help , I love you..."
    stop music
    play music "/audio/choicmusic.ogg"
    Mia "Love? What... is happening I should do something."
    menu:
        "Let it happen":
            #TODO add kiara corruption by 1
            $ mc_stats.adjust_corruption(1)
            call ACCEPTEDLAW from _call_ACCEPTEDLAW
        "No I can't do this":
            call REJECTEDLAW from _call_REJECTEDLAW
    jump Momspyscene

label ACCEPTEDLAW:
    stop music
    play music "/audio/mmsx.ogg"
    show bg mumlawyeraccpt 1 with Dissolve (0.8)
    Mia "Who am I fooling... I want this badly."
    show bg mumlawyeraccpt 2 with Dissolve (0.8)
    Mia "Do you love me?..."
    Mason "I know what this may seem to you, and I am sexually attracted, but believe me, I value you, I always have."
    show bg mumlawyeraccpt 3 with Dissolve (0.8)
    Mia "Shush... let me help. Let us enjoy this moment."
    show bg mumlawyeraccpt 4 with Dissolve (0.8)
    Mason "Oh god... this is happening."
    show bg mumlawyeraccpt 5 with Dissolve (0.8)
    Mason "The woman I’ve dreamt of being with is on her knees taking out my dick... wow."
    show bg mumlawyeraccpt 6 with Dissolve (0.8)
    Mason "Please don’t let this be  a dream... please."
    show bg mumlawyeraccpt 7 with Dissolve (0.8)
    Mia "Wow... you’re... big."
    show bg mumlawyeraccpt 8 with Dissolve (0.8)
    Mason " You think so?..."
    show bg mumlawyeraccpt 9 with Dissolve (0.8)
    Mia "Maybe I can make it bigger, huh?"
    show bg mumlawyeraccpt 10 with Dissolve (0.8)
    Mason "Mia, you're so adorable but hot."
    show bg mumlawyeraccpt 11 with Dissolve (0.8)
    Mia "*glug*"
    show bg mumlawyeraccpt 12 with Dissolve (0.8)
    Mason "Wow, her lips are so soft..."
    Mia "Sorry... you're very...kinda hurts."
    show bg mumlawyeraccpt 13 with Dissolve (0.8)
    Mia "*Smooch* thank you."
    show bg mumlawyeraccpt 14 with Dissolve (0.8)
    Mason "Mia, you look so pretty."
    show bg mumlawyeraccpt 14pt2 with Dissolve (0.8)
    Mia "Thank you. I needed this."
    show bg mumlawyeraccpt 15 with Dissolve (0.8)
    Mason "It's not over... stay still."
    Mia "I can't stop him... I love this."
    show bg mumlawyeraccpt 18 with Dissolve (0.8)
    Mason "His hands feel so good against my cheeks. Squeeze harder, Mason!"
    show bg mumlawyeraccpt 19 with Dissolve (0.8)
    Mason "Bend over Mia. I can't hold back anymore."
    Mia "Ah... um, are we?"
label Momspyscene:
    show bg mumlawyerspy 1 with Dissolve(0.8)
    ChrisInvestigator "Heh, Mason, see even the best of best lawyers slide when the pussy is there, can't blame you, brother. That is one hot babe. "
    show bg mumlawyerspy 2 with Dissolve(0.8)
    ChrisInvestigator "Mr.john will be pleased with these... shame he's a sly dog, had quite the babe to himself hah."
    stop music

    jump PLANESEGMENT
label REJECTEDLAW:
    stop music
    show bg mumlawyer rejctd1 with Dissolve(0.8)
    Mia "Mason!..., please wait... we can't do this...It's not you. It's me I just can't after tonight."

    Mason " I- I'm so sorry. I don't know what got in me... I've always liked you. I saw you stressed and... it just... I'm sorry."
    show bg mumlawyer rejctd2 with Dissolve(0.8)
    Mia "Hey, Hey, don't be sorry... you didn't do anything wrong I know you've liked me since uni. I just... I've had a rough night...I'm sorry."
    show bg mumlawyer rejctd3 with Dissolve(0.8)
    Mason "I promise I'll be here for you... you're more than just a friend to me."

    Mia "Oh Mason... I'm here for you too... maybe not now... but maybe a future we can have the ending we seek."
    show bg mumlawyer rejctd4 with Dissolve(0.8)
    "" "Mia and Maison merely leave it at a kiss."

    jump Momspyscene

label PLANESEGMENT:
    stop music
    "" "Back at the international airport..."
    show bg ontheplane 1 with Dissolve(0.8)
    "Plane Pilot" "This is your pilot with my lovely assistant Cassandra. The flight to Osaka will depart shortly. Please find your seats."
    play music "/audio/plnsc.ogg"
    show bg ontheplane 2 with Dissolve(0.8)
    Kiara "Okay, that takes care of the luggage... now, Kiara, act normal and don't be a clown... it's just one trip."
    show bg ontheplane 3 with Dissolve(0.8)
    Kiara "Um, excuse me, I can't find 712 ... is it the one next to you? I'm sorry for bothering you."
    show bg ontheplane 4 with Dissolve(0.8)
    Azumi "Please don't be sorry. Even if it weren't, I'd let you sit, but yes, this is 712. Feel free."
    show bg ontheplane 6 with Dissolve(0.8)
    Kiara "Thank you!"
    Azumi "You're welcome. I'm Azumi."
    show bg ontheplane 6pt2 with Dissolve(0.8)
    Kiara "I'm Kiara. Sorry, but I want to say your hair and outfit look immaculate."
    Azumi "You think so?... thank you."
    show bg ontheplane 7 with Dissolve(0.8)
    Azumi "Speaking of dress though... I must say you have unique taste indeed."
    show bg ontheplane 8 with Dissolve(0.8)
    Azumi "Not that I mind the view."
    show bg ontheplane 9 with Dissolve(0.8)
    Kiara "Oh haha, this ... I had a situation and had to borrow a dress, so... yeah."
    show bg ontheplane 10 with Dissolve(0.8)
    Azumi "Even tho she has a lovely body and that dress, I can't take my eyes off her pretty smile."
    show bg ontheplane 11 with Dissolve(0.8)
    Azumi "So japan, huh? How come? A trip?"
    Kiara "No, I'm actually moving there... can't say much but let us just say life has led me here."
    show bg ontheplane 12 with Dissolve(0.8)
    Azumi "Well, I'm thrilled to have such great company."
    Kiara "Likewise (Did she just flirt?... that was unexpected but cute)"
    show bg ontheplane 13 with Dissolve(0.8)
    Kiara "So what about you?"
    Azumi "Oh, I live there, I was here for a work trip. Where are you staying in Osaka?"
    Kiara "I am moving in with my aunt due to.... problems."
    Azumi "How about job and stuff then?"
    show bg ontheplane 14 with Dissolve(0.8)
    Kiara "Who knows... let's hope I find something."
    show bg ontheplane 15 with Dissolve(0.8)
    Azumi "Um... well, all the power to you, but if not, I work at a school. Perhaps we could arrange something. Call me?"
    Kiara "Thank you so much. I appreciate this."
    show bg ontheplane 16 with Dissolve(0.8)
    Azumi "Wel-...(She's so pure...)"
    show bg ontheplane 17 with Dissolve(0.8)
    Azumi "Most welcome. Now rest a little we've got a long flight ahead."
    stop music

    jump kiaraairport
