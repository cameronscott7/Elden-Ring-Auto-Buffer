import pydirectinput
import time

def test_macro():
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

if __name__ == "__main__":
    test_macro()
