from Buff import Buff

class Spell(Buff):
    def __init__(self, name="Placeholder", priority=99, FP=0, damage=0, damageType="None", buffType="None", statusBuildup=0,
                  buffTime= 0.00, isRightHand=True, isSorcery=True):
        super().__init__(name, priority, FP, damage, damageType, buffType, statusBuildup, buffTime)
        self.isRightHand = isRightHand
        self.isSorcery = isSorcery

    def getIsSorcery(self):
        return self.isSorcery
    
    
    
    
