import subprocess
from random import randint

def generate_random_sentence():
	sentence = ''	
	sz = 20597
	r = 0
	while (sentence == '' or len(sentence) > 280):
		while (r + 3 <= sz):
			r = randint(1, sz + 1)
		s = "sed -n '" + str(r) + "," + str(r + 3) + "p' ./data/all_songs.txt" 
		sentence = subprocess.call([s], shell = True)	
	return sentence

