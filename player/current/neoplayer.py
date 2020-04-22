from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from ConfigParser import ConfigParser

from pyvirtualdisplay import Display

from random import uniform
from time import sleep
from sys import stderr, exit

from foodclub import *
from dtfns import *
from xpath import *
from url import *

class Player():
	parser		= ConfigParser()
	parser.read('config.ini') # ?? lel
	username	= parser.get('account', 'username')
	password	= parser.get('account', 'password')
	profile		= parser.get('player', 'profile')
	log			= parser.get('io', 'logfile')

	def __init__(self):
		self.display	= Display(visible = 0, size = (1920, 1080)).start()
		self.driver		= WebDriver(firefox_profile = FirefoxProfile(self.profile))
		self.fout		= open(self.log, 'a')
		self.attempt	= 0
		self.febx		= self.driver.find_element_by_xpath
		
		#self.driver.set_window_size(1280, 800)

	# TODO: Delegate to main.py
	def start(self):
		# Ensure we have 5,000 dosh on-hand
		#self.five()

		self.dailies()
		self.winnings()
		#self.foodclub()
		#self.battle()
		self.safe()
		self.deposit()

	def stop(self):
		self.fout.close()
		self.driver.quit()
		self.display.stop()

	def login(self):
		self.driver.get(url['main'])
		sleep(uniform(1.5, 3.5))

		try:
			# Open login popup
			self.febx(xpath['login']).click()
			sleep(uniform(0.5, 1))
			# Enter username
			ufield = self.febx(xpath['username'])
			ufield.click()
			sleep(uniform(0.5, 1.0))
			ufield.send_keys(self.username)
			sleep(uniform(0.5, 1.0))
			# Enter password
			pfield = self.febx(xpath['password'])
			pfield.click()
			sleep(uniform(0.5, 1.0))
			pfield.send_keys(self.password)
			sleep(uniform(0.5, 1.0))
			# Click login button
			self.febx(xpath['button']).click()
			sleep(uniform(5, 10))

			self.fout.write("Successfully logged into " + self.username + ".\n")
			self.fout.flush()

			# Verify login
			try:
				if self.febx(xpath['loggedin']).text == "asdf":
					self.fout.write("Successful login confirmed.\n")
					self.fout.flush()
				else:
					self.fout.write("Successful login not confirmed wat\n")
					self.fout.write("\t" + self.febx(xpath['loggedin']).text + "\n")
					self.fout.flush()
			except:
				stderr.write("Failed to find username element during login confirmation.\n")

			return self
		except:
			self.attempt = self.attempt + 1
			self.fout.write("Login failed.\n")
			self.fout.flush()
			sleep(uniform(1, 2))

			if self.attempt < 3:
				self.login()
			else:
				raise Exception("Could not log in.")

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

		self.springs()

	# Action wrapper
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

	# TODO: Move this to main.py
	def sleepfor(self):
		seconds = generate_cycle_time()

		self.fout.write("Sleeping for " + str(seconds) + " seconds.\n\n")
		self.fout.flush()

		return seconds

########################################################################################################################
##                                                                                                                    ##
##                                                                                                                    ##
##                                                                                                                    ##
########################################################################################################################

	def five(self):
		dosh = self.dosh()

		if dosh < 5000:
			self.bank('withdraw', 5000 - dosh)
		if dosh > 5000:
			self.deposit()

	def springs(self): # look into suppressing purchase confirmation
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

	def bank(self, action, amount):
		self.driver.get(url['bank'])
		sleep(uniform(2, 4))

		try:
			self.febx(xpath[action]).send_keys(str(amount) + Keys.RETURN)
			sleep(uniform(4, 7))
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

	# Detect how much dosh we have on hand
	def dosh(self):
		try:
			amount = self.febx(xpath['dosh']).text.replace(',', '')
			return int(amount)
		except:
			print "An error occurred. Could not detect dosh.\n"
			return 0

	# Deposit items on hand into SDB
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
		fights = 15
		fought = 0
		prizes = 0

		self.driver.get(battledome_url['main'])

		self.fout.write("Battling. Beaten 0")
		self.fout.flush()

		try:
			self.febx(battledome_x['battle1']).click()
			sleep(uniform(1, 1.5))

			# If we're already in battle, skip this section
			try:
				self.febx(battledome_x['continue1']).click()
				sleep(uniform(1, 2))
				self.febx(battledome_x['continue2']).click()
				sleep(uniform(2.5, 3.5))
				self.febx(battledome_x['chiaclown']).click()
				sleep(uniform(1, 2.5))
				self.febx(battledome_x['battle2']).click()
				sleep(uniform(10, 15))
			except:
				pass

			#while prizes < 15:
			while fought < fights:
				try:
					# We should be at this screen right now
					self.febx(battledome_x['fight1']).click()
					sleep(uniform(3.5, 5))
				except:
					# But if fucking not, somehow, try the beginning again
					try:
						# Let's also try this, why not
						try:
							self.febx(battledome_x['battle1']).click()
							sleep(uniform(1, 1.5))
						except:
							pass

						self.febx(battledome_x['continue1']).click()
						sleep(uniform(1, 2))
						self.febx(battledome_x['continue2']).click()
						sleep(uniform(2.5, 3.5))
						self.febx(battledome_x['chiaclown']).click()
						sleep(uniform(1, 2.5))
						self.febx(battledome_x['battle2']).click()
						sleep(uniform(10, 15))
						self.febx(battledome_x['fight1']).click()
						sleep(uniform(3.5, 5))
					except Exception as e:
						self.fout.write("\n")
						self.fout.write("I don't even fucking know anymore.\n")
						self.fout.flush()
						stderr.write("%s\n" % e)
						stderr.flush()

				self.febx(battledome_x['slot1']).click()
				sleep(uniform(0.5, 1.5))

				try:
					self.febx(battledome_x['item1']).click()
					sleep(uniform(1, 2))
				except:
					self.fout.write(", %ih" % fought + 1)
					self.fout.flush()
					self.febx(battledome_x['slot1']).click()
					sleep(uniform(0.5, 1.5))
					self.febx(battledome_x['item1']).click()
					sleep(uniform(1, 2))

				self.febx(battledome_x['slot2']).click()
				sleep(uniform(0.5, 1.5))
				self.febx(battledome_x['item2']).click()
				sleep(uniform(1, 2))
				self.febx(battledome_x['ability']).click()
				sleep(uniform(0.5, 1.5))
				self.febx(battledome_x['flare']).click()
				sleep(uniform(1, 2))
				self.febx(battledome_x['fight2']).click()
				sleep(uniform(3, 4.5))

				try:
					self.febx(battledome_x['skip']).click()
					sleep(uniform(0.5, 1.5))
				except:
					sleep(uniform(4, 7))

				self.febx(battledome_x['collect']).click()
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
					self.febx(battledome_x['again']).click()
					sleep(uniform(5, 10))
				else:
					self.febx(battledome_x['exit']).click()
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

	def foo(self):
		self.driver.get(battledome_url['stats'])
		sleep(uniform(4, 6))
		self.febx(battledome_stats['pet2']).click()

		pet = self.febx(battledome_stats['name']).text
		hunger = self.febx(battledome_stats['hunger']).text
		hitpoints = self.febx(battledome_stats['hitpoints']).text
		attack = self.febx(battledome_stats['attack']).text
		defense = self.febx(battledome_stats['defense']).text
		agility = self.febx(battledome_stats['agility']).text
		intelligence = self.febx(battledome_stats['intelligence']).text
		level = self.febx(battledome_stats['level']).text

		self.fout.write(pet + '\n')
		self.fout.write(hunger + '\n')
		self.fout.write(hitpoints + '\n')
		self.fout.write(attack + '\n')
		self.fout.write(defense + '\n')
		self.fout.write(agility + '\n')
		self.fout.write(intelligence + '\n')
		self.fout.write(level + '\n')

	def foodclub(self):
		bets_arenas_list = []
		bets_pirates_list = []

		self.driver.get(url_foodclub['hugo'])
		sleep(uniform(2, 4))

		# 1 - 12 ??? confus
		for i in range(1, 11):
			bets_arenas = []
			bets_pirates = []

			# Retrieve individual bets as a Selenium element
			bet1 = self.febx(xpath_foodclub['bet' + str(i)])
			# Each line is an individual arena and its pirate
			bets1 = bet1.text.rstrip().split('\n')
			
			# Parse list into two parallel lists
			for bet in bets1:
				for arena in arenas:
					if arena in bet:
						bets_arenas.append(arena)
						for pirate in pirates:
							if pirate in bet:
								bets_pirates.append(pirate)

			# Add lists to lists of lists
			bets_arenas_list.append(bets_arenas)
			bets_pirates_list.append(bets_pirates)

		# Withdraw betting money
		self.driver.get(url_foodclub['place'])
		amount = self.febx(xpath_foodclub['amount']).text
		self.driver.get(url['bank'])
		self.bank('withdraw', int(amount) * 10)

		self.driver.get(url_foodclub['place'])
		sleep(uniform(1, 3))

		# Place bets
		for i in range(0, 10):
			for j in range(0, len(bets_arenas_list[i])):
				self.febx(xpath_foodclub[bets_arenas_list[i][j]]).click()
				sleep(uniform(0.5, 1))
				Select(self.febx(xpath_foodclub[bets_arenas_list[i][j] + "2"])).select_by_value(str(dict_pirates[bets_pirates_list[i][j]]))
				sleep(uniform(0.5, 1))
			field = self.febx(xpath_foodclub['bet_field'])
			field.click()
			sleep(uniform(1, 2))
			field.send_keys(Keys.DELETE + amount)
			sleep(uniform(1, 2))
			self.febx(xpath_foodclub['place']).click()
			sleep(uniform(2, 3))
			self.driver.get(url_foodclub['place'])
			sleep(uniform(1, 2))


if __name__ == '__main__':
	player = Player()
	player.login()
	player.start()
	player.stop()
