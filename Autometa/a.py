import pyautogui
import time
from autometa_concerns import Autometa
start_time = time.time()
key = "kJcrmxiyyjM_hu-srov07123xdlRkCf2k9zk-WWLI9Y="
accounts = ["email1@gmail.com", "email2@gmail.com"]
for index, account in enumerate(accounts):
    print(f"{index+1}: {account}")
index_number = int(input("Enter Index Number: "))

password = ""

obj = Autometa()

obj.login(accounts[index_number-1], password, key)

for i in range(5):
    random_text = obj.get_random_text()
    if random_text != None:
        obj.hit_link(random_text)

time_elapsed = time.time() - start_time
pyautogui.alert("Developed by Shyam Sarkar\n\n---Code Execution Done---\n\n--Time Elapsed : %.2f--\n\n"%time_elapsed)

