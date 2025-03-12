import requests
import pyautogui
import time
import subprocess
import random
from cryptography.fernet import Fernet


class Autometa:
    def __init__(self):
        print("-----Running ShyamSarkar Autometa-----")
        # try:
        #     # command_to_execute = ["google-chrome", "https://www.bing.com"]
        #     command_to_execute = ["google-chrome"]
        #     run = subprocess.run(command_to_execute, capture_output=True)
        # except:
        #     # command_to_execute = ["start", "chrome", "https://www.bing.com"]
        #     command_to_execute = ["start", "chrome"]
        #     run = subprocess.run(command_to_execute, capture_output=True)
        # print(run.stdout)
        # print(run.stderr)
        # print(pyautogui.position())
        time.sleep(1.5)

    def mouse_pointer_position(self):
        """-----(x=35, y=1955) Window Key Position"""
        time.sleep(2)
        return pyautogui.position() # position tracker of mouse

    def open_website(self, site_url="https://www.bing.com/"):
        """-----Running for the first time-----"""
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.typewrite(site_url)
        pyautogui.press('enter')

    def hit_link(self, random_text):
        character_count = 0
        for character in random_text:
            pyautogui.typewrite(character)
            character_count += 1
            if character_count > 60:
                break
        # pyautogui.typewrite(random_text)
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(3)

    def get_random_text(self):
        methods_list = [self.string_one, self.string_two, self.string_three, self.string_four, self.string_five]
        random_method = random.choice(methods_list)
        return random_method()
            
    def string_one(self):
        try:
            resp = requests.get('https://random-word-api.herokuapp.com/word')
            return f"What is the meaning of {resp.json()[0]} in hindi"
        except:
            return None

    def string_two(self):
        try:
            resp = requests.get('https://www.boredapi.com/api/activity')
            return resp.json()['activity']
        except:
            return None

    def string_three(self):
        try:
            resp = requests.get('https://official-joke-api.appspot.com/random_joke')
            return resp.json()['setup']
        except:
            return None

    def string_four(self):
        try:
            resp = requests.get('https://randomuser.me/api/')
            details = resp.json()["results"][0]
            return f"Who is {details['name']['first']} {details['name']['last']} from {details['location']['country']}"
        except:
            return None

    def string_five(self):
        try:
            resp = requests.get('https://catfact.ninja/fact')
            return resp.json()['fact']
        except:
            return None

    # def search_begin(self, random_word):
    #     """-----Searching On Searchbar-----"""
    #     time.sleep(1)
    #     # pyautogui.click(x=1343, y=661)
    #     pyautogui.typewrite(f"what is the meaning of {random_word} in hindi")
    #     pyautogui.press('enter')

    #     if resp.status_code == 200:
    #         return resp.json()[0]
    #     else:
    #         return None

    # def search_again(self, random_word):
    #     pyautogui.typewrite(f"what is the meaning of {random_word} in hindi")
    #     pyautogui.press('enter')

    #     time.sleep(1)
    #     """-----Again Search-----"""
    #     pyautogui.click(x=820, y=355) #select the text search box
    #     pyautogui.hotkey('ctrl', 'a')

    # def open_url(self, site_url):
    #     pyautogui.hotkey('ctrl', 'l')
    #     pyautogui.typewrite(site_url)
    #     pyautogui.press('enter')

    

    def encrypt_str(self, input_text, key=None):

        if key==None:
            key = Fernet.generate_key()
            print(key)
        f= Fernet(key)
        encMessage = f.encrypt(input_text.encode())
        return encMessage
    
    def decrypt_str(self, input_text, key=None):
        if key==None:
            key = Fernet.generate_key()
            print(key)
        f= Fernet(key)
        decMessage = f.decrypt(input_text).decode()
        return decMessage

    def log_out(self):
        time.sleep(1)
        self.open_website("https://rewards.bing.com/Signout")
        """
        self.open_website("https://rewards.bing.com/?ref=rewardspanel")
        time.sleep(3)
        pyautogui.click(x=2971, y=225)
        time.sleep(0.7)
        pyautogui.click(x=2882, y=359)
        """
        time.sleep(13)

    def login(self, account, password, key):
        self.open_website()
        time.sleep(3)
        password = self.decrypt_str(password, key)
        pyautogui.click(x=2325, y=256)
        time.sleep(4)
        pyautogui.typewrite(account)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        
    def previous_windows(self):
        print("Previous Window")
        #pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'w')

    def change_account(self, x, y, account_icon=(2976, 104) ):
        print("Changing Account")
        pyautogui.click(x=account_icon[0], y=account_icon[1])
        time.sleep(0.3)
        pyautogui.click(x, y)

    def random_search(self, search_count=1):
        self.open_website()
        time.sleep(3)
        for i in range(search_count):
            random_text = self.get_random_text()
            if random_text != None:
                self.hit_link(random_text)   