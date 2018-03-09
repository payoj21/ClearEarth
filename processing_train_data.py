import os
from collections import defaultdict

def num_of_entities(filename, entity_dict):
	# entities = set()
	# entity_dict = defaultdict(set())
	f = open(filename,'r')
	entity_name = ''
	entity_type = ''
	prev_pos = 'O'
	curr_pos = 'O'
	for line in f:

		# print('length ',len(line))
		if line != '\n':
			prev_pos = curr_pos
			text = line.strip().split()
			token = text[0]
			entity = text[3]
			if entity != 'O':
				entity = entity.split('-')
				
				entity_type_position = entity[1]
				curr_pos = entity_type_position
				if curr_pos == 'B':
					if prev_pos == 'I' or prev_pos == 'B':
						# print('ENTITY: ', entity_name, 'ENTITY TYPE: ',entity_type)
						entity_dict[entity_type]['Tokens'].add(entity_name)

					entity_type = entity[0]
					entity_name = token
					# prev_pos = 'O'
					if entity_type not in entity_dict:
						# print('TOKEN: ',token, 'TYPE: ', entity_type)
						entity_dict[entity_type] = {'Occurences':1,'Tokens': set()}
					else:
						# print('TOKEN: ',token, 'TYPE: ', entity_type)
						entity_dict[entity_type]['Occurences'] += 1
					

				if curr_pos == 'I':
					entity_name += ' '+token

			else:
				curr_pos = 'O'
				if prev_pos == 'I' or prev_pos == 'B':
					# print('ENTITY: ', entity_name, 'ENTITY TYPE: ',entity_type)
					# print(line)
					# print(entity_type, entity_name)
					entity_dict[entity_type]['Tokens'].add(entity_name)
				entity_name = ''
				entity_type = ''
		else:
			curr_pos = 'O'
			entity_name = ''
	# return len(entities), entities, entity_dict

	f.close()
	
path = ["data/geo/train/","data/bio/train/","data/sea_ice/train/"]
# path = ["data/bio/sample_train/"]

for p in path:
	# entities = set()

	entity_dict = defaultdict()
	print('\n\nRunning for '+p.split('/')[1].upper()+'\n\n')
	for filename in os.listdir(p):
		if filename[0] != '.':
			print(filename)
			num_of_entities(p+filename,entity_dict)
	folders = p.split('/')

	f = open(folders[0]+'/'+folders[1]+'/'+folders[1]+'_Entities.txt', 'w')
	f.write('Total number of entity types: '+str(len(entity_dict))+'\n\n')
	for e in entity_dict:
		f.write(e.upper()+'\nTotal occurences: '+str(entity_dict[e]['Occurences'])+'\n')
		tokens = str(entity_dict[e]['Tokens']).strip('{').strip('}')
		f.write('Total Unique entities: '+ str(len(entity_dict[e]['Tokens']))+'\n')

		avg = float(entity_dict[e]['Occurences'])/float(len(entity_dict[e]['Tokens']))
		
		f.write('Average Frequency of each token: '+str(avg)+'\n')
		f.write(tokens+'\n\n\n')

	