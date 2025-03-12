import pyautogui
import time
time.sleep(1)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letter in alphabet:
    print(letter)
pyautogui.hotkey('command', 'v')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'tab')


