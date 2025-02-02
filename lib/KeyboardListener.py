import keyboard
import winsound
import time
from threading import Thread

class KeyboardListener:
    def __init__(self, listenKey: str, beepSound: bool = True) -> None:
        self.listenKey = listenKey.lower()
        self.beepSound = beepSound
        self.status = False
        self._isKeyDown = False
        self._running = False

    def _beep(self, frequency: int, duration: int, count: int = 1) -> None:
        if self.beepSound:
            for _ in range(count):
                winsound.Beep(frequency, duration)

    def _toggleStatus(self) -> None:
        while self._running:
            if keyboard.is_pressed(self.listenKey):
                if not self._isKeyDown:
                    self._isKeyDown = True
                    self.status = not self.status
                    self._beep(1000, 200, 1 if self.status else 2)
            else:
                self._isKeyDown = False
            time.sleep(0.03)

    def start(self) -> None:
        self._running = True
        self._listenerThread = Thread(target=self._toggleStatus)
        self._listenerThread.start()

    def stop(self) -> None:
        self._running = False
        self._listenerThread.join()
