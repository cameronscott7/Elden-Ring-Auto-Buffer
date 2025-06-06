from BuffSelector import BuffSelector
import pydirectinput
import time
from Spell import Spell

class Input:
    def __init__(self, player=None, usables=[]):
        self.player = player
        self.usables = usables
        self.leftHandIndex = player.getNumRightHandWeapons()
        self.rightHandIndex = 0
        self.usablesIndex = 0
        self.spellIndex = 0
        self.staffIndex = 0
        self.sealIndex = 0

    def applyBuffs(self):
        print("Applying Buffs")

        fpFlaskIndex = next((i for i, obj in enumerate(self.usables) if obj.name == "FP Flask"), -1)
        print("FP Flask Index:", fpFlaskIndex)

        buffSel = BuffSelector(self.player, self.usables[fpFlaskIndex])
        buffOrder = buffSel.findBuffOrderByPrio()

        time.sleep(5)

        print("Sorted:", buffOrder)

        if len(self.player.getSpells()) > 0:
            hasSpell = True

        if hasSpell:
            print("Weapons", self.player.getWeapons())
            if "Staff" in self.player.getWeapons():
                self.staffIndex = self.player.getWeapons().index("Staff")
            if "Seal" in self.player.getWeapons():
                self.sealIndex = self.player.getWeapons().index("Seal")

        for buff in buffOrder:
            if buff in self.player.getAshesOfWar():
                index = self.player.getAshesOfWar().index(buff)
                type = "AshOfWar"
            elif buff in self.usables:
                print("Usables:", self.usables)
                index = self.usables.index(buff)
                type = "Usable"
            elif buff in self.player.getSpells():
                index = self.player.getSpells().index(buff)
                type = "Spell"
            else:
                index = -1
                type = "None"
                #Not Found

            self.inputBuff(index, buff, type)

        print("Buffs Complete")   

    def inputBuff(self, buffIndex, buff, type):
        if type == "AshOfWar":
            if buff.getName() in self.player.getWeapons():
                buffIndex = self.player.getWeapons().index(buff.getName())
            if buffIndex < self.player.getNumRightHandWeapons():
                self.moveRightHand(buffIndex)
                self.applyRightHandAshOfWar(buff)
            else:
                self.moveLeftHand(buffIndex)
                self.applyLeftHandAshOfWar(buff)
        elif type == "Usable":
            self.applyUsables(buffIndex, buff)
        elif type == "Spell":
            if (buff.getIsSorcery()):
                moveIndex = self.staffIndex
            else:
                print("Seal Index:", self.sealIndex)
                moveIndex = self.sealIndex
            if moveIndex < self.player.getNumRightHandWeapons():
                self.moveRightHand(moveIndex)
                self.moveSpell(buffIndex)
                self.applyRightSpell(buff)
            else:
                self.moveLeftHand(moveIndex)
                self.moveSpell(buffIndex)
                self.applyLeftSpell(buff)

    def moveLeftHand(self, buffIndex):
        while self.leftHandIndex != buffIndex:
            pydirectinput.press("left")
            time.sleep(0.5)
            if (self.leftHandIndex < len(self.player.getWeapons()) - 1):
                self.leftHandIndex += 1
            else: 
                self.leftHandIndex = self.player.getNumRightHandWeapons()

    def moveRightHand(self, buffIndex):
        while self.rightHandIndex != buffIndex:
            pydirectinput.press("right")
            print("Right Hand Index:", self.rightHandIndex)
            print("Buff Index:", buffIndex)
            time.sleep(0.5)
            if (self.rightHandIndex < self.player.getNumRightHandWeapons() - 1):
                self.rightHandIndex += 1
            else: 
                self.rightHandIndex = 0
            
    
    #TODO
    #Need to check if if index goes above size of usables
    def applyUsables(self, buffIndex, buff):
        while self.usablesIndex != buffIndex:
            pydirectinput.press("down")
            time.sleep(0.5)
            if (self.usablesIndex < len(self.usables) - 1):
                self.usablesIndex += 1
            else:
                self.usablesIndex = 0
        pydirectinput.press("r")
        time.sleep(buff.getBuffTime())
    
    def moveSpell(self, buffIndex):
        print("Spell Index:", self.spellIndex)
        print("Buff Index:", buffIndex)
        while self.spellIndex != buffIndex:
            pydirectinput.press("up")
            time.sleep(0.5)
            if (self.spellIndex < len(self.player.getSpells())- 1):
                self.spellIndex += 1
            else: 
                self.spellIndex = 0
    
    def applyLeftHandAshOfWar(self, buff):
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

    def applyRightHandAshOfWar(self, buff):
        pydirectinput.keyDown('e')
        pydirectinput.mouseDown(button="left")
        pydirectinput.mouseUp(button="left")
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

    def applyLeftSpell(self, buff):
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(buff.getBuffTime())
    
    def applyRightSpell(self, buff):
        pydirectinput.mouseDown(button="left")
        pydirectinput.mouseUp(button="left")
        time.sleep(buff.getBuffTime())
    


