class BuffSelector:
    def __init__(self, player=None):
        self.player = player
    
    def removeDuplicates(self):
        buffs = self.player.getAshesOfWar() + self.player.getSpells() + self.player.getUsables()
        unique_buffs = []  # Stores buffs without duplicates

        for buff in buffs:
            found = False
            for existing in unique_buffs:
                if buff.getBuffType() == existing.getBuffType():
                    # Keep the one with the highest priority
                    if buff.getPriority() > existing.getPriority():
                        unique_buffs.remove(existing)
                        unique_buffs.append(buff)
                    found = True
                    break
            if not found:
                unique_buffs.append(buff)

        return unique_buffs

    #IS WRONG AND NEEDS TO BE FIXED
    def findBuffOrderByNumber(self):
        allBuffs = self.removeDuplicates()
        buffOrder = []
        sortedBuffs = sorted(allBuffs, key=lambda buff: buff.priority)  # Highest priority first

        i = 0
        while i < len(sortedBuffs):
            buff = sortedBuffs[i]

            # If enough FP is available, apply the highest-priority buff
            if buff.getFP() <= self.player.getFP():
                buffOrder.append(buff)
                self.player.setFP(self.player.getFP() - buff.getFP())
                i += 1  # Move to the next buff
                continue

            # Try to use as many lower-cost buffs as possible before consuming a flask
            applied_lower_cost_buff = False
            for j in range(i + 1, len(sortedBuffs)):  # Look ahead for any buffs that can be used
                if sortedBuffs[j].getFP() <= self.player.getFP():
                    buffOrder.append(sortedBuffs[j])
                    self.player.setFP(self.player.getFP() - sortedBuffs[j].getFP())
                    applied_lower_cost_buff = True  # Mark that we applied at least one lower-cost buff
            
            # If no other buffs could be applied, then consume a flask to apply the highest-priority buff
            if not applied_lower_cost_buff:
                if self.player.getNumFPFlasks() > 0:
                    self.player.setNumFPFlasks(self.player.getNumFPFlasks() - 1)
                    self.player.setFP(self.player.getFP() + self.player.getFPRestoreAmount())
                else:
                    break  # No flasks left, stop attempting buffs

        return buffOrder
    
    def findBuffOrderByPrio(self):
        allBuffs = self.removeDuplicates()
        buffOrder = []
        sortedBuffs = sorted(allBuffs, key=lambda buff: buff.priority)  # Highest priority first

        i = 0
        while i < len(sortedBuffs):
            buff = sortedBuffs[i]

            # If enough FP is available, apply the highest-priority buff
            if buff.getFP() <= self.player.getFP():
                buffOrder.append(buff)
                self.player.setFP(self.player.getFP() - buff.getFP())
                i += 1  # Move to the next buff

            elif buff.getFP() <= self.player.getMaxFP():
                # Use flask if available
                if self.player.getNumFPFlasks() > 0:
                    self.player.setNumFPFlasks(self.player.getNumFPFlasks() - 1)
                    self.player.setFP(self.player.getFP() + self.player.getFPRestoreAmount())
                    # Don't increment i — retry this buff with the new FP
                else:
                    # Can't use flask, move on
                    i += 1
            else:
                # Buff requires more FP than max FP — skip it
                i += 1

        return buffOrder

