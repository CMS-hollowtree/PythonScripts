#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pywapi, string, random, os, sys 
from termcolor import colored

noaa_result = pywapi.get_weather_from_noaa('KBKL')

strsuchtemp = noaa_result['temp_f'].split(".")
suchtemp = int(strsuchtemp[0])
status = string.lower(noaa_result['weather'])

def dogebanner(responce, temp) :
	os.system('clear')
	colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
	doge = '░░░░░░░░░▄░░░░░░░░░░░░░░▄\n'
	doge += '░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌' 
	doge += '\twow,\n' 
	doge += '░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐\n'
	doge += '░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐' 
	doge += '\t' + responce + '\n'
	doge += '░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐\n'
	doge += '░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌' 
	doge += '\tits currently\n' 
	doge += '░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌ \n' 
	doge += '░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐'
	doge += '\t' + temp + '\n'
	doge += '░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌\n'
	doge += '░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌' 
	doge += '\tF, in Cleveland\n' 
	doge += '▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐\n'
	doge += '▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n'
	doge += '▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐\n'
	doge += '░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌\n'
	doge += '░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐\n'
	doge += '░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌\n'
	doge += '░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀\n'
	doge += '░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀\n'
	doge += '░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀'
	doge = colored(doge, random.choice(colors)) 
	print doge
if (suchtemp <= 0) :
	suchwords = ["winter", "freeze", "polar vortex", "ridiculous", "hibernate", "climate change", "doom"]
elif (suchtemp > 0 and suchtemp <= 10) :
	suchwords = ["cold", "freeze", "shiver", "ice", "yuck", "climate change", "popsicle"]
elif (suchtemp > 10 and suchtemp <= 20) :
	suchwords = ["icy", "winter", "chill", "crisp", "brrrrr", "cool", "not okay"]
elif (suchtemp > 20 and suchtemp <= 30) :
	suchwords = ["icy", "frost", "numb", "shiver", "brrr", "chilly", "below freezing point"]
elif (suchtemp > 30 and suchtemp <= 40) :
	suchwords = ["chilly", "concern", "coat", "frosty", "uh oh", "brrrr", "almost freezing"]
elif (suchtemp > 40 and suchtemp <= 60) :
	suchwords = ["moderate", "mild", "okay", "medium", "cool", "whatever", "brisk"]
elif (suchtemp > 60 and suchtemp <= 75) :
	suchwords = ["heat", "warmth", "climate", "sweating", "balmy", "nice day", "ambient", "excite", "amaze"]
elif (suchtemp > 75) :
	suchwords = ["boiling", "bake", "melt", "dying", "suffer", "global warming", "tropical heat"]
else :
	suchwords = ["concern", "climate", "degrees", "shrug", "wow", "celcius", "farenheit"]

dogewords = ['such ', 'very ', 'much ', 'so ']
suchresponce = random.choice(dogewords) + random.choice(suchwords)

dogebanner(suchresponce, str(suchtemp))
