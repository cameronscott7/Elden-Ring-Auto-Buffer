from Buff import Buff

class Usable(Buff):
    def __init__(self, name="Placeholder", priority=99, FP=0, buffType="None", buffTime= 0.00, 
                 isWondFlask=True):
        super().__init__(name, priority, FP, buffType, buffTime)
        self.isWondFlask = isWondFlask

    def getIsWondFlask(self):
        return self.isWondFlask
    
    
    
    
