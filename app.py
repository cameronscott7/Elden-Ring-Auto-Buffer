import customtkinter
import pydirectinput
import time
from Weapon import Weapon
from AshOfWar import AshOfWar
from Usable import Usable
from Spell import Spell
from Player import Player
from BuffSelector import BuffSelector
import tkinter.messagebox as messagebox


#TODO
#add manual mode where user can specify the order the buffs should be applied in.
#Add file to read in of buff priorities for user to edit (Might work as manual mode) (actually wound't work as manual mode since still have to check for mana and such)
#Add in file to read in all buffs for user to add new weapons if they want.
#NEED TO ADD SPELLS SECTION ASWELL
#IF WANTING TO USE SPELLS OR INCANTATIONS, MUST CHECK FOR IS USER HAS A seal or staff equipped.
#ADD CHECKBOXES FOR CHECKING IF WEAPON IS ONE HANDED OR TWO HANDED
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")
        #self.grid_rowconfigure(0, weight=1)  # configure grid system
        #self.grid_columnconfigure(0, weight=1)

        self.title("Combo Box Layout")
        self.mainLabel = customtkinter.CTkLabel(self, text="Elden Ring Auto Buffer", font=("Arial", 20),
            anchor="w")
        self.mainLabel.grid(row=0, column=0, padx=10, pady=5)

        self.row1Frame = customtkinter.CTkFrame(self)
        self.row1Frame.grid(row=1, column=0, padx=20, pady=5, sticky="nsw")

        self.row2Frame = customtkinter.CTkFrame(self)
        self.row2Frame.grid(row=2, column=0, padx=20, pady=5, sticky="nsw")

        self.row3Frame = customtkinter.CTkFrame(self)
        self.row3Frame.grid(row=3, column=0, padx=20, pady=5, sticky="nsw")

        self.initializeBuffs()
        self.loadBuffsFromFile(r"Elden-Ring-Auto-Buffer\Buffs.txt")

        self.createWeaponCombos(self.row1Frame)
        self.createUsableCombos(self.row2Frame)
        self.createSpellsCombos(self.row3Frame)
        self.createRightFrame(self.row1Frame)

    def initializeBuffs(self):
        self.weaponsDict = {
            "Staff": Weapon("Staff", "Medium"),
            "Seal": Weapon("Seal", "Medium"),
        }

        self.ashesOfWarDict = {}

        self.usablesDict = {}

        self.spellsDict = {}
    
    def loadBuffsFromFile(self, filepath):
        with open(filepath, "r") as file:
            lines = [line.strip() for line in file if line.strip() and not line.startswith("#")]

        current_buff = {}
        for line in lines:
            if line.startswith("Name:"):
                if current_buff:
                    self.processBuff(current_buff)
                    current_buff = {}
                current_buff["Name"] = line.split("Name:")[1].strip()
            else:
                key, value = line.split(":", 1)
                current_buff[key.strip()] = value.strip()

        # Process last buff
        if current_buff:
            self.processBuff(current_buff)

    def processBuff(self, buff_data):
        name = buff_data["Name"]
        type_ = buff_data["Type"].lower()

        priority = int(buff_data["Priority"])
        fp = int(buff_data["FP"])
        category = buff_data["Buff Category"]
        buff_time = int(buff_data["BuffTime (Seconds)"])
        is_sorcery = buff_data.get("isSorcery", "False").lower() == "true"

        if type_ == "usable":
            self.usablesDict[name] = Usable(name, priority, fp, category, buff_time, True)
        elif type_ == "spell":
            self.spellsDict[name] = Spell(name, priority, fp, category, buff_time, is_sorcery)
        elif "ash" in type_:
            self.ashesOfWarDict[name] = AshOfWar(name, priority, fp, category, buff_time)
            self.weaponsDict[name] = Weapon(name, AshOfWar)
        else:
            # Unknown type, ignore or log
            print(f"Unknown type '{type_}' for buff '{name}'")


    def addLableEntry(self, parent, labelText):
        self.frame = customtkinter.CTkFrame(parent)
        self.frame.pack(pady=5, padx=10, fill="x")  # each row stacked vertically

        label = customtkinter.CTkLabel(self.frame, text=labelText, width=80, anchor="w")
        label.pack(side="left")

        entry = customtkinter.CTkEntry(self.frame)
        entry.pack(side="left", expand=True, fill="x", padx=(5, 0))

        return entry
        
    def createRightFrame(self, parent):
        self.rightFrame = customtkinter.CTkFrame(parent)
        self.rightFrame.pack(side="left", expand=True, fill="x", padx=(20, 0))

        # Create the submit button on the right

        self.maxFP= self.addLableEntry(self.rightFrame, "Max FP:")
        self.numFlasks = self.addLableEntry(self.rightFrame,"Number of Flasks:")
        self.flaskLevel = self.addLableEntry(self.rightFrame,"Flask Level:")

        self.submitButton = customtkinter.CTkButton(self.rightFrame, text="Submit", command=self.submitAction)
        self.submitButton.pack(side="left")

    def createWeaponCombos(self, parent):
        buffNames = list(self.weaponsDict.keys())

        # Main frame holding everything
        self.weaponFrame = customtkinter.CTkFrame(parent)
        self.weaponFrame.pack(side="left", expand=True, fill="x", padx=(5, 0))

        # Row 1 frame
        row1 = customtkinter.CTkFrame(self.weaponFrame)
        row1.pack(fill="x", pady=5)

        self.weapon1 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.weapon1.pack(side="left", padx=10, pady=5)
        self.weapon1.set("Empty")

        self.weapon2 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.weapon2.pack(side="left", padx=10, pady=5)
        self.weapon2.set("Empty")

        self.weapon3 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.weapon3.pack(side="left", padx=10, pady=5)
        self.weapon3.set("Empty")

        # Row 2 frame
        row2 = customtkinter.CTkFrame(self.weaponFrame)
        row2.pack(fill="x", pady=5)

        self.weapon4 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.weapon4.pack(side="left", padx=10, pady=5)
        self.weapon4.set("Empty")

        self.weapon5 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.weapon5.pack(side="left", padx=10, pady=5)
        self.weapon5.set("Empty")

        self.weapon6 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.weapon6.pack(side="left", padx=10, pady=5)
        self.weapon6.set("Empty")

    def createUsableCombos(self, parent):
        buffNames = list(self.usablesDict.keys())

        self.usableFrame = customtkinter.CTkFrame(parent)
        self.usableFrame.pack(padx=20, pady=20, anchor="w")

        # Row 1
        row1 = customtkinter.CTkFrame(self.usableFrame)
        row1.pack(fill="x")

        self.usable1 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.usable1.pack(side="left", padx=10, pady=10)
        self.usable1.set("Empty")

        self.usable2 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.usable2.pack(side="left", padx=10, pady=10)
        self.usable2.set("Empty")

        self.usable3 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.usable3.pack(side="left", padx=10, pady=10)
        self.usable3.set("Empty")

        self.usable4 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.usable4.pack(side="left", padx=10, pady=10)
        self.usable4.set("Empty")

        self.usable5 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.usable5.pack(side="left", padx=10, pady=10)
        self.usable5.set("Empty")

        # Row 2
        row2 = customtkinter.CTkFrame(self.usableFrame)
        row2.pack(fill="x")

        self.usable6 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.usable6.pack(side="left", padx=10, pady=10)
        self.usable6.set("Empty")

        self.usable7 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.usable7.pack(side="left", padx=10, pady=10)
        self.usable7.set("Empty")

        self.usable8 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.usable8.pack(side="left", padx=10, pady=10)
        self.usable8.set("Empty")

        self.usable9 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.usable9.pack(side="left", padx=10, pady=10)
        self.usable9.set("Empty")

        self.usable10 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.usable10.pack(side="left", padx=10, pady=10)
        self.usable10.set("Empty")


    def createSpellsCombos(self, parent):
        buffNames = list(self.spellsDict.keys())

        self.spellFrame = customtkinter.CTkFrame(parent)
        self.spellFrame.pack(padx=20, pady=20)

        # Row 1
        row1 = customtkinter.CTkFrame(self.spellFrame)
        row1.pack(fill="x")

        self.spell1 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.spell1.pack(side="left", padx=10, pady=10)
        self.spell1.set("Empty")

        self.spell2 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.spell2.pack(side="left", padx=10, pady=10)
        self.spell2.set("Empty")

        self.spell3 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.spell3.pack(side="left", padx=10, pady=10)
        self.spell3.set("Empty")

        self.spell4 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.spell4.pack(side="left", padx=10, pady=10)
        self.spell4.set("Empty")

        self.spell5 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.spell5.pack(side="left", padx=10, pady=10)
        self.spell5.set("Empty")

        self.spell6 = customtkinter.CTkComboBox(row1, values=buffNames, state="readonly")
        self.spell6.pack(side="left", padx=10, pady=10)
        self.spell6.set("Empty")

        # Row 2
        row2 = customtkinter.CTkFrame(self.spellFrame)
        row2.pack(fill="x")

        self.spell7 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.spell7.pack(side="left", padx=10, pady=10)
        self.spell7.set("Empty")

        self.spell8 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.spell8.pack(side="left", padx=10, pady=10)
        self.spell8.set("Empty")

        self.spell9 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.spell9.pack(side="left", padx=10, pady=10)
        self.spell9.set("Empty")

        self.spell10 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.spell10.pack(side="left", padx=10, pady=10)
        self.spell10.set("Empty")

        self.spell11 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.spell11.pack(side="left", padx=10, pady=10)
        self.spell11.set("Empty")

        self.spell12 = customtkinter.CTkComboBox(row2, values=buffNames, state="readonly")
        self.spell12.pack(side="left", padx=10, pady=10)
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

        hasStaff = False
        hasSeal = False

        for weapon in weapons:
            if (weapon == "Staff"):
                hasStaff = True
            elif (weapon == "Seal"):
                hasSeal = True

        filteredAshesOfWar = [self.ashesOfWarDict[key] for key in ashesOfWar if key in self.ashesOfWarDict]
        moreFilteredSpells = [self.spellsDict[key] for key in filteredSpells if key in self.spellsDict]
        moreFilteredUsables = [self.usablesDict[key] for key in filteredUsables if key in self.usablesDict]

        sorceries = [spell for spell in moreFilteredSpells if spell.isSorcery]
        incantations = [spell for spell in moreFilteredSpells if not spell.isSorcery]

        print("Selections:", filteredWeapons)
        print("Selections:", filteredUsables)

        if not (hasStaff):
            if (len(sorceries) > 0):
                messagebox.showinfo(title="Error", message="Must Equip Staff In Order To Use A Sorcery")
                return
            
        if not (hasSeal):
            if (len(incantations) > 0):
                messagebox.showinfo(title="Error", message="Must Equip Seal In Order To Use A Incantation")
                return
            
        if int(self.numFlasks.get()) > 0:
            if "FP Flask" not in usables:
                messagebox.showinfo(title="Error", message="Must Equip FP Flask if Number of Flasks is Greater than 0.")
                return

        try:
            player = Player(int(self.maxFP.get()), int(self.maxFP.get()), 100, int(self.numFlasks.get()), 
                            int(self.flaskLevel.get()), weapons, filteredAshesOfWar, moreFilteredSpells, 
                            moreFilteredUsables)
        except:
            messagebox.showinfo(title="Error", message="Please enter in valid Integers")
            return
        
        buffSel = BuffSelector(player)

        print("Sorted:", buffSel.findBuffOrderByPrio())

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