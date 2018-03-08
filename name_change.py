import os

path_xml = ["data/geo/xml/","data/bio/xml/","data/sea_ice/xml/"]
path_txt = ["data/geo/txt/","data/bio/txt/","data/sea_ice/txt/"]

for p in path_xml:
	for filename in os.listdir(p):
		if filename[0] != '.':
			text = filename.split('.')
			print text
			new_name = text[0]+'.xml'
			print new_name
			os.rename(p+filename,p+new_name)

for p in path_txt:
	for filename in os.listdir(p):
		if filename[0] != '.':
			new_name = filename+'.txt'
			os.rename(p+filename,p+new_name)
