from Buff import Buff

class AshOfWar(Buff):
    def __init__(self, name="Placeholder", priority=99, FP=0, damage=0, damageType="None", buffType="None", statusBuildup=0,
                  buffTime= 0.00, isRightHand=True, isOneHanded=True):
        super().__init__(name, priority, FP, damage, damageType, buffType, statusBuildup, buffTime)
        self.isRightHand = isRightHand
        self.isOneHanded = isOneHanded

    def getIsOneHanded(self):
        return self.isOneHanded
    