import os
import eval_ner
result_path = ["data/bio/train/"]
output_path = ["data/bio/test/"]
#path = ["data/bio/sample_xml/"]

for i,p in enumerate(result_path):
	print('\n\nRunning for '+p.split('/')[1].upper())
	precision = [] 
	recall = []
	f1 = []
	for filename in os.listdir(p):
		if filename[0] != '.':
			file = filename[:filename.find('.train')]
			print file
			testfile = output_path[i]+file+'.ner'
			pr, r, f = eval_ner.evaluate_ner(p+filename,testfile)
			
			precision.append(pr)
			recall.append(r)
			f1.append(f)

print(precision,recall,f)
avg_p = float(sum(precision))/float(len(precision))
print(avg_p)
avg_r = float(sum(recall))/float(len(recall))
print(avg_r)
print(float(2*avg_p*avg_r)/float(avg_p+avg_r))