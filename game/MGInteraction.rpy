define MGName = ""
define MGColor = ""
define MGImage = ""
define MGI = DynamicCharacter("MGName", color="MGColor", image="MGImage")
define MGIS = MGStats(5, "", False, 0, 0, False, 10)
define MGID = MGData(4, 3, False, False, False, False, False, False, False, False)

define INLocation = ""

label TalkTo(MGI="MGN", MGIS="MGS", MGID="MGD"):

  if MGIS.Patience < 1:
    MGI "I don't want to talk right now."
    jump Loactions
  else:
    MGI "What do you want to talk about?"
    menu:
       "Topics"
       "About you":
        jump AboutMG
       "About Me":
        jump AboutPov 
       "Date" if MGIS.Affection > 10:
        jump DateMG
       "Bye":
        MGI "Have fun."
        jump Loactions

return 

label AboutMG:
    menu:
       "What about her"
       "Compliment":
        jump ComplimentMG
       "Tease":
        jump TeaseMG 

return 

label AboutPov:

    if povName == 'Dev':
       Dev "PovCha=[PovCha], MGIS.Patience=[MGIS.Patience]."
    Dev "Work in progress."
    if PovCha < 20 or MGIS.Personality == "Aloof":
      $ MGIS.Patience -= 1
    call TalkTo(MGI, MGIS, MGID)

return 

label DateMG:
    menu:
       "Let's go for a swim" if INLocation == "Beach":
         if MGID.CanSwimLong == True:
           MGI Happy "I love swiming!"
           $ MGIS.Mood += 10
           $ MGIS.Affection += 10
    Dev "Work in progress."
    call TalkTo(MGI, MGIS, MGID)

return 

label ComplimentMG:
    menu:
       "On her Hair":
        jump HairComplimentMG
       "On her Scales" if MGID.HasScales == True:
        jump ScaleComplimentMG

return 

label HairComplimentMG:

    pov "I like your hair color"
    MGI "Thank you."
    $ MGIS.Affection += 10

    call TalkTo(MGI, MGIS, MGID)

return 

label ScaleComplimentMG:

    pov "I like your scale coloring"
    MGI "Thank you."
    $ MGIS.Affection += 10

    call TalkTo(MGI, MGIS, MGID)

return 

label TeaseMG:
    Dev "Work in progress."
    call TalkTo(MGI, MGIS, MGID)

return 
