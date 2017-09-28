define MGName = ""
define MGColor = ""
define MGImage = ""
define MGI = DynamicCharacter("MGName", color="MGColor", image="MGImage")
define MGIS = MGStats(5, "", False, 0, 0, False, 10)
define MGID = MGData(4, 3, False, False, False, False, False, False, False, False, False, False, False, False, False)
define ref = ""

define INLocation = ""
define DateLocation = ""
define FindDateLocation = False

label TalkTo(MGI="MGN", MGIS="MGS", MGID="MGD", reference):
  $ ref = reference
  if MGIS.Patience < 1:
    MGI Mad "I don't want to talk right now."
    jump Locations
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
        jump Locations

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
    call TalkTo(MGI, MGIS, MGID, ref)

return 

label DateMG:

    $ MGD = MGI
    $ MGDS = MGIS
    $ MGDD = MGID
    $ renpy.show(ref) # $ renpy.show() will show whatever image name you pass. It can be passed in the form of a variable containing a string.
    if povName == 'Dev':
       Dev "DateLocation=[DateLocation], FindDateLocation=[FindDateLocation]"
    menu:
       "Let's go for a swim" if DateLocation == "Beach":
         if MGDD.CanSwimLong == True:
           MGD Happy "I love swiming!"
           $ MGDS.Mood += 10
           $ MGDS.Affection += 10
       "Let's go for a walk" if DateLocation == "Park":
           $ MGDS.Mood += 5
           $ MGDS.Affection += 5
       "Let's go Someplace else":
         $ FindDateLocation = True
         jump Locations
    Dev "Work in progress."
    call TalkTo(MGD, MGDS, MGDD, ref)

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

    call TalkTo(MGI, MGIS, MGID, ref)

return 

label ScaleComplimentMG:

    pov "I like your scale coloring"
    MGI "Thank you."
    $ MGIS.Affection += 10

    call TalkTo(MGI, MGIS, MGID, ref)

return 

label TeaseMG:
    Dev "Work in progress."
    call TalkTo(MGI, MGIS, MGID, ref)

return 
