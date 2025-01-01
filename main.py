from classes import KeyboardListener, MouseController
import ctypes
import sys
import time

def runAsAdministrator() -> bool:
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        return False

def main():
    listenKey = "z"
    keyboardListener = KeyboardListener(listenKey=listenKey, beepSound=True)
    keyboardListener.start()

    mouseController = MouseController()

    print(f"Press '{listenKey}' to start/stop.")
    
    while True:
        if keyboardListener.status == True:
            mouseController.move(0, 0, 1)
        time.sleep(0.1)

if __name__ == '__main__':
    if runAsAdministrator():
        main()