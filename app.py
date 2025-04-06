import customtkinter
import pydirectinput
import time
from Weapon import Weapon
from AshOfWar import AshOfWar
from Usable import Usable
from Spell import Spell
from Player import Player
from BuffSelector import BuffSelector

#TODO
#add manual mode where user can specify the order the buffs should be applied in.
#Add file to read in of buff priorities for user to edit (Might work as manual mode) (actually wound't work as manual mode since still have to check for mana and such)
#Add in file to read in all buffs for user to add new weapons if they want.
#NEED TO ADD SPELLS SECTION ASWELL
#IF WANTING TO USE SPELLS OR INCANTATIONS, MUST CHECK FOR IS USER HAS A seal or staff equipped.
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        #self.grid_rowconfigure(0, weight=1)  # configure grid system
        #self.grid_columnconfigure(0, weight=1)

        self.title("Combo Box Layout")
        self.mainLabel = customtkinter.CTkLabel(self, text="Elden Ring Auto Buffer", font=("Arial", 20),
            anchor="w")
        self.mainLabel.pack(side="left", expand=True, fill="x", padx=(5, 0))

        #TODO
        #MAKE A NEW METHOD FOR THIS
        self.weaponsDict = {
            "Golden Vow (Ash of War)": Weapon("Golden Vow", AshOfWar),
            "Staff": Weapon("Staff", Spell),
        }

        self.ashesOfWarDict = {
            "Golden Vow (Ash of War)": AshOfWar("Golden Vow (Ash of War)", 3, 20, 10, "None", "Body", 0, 0.00, True, True),
        }

        self.usablesDict = {
            "Flask of Wondrous Physick": Usable("Flask of Wondrous Physick", 0, 0, 10, "None", "Aura", 0, 0.00, True),
        }

        self.spellsDict = {
            "Terra Magica": Spell("Flask of Wondrous Physick", 2, 50, 10, "None", "Area", 0, 0.00, True, True),
        }

        self.createWeaponCombos()
        self.createUsableCombos()
        self.createSpellsCombos()
        self.createRightFrame()

    def addLableEntry(self, parent, labelText):
        self.frame = customtkinter.CTkFrame(parent)
        self.frame.pack(pady=5, padx=10, fill="x")  # each row stacked vertically

        label = customtkinter.CTkLabel(self.frame, text=labelText, width=80, anchor="w")
        label.pack(side="left")

        entry = customtkinter.CTkEntry(self.frame)
        entry.pack(side="left", expand=True, fill="x", padx=(5, 0))

        return entry
        
    def createRightFrame(self):
        self.rightFrame = customtkinter.CTkFrame(self)
        self.rightFrame.pack(side="left", expand=True, fill="x", padx=(5, 0))

        # Create the submit button on the right

        self.maxFP= self.addLableEntry(self.rightFrame, "Max FP:")
        self.numFlasks = self.addLableEntry(self.rightFrame,"Number of Flasks:")
        self.flaskLevel = self.addLableEntry(self.rightFrame,"Flask Level:")

        self.submitButton = customtkinter.CTkButton(self.rightFrame, text="Submit", command=self.submitAction)
        self.submitButton.pack(side="left")

    def createWeaponCombos(self):
        buffNames=list(self.weaponsDict.keys())

        # Create a frame for the combo boxes on the left
        self.weaponFrame = customtkinter.CTkFrame(self)
        self.weaponFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w", columnspan=3)

        # Create 3 combo boxes on the top
        self.weapon1 = customtkinter.CTkComboBox(self.weaponFrame, values=buffNames, state="readonly")
        self.weapon1.grid(row=0, column=0, padx=10, pady=10)
        self.weapon1.set("Empty")

        self.weapon2 = customtkinter.CTkComboBox(self.weaponFrame, values=buffNames, state="readonly")
        self.weapon2.grid(row=0, column=1, padx=10, pady=10)
        self.weapon2.set("Empty")

        self.weapon3 = customtkinter.CTkComboBox(self.weaponFrame, values=buffNames, state="readonly")
        self.weapon3.grid(row=0, column=2, padx=10, pady=10)
        self.weapon3.set("Empty")

        self.weapon4 = customtkinter.CTkComboBox(self.weaponFrame, values=buffNames, state="readonly")
        self.weapon4.grid(row=1, column=0, padx=10, pady=10)
        self.weapon4.set("Empty")

        self.weapon5 = customtkinter.CTkComboBox(self.weaponFrame, values=buffNames, state="readonly")
        self.weapon5.grid(row=1, column=1, padx=10, pady=10)
        self.weapon5.set("Empty")

        self.weapon6 = customtkinter.CTkComboBox(self.weaponFrame, values=buffNames, state="readonly")
        self.weapon6.grid(row=1, column=2, padx=10, pady=10)
        self.weapon6.set("Empty")


    def createUsableCombos(self):
        buffNames=list(self.usablesDict.keys())

        self.usableFrame = customtkinter.CTkFrame(self)
        self.usableFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsw")

        # Create 3 combo boxes on the top
        self.usable1 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable1.grid(row=0, column=0, padx=10, pady=10)
        self.usable1.set("Empty")

        self.usable2 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable2.grid(row=0, column=1, padx=10, pady=10)
        self.usable2.set("Empty")

        self.usable3 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable3.grid(row=0, column=2, padx=10, pady=10)
        self.usable3.set("Empty")

        self.usable4 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable4.grid(row=0, column=3, padx=10, pady=10)
        self.usable4.set("Empty")

        self.usable5 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable5.grid(row=0, column=4, padx=10, pady=10)
        self.usable5.set("Empty")

        self.usable6 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable6.grid(row=1, column=0, padx=10, pady=10)
        self.usable6.set("Empty")
        
        self.usable7 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable7.grid(row=1, column=1, padx=10, pady=10)
        self.usable7.set("Empty")

        self.usable8 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable8.grid(row=1, column=2, padx=10, pady=10)
        self.usable8.set("Empty")

        self.usable9 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable9.grid(row=1, column=3, padx=10, pady=10)
        self.usable9.set("Empty")

        self.usable10 = customtkinter.CTkComboBox(self.usableFrame, values=buffNames, state="readonly")
        self.usable10.grid(row=1, column=4, padx=10, pady=10)
        self.usable10.set("Empty")

    def createSpellsCombos(self):
        buffNames=list(self.spellsDict.keys())

        self.spellFrame = customtkinter.CTkFrame(self)
        self.spellFrame.grid(row=3, column=0, padx=20, pady=20)

        self.spell1 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell1.grid(row=0, column=0, padx=10, pady=10)
        self.spell1.set("Empty")

        self.spell2 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell2.grid(row=0, column=1, padx=10, pady=10)
        self.spell2.set("Empty")

        self.spell3 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell3.grid(row=0, column=2, padx=10, pady=10)
        self.spell3.set("Empty")

        self.spell4 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell4.grid(row=0, column=3, padx=10, pady=10)
        self.spell4.set("Empty")

        self.spell5 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell5.grid(row=0, column=4, padx=10, pady=10)
        self.spell5.set("Empty")

        self.spell6 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell6.grid(row=0, column=5, padx=10, pady=10)
        self.spell6.set("Empty")
        
        self.spell7 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell7.grid(row=1, column=0, padx=10, pady=10)
        self.spell7.set("Empty")

        self.spell8 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell8.grid(row=1, column=1, padx=10, pady=10)
        self.spell8.set("Empty")

        self.spell9 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell9.grid(row=1, column=2, padx=10, pady=10)
        self.spell9.set("Empty")

        self.spell10 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell10.grid(row=1, column=3, padx=10, pady=10)
        self.spell10.set("Empty")

        self.spell11 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell11.grid(row=1, column=4, padx=10, pady=10)
        self.spell11.set("Empty")

        self.spell12 = customtkinter.CTkComboBox(self.spellFrame, values=buffNames, state="readonly")
        self.spell12.grid(row=1, column=5, padx=10, pady=10)
        self.spell12.set("Empty")

    def submitAction(self):
        # Action when the submit button is clicked (just printing combo box selections)
        weapons = [self.weapon1.get(), self.weapon2.get(), self.weapon3.get(),
                      self.weapon4.get(), self.weapon5.get(), self.weapon6.get()]
        
        usables = [self.usable1.get(), self.usable2.get(), self.usable3.get(),
                      self.usable4.get(), self.usable5.get(), self.usable6.get(),
                      self.usable7.get(), self.usable8.get(), self.usable9.get(),
                      self.usable10.get()]
        
        spells = [self.spell1.get(), self.spell2.get(), self.spell3.get(),
                      self.spell4.get(), self.spell5.get(), self.spell6.get(),
                      self.spell7.get(), self.spell8.get(), self.spell9.get(),
                      self.spell10.get(), self.spell11.get(), self.spell12.get()]
        
        filteredWeapons = [item for item in weapons if item != "Empty"]
        filteredUsables = [item for item in usables if item != "Empty"]
        filteredSpells = [item for item in spells if item != "Empty"]
        ashesOfWar = [item for item in weapons if item != "Staff"]

        filteredAshesOfWar = [self.ashesOfWarDict[key] for key in ashesOfWar if key in self.ashesOfWarDict]
        moreFilteredSpells = [self.spellsDict[key] for key in spells if key in self.spellsDict]
        moreFilteredUsables = [self.usablesDict[key] for key in filteredUsables if key in self.usablesDict]

        print("Selections:", filteredWeapons)
        print("Selections:", filteredUsables)


        player = Player(100, 100, 100, 0, 0, weapons, filteredAshesOfWar, moreFilteredSpells, moreFilteredUsables)

        buffSel = BuffSelector(player)

        print("Sorted:", buffSel.findBuffOrderByNumber())

    def button_callbck(self):
        print("Macro starts in 5 seconds...")
        time.sleep(5)

        print("Performing test inputs")

        pydirectinput.press("down")
        time.sleep(0.5)
        pydirectinput.press("r")
        time.sleep(3)
        pydirectinput.keyDown('e')
        time.sleep(0.5)
        pydirectinput.mouseDown(button="left")
        pydirectinput.mouseUp(button="left")
        time.sleep(0.5)
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(0.5)
        pydirectinput.keyUp('e')
        time.sleep(0.5)
        pydirectinput.keyDown('shift')
        time.sleep(.5)
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(3)
        pydirectinput.keyUp('shift')
        time.sleep(.5)
        pydirectinput.press("left")
        time.sleep(.5)
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(3)
        pydirectinput.keyDown('e')
        time.sleep(0.5)
        pydirectinput.mouseDown(button="left")
        pydirectinput.mouseUp(button="left")
        time.sleep(0.5)
        pydirectinput.keyUp('e')
        time.sleep(0.5)
        pydirectinput.keyDown('shift')
        time.sleep(.5)
        pydirectinput.mouseDown(button="right")
        pydirectinput.mouseUp(button="right")
        time.sleep(3)
        pydirectinput.keyUp('shift')

        print("Test complete!")

app = App()
app.mainloop()