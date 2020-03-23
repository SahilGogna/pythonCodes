import requests
r = requests.get('https://pomber.github.io/covid19/countries.json')
data = r.json()

keys = data.keys()
values = data.values()

# print(len(values))  // counting length of the dictionary

count = 0
for value in values:
    print(value.get('code'))
    count = count+1

print(count)