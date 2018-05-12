import os


f = open('geology.txt','r')

for line in f:
	line = line.strip('\n')
	txt = line.split('.')
	txtfile = txt[0]
	string1 = "scp -r paja3104@verbs.colorado.edu:/data/clearearth/anaforaProjectFile/geo/"+line+" /Users/payoj/Documents/Spring\ 2018/Independent\ Study\ \(ClearEarth\)/data/geo/xml_test/"
	string2 = "scp -r paja3104@verbs.colorado.edu:/data/clearearth/anaforaProjectFile/geo/"+txtfile+" /Users/payoj/Documents/Spring\ 2018/Independent\ Study\ \(ClearEarth\)/data/geo/txt_test/"
	
	os.system(string1)
	os.system(string2)

