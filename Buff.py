
#break class into a weapons buff, and a usable buff classes, (top 10 boxes and lower 10 boxes)
#need variable for if weapon is one handed or two handed (one or two weapons)
#also need times it takes to do buff.
class Buff:
    def __init__(self, name="Placeholder", FP=0, damage=0, damageType="None", buffType="None", statusBuildup=0):
        #Buff Types: Weapon, Shield, Body, Aura, Health Regen, Stamina Regen, Fall Damage, Dodge Roll, Unique
        self.name = name
        self.FP = FP
        self.damage = damage
        self.damageType = damageType
        self.buffType = buffType
        self.statusBuildup = statusBuildup
    
    def get_name(self):
        return self.name

    def get_FP(self):
        return self.FP

    def get_damage(self):
        return self.damage

    def get_damageType(self):
        return self.damageType

    def get_buffType(self):
        return self.buffType

    def get_statusBuildup(self):
        return self.statusBuildup
    
    
    
