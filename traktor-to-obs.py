import re
import string
import time
import os

timer = 15
base_directory = "v:\\"
file_current  = "current_song.txt"

file_list = []

print("Timer: " + str(timer))
print("Base directory: " + base_directory)
print("---------------")

while 1:

	dirs = os.listdir( base_directory )

	files = sorted((f for f in os.listdir(base_directory) if f.find('Playlist_') != -1), 
               key=lambda f: os.stat(os.path.join(base_directory, f)).st_mtime)
	recent = files[-1]

	print("Recent file found: " + recent)

	f = open(base_directory + recent)
	lineList = f.readlines()
	f.close()
	song = lineList[-1]
	song = song.split(' ', 1)[-1]
# 
	print("Current song: " + song)

	with open(base_directory + file_current, "w") as text_file:
		text_file.write(format(song))

	time.sleep(timer)
