from Buff import Buff

class AshOfWar(Buff):
    def __init__(self, name="Placeholder", priority=99, FP=0, buffType="None", buffTime= 0.00):
        super().__init__(name, priority, FP, buffType, buffTime)