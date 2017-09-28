define MGChance = renpy.random.randint(1, 10)
define distance = 0

image bg Beach = "Beach_Backgroud.jpg"
image bg Warehouse = "Warehouse_Background.jpg"

label Locations:

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
         jump Locations

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
       $ distance = 0
       jump Locations
     "Walk":
       if distance < 1:
         "It's nice out, and very spacious. Can't imagine anyone would mind a walk out here."
         $ distance += 1
         jump Park
       if distance < 2:
         "The sky is getting dark."
         $ distance += 1
         jump Park
       if distance < 3:
         "The path ends where it meets a road at the edge of the park."
         $ distance += 1
         jump Park
       menu:
        "You see a small warehouse. It's labeled \"Park Storage\" but it doesn't seem like someone has used it in a while."
        "Try to enter":
          $ MGChance = renpy.random.randint(1, 10)
          if MGChance < 11:
            "The door is surprisingly open."
            jump Warehouse
          "It's locked."
          jump Locations
        "Leave":
          jump Locations

return

label Warehouse:
    
    scene bg Warehouse with dissolve:
        subpixel True
        yalign 1.0
        linear 5.0 yalign 0.0
    "Inside the warehouse is empty save for some boxes stacked against a corner."
    "It hasn't been dusted out in a while, loose cobwebs are scattered about, some obscuring the moonlight from the windows."
    jump RachneraMain
    
return