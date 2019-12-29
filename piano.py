#!/usr/bin/python
# encoding:utf-8
 
import pyaudio
import wave
import threading
import time
import pygame
import sys
import os
pygame.init()
p = pyaudio.PyAudio()
pressDict={"1":False,"2":False,"3":False}

keyDict={
	pygame.K_1:"c",
	pygame.K_2:"d",
	pygame.K_3:"e",
	pygame.K_4:"f",
	pygame.K_5:"g",
	pygame.K_6:"a",
	pygame.K_7:"b",
	pygame.K_8:"c1",
	pygame.K_9:"d1",
	pygame.K_0:"e1",
	pygame.K_MINUS:"f1",

	pygame.K_EQUALS:'g1',
	pygame.K_q:'a1',
	pygame.K_w:'b1',
	pygame.K_e:'c2',
	pygame.K_r:'d2',
	pygame.K_t:'e2',
	pygame.K_y:'f2',
	pygame.K_u:'g2',
	pygame.K_i:'a2',
	pygame.K_o:'b2',
	pygame.K_p:'c3',
	pygame.K_a:'d3',
	pygame.K_s:'e3',
	pygame.K_d:'f3',
	pygame.K_f:'g3',
	pygame.K_g:'a3',
	pygame.K_h:'b3',

	pygame.K_j:'c4',
	pygame.K_k:'d4',
	pygame.K_l:'e4',
	pygame.K_z:'f4',
	pygame.K_x:'g4',
	pygame.K_c:'a4',
	pygame.K_v:'b4',
	pygame.K_b:'c5'


}



def play(path,key):
	CHUNK = 1024
	# 从目录中读取语音
	wf = wave.open(path, 'rb')
	# read data
	data = wf.readframes(CHUNK)
	# 创建播放器
	global p
	

	# 获得语音文件的各个参数
	FORMAT = p.get_format_from_width(wf.getsampwidth())
	CHANNELS = wf.getnchannels()
	RATE = wf.getframerate()
	print(keyDict[key],end=' ')
	sys.stdout.flush() 
	# 打开音频流， output=True表示音频输出

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                frames_per_buffer=CHUNK,
	                output=True)
	# play stream (3) 按照1024的块读取音频数据到音频流，并播放
	while len(data) > 0:
	    stream.write(data)
	    data = wf.readframes(CHUNK)
	    # if not pressDict[key]:
	    # 	break


while True:
	time.sleep(0.01)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			key = event.key
			if(key == pygame.K_ESCAPE):
				pygame.quit()

			elif key in keyDict.keys():
				fileName = "./audios/"+str(keyDict[key])+".wav"
				if os.path.exists(fileName):
					threading.Thread(target=play, args=(fileName,key)).start()



			

			
		elif event.type == pygame.KEYUP:
			#time.sleep(0.5)
			key = event.key
			pressDict[key]=False



	



