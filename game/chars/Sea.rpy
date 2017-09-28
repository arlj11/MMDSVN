define SeaMG = Character("Sea", who_color="#b1dffa", image="Sea")
define SeaMGS = MGStats(5, "Aloof", False, 0, 0, False, 10)
define SeaMGD = MGData.Lamia(Size=4, BSize=3)
$ SeaMGD.CanSwimLong = True

image Sea = "0001_Sea/0001_Full_A.png"
image Sea Happy = "0001_Sea/0001_Full_B.png"
image Sea HappyEC = "0001_Sea/0001_Full_C.png"
image Sea Embassed = "0001_Sea/0001_Full_D.png"
image Sea Sad = "0001_Sea/0001_Full_E.png"
image Sea Mad = "0001_Sea/0001_Full_F.png"
image Sea AffectionA = "0001_Sea/0001_Affection_A.jpg"

label SeaMain:

    show Sea

    if povName == 'Dev':
       Dev "[SeaMG] Stats: Met=[SeaMGS.Met], Mood=[SeaMGS.Mood], Affection=[SeaMGS.Affection], AffectionEvent=[SeaMGS.AffectionEvent], Patience=[SeaMGS.Patience]."
       Dev "[SeaMG] Data: Size=[SeaMGD.Size], BSize=[SeaMGD.BSize], HasHands=[SeaMGD.HasHands], HasWings=[SeaMGD.HasWings], HasLegs=[SeaMGD.HasLegs], HasTail=[SeaMGD.HasTail], HasScales=[SeaMGD.HasScales], HasGills=[SeaMGD.HasGills], CanSwim=[SeaMGD.CanSwimLong], CanFly=[SeaMGD.CanFly], IsColdB=[SeaMGD.IsColdB], CanWeb=[SeaMGD.CanWeb], CanShapeshift=[SeaMGD.CanShapeshift], IsUndead=[SeaMGD.IsUndead], IsPlant=[SeaMGD.IsPlant]."

    if SeaMGS.Met == False:
      jump .intro
    else:
      jump .MeetAgain

label .intro:

    show Sea

    "Before you is a woman with long blue hair and the lower body of serpent."
    SeaMG "Greetings. My name is Sea. What's yours?"
    pov "My name is [povName]."
    $ SeaMGS.Met = True

    menu:
      pov "You have a..."
      "Lovey Name.":
        SeaMG Happy "Thank you."
        $ SeaMGS.Mood += 1 
        $ SeaMGS.Affection += 1
      "Funny Name.":
        SeaMG Mad "Excuse Me."
        $ SeaMGS.Mood -= 1 
        $ SeaMGS.Affection -= 1
    
    call TalkTo(SeaMG, SeaMGS, SeaMGD, "Sea")

    return 

label .MeetAgain:
    
    if SeaMGS.Affection < 0:
        show Sea Mad
        SeaMG "Oh, You again."
    elif SeaMGS.Affection > 100 and SeaMGS.AffectionEvent == False and INLocation == "Beach":
      jump .AffectionEvent
    else:
        show Sea
        SeaMG "Hello there."

    call TalkTo(SeaMG, SeaMGS, SeaMGD, "Sea")

    return 

label .AffectionEvent:
    $ SeaMGS.AffectionEvent = True
    scene Sea AffectionA at top
    "She lays before you."

    return 
