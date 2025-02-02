from pynput.mouse import Controller, Button
import random
import time

class MouseController:
    def __init__(self):
        self.mouse = Controller()
        self.buttons = {
            "left": Button.left,
            "right": Button.right
        }
        self.buttonLeft = Button.left
        self.buttonRight = Button.right

    def _getButton(self, button: str) -> Button:
        button = button.lower()
        button = self.buttons.get(button)
        return button

    def click(self, button: str) -> bool:
        button = self._getButton(button)
        self.mouse.press(button)
        time.sleep(random.uniform(0.03, 0.07))
        self.mouse.release(button)
        return True
    
    def hold(self, button: str) -> bool:
        button = self._getButton(button)
        self.mouse.press(button)
        return True
    
    def release(self, button: str) -> bool:
        button = self._getButton(button)
        self.mouse.release(button)
        return True
    
    def move(self, x: int, y: int, duration: float = 1.0) -> bool:
        startX, startY = self.mouse.position

        steps = int(duration * 100)
        if steps == 0:
            steps = 1
            
        deltaX = (x - startX) / steps
        deltaY = (y - startY) / steps
        for step in range(steps):
            newX = startX + deltaX * step
            newY = startY + deltaY * step
            self.mouse.position = (newX, newY)
            time.sleep(0.01)
        self.mouse.position = (x, y)
        return True