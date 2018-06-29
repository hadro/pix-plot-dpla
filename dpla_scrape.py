import pandas as pd
import requests
import os.path

df = pd.read_csv('ids.csv')

images = [x for x in df.ix[:, 0]]

base = 'https://dp.la/thumb/'

for i in images: 
	r = requests.get(base + str(i))
	header = r.headers#
	if r.status_code == 200:
		if not os.path.isfile('./thumbs/'+i+'.jpg'):
			print("Downloading: ", i)
			with open('./thumbs/'+i+'.jpg',"wb") as f:
				f.write(r.content)
		else: 
			print('ALREADY DOWNLOADED: ', i)
	else:
		with open('error_log.txt', 'a') as f:
			f.write("ERROR: " + i+'\n')
