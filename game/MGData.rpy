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

    class MGData(store.object):
        def __init__(self, Size, BSize, HasHands, HasWings, HasLegs, HasTail, HasScales, CanSwimLong, CanFly, IsColdB):
            self.Size = Size  #0 = Diminutive, 1 = Tiny, 2 = Small, 3 = Meduim, 4 = Large, 5 = Extra-Large
            self.BSize = BSize 
            self.HasHands = bool(HasHands)
            self.HasWings = bool(HasWings)
            self.HasLegs = bool(HasLegs)
            self.HasTail = bool(HasTail)
            self.HasScales = bool(HasScales)
            self.CanSwimLong = bool(CanSwimLong)
            self.CanFly = bool(CanFly)
            self.IsColdB = bool(IsColdB)
