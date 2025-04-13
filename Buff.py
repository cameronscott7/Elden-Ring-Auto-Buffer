class Buff:
    def __init__(self, name="Placeholder", priority=99, FP=0, buffType="None", buffTime=0.00):
        #Buff Types: Weapon, Shield, Body, Aura, Health Regen, Stamina Regen, Fall Damage, Dodge Roll, Unique
        self.name = name
        self.priority=priority
        self.FP = FP
        self.buffType = buffType
        self.buffTime = buffTime
    
    def getName(self):
        return self.name
    
    def getPriority(self):
        return self.priority

    def getFP(self):
        return self.FP

    def getBuffType(self):
        return self.buffType
    
    def getBuffTime(self):
        return self.buffTime
    
    
    
