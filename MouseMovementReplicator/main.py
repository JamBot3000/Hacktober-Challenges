import time

from pynput.mouse import Listener as MouseListener, Controller
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key

mouse = Controller()
recorded_mouse_positions = []


def record_mouse_movements():
    with MouseListener(on_move=on_move, on_click=on_click) as listener, \
            KeyboardListener(on_press=on_press) as listener:
        listener.join()


def on_press(key):
    if key == Key.esc:
        exit(0)
        return False


def on_move(x, y):
    recorded_mouse_positions.append((x, y))


def on_click(x, y, button, pressed):
    if not pressed:
        replicate_recorded_movements()
        return False


def replicate_recorded_movements():
    for position in recorded_mouse_positions:
        time.sleep(0.01)
        mouse.position = position


if __name__ == "__main__":
    print("{ Welcome to Mouse Movement Replicator! }\n")
    print("MMR is now recording the movement of your mouse and "
          "when you *click* it will replicate your movements.\n")
    print("[WARNING] Press ESC to terminate program.")
    record_mouse_movements()
