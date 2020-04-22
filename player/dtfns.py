from datetime import datetime, timedelta
from random import seed, randint

def datetime_string():
	return datetime.now().strftime('%Y-%m-%d|%H:%M:%S')

def generate_cycle_time():
	seed()

	now = datetime.now()

	s = randint(0, 59)
	m = randint(0, 59)
	h = randint(9, 12)

	nxt = now + timedelta(days = 1)
	nxt = nxt.replace(hour = h, minute = m, second = s)

	delta = nxt - now

	return delta.total_seconds()

def generate_sub_time(time):
	seed()

	if time == 'half':
		return randint(2000, 2400)
	elif time == 'thirds':
		return randint(2500, 3000)
	elif time == 'two':
		return randint(7400, 9600)
	elif time == 'six':
		return randint(23000, 34000)
