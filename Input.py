from BuffSelector import BuffSelector
import pydirectinput
import time

class Input:
    def __init__(self, player=None, weapons=[], ashesOfWar=[], usables=[], spells=[]):
        self.player = player
        self.weapons=weapons
        self.ashesOfWar = ashesOfWar
        self.usables = usables
        self.spells = spells
        self.leftHandIndex = 3
        self.rightHandIndex = 0
        self.usablesIndex = 0
        self.spellIndex = 0
        self.staffIndex = 0
        self.sealIndex = 0

    def applyBuffs(self):
        buffSel = BuffSelector(self.player)
        buffOrder = buffSel.findBuffOrderByPrio()

        if len(self.player.getSpells()) > 0:
            hasSpell = True

        if hasSpell:
            if "Staff" in self.weapons:
                self.staffIndex = self.weapons.index("Staff")
            else:
                self.sealIndex = self.weapons.index("Seal")

        for buff in buffOrder:
            if isinstance(buff, str):
                name = buff
            else:
                name = buff.getName()

            if name in self.ashesOfWar:
                index = self.ashesOfWar.index(name)
                type = "AshOfWar"
            elif name in self.usables:
                index = self.usables.index(name)
                type = "Usable"
            elif name in self.spells:
                index = self.spells.index(name)
                type = "Spell"
            else:
                index = -1
                type = "None"
                #Not Found

            self.inputBuff(index, buff, type)

    def inputBuff(self, buffIndex, buff, type):
        if type == "AshOfWar":
            if buff.getName() in self.weapons:
                buffIndex = self.weapons.index(buff)
            self.moveWeapon(buffIndex)
            self.applyAshOfWar(buff)
        elif type == "Usable":
            self.applyUsables(buffIndex, buff)
        elif type == "Spell":
            if (buff.isSorcery()):
                self.moveWeapon(self.staffIndex)
            else:
                self.moveWeapon(self.sealIndex)
            self.applySpell(buff)
        print("Buffs Complete")    
    
    def moveWeapon(self, buffIndex):
        if buffIndex < 3:
            self.moveLeftHand(buffIndex)
        else:
            self.moveRightHand(buffIndex)

    def moveLeftHand(self, buffIndex):
        while self.leftHandIndex != buffIndex:
            pydirectinput.mouseDown(button="left")
            pydirectinput.mouseUp(button="left")
            time.sleep(0.5)
            self.leftHandIndex += 1

    def moveRightHand(self, buffIndex):
        while self.rightHandIndex != buffIndex:
            pydirectinput.mouseDown(button="right")
            pydirectinput.mouseUp(button="right")
            time.sleep(0.5)
            self.rightHandIndex += 1
    
    def applyUsables(self, buffIndex, buff):
        while self.usablesIndex != buffIndex:
            pydirectinput.press("down")
            time.sleep(0.5)
            self.usablesIndex += 1
        pydirectinput.press("r")
        time.sleep(buff.getBuffTime())
    
    def applyAshOfWar(self, buff):
        pydirectinput.keyDown('shift')
        time.sleep(.5)
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(buff.getBuffTime())
        pydirectinput.keyUp('shift')
        time.sleep(0.5)

    def applySpell(self, buff):
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(buff.getBuffTime())
    


