from ConfigParser import ConfigParser
from neoplayer import Player
from daemonize import Daemon
from dtfns import *
import sys, time

class MyDaemon(Daemon):
	def run(self):
		while True:
			player = Player()

			try:
				player.login()
				player.start()

				seconds = player.sleepfor()
			except Exception as e:
				stderr.write(str(e))

			player.stop()

			six = generate_sub_time('six')
			seconds -= six
			time.sleep(six)

			player = Autoplayer()

			try:
				player.login()
				player.springs()
				player.scratchcard()
			except Exception as e:
				stderr.write(str(e))

			player.lol()
			player.stop()

			time.sleep(seconds)

if __name__ == "__main__":
	parser = ConfigParser()
	parser.read('config.ini')

	stdin	= parser.get('io', 'stdin')
	stdout	= parser.get('io', 'stdout')
	stderr	= parser.get('io', 'stderr')

	pidfile	= parser.get('daemon', 'pidfile')
	daemon = MyDaemon(pidfile, stdin, stdout, stderr)

	if len(sys.argv) == 2:
		if sys.argv[1] == 'start':
			daemon.start()

		elif sys.argv[1] == 'stop':
			daemon.stop()

		elif sys.argv[1] == 'restart':
			daemon.stop()
			time.sleep(1)
			daemon.start()

		sys.exit(0)

	else:
		print "usage: %s start|stop|restart" % sys.argv[0]

		sys.exit(1)
