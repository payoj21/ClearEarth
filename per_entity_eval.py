import sys
import os
# import eval_ner

path = ['data/bio/','data/geo/']
# path = ['data/bio/']
eval_script = 'test_new_eval_script.txt'
filename = 'entity_types.txt'
for p in path:
	f = open(p+filename,'r')
	entity_dict = set()
	for line in f:
		entity_dict.add(line.strip().split('-')[0].lower())

	

	for e in entity_dict:
		fw = open(p+'new_entity_result/'+e+'.txt','w')
		fd = open(p+eval_script, 'r')
		prev_line = ''
		for line in fd:
			if line != '\n':
				l = line.strip()
				content = l.split('\t')
				true = content[1]
				pred = content[2]
				if true.split('-')[0].lower() == e or pred.split('-')[0].lower() == e:
					if prev_line == '\n':
						fw.write('\n')
					fw.write(line)
			prev_line = line
		fw.close()
		fd.close()
		
		# eval_ner.preprocessing(p+'/entity/'+e+'.txt')