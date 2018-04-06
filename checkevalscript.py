import os
import sys

def checkillegaloutput(filename, new_file_path):

	f = open(filename,'r')
	print(filename)
	lines = []
	prev_token = ''
	prev_gold = ''
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
			# index = content[0]
			token = content[0]
			gold = content[1]
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
						curr_entity = prev_entity
						# prev = prev_entity+'-I'
					if prev == 'O':
						prev_entity = curr_entity
						prev = 'B'
					# if curr_entity != prev_entity or prev == 'O':
					# 	print(filename, entity, curr_entity+'-'+curr, prev_entity+'-'+prev)
					# 	count_wrong += 1
					lines = lines[:-1]
					lines.append(prev_token+'\t'+prev_gold+'\t'+prev_entity+'-'+prev)
				lines.append(token+'\t'+gold+'\t'+curr_entity+'-'+curr)
				prev_token = token
				prev_gold = gold
				prev_entity = curr_entity
			else:
				curr = 'O'
				lines.append(token+'\t'+gold+'\t'+curr)
				prev_token = token
				prev_gold = gold
				prev_entity = curr
		else:
			curr = 'O'
			lines.append('\n')
			prev_token = '\n'
			prev_entity = curr
			# print('Current: '+curr)
		prev = curr
	f.close()
	fd = open(new_file_path, 'w')
	for l in lines:
		if l !='\n':
			fd.write(l+'\n')
		else:
			fd.write(l)
	fd.close()
	# fd.write('\n')
	# return count, count_wrong


# path = ["data/geo/prediction/","data/bio/prediction/","data/sea_ice/prediction/"]
# # path = ["data/geo/gold/","data/bio/gold/","data/sea_ice/gold/"]
# new_path = ["data/geo/new_prediction/","data/bio/new_prediction/","data/sea_ice/new_prediction/"]
#path = ["data/bio/sample_xml/"]
file_path = ["data/geo/test_eval_script.txt", "data/bio/test_eval_script.txt"]
new_file_path = ["data/geo/test_new_eval_script.txt", "data/bio/test_new_eval_script.txt"]
for i,p in enumerate(file_path):
	print('\n\nRunning for '+p.split('/')[1].upper())
	count = 0

	new_file = new_file_path[i]
	print(new_file_path)
	# for filename in os.listdir(p):
	# 	if filename[0] != '.':
			# c, cw = checkillegaloutput(p+filename,new_path)
	checkillegaloutput(p,new_file)
			# count += cw
	# print('Illegal counts for '+p[p.find('/'):p.find('/prediction/')]+' : '+ str(count))

	# print('\n\n')