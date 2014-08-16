#!/usr/bin/env python2.7

import random
import sys

def roll_d20():
	return random.randint(1,20)

def roll_d6():
	return random.randint(1,6)

def flip_coin():
	return bool(random.getrandbits(1))

def morning():
	direction = roll_d20()
	kilometers = roll_d20() * 10
	direction_string = None
	if direction >= 1 and direction <= 5:
		direction_string = "north"
	elif direction >= 6 and direction <= 10:
		direction_string = "east"
	elif direction >= 11 and direction <= 15:
		direction_string = "south"
	elif direction >= 16 and direction <= 20:
		direction_string = "west"

	print "Go %s for %d kilometers" % (direction_string, kilometers)

def city():
	if flip_coin():
		print "Visit the city."
	else:
		print "Don't visit the city."

def intersection(p):
	if p == 2:
		sys.stdout.write("Two possibilities: ")
		if flip_coin():
			print "Go left."
		else:
			print "Go right."
	else:
		sys.stdout.write("Three possibilities: ")
		direction = roll_d6()
		if direction % 3 == 0:
			print "Go left."
		elif direction % 3 == 1:
			print "Go straight on."
		else:
			print "Go right."

def roundabout(exits):
	print "On a roundabout: Take exit %d." % (roll_d6() % exits)

def rules():
	intersection(2)
	intersection(3)

	for i in range(6):
		if i == 0 or i == 1: continue
		roundabout(i)
	city()


def main():
	morning()
	print
	i = 1
	print "To get the next intersection/roundabout press 'Enter'."

	try:
		while(True):
			print "Intersection/Roundabout %d:" % (i)
			rules()
			i += 1
			raw_input()
	except EOFError:
		sys.exit(0)

if __name__ == "__main__":
	main()
