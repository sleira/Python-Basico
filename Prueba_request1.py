import requests
url="https://jsonplaceholder.typicode.com/posts"

r = requests.get(url)

datos = r.json()

for d in datos:
	print(d["title"])
	print("************************")