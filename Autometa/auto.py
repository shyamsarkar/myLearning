import pyautogui
import time
from autometa_concerns import Autometa
start_time = time.time()
click_positions = [(2499, 666), (2499, 737), (2499, 812), (2499, 879), (2499, 948)]

obj = Autometa()

time.sleep(2)
obj.random_search(5)

for account_position in click_positions:
    time.sleep(0.5)
    obj.change_account(account_position[0], account_position[1])
    time.sleep(1)
    obj.random_search(5)
    obj.previous_windows()


time_elapsed = time.time() - start_time
pyautogui.alert("Developed by Shyam Sarkar\n\n---Code Execution Done---\n\n--Time Elapsed : %.2f--\n\n"%time_elapsed)

