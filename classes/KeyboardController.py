import keyboard
import random
import time

class KeyboardController:
    def __init__(self):
        self.keyList = {
            32: "space",
            34: '"',
            39: "'",
            42: "*",
            43: "+",
            44: ",",
            45: "-",
            46: ".",
            47: "/",
            48: "0",
            49: "1",
            50: "2",
            51: "3",
            52: "4",
            53: "5",
            54: "6",
            55: "7",
            56: "8",
            57: "9",
            60: "<",
            62: ">",
            63: "?",
            65: "a",
            66: "b",
            67: "c",
            68: "d",
            69: "e",
            70: "f",
            71: "g",
            72: "h",
            73: "i",
            74: "j",
            75: "k",
            76: "l",
            77: "m",
            78: "n",
            79: "o",
            80: "p",
            81: "q",
            82: "r",
            83: "s",
            84: "t",
            85: "u",
            86: "v",
            87: "w",
            88: "x",
            89: "y",
            90: "z",
            92: "\\",
            95: "_",
            199: "ç",
            214: "ö",
            220: "ü",
            286: "ğ",
            350: "ş",
            16777216: "esc",
            16777217: "tab",
            16777219: "backspace",
            16777220: "enter",
            16777221: "num enter",
            16777222: "insert",
            16777223: "delete",
            16777227: "clear",
            16777232: "home",
            16777233: "end",
            16777234: "left",
            16777235: "up",
            16777236: "right",
            16777237: "down",
            16777238: "page up",
            16777239: "page down",
            16777248: "shift",
            16777249: "ctrl",
            16777251: "alt",
            16777252: "caps lock",
            16777253: "num lock",
            16777264: "f1",
            16777265: "f2",
            16777266: "f3",
            16777267: "f4", 
            16777268: "f5",
            16777269: "f6",
            16777270: "f7",
            16777271: "f8",
            16777272: "f9",
            16777273: "f10",
            16777274: "f11",
            16777275: "f12"
        }

    def checkKeyCode(self, keyCode: str) -> bool:
        return keyCode in self.keyList.keys()
    
    def checkKey(self, key: str) -> bool:
        return key in self.keyList.values()

    def press(self, key: str) -> bool:
        try:
            keyboard.press(key)
            time.sleep(random.uniform(0.1, 0.15))
            keyboard.release(key)
            return True
        except:
            return False
    
    def hold(self, key: str, seconds: int) -> bool:
        try:
            startTime = time.time()
            while time.time() - startTime < seconds:
                keyboard.press(key)
                time.sleep(0.03)
            keyboard.release(key)
            return True
        except:
            return False