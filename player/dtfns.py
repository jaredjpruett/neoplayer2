from datetime import datetime, timedelta
from random import seed, randint

def datetime_string():
	now = datetime.now()

	return now.strftime('%Y - %m - %d | %H : %M : %S')

def datetime_list(now):
	return [int(i) for i in now.split() if i.isdigit()]

def datetime_seconds(nownums, nxtnums):
	time = (nxtnums[5] - nownums[5]) + (nxtnums[4] - nownums[4]) * 60 + (nxtnums[3] - nownums[3]) * 3600
	if nxtnums[2] != nownums[2]: time += 86400

	return time

def generate_time():
	seed()

	s = randint(0, 59)
	m = randint(0, 59)
	h = randint(9, 12)

	when = datetime.now() + timedelta(days = 1)
	when = when.replace(hour = h, minute = m, second = s)
	when = when.strftime('%Y - %m - %d | %H : %M : %S')

	return when

def generate_time_for(time):
	seed()

	if time == 'half':
		return randint(2000, 2400)
	elif time == 'thirds':
		return randint(2500, 3000)
	elif time == 'two':
		return randint(7400, 9600)
	elif time == 'six':
		return randint(22222, 33333)
