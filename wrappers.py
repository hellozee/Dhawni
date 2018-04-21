#!/usr/bin/env python3

import os, subprocess

def volumeInc(percentage):
	if os.system("amixer -D pulse sset Master %s\%+" %(percentage)):
		return True
	return False

def volumeDec(percentage):
	if os.system("amixer -D pulse sset Master %s\%-" %(percentage)):
		return True
	return False

def volumeSet(percentage):
	if os.system("amixer -D pulse sset Master %s\%" %(percentage)):
		return True
	return False

def backlightInc(percentage):
	if os.system("xbacklight -inc %s" %(percentage)):
		return True
	return False

def backlightDec(percentage):
	if os.system("xbacklight -dec %s" %(percentage)):
		return True
	return False

def backlightSet(percentage):
	if os.system("xbacklight -set %s" %(percentage)):
		return True
	return False

def openMusicPlayer(name=None):
	application_desktop = subprocess.Popen(["xdg-mime", "query", "default", "audio/wav"], stdout=subprocess.PIPE).stdout.read()
	possible_execs = []
	if application_desktop and not name:
		with open("/usr/share/applications/%s" %(application_desktop), "r") as f:
			for line in f.readlines():
				if line[:4] in "Exec":
					possible_execs.append(line.split()[0].split("=")[1])

		if len(set(possible_execs)) == 1:
			os.system(possible_execs[0])
			return 2
		
		os.system(possible_execs[0])
		return True
	else:
		print("[WARNING] Could not find xdg default audio player! Trying to use manually set \
		player")
		try:
			os.system(name)
			print("[INFO   ] Opened default web browser")
		except TypeError:
			raise Exception('Could not open default browser. Have you set it?')
		return False

openMusicPlayer("firefox")
