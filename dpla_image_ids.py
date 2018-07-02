from dpla.api import DPLA

dpla = DPLA('your_key_here')

fields = {"sourceResource.type" : "image"}

search_query = '"fourth of july" OR "independence day" OR "July 4th" OR "July Fourth"'

result = dpla.search(search_query, searchFields=fields, page_size=10000)

print(result.count)

with open('ids.csv', "w") as f:
	for x in result.all_records():
		f.write(x['id']+"\n")