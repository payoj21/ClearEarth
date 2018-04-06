import os
import sys

def checkillegaloutput(filename, old_path, new_path):

	f = open(old_path+filename,'r')
	print(filename)
	lines = []
	prev_token = ''
	prev_entity = 'O'
	curr_entity = ''
	prev = 'O'
	curr = ''
	count = 0
	count_wrong = 0
	for line in f:
		# print('Previous: '+prev)
		

		if line != '\n':
			print(line)
			content = line.strip('\n').split()
			index = content[0]
			token = content[1]
			entity = content[2]
			# print curr_entity
			if entity != 'O':
				curr_entity = entity.split('-')[0]
				curr = entity.split('-')[1]
				# print(curr)
				# print('Current: '+curr)
				# if prev == 'O' and curr == 'I':
				# 		count += 1
				
				if curr == 'I':

					# print(curr, curr_entity, prev_entity, prev)
					if curr_entity != prev_entity:
						prev_entity = curr_entity
						prev = prev_entity+'-I'
					if prev == 'O':
						prev = curr_entity+'-B'
					# if curr_entity != prev_entity or prev == 'O':
					# 	print(filename, entity, curr_entity+'-'+curr, prev_entity+'-'+prev)
					# 	count_wrong += 1
				lines = lines[:-1]
				lines.append(str(int(index)-1)+'\t'+prev_token+'\t'+prev)
				lines.append(str(index)+'\t'+token+'\t'+curr_entity+'\t'+curr)
				prev_token = token
				prev_entity = curr_entity
			else:
				curr = 'O'
				lines.append(str(index)+'\t'+token+'\t'+curr)
				prev_token = token
				prev_entity = curr
		else:
			curr = 'O'
			lines.append('\n')
			prev_token = '\n'
			prev_entity = curr
			# print('Current: '+curr)
		prev = curr
	f.close()
	fd = open(new_path+filename, 'w')
	for l in lines:
		fd.write(l+'\n')
	fd.close()
	# fd.write('\n')
	# return count, count_wrong


path = ["data/geo/prediction/","data/bio/prediction/","data/sea_ice/prediction/"]
# path = ["data/geo/gold/","data/bio/gold/","data/sea_ice/gold/"]
new_path = ["data/geo/new_prediction/","data/bio/new_prediction/","data/sea_ice/new_prediction/"]
#path = ["data/bio/sample_xml/"]

for i,p in enumerate(path):
	print('\n\nRunning for '+p.split('/')[1].upper())
	count = 0

	new_path = new_path[i]
	print(new_path)
	for filename in os.listdir(p):
		if filename[0] != '.':
			# c, cw = checkillegaloutput(p+filename,new_path)
			checkillegaloutput(filename,p,new_path)
			# count += cw
	# print('Illegal counts for '+p[p.find('/'):p.find('/prediction/')]+' : '+ str(count))

	# print('\n\n')