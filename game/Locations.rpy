define MGChance = renpy.random.randint(1, 10)

image bg Beach = "Beach_Backgroud.jpg"

label Loactions:

    scene bg map with dissolve

    menu:
     "Where to?"
     "Beach":
         jump Beach
     "Park":
         jump Park

    return

label Beach:

    scene bg Beach with dissolve
    
    if FindDateLocation == True:
        $ DateLocation = "Beach"
        $ FindDateLocation = False
        jump DateMG

    $ INLocation = "Beach"
    $ DateLocation = INLocation

    menu:
     "What do you want to do?"
     "Look around":
       $ MGChance = renpy.random.randint(1, 10)
       if MGChance < SeaMGS.Chance:
         "You see a woman near surf."
         jump SeaMain
       else:
         "Nobody is here."
         jump Loactions

return

label Park:

    scene bg Park with dissolve
    if FindDateLocation == True:
        $ DateLocation = "Park"
        $ FindDateLocation = False
        jump DateMG

    $ INLocation = "Park"
    $ DateLocation = INLocation

    menu:
     "What do you want to do?"
     "Look around":
        "Nobody is here."
        jump Loactions

return
