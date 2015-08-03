import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Vadodara,in')
print r.encoding
print r.status_code
print r.json()
