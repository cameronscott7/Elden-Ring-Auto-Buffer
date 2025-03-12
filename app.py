import customtkinter
import pydirectinput
import time

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x500")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)
    
    #def readBuffs():
    #hold down down arrow to return to first pocket item.
    #add manual mode where user can specify the order the buffs should be applied in.

    def button_callbck(self):
        print("Switch to Elden Ring now! Macro starts in 5 seconds...")
        time.sleep(5)

        print("Performing test inputs...")

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