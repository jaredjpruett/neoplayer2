from autoplayer import Autoplayer
from daemonize import Daemon
from dtfns import *
import sys, time

class MyDaemon(Daemon):
    def run(self):
        username = ''
        password = ''

        while True:
            player = Autoplayer()
            seconds = player.start(username, password)
            player.stop()
            six = generate_time_for('six')
            seconds = seconds - six
            time.sleep(six)

            player = Autoplayer()
            player.login(username, password)
            player.springs()
            player.scratchcard()
            player.safe()
            player.lol()
            player.stop()
            time.sleep(seconds)

if __name__ == "__main__":
    pidfile = '/tmp/autoplayer.pid'
    stdin = '/dev/null'
    stdout = 'stdout.txt'
    stderr = 'stderr.txt'

    daemon = MyDaemon(pidfile, stdin, stdout, stderr)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            daemon.start()

        elif sys.argv[1] == 'stop':
            daemon.stop()

        elif sys.argv[1] == 'restart':
            daemon.stop()
            daemon.start()

        sys.exit(0)

    elif len(sys.argv) == 1:
        daemon.start()

    else:
        print "usage: %s start|stop|restart" % sys.argv[0]

        sys.exit(1)
