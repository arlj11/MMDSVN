init python:
    import renpy.store as store
    
    class MGStats(store.object):
        def __init__(self, Chance, Personality, Met, Mood, Affection, AffectionEvent, Patience):
            self.Chance = Chance
            self.Personality = Personality
            self.Met = Met
            self.Mood = Mood
            self.Affection = Affection
            self.AffectionEvent = AffectionEvent
            self.Patience = Patience
    
    # Make sure to add any new arguments for new species to the instances where MGData is called in MGInteraction.rpy and PovData.rpy
    class MGData(store.object):
        def __init__(self, Size, BSize, HasHands, HasWings, HasLegs, HasTail, HasScales, CanSwimLong, CanFly, IsColdB, CanWeb):
            self.Size = Size  #0 = Diminutive, 1 = Tiny, 2 = Small, 3 = Meduim, 4 = Large, 5 = Extra-Large
            self.BSize = BSize #1 = A Cup etc.
            self.HasHands = bool(HasHands)
            self.HasWings = bool(HasWings)
            self.HasLegs = bool(HasLegs)
            self.HasTail = bool(HasTail)
            self.HasScales = bool(HasScales)
            self.CanSwimLong = bool(CanSwimLong)
            self.CanFly = bool(CanFly)
            self.IsColdB = bool(IsColdB)
            self.CanWeb = bool(CanWeb)
        
        # Creating a Species Preset:
        #
        # @staticmethod
        # def Species(Special Arguments)
        #     return MGData(Size, BSize, HasHands, HasWings, HasLegs, HasTail, HasScales, CanSwimLong, CanFly, IsColdB, CanWeb)
        
        @staticmethod
        def Lamia(Size, BSize):
            return MGData(Size, BSize, True, False, False, True, True, True, False, True, False)
        
        @staticmethod
        def Arachne(Size, BSize):
            return MGData(Size, BSize, True, False, True, False, False, False, False, False, True)
            
        @staticmethod
        def Centaur(Size, BSize):
            return MGData(Size, BSize, True, False, True, True, False, False, False, False, False)
            
        @staticmethod
        def Harpy(Size, BSize):
            return MGData(Size, BSize, False, True, True, False, False, False, True, False, False)
            
        @staticmethod
        def Slime(Size, BSize):
            return MGData(Size, BSize, True, False, True, False, False, False, False, False, False)
            
        @staticmethod
        def Mermaid(Size, BSize):
            return MGData(Size, BSize, True, False, False, True, False, True, False, False, False)
            
        @staticmethod
        def Monoeye(Size, BSize):
            return MGData(Size, BSize, True, False, True, False, False, False, False, False, False)
            
        @staticmethod
        def Ogre(Size, BSize):
            return MGData(Size, BSize, True, False, True, False, False, False, False, False, False)
            
        @staticmethod
        def Zombie(Size, BSize):
            return MGData(Size, BSize, True, False, True, False, False, False, False, False, False)
