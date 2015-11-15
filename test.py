import urllib2
import json

#url = "https://www.google.com/#safe=off&q=iguana"

url='http://api.wordnik.com:80/v4/word.json/Title/etymologies?useCanonical=true&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
"""

request = urllib2.urlopen(url)
result = request.read()
r = json.loads(result)
print result
print "\n"
print r
print "\n"
print r.keys()

url='http://api.openweathermap.org/data/2.5/weather?q="nyc"&appid=ecdb9f3fb43f5f8663867db2633c7638&units=imperial'
"""

request = urllib2.urlopen(url)
result = request.read()
r = json.loads(result)
print result
print
print r
print
print r.keys()
print r['main']
print r['main']['temp']
