from pyvirtualdisplay import Display
from neoplayer import Player
from sys import stderr

#display = Display(visible = 1, size = (1920, 1080)).start()

try:
	player = Player()
	player.login()
	player.bet()
except KeyboardInterrupt:
	print "\nPlayer terminated.\n"

#display.stop()
