piano_keys=["A2","A2#","B2",
"_C1","_C1#","_D1","_D1#","_E1","_F1","_F1#","_G1","_G1#","_A1","_A1#","_B1",
"_C","_C#","_D","_D#","_E","_F","_F#","_G","_G#","_A","_A#","_B",
"c","c#","d","d#","e","f","f#","g","g#","a","a#","b",
"c1","c1#","d1","d1#","e1","f1","f1#","g1","g1#","a1","a1#","b1",
"c2","c2#","d2","d2#","e2","f2","f2#","g2","g2#","a2","a2#","b2",
"c3","c3#","d3","d3#","e3","f3","f3#","g3","g3#","a3","a3#","b3",
"c4","c4#","d4","d4#","e4","f4","f4#","g4","g4#","a4","a4#","b4",
"c5"
]

import os
dirpath = os.path.abspath('audios/')
files = os.listdir(dirpath)
files.sort()
index=0
for file in files:
	os.rename(dirpath+file,dirpath+piano_keys[index]+".wav")
	index = index+1
