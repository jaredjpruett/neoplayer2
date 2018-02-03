from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pyvirtualdisplay import Display

from random import uniform
from time import sleep
from sys import stderr, exit

from dtfns import *
from xpath import xpath, foodclub, battledome
from url import url, battledome_url

class Autoplayer():
	def __init__(self):
		# 
		home			= ""
		autoplayer		= home + ""

		# Virtual display
		self.display	= Display(visible = 0, size = (800, 600)).start()
		# Selenium objects
		self.profile	= FirefoxProfile("")
		self.driver		= WebDriver(firefox_profile = self.profile)
		# Write to log file
		self.fout		= open(autoplayer + "log.txt", "a")
		# Track login attempts
		self.attempt	= 0
		# Alias 'driver.find_element_by_xpath' as 'febx'
		self.febx		= self.driver.find_element_by_xpath

	def start(self, username, password):
		self.login(username, password)
		self.dailies()
		#self.winnings()
		#self.gamble()
		#self.battle()
		self.safe()
		self.deposit()

		return self.sleepfor()

	def stop(self):
		self.fout.close()
		self.driver.quit()
		self.display.stop()

	def login(self, username, password):
		self.driver.get(url['main'])
		sleep(uniform(1.5, 3.5))

		try:
			self.febx(xpath['login']).click()
			sleep(uniform(0.5, 1))

			ufield = self.febx(xpath['username'])
			ufield.click()
			sleep(uniform(0.5, 1.0))
			ufield.send_keys(username)
			sleep(uniform(0.5, 1.0))

			pfield = self.febx(xpath['password'])
			pfield.click()
			sleep(uniform(0.5, 1.0))
			pfield.send_keys(password)
			sleep(uniform(0.5, 1.0))

			self.febx(xpath['button']).click()
			sleep(uniform(5, 10))

			self.fout.write("Successfully logged into " + username + ".\n")
			self.fout.flush()

		except:
			self.attempt = self.attempt + 1
			self.fout.write("Login failed.\n")
			self.fout.flush()
			sleep(uniform(1, 2))

			if self.attempt < 3:
				self.login(username, password)
			else:
				self.sleepfor()
				exit(9)

	def dailies(self):
		self.perform('jelly')
		self.perform('omelette')
		self.perform('interest')
		self.perform('altador')
		self.perform('offers')
		self.perform('chest')
		self.perform('anchor')
		self.perform('scratchcard')
		self.perform('tombola')
		self.perform('fruits')
		self.perform('coltzan')
		self.perform('plushie')
		self.perform('fishing')
		self.perform('shore')
		self.perform('springs')

		try:
			self.driver.get(url['springs'])
			self.febx(xpath['sale']).click()
			self.febx(xpath['buy']).click()

			self.fout.write("Bought a potion from Healing Springs shop.\n")
			self.fout.flush()
		except:
			self.fout.write("Error buying from Healing Springs shop.\n")
			self.fout.flush()

	def springs(self):
		try:
			self.driver.get(url['springs'])
			self.febx(xpath['sale']).click()
			self.febx(xpath['buy']).click()

			self.fout.write("Bought a potion from Healing Springs shop.\n")
			self.fout.flush()
		except:
			self.fout.write("Error buying from Healing Springs shop.\n")
			self.fout.flush()

	def scratchcard(self):
		self.perform('scratchcard')

	def sleepfor(self):
		now = datetime_string()
		nat = generate_time()
		nownums = [int(i) for i in now.split() if i.isdigit()]
		nxtnums = [int(i) for i in nat.split() if i.isdigit()]
		seconds = (nxtnums[5] - nownums[5]) + (nxtnums[4] - nownums[4]) * 60 + (nxtnums[3] - nownums[3]) * 3600

		if nxtnums[2] != nownums[2]: seconds += 86400

		self.fout.write("Sleeping for " + str(seconds) + " seconds.\n\n")
		self.fout.flush()

		return seconds

	def perform(self, action):
		self.driver.get(url[action])
		sleep(uniform(1, 5))

		try:
			self.febx(xpath[action]).click()
			self.fout.write("Successfully executed '" + str(action) + "' task at " + datetime_string() + ".\n")
			self.fout.flush()
		except:
			self.fout.write("Unsuccessfully executed '" + str(action) + "' task at " + datetime_string() + ".\n")
			self.fout.flush()

		sleep(uniform(3, 7))

	def bank(self, action, amount):
		self.driver.get(url['bank'])
		sleep(uniform(2, 4))

		try:
			#element = self.febx(xpath[action])
			#element.send_keys(str(amount) + Keys.RETURN)
			self.febx(xpath[action]).send_keys(str(amount) + Keys.RETURN)
			sleep(uniform(1, 3))
		except:
			print "An error occurred. Could not bank properly.\n"

	def deposit(self):
		try:
			money = self.dosh()

			if money > 5000:
				money = money - 5000
				self.bank('deposit', money)
				self.fout.write("Deposited " + str(money) + " points.\n")
				self.fout.flush()
			else:
				self.fout.write("Only had " + str(money) + " points on hand; did not deposit.\n")
				self.fout.flush()
		except:
			self.fout.write("An error occurred. Could not deposit points.\n")
			self.fout.flush()

	def dosh(self):
		try:
			amount = self.febx(xpath['dosh']).text.replace(',', '')
			return int(amount)
		except:
			print "An error occurred. Could not detect dosh.\n"
			return 0

	def safe(self):
		self.driver.get(url['inventory'])
		sleep(uniform(3, 6))

		try:
			self.driver.find_element_by_xpath(xpath['noitems'])
			self.fout.write('No items to deposit.\n')
			self.fout.flush()
			sleep(uniform(3, 10))
		except:
			self.driver.get(url['quickstock']) # change to click
			self.fout.write('Deposited items.\n')
			self.fout.flush()
			sleep(uniform(1.5, 3.5))

	def gamble(self):
		done = False
		checks = 0

		self.fout.write("Attempting to place bets...\n")
		self.fout.flush()

		self.driver.get(url['bets'])
		sleep(uniform(1, 3))

		try:
			self.febx(foodclub['tenth'])
			self.fout.write("Bets have already been placed.\n")
			self.fout.flush()
			return
		except:
			pass

		self.driver.get(url['foodclub'])
		sleep(uniform(1.5, 4.5))

		try:
			amount = int(self.febx(xpath['betamount']).text) * 10
			dosh = self.dosh() - 5000

			if dosh < amount:
				self.bank('withdraw', amount + 5000 - dosh)
				sleep(uniform(2, 5))

			self.driver.get(url['foodclubbets'])
			sleep(uniform(10, 20))

			try:
				eletext = self.febx("html/body/center[2]/table/tbody/tr[3]/td").text

				if eletext == "You do not have any bets placed for this round!":
					self.fout.write("Looks like Hugo didn't place bets today.\n")
					self.fout.flush()
					return
			except:
				self.fout.write("An error occurred while parsing Hugo's page. ")
				self.fout.write("We'll try to press on and see what happens.\n")
				self.fout.flush()

			# Start the betting script
			try:
				self.febx(xpath['gamble']).click()
				sleep(uniform(5, 10))

				try:
					self.febx(foodclub['error'])
					self.fout.write("The script returned an error. ")
					self.fout.write("Hugo probably hasn't updated the page yet today.\n")
					self.fout.flush()
					return
				except:
					pass

				sleep(uniform(60, 90))

				try:
					while done == False and checks < 10:
						try:
							self.febx(foodclub['tenth'])
							self.fout.write("Bets successfully placed.\n")
							self.fout.flush()
							done = True
						except:
							checks += 1
							sleep(60)
				except:
					self.fout.write("Could not place all bets.\n")
					self.fout.flush()
			except Exception as e:
				stderr.write("An error occurred. Could not place bets. ")
				stderr.write("It seems like the button to start the script didn't show up.\n")
				stderr.write("%s\n" % str(e))
				stderr.flush()
		except Exception as e:
			stderr.write("An error occurred. I don't even know. ")
			stderr.write("Maybe we couldn't find our dosh. We're probably not logged in.\n")
			stderr.write("%s\n" % str(e))
			stderr.flush()

	def winnings(self):
		self.driver.get(url['foodclub'])
		sleep(uniform(1, 4))

		self.driver.get(url['winnings']) # convert into a link click
		sleep(uniform(3, 7))

		try:
			self.febx(xpath['winnings']).click()
			self.fout.write("Winnings collected.\n")
			self.fout.flush()
			sleep(uniform(2, 4))
		except:
			self.fout.write("No winnings today.\n")
			self.fout.flush()

	def battle(self):
		self.driver.get(battledome_url['main'])
		fights = 15
		fought = 0
		prizes = 0

		self.fout.write("Battling. Beaten 0")
		self.fout.flush()

		try:
			self.febx(battledome['battle1']).click()
			sleep(uniform(1, 1.5))

			# If we're already in battle, skip this section
			try:
				self.febx(battledome['continue1']).click()
				sleep(uniform(1, 2))
				self.febx(battledome['continue2']).click()
				sleep(uniform(2.5, 3.5))
				self.febx(battledome['chiaclown']).click()
				sleep(uniform(1, 2.5))
				self.febx(battledome['battle2']).click()
				sleep(uniform(10, 15))
			except:
				pass

			while fought < fights:
				try:
					# We should be at this screen right now
					self.febx(battledome['fight1']).click()
					sleep(uniform(3.5, 5))
				except:
					# But if fucking not, somehow, try the beginning again
					try:
						# Let's also try this, why not
						try:
							self.febx(battledome['battle1']).click()
							sleep(uniform(1, 1.5))
						except:
							pass

						self.febx(battledome['continue1']).click()
						sleep(uniform(1, 2))
						self.febx(battledome['continue2']).click()
						sleep(uniform(2.5, 3.5))
						self.febx(battledome['chiaclown']).click()
						sleep(uniform(1, 2.5))
						self.febx(battledome['battle2']).click()
						sleep(uniform(10, 15))
						self.febx(battledome['fight1']).click()
						sleep(uniform(3.5, 5))
					except Exception as e:
						self.fout.write("\n")
						self.fout.write("I don't even fucking know anymore.\n")
						self.fout.flush()
						stderr.write("%s\n" % e)
						stderr.flush()

				self.febx(battledome['slot1']).click()
				sleep(uniform(0.5, 1.5))

				try:
					self.febx(battledome['item1']).click()
					sleep(uniform(1, 2))
				except:
					self.fout.write(", %ih" % fought + 1)
					self.fout.flush()
					self.febx(battledome['slot1']).click()
					sleep(uniform(0.5, 1.5))
					self.febx(battledome['item1']).click()
					sleep(uniform(1, 2))

				self.febx(battledome['slot2']).click()
				sleep(uniform(0.5, 1.5))
				self.febx(battledome['item2']).click()
				sleep(uniform(1, 2))
				self.febx(battledome['ability']).click()
				sleep(uniform(0.5, 1.5))
				self.febx(battledome['flare']).click()
				sleep(uniform(1, 2))
				self.febx(battledome['fight2']).click()
				sleep(uniform(3, 4.5))

				try:
					self.febx(battledome['skip']).click()
					sleep(uniform(0.5, 1.5))
				except:
					sleep(uniform(4, 7))

				self.febx(battledome['collect']).click()
				sleep(uniform(3, 5))

				fought += 1

				# Count the number of prizes we received for this fight
				prize = 1
				found = True
				while found == True:
					try:
						self.febx(".//*[@id='bd_rewardsloot']/tbody/tr/td[" + str(prize) + "]/img")
						prize += 1
						prizes += 1
					except:
						found = False

				self.fout.write(", %i" % fought)
				self.fout.flush()

				# Don't initiate another battle after our last fight
				if fought < fights:
					self.febx(battledome['again']).click()
					sleep(uniform(5, 10))
				else:
					self.febx(battledome['exit']).click()
					sleep(uniform(3, 5))

			self.fout.write(". Done!\n")
			self.fout.write("Battledome task successfully executed. Received " + str(prizes - fights) + " prizes.\n")
			self.fout.flush()

		except Exception as e:
			self.fout.write("\n")
			self.fout.flush()
			self.fout.write("An error occurred while battling.\n")
			stderr.write("%s\n" % e)
			stderr.flush()

	def lol(self):
		self.fout.write("\n")

	def bar(self):
		self.driver.get(url['bets'])

		trs = self.driver.find_elements(By.TAG_NAME, "tr") 
		tds = trs[1].find_elements(By.TAG_NAME, "td")

		self.fout.write(trs)
		self.fout.write('\n\n')
		self.four.write(tds)
