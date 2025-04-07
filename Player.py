class Player:
    #consider using hashmap instead of array
    def __init__(self, FP=0, maxFP=0, health=0, numFPFlasks=0, flaskLevel=0, weapons=[], ashesOfWar=[],
                 spells=[], usables=[]):
        self.FP = FP
        self.maxFP = maxFP
        self.health = health
        self.numFPFlasks = numFPFlasks
        self.flaskLevel = flaskLevel
        self.weapons = weapons
        self.ashesOfWar = ashesOfWar
        self.spells = spells
        self.usables = usables

    def getFP(self):
        return self.FP
    
    def getMaxFP(self):
        return self.maxFP
    
    def getHealth(self):
        return self.health
    
    def getNumFPFlasks(self):
        return self.numFPFlasks
    
    def getFlaskLevel(self):
        return self.flaskLevel
    
    def getFPRestoreAmount(self):
        if self.flaskLevel == 0:
            return 80
        elif self.flaskLevel == 1:
            return 95
        elif self.flaskLevel == 2:
            return 110
        elif self.flaskLevel == 3:
            return 125
        elif self.flaskLevel == 4:
            return 140
        elif self.flaskLevel == 5:
            return 150
        elif self.flaskLevel == 6:
            return 160
        elif self.flaskLevel == 7:
            return 170
        elif self.flaskLevel == 8:
            return 180
        elif self.flaskLevel == 9:
            return 190
        elif self.flaskLevel == 10:
            return 200
        elif self.flaskLevel == 11:
            return 210
        else:
            return 220
    
    def getWeapons(self):
        return self.weapons
    
    def getAshesOfWar(self):
        return self.ashesOfWar
    
    def getSpells(self):
        return self.spells
    
    def getUsables(self):
        return self.usables
    
    def setFP(self, FP):
        if (FP < self.maxFP):
            self.FP = FP
        else:
            self.FP = self.maxFP

    def setNumFPFlasks(self, numFPFlasks):
        self.numFPFlasks = numFPFlasks