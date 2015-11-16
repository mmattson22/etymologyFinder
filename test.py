import urllib2
import json
from json2html import *


url='http://api.wordnik.com:80/v4/word.json/equal/etymologies?useCanonical=true&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'


request = urllib2.urlopen(url)
result = request.read()
print result
r = json.loads(result)
print
print r
print
print json2html.convert(json = r)
