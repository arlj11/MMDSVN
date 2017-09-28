## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define povFirstName = ""
define povLastName = ""
define povName = "Dev"             # povName = povFirstName + povLastName
define pov = DynamicCharacter("povName")

define Smith = Character('Ms. Smith')
define Myuu = Character('Myuu', image="Myuu")
define Dev = Character('Dev', color="#ff0000", what_prefix='(', what_suffix=')')

image Smith = Image("Smith.png", yalign= .1)
image Myuu = "0000_Full_A.png"
image Myuu Happy = "0000_Full_B.png"
image Myuu Awkward = "0000_Full_C.png"

image Riado = "Riado.png"
image Rudoru = "Rudoru.png"
image Elder = "Elder_full.png"

## The game starts here.

label start:

  scene bg room
  
  if povName == 'Dev':
    jump Locations
  else:
    "Welcome to the world of Monsters Musume Dating."
    if povName == '':
        "Please enter your name."
        if not renpy.variant('touch'):
            $ povFirstName = renpy.input("What is your first name?", length=16) or "Kimihito"
            $ povLastName = renpy.input("What is your last name?", length=16) or "Kurusu"

        elif renpy.variant('touch'):
            info "What is your first name? (leave blank for 'Kimihito')"
            $ input_header = 'First name:'
            call inputter
            $ povFirstName = input_text or "Kimihito"
            info "What is your last name? (leave blank for 'Kurusu')"
            $ input_header = 'Last name:'
            $ text_group = 1
            $ input_text = ''
            call inputter
            $ povLastName = input_text or "K"

        else:
            $ povFirstName = "Kimihito"
            $ povLastName = "Kurusu"
        
        $ povName = povFirstName



    show Smith

    "If you know the genral story of Monsters Musume, then she needs no introduction."
    
    menu:
     "Do you know her?"

     "Yes.":
         "Good we can get this thing started."
         jump Begin

     "No.":
         "Then I'm going to give you a quick run down."
         jump MGExplained


    return

label MGExplained:

    scene bg room with dissolve
    "In the world of Monster Musume A.K.A \"Everyday life with Monster Girls\", Mosterous humandoids are real. The goverments were just hiding it from people."
    "The goverments deiced it to revel this and start an exchange program to help integrate them."
    "What is a moster girl?"
    show Myuu with dissolve
    "This is a monster girl."
    "Note her diffences from normal humans."
    show Myuu Happy
    "She has horns and some scale on her cheeks."
    "She also has a great tail."
    show Myuu Awkward
    "I mean literality dear."
    show Myuu
    "So you see their not that much diffenet from other people."
    hide Myuu with dissolve
    show Riado at left
    show Elder
    show Rudoru at right
    with dissolve
    "They can vary greatly to."
    hide Riado
    hide Elder
    hide Rudoru
    with dissolve
    show Myuu with dissolve
    "The laws at first limited the interaction with the two groups. But after awaile they deiced to futher the integrations by interducing relationships into the mix."
    "Thus you are free to date and woo them."
    pov "May I date her?"
    show Myuu Awkward
    "Sorry not at this time."
    Dev "Need more images"

label Begin:

    scene bg room with dissolve

    "Now there are many Monster girls in this game."
    Dev "Going to try to implement them all"
    "You fist have to meet them then earn their affection in order to date and woo them."
    "This will be easy for some girls. But harder for others."
    Dev "Going to use the rarity system as the bases of how challenging they will be."
    "You won't see all the girls. You will need to unlock them with special requirements."
    Dev "Will make a NPC to give tips and tricks in game."
    jump Locations
    return
