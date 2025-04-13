from BuffSelector import BuffSelector
import pydirectinput
import time

class Input:
    def __init__(self, player=None, usables=[]):
        self.player = player
        self.usables = usables
        self.leftHandIndex = 3
        self.rightHandIndex = 0
        self.usablesIndex = 0
        self.spellIndex = 0
        self.staffIndex = 0
        self.sealIndex = 0

    def applyBuffs(self):
        time.sleep(10)
        print("Applying Buffs")

        buffSel = BuffSelector(self.player)
        buffOrder = buffSel.findBuffOrderByPrio()

        print("Sorted:", buffSel.findBuffOrderByPrio())

        if len(self.player.getSpells()) > 0:
            hasSpell = True

        if hasSpell:
            if "Staff" in self.weapons:
                self.staffIndex = self.weapons.index("Staff")
            else:
                self.sealIndex = self.weapons.index("Seal")

        for buff in buffOrder:

            if buff in self.player.getAshesOfWar():
                index = self.player.getAshesOfWar().index(buff)
                type = "AshOfWar"
            elif buff in self.player.getUsables():
                index = self.player.getUsables().index(buff)
                type = "Usable"
            elif buff in self.player.getSpells():
                index = self.player.getSpells().index(buff)
                type = "Spell"
            else:
                index = -1
                type = "None"
                #Not Found

            self.inputBuff(index, buff, type)

    def inputBuff(self, buffIndex, buff, type):
        if type == "AshOfWar":
            if buff.getName() in self.player.getWeapons():
                buffIndex = self.player.getWeapons().index(buff.getName())
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
        if buffIndex < self.player.getNumRightHandWeapons():
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
        pydirectinput.keyDown('e')
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(0.5)
        pydirectinput.keyUp('e')
        time.sleep(0.5)
        pydirectinput.keyDown('shift')
        time.sleep(.5)
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(buff.getBuffTime())
        pydirectinput.keyUp('shift')
        time.sleep(0.5)
        pydirectinput.keyDown('e')
        pydirectinput.mouseDown(button="left")
        pydirectinput.mouseUp(button="left")
        time.sleep(0.5)
        pydirectinput.keyUp('e')
        time.sleep(0.5)

    def applySpell(self, buff):
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(buff.getBuffTime())
    


