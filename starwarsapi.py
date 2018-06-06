from sys import argv
import requests
def starwarsapi(people):
	url="https://swapi.co/api/people"
	data={
			"people":search
	}
	r=requests.get(url=url,json=data)
	return r.json()
	
search=argv[1]
d=starwarsapi(search)
#print result
for i in d['results']:
	print i['name']