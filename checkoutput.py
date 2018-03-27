import os
import sys

def checkillegaloutput(filename):

	f = open(filename,'r')
	prev_entity = 'O'
	curr_entity = ''
	prev = 'O'
	curr = ''
	count = 0
	count_wrong = 0
	for line in f:
		# print('Previous: '+prev)
		

		if line != '\n':

			entity = line.strip('\n').split()[2]
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
					if curr_entity != prev_entity or prev == 'O':
						print(curr_entity+'-'+curr, prev_entity+'-'+prev)
						count_wrong += 1
				prev_entity = curr_entity
		else:
			curr = 'O'
			prev_entity = curr
			# print('Current: '+curr)
		prev = curr
		
	return count, count_wrong


path = ["data/geo/prediction/","data/bio/prediction/","data/sea_ice/prediction/"]
# path = ["data/geo/gold/","data/bio/gold/","data/sea_ice/gold/"]

#path = ["data/bio/sample_xml/"]

for p in path:
	print('\n\nRunning for '+p.split('/')[1].upper())
	count = 0
	for filename in os.listdir(p):
		if filename[0] != '.':
			c, cw = checkillegaloutput(p+filename)
			count += cw

	print('Illegal counts for '+p[p.find('/'):p.find('/prediction/')]+' : '+ str(count))

	print('\n\n')