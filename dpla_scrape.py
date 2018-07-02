import pandas as pd
import requests
import os.path

df = pd.read_csv('ids.csv')

images = [x for x in df.ix[:, 0]]

base = 'https://dp.la/thumb/'

for i in images: 
	if not os.path.isfile('./thumbs/'+i+'.jpg'):
		r = requests.get(base + str(i))
		if r.status_code == 200:
			print("Downloading: ", i)
			with open('./thumbs/'+i+'.jpg',"wb") as f:
				f.write(r.content)
		else:
			with open('error_log.txt', 'a') as f:
				f.write("ERROR: " + i+'\n')
	else: 
		print('ALREADY DOWNLADED ', i)
	
