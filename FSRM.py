#!/usr/bin/env python3

import requests, codecs, datetime, urllib, os

URL = 'https://fsrm.experiant.ca/api/v1/get'

r = requests.get(URL)
date = r.json()['lastUpdated']['date'].split()[0]
filters = r.json()['filters']
today = datetime.date.today()
patterns = []

def IsToday():
	if ( str(today) != str(date) ):
		return True
	else:
		return False
def XML():
	xml = ""
	xml += '<?xml version="1.0" ?>'
	xml += "\n<Root >"
	xml += "\n\t<Header DatabaseVersion = '2.0' ></Header>"
	xml += "\n\t<QuotaTemplates ></QuotaTemplates>"
	xml += "\n\t<DatascreenTemplates ></DatascreenTemplates>"
	xml += "\n\t<FileGroups >"
	xml += "\n\t\t<FileGroup Name = 'CryptoCanary' Id = '{63475479-1f5f-43c8-bbf5-faafd9aedadf}' Description = '' >"
	xml += "\n\t\t\t<Members >"
	# Patterns
	for pattern in patterns:
		xml += "\n\t\t\t\t<Pattern PatternValue ='" + pattern + "' ></Pattern>"
	# /Patterns
	xml += "\n\t\t\t</Members>"
	xml += "\n\t\t\t<NonMembers ></NonMembers>"
	xml += "\n\t\t</FileGroup>"
	xml += "\n\t</FileGroups>"
	xml += "\n</Root>"
	return xml

def Patterns():
	for ext in filters:
		patterns.append(ext)

if IsToday():
	Patterns()
	print( XML() )

	with open('FSRMpatterns.xml', 'wb') as f:
		f.write(codecs.BOM_UTF16_LE)
		f.write( XML().encode('utf-16-le') )
else:
	print('No updates since ' + str(date) )
