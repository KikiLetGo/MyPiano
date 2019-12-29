import pygame
import time
import threading
pygame.init()
pygame.mixer.init()

for i in range(0,5):
	index = 21+i*10
	pygame.mixer.music.load("./mp3source/"+str(index)+".mp3")

def play_music(path):
	print("start")

	
	pygame.mixer.music.play(start=0.2)

def onKeyPress(key):

	musicPath = "./source/German Concert D 021 083.wav"
	if key == pygame.K_1:
		musicPath = "./mp3source/21.mp3"
	elif key == pygame.K_2:
		musicPath = "./mp3source/31.mp3"
	elif key == pygame.K_3:
		musicPath = "./mp3source/41.mp3"
	elif key == pygame.K_4:
		musicPath = "./mp3source/51.mp3"
	elif key == pygame.K_5:
		musicPath = "./mp3source/61.mp3"
	elif key == pygame.K_6:
		musicPath = "./mp3source/71.mp3"
	elif key == pygame.K_7:
		musicPath = "./mp3source/81.mp3"
	else:
		pass


	t = threading.Thread(target=play_music, args=(musicPath,))
	t.start()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			onKeyPress(event.key)
			
		elif event.type == pygame.KEYUP:
			#time.sleep(0.5)
			print("up")
			pygame.mixer.music.pause()