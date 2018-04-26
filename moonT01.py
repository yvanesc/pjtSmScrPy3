#!/usr/bin/python
# -*- coding: utf-8 -*-

#import urllib2
from urllib.request import urlopen
import simplejson as json

datasource = "http://api.wunderground.com/api/a71894d18588a38f/forecast/q/CH/Lausanne.json"
datasource1 = "http://api.wunderground.com/api/a71894d18588a38f/astronomy/q/CH/Lausanne.json"
page = urlopen(datasource)
page1 = urlopen(datasource1)
weather = json.load(page)
astro = json.load(page1)
detail = weather['forecast']['simpleforecast']['forecastday']
detail1 = astro['moon_phase']['percentIlluminated']#['forecastday']
#moonphase = astro['percentIlluminated']
for day in detail:
    weatherdate = day['date']['weekday']
    weatherhigh = day['high']['celsius'] + u'\xb0' + "C"
    weatherlow = day['low']['celsius'] + u'\xb0' + "C"
    weatherpop = str(day['pop']) + "%"
    print (weatherdate)
    print ("\tHigh:\t\t%s" % weatherhigh)
    print ("\tLow:\t\t%s" % weatherlow)
    print ("\tChance of rain:\t%s" % weatherpop)
    
print ("\nPercent moon phase:\t%s" % detail1    )
print ("-----------------------------")
