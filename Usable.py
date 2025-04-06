from Buff import Buff

class Usable(Buff):
    def __init__(self, name="Placeholder", priority=99, FP=0, damage=0, damageType="None", buffType="None", statusBuildup=0,
                  buffTime= 0.00, isWondFlask=True):
        super().__init__(name, priority, FP, damage, damageType, buffType, statusBuildup, buffTime)
        self.isWondFlask = isWondFlask

    def getIsWondFlask(self):
        return self.isWondFlask
    
    
    
    
