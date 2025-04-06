class Buff:
    def __init__(self, name="Placeholder", priority=99, FP=0, damage=0, damageType="None", buffType="None", statusBuildup=0,
                 buffTime=0.00):
        #Buff Types: Weapon, Shield, Body, Aura, Health Regen, Stamina Regen, Fall Damage, Dodge Roll, Unique
        self.name = name
        self.priority=priority
        self.FP = FP
        self.damage = damage
        self.damageType = damageType
        self.buffType = buffType
        self.statusBuildup = statusBuildup
        self.buffTime = buffTime
    
    def getName(self):
        return self.name
    
    def getPriority(self):
        return self.priority

    def getFP(self):
        return self.FP

    def getDamage(self):
        return self.damage

    def getDamageType(self):
        return self.damageType

    def getBuffType(self):
        return self.buffType

    def getStatusBuildup(self):
        return self.statusBuildup
    
    def getBuffTime(self):
        return self.buffTime
    
    
    
