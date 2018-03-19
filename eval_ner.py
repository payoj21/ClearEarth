import sys
import os
from collections import defaultdict

def preprocessing(filename):
    lines = []

    f = open(filename, 'r')
    for line in f:
        if line != '\n':
            lines.append(line)

    f.close()
    f = open(filename,'w')
    count = 1
    for i,line in enumerate(lines):
        if line.split()[1] == '.':
            f.write(line+'\n')
            count = 0
        else:
            f.write(str(count)+'\t'+line.split()[1]+'\t'+line.split()[2]+'\n')
        count += 1
    f.close()

def join(c,p,gold,predict):
    print gold
    fg = open(gold,'r')
    fp = open(predict, 'r')
    fw = open(p[:p.find('/prediction/')]+'/evaluate_script'+'.txt','a')
    g_dict = defaultdict(list)
    lineg = []
    count = 0
    for line in fg:
        if line != '\n':
            lineg.append(line)
        else:
            # print lineg
            g_dict[count] = lineg
            lineg = []
            count += 1
    p_dict = dict()
    linep = []
    count = 0
    for line in fp:
        if line != '\n':
            linep.append(line)
        else:
            p_dict[count] = linep
            linep = []
            count += 1

    for i in range(count+1):
        j = 0
        # print(i, len(g_dict))
        while( j< len(g_dict[i]) and j < len(p_dict[i]) and i in g_dict and i in p_dict):
            if g_dict[i][j].split()[1] == p_dict[i][j].split('\t')[1]:
                print(g_dict[i][j].split()[1])
                fw.write(g_dict[i][j].split()[1]+'\t'+g_dict[i][j].split()[2]+'\t'+p_dict[i][j].split()[2]+'\n')
            j += 1
        fw.write('\n')
    fw.close()
path = ["data/bio/prediction/"]


for p in path:
    print('\n\nRunning for '+p.split('/')[1].upper())
    i = 0
    for filename in os.listdir(p):
        if filename[0] != '.':
            preprocessing(p+filename)
            join(i,p,p[:p.find('prediction/')]+'gold/'+filename[:filename.find('.ner')]+'.train',p+filename)
            i += 1
