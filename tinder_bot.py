from selenium import webdriver
from time import sleep

from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        # wait 5 sec till login prompted
        sleep(5)

        # accept cookies
        accept_cookies_popup = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_cookies_popup.click()

        # close login prompt (this is in case not able to access the fb button),
        # solution is to close login prompt and manual click on login button
        close_login_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button')
        close_login_popup.click()

        # get fb login button (sometime fb login button is at position 2 or 3)
        try:
            # manual click on login button
            login_button = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_button.click()

            # check if fb login button at position 2, if not will throw an exception
            fb_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        except Exception:
            # if phone login button is popup, close it
            close_phone_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div[2]/button')
            close_phone_btn.clock()

            # manual click on login button
            login_button = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_button.click()

            # check if fb login button at position 2
            fb_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')

        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        # enter fb email
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        # enter fb password
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        # login using fb, click on login btn
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        # return to parent window from login popup window
        self.driver.switch_to_window(base_window)

        # enable location
        location_enable_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location_enable_popup.click()

        # enable notification
        notification_enable_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification_enable_popup.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    # close popup of match found
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
