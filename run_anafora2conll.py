import os
import anafora2conll

path = ["data/geo/xml/","data/bio/xml/","data/sea_ice/xml/"]

for p in path:
	for filename in os.listdir(p):
		if filename[0] != '.':
			anafora2conll.conv2train(filename,p)
