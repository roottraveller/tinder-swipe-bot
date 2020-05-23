import pyautogui
import time


# You must be login to tinder.com and mouse hover to live icon to get the x,y cords
class TinderBot:

    def like(self):
        # Mouse hover to tinder like button to get the (x,y) cords
        # pyautogui.position();
        # (1109, 784)

        i = 0
        while i < 10:
            print("Getting a like for you. likes count=", i)
            # pyautogui.click(1109, 784)
            time.sleep(2)
            i += 1


bot = TinderBot()
bot.like()
