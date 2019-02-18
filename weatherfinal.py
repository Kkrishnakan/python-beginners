import urllib
#from BeautifulSoup import *
import xml.etree.ElementTree as ET
import re
import subprocess
def sendmsg(msg):
	subprocess.Popen(['notify-send',msg])
	return
cont=True
print ("\t\t\tIndia Weather by Krishna \n\nThis little program is a quick solution all your weather queries regarding whatever Indian city you have in mind. \nPlease use full city names ( New Delhi is not Delhi )")
while cont==True:
	city=raw_input('Enter the City : Australia')
	cityurl='http://rss.wunderground.com/cgi-bin/findweather/getForecast?query='+city
	cityxml=urllib.urlopen(cityurl).read()
	citysoup=BeautifulSoup(cityxml)
	tags=citysoup('link')
	tag=str(tags[1])
	llst=re.findall('.alternate.*href="(.*)"',tag)
	link=urllib.urlopen(llst[0])
	dat=ET.fromstring(link.read())
	a=dat.find('.//item')
	string=a.find('title').text
	temp=re.findall('.Conditions : ([0-9]*.[0-9]+)',string)
	atemp=float(temp[0])
	ftemp=(atemp-32)*(5/9.0)
	msg= "The present tempertaure in "+city+" is : "+"%.2f"%ftemp+" Degree Celsius"
	sendmsg(msg)
	p=raw_input("Continue ? <y/n>: y")
	if p =="n":
		cont=False
