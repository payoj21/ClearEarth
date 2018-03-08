import os


f = open('sea_ice.txt','r')

for line in f:
	line = line.strip('\n')
	txt = line.split('.')
	txtfile = txt[0]
	string1 = "scp -r paja3104@verbs.colorado.edu:/data/clearearth/anaforaProjectFile/sea-ice/"+line+" /Users/payoj/Documents/Spring\ 2018/Independent\ Study\ \(ClearEarth\)/data/sea_ice/xml/"
	string2 = "scp -r paja3104@verbs.colorado.edu:/data/clearearth/anaforaProjectFile/sea-ice/"+txtfile+" /Users/payoj/Documents/Spring\ 2018/Independent\ Study\ \(ClearEarth\)/data/sea_ice/txt/"
	
	os.system(string1)
	os.system(string2)

