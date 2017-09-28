define RachneraMG = Character("Rachnera", who_color="e6e6fa", image="Rachnera")
define RachneraMGS = MGStats(3, "Reserved", False, 0, 0, False, 2)
define RachneraMGD = MGData.Arachne(Size=4, BSize=8)

image Rachnera = "0070_Rachnera/0070_Full_A.png"
#TODO Other Images

label RachneraMain:
    
    if povName == 'Dev':
       Dev "[RachneraMG] Stats: Met=[RachneraMGS.Met], Mood=[RachneraMGS.Mood], Affection=[RachneraMGS.Affection], AffectionEvent=[RachneraMGS.AffectionEvent], Patience=[RachneraMGS.Patience]."
       Dev "[RachneraMG] Data: Size=[RachneraMGD.Size], BSize=[RachneraMGD.BSize], HasHands=[RachneraMGD.HasHands], HasWings=[RachneraMGD.HasWings], HasLegs=[RachneraMGD.HasLegs], HasTail=[RachneraMGD.HasTail], HasScales=[RachneraMGD.HasScales], HasGills=[RachneraMGD.HasGills], HasMagic=[RachneraMGD.HasMagic], CanSwim=[RachneraMGD.CanSwimLong], CanFly=[RachneraMGD.CanFly], IsColdB=[RachneraMGD.IsColdB], CanWeb=[RachneraMGD.CanWeb], CanShapeshift=[RachneraMGD.CanShapeshift], IsUndead=[RachneraMGD.IsUndead], IsPlant=[RachneraMGD.IsPlant]."

    if RachneraMGS.Met == False:
        jump .intro
    else:
        jump .MeetAgain

label .intro:
    
    show Rachnera with dissolve:
        subpixel True
        zoom 3.0
        yalign 1.0
        linear 10.0 yalign 0.6
    "Someone appears out of nowhere, walking on eight long and rigid legs."
    show Rachnera with dissolve:
        subpixel True
        zoom 3.0
        yalign 0.6
        linear 10.0 yalign 0.5 xalign 0.3
    "The legs all meet at the body of an enormous spider. The smooth chitin shimmers purple in the moonlight."
    show Rachnera with dissolve:
        subpixel True
        zoom 4.0
        yalign 0.3
        xalign 0.8
        linear 10.0 yalign 0.0
    "Soft, pale skin forms above her clothed hips, it continues up her body forming a slender waist."
    "A white shirt alone conceals her large beautiful breasts, but is lazily only half-buttoned, revealing her midriff and collar."
    "Her face has six eyes, lavender hair, and is smiling softly at you."
    RachneraMG "I don't believe I've ever had a visitor."
    hide Rachnera with dissolve
    show Rachnera:
        subpixel True
        zoom 1.0
        yalign 0.0
        xalign 0.0
    menu:
        RachneraMG "You are seem quite interested in my form. Do you find it frightening?"
        "Actually, you're rather attractive.":
            menu:
                RachneraMG "Ahahaha~! Attractive? How, exactly? And do be honest, I'm curious what would attract you to an Arachne."
                "Well, your um, your breasts are very alluring.":
                    "She appears dissapointed. But returns to her soft smile, and cups a breast with her hand."
                    RachneraMG "I see, it's my human features that arouse you."
                    $ RachneraMGS.Mood -= 1
                    $ RachneraMGS.Patience -= 1
                    $ RachneraMGS.Affection += 2
                "I like your hair.":
                    "She brushes it aside with her hand."
                    RachneraMG "Oh? Thank you, I don't even do anything to it."
                    $ RachneraMGS.Mood += 1
                    $ RachneraMGS.Affection += 1
                "Your eyes are really cute.":
                    "She turns red and responds louder in surprise."
                    RachneraMG "My eyes? Oh, well, thank you."
                    $ RachneraMGS.Mood += 1
                    $ RachneraMGS.Affection += 2
                "It's embarassing, but I kind of like your legs.":
                    "Her smile widens."
                    RachneraMG "Well aren't you kinky. I like that."
                    $ RachneraMGS.Mood += 5
                    $ RachneraMGS.Affection += 5
                "You have a sort of commanding attitude. It's charming.":
                    "Her smile widens."
                    RachneraMG "I appreciate your honesty, it's a pleasure to meet you."
                    $ RachneraMGS.Mood += 1
                    $ RachneraMGS.Affection += 5
                    $ RachneraMGS.Patience += 5
        "Perhaps a little...":
            menu:
                # Mad
                RachneraMG "Then run, I won't stop you."
                "Run":
                    $ RachneraMGS.Mood -= 5
                    $ RachneraMGS.Patience -= 2
                    $ RachneraMGS.Affection -= 5
                    jump Locations
                "Stay":
                    pov "No. I don't mind."
                    #Happy
                    RachneraMG "Well I apprecitate you being honest with me then."
                    $ RachneraMGS.Mood += 1
                    $ RachneraMGS.Affection += 2
                    $ RachneraMGS.Patience += 2
    RachneraMG "My name is Rachnera Arachnera, and I am an Arachne."
    pov "My name is [povName]"
    call TalkTo(RachneraMG, RachneraMGS, RachneraMGD, "Rachnera")
        
    return
        
label .MeetAgain:
    
    if RacheraMGS.Affection < 0:
        #Mad
        RachneraMG "Oh. You're back."
    elif RacheraMGS.Affection > 100 and RachneraMGS.AffectionEvent == False and INLocation == "Warehouse":
        RachneraMG "There you are, Honey. I've been waiting for you."
    else:
        show Rachnera
        RachneraMG "What brings you back here?"
        
    call TalkTo(RachneraMG, RachneraMGS, RachneraMGD, "Rachnera")
    
    return
