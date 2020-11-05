from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import re
import sys
import time
import random

from url import URLs
import locators 
import foodclub

class Player():
    profile  = "$HOME/.mozilla/firefox/neoplayer"
    driver   = None
    tries    = 3

    username = ""
    password = ""

    ####################################################################################################################
    # Constructor and destructor                                                                                       #
    ####################################################################################################################

    def __init__(self):
        self.driver = WebDriver(firefox_profile = FirefoxProfile(self.profile))
        self.driver.implicitly_wait(10)
        self.febx = self.driver.find_element_by_xpath
        self.febcn = self.driver.find_element_by_class_name
        self.febcs = self.driver.find_element_by_css_selector

    def __del__(self):
        self.driver.quit()

    ####################################################################################################################
    # Wrappers                                                                                                         #
    ####################################################################################################################

    def sleepRange(self, lower, upper, variation = 1.25):
        lower = random.uniform(lower / variation, lower * variation)
        upper = random.uniform(lower / variation, upper * variation)
        time.sleep(random.uniform(lower, upper))

    ####################################################################################################################
    # Controls                                                                                                         #
    ####################################################################################################################

    def getAndWait(self, url, sleep_lower, sleep_upper):
        try:
            self.driver.get(url)
            self.sleepRange(sleep_lower, sleep_upper)
            return True
        except Exception as e:
            sys.stderr.write("getAndWait: encountered exception: %s\n", e.message)
            return False

    # TODO: check if visible, scroll to element
    def clickAndWait(self, element, sleep_lower, sleep_upper):
        try:
            element.click()
            self.sleepRange(sleep_lower, sleep_upper)
            return True
        except Exception as e:
            sys.stderr.write("clickAndWait: encountered exception: %s\n", e.message)
            return False

    def typeAndWait(self, element, keys, sleep_lower, sleep_upper):
        try:
            for letter in keys:
                element.send_keys(letter)
                self.sleepRange(0.05, 0.07, 1.0)
            self.sleepRange(sleep_lower, sleep_upper)
            return True
        except Exception as e:
            sys.stderr.write("typeAndWait: encountered exception: %s\n", e.message)
            return False

    def selectAndWait(self, element, value, sleep_lower, sleep_upper):
        try:
            element.select_by_value(value)
            self.sleepRange(sleep_lower, sleep_upper)
            return True
        except Exception as e:
            sys.stderr.write("selectAndWait: encountered exception: %s\n", e.message)
            return False

    ####################################################################################################################
    # Actions                                                                                                          #
    ####################################################################################################################

    def login(self):
        self.getAndWait(URLs.login['login'], 0.5, 1)

        element_field_username = self.febx(locators.login['field_username'].XPath)
        element_field_password = self.febx(locators.login['field_password'].XPath)
        element_button_login = self.febcn(locators.login['button_login'].Class)

        # TODO: make sure correct elements are focused as we go
        self.clickAndWait(element_field_username, 0.5, 1.0)
        self.typeAndWait(element_field_username, self.username + Keys.TAB, 0.5, 1.0)
        self.typeAndWait(element_field_password, self.password, 0.5, 1.0)
        self.clickAndWait(element_button_login, 3.0, 5.0)

        # TODO: wait for some new element or lack of old or url change to confirm login complete
        #WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
        #wait(driver, 15).until_not(EC.title_is(title))

    def bank(self, action, amount):
        self.getAndWait(URLs.bank['bank'], 0.5, 1)

        if action == "withdraw":
            element_field_withdraw = self.febx(locators.bank['element_field_withdraw'].XPath)
            element_button_withdraw = self.febx(locators.bank['element_button_withdraw'].XPath)

            self.clickAndWait(element_field_withdraw, 0.5, 1.0)
            self.typeAndWait(element_field_withdraw, str(amount), 0.5, 1.0)
            self.clickAndWait(element_button_withdraw, 1.5, 2.5)

            # TODO: formal driver wait for dialog box
            try:
                self.driver.switch_to.alert.accept()
                self.sleepRange(1.0, 2.0)
            except:
                pass

    # TODO: validate bets before beginning
    def bet(self):
        # TODO: count bets to see if they're already placed
        #self.getAndWait(URLs.foodclub['current'], 1.0, 2.0)
        #bets_table = febx(xpath_current['bets_table'])
        #bets_rows = bets_table.find_elements_by_tag_name('tr')

        self.getAndWait(URLs.foodclub['boochi'], 0.5, 1.0)

        # The date the bets are for
        bets_for = self.febcs("body > center:nth-child(6) > p:nth-child(1) > font:nth-child(1)").text

        # Each set consists of one or more pairs
        sets = []

        # Forumlate set of all bets by parsing somebody's bets table
        source = self.driver.page_source
        bets = re.findall("<td><b>[^=]+<br><\/td>", source)
        for bet in bets:
            # Each pair consist of arena name and pirate name
            pairs = re.findall("<b>([^<]*)<\/b>: ([^<]*)<br>", bet)
            s = []
            for pair in pairs:
                s.append(pair)
            sets.append(s)

        self.getAndWait(URLs.foodclub['place'], 0.5, 1.0)

        # TODO: instead of or in addtion to this, validate scraped bets as possible for the current day
        next_round = str([int(c) for c in self.febcs(".content > center:nth-child(1) > b:nth-child(2)").text.split() if c.isdigit()][0])
        if next_round not in bets_for:
            sys.stderr.write("These bets don't appear to be up to date.\n")
            return

        # Parse bet amount from bets page, withdraw for ten bets
        amount = self.febx(foodclub.xpath_foodclub['bet_amount']).text
        self.bank('withdraw', str(int(amount) * 10))

        # Place each set of bets
        for s in sets:
            self.getAndWait(URLs.foodclub['place'], 1.0, 2.0)
            bet_element = self.febx(foodclub.xpath_foodclub['place_bet'])
            # Pairs consist of arena in first index, pirate in second
            for pair in s:
                element_arena = self.febx(foodclub.xpath_arena[pair[0]])                                               # Arena checkbox element
                element_pirate = self.febx(foodclub.xpath_pirate[pair[0]])                                             # Pirate option element?
                element_option = Select(element_pirate)                                                                # Arena pirate option box element
                self.clickAndWait(element_arena, 0.5, 1.0)                                                             # Click arena checkbox
                self.selectAndWait(element_option, foodclub.dict_pirates[pair[1]], 0.5, 1.0)                           # Select pirate from option box
            element_amount = self.febx(foodclub.xpath_foodclub['bet_box'])                                             # Bet amount text box element
            self.clickAndWait(element_amount, 0.5, 1.0)
            self.typeAndWait(element_amount, amount, 0.5, 1.0)
            self.clickAndWait(bet_element, 2.0, 3.0)
            #self.wait()
            WebDriverWait(self.driver, 10).until_not(EC.title_is(URLs.foodclub['place']))
    
    def wait(self):
        for count in xrange(0, 30):
            # Look for success page
            try:
                bets = self.febx(foodclub.xpath_foodclub['current_bets'])
                bets.click() # ???
                if bets.text == "Current Bets": # ???
                    return
            except:
                # Look for duplicate bet page
                try:
                    bets = self.febx(foodclub.xpath_foodclub['duplicate'])
                    bets.click() # ???
                    return
                except:
                    count += 1
                    self.sleepRange(1.0, 2.0)

# TODO: fout debug
