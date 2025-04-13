from Buff import Buff

class Spell(Buff):
    def __init__(self, name="Placeholder", priority=99, FP=0, buffType="None", buffTime= 0.00, 
            isSorcery=True):
        super().__init__(name, priority, FP, buffType, buffTime)
        self.isSorcery = isSorcery

    def getIsSorcery(self):
        return self.isSorcery
    
    
    
    
