class Player:
    def __init__(self, FP=0, health=0, weapons=[], usables=[]):
        self.FP = FP
        self.health = health
        self.weapons = weapons
        self.usables = usables

    def getFP(self):
        return self.FP
    
    def getHealth(self):
        return self.health
    
    def getWeapons(self):
        return self.weapons
    def getUsables(self):
        return self.usables


    
