import os
import anafora2conll

path = ["data/geo/xml/","data/bio/xml/","data/sea_ice/xml/"]
#path = ["data/bio/sample_xml/"]

for p in path:
	print('\n\nRunning for '+p.split('/')[1].upper())
	for filename in os.listdir(p):
		if filename[0] != '.':
			anafora2conll.conv2train(filename,p)
