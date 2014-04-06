#!/usr/bin/env python

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

# Definition of paths on server
# log file location
LogfileName = "/home/pi/Radiorecorder/recorder.log"
# output RSS filename
rssFileName = "/home/pi/Radiorecorder/podcast.rss"

# podcast meta data
# podcast name
rssTitle = "Radiorecorder"
# podcast description
rssDescription = "Recorded radio shows by cosmovisionas"
# url of the folder where the items will be stored
rssItemURL = "http://cosmovisionas.de/records"
# url to the podcast html file
rssLink = "http://cosmovisionas.de"
# url to the podcast image
rssImageUrl = "http://cosmovisionas.de/records/image.jpg"
# contact details of the web master
rssWebMaster = "mail@cosmovisionas.de"

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

# Main program

# import libraries
import os
import sys
import datetime
import time

# import constants from stat library
from stat import * # ST_SIZE ST_MTIME

# format date method
def formatDate(dt):
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")

# format date method
def formatTimeStamp(dt):
    return dt.strftime("%d.%m.%Y")

now = datetime.datetime.now()

# open logfile and read into list
Logfile = open(LogfileName) 
downloadHistory = Logfile.readlines() 
Logfile.close()

# open rss file
rssFile = open(rssFileName, "w")

# write rss header
rssFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>" + "\n")
rssFile.write("<rss version=\"2.0\">" + "\n")
rssFile.write("<channel>\n")
rssFile.write("<title>" + rssTitle + "</title>\n")
rssFile.write("<description>" + rssDescription + "</description>\n")
rssFile.write("<link>" + rssLink + "</link>\n")
rssFile.write("<image><url>" + rssImageUrl + "</url><title>" + rssTitle + "</title><link>" + rssLink +"</link></image>\n")
rssFile.write("<copyright>CC BY-NC-SA cosmovisionas</copyright>\n")
rssFile.write("<language>de-de</language>\n")
rssFile.write("<lastBuildDate>" + formatDate(now) + "</lastBuildDate>\n")
rssFile.write("<pubDate>" + formatDate(now) + "</pubDate>\n")
rssFile.write("<webMaster>" + rssWebMaster + "</webMaster>\n")

# go through logfile
for download in downloadHistory:
	
	# split logfile into data
	downloadData = download.split("|")

	# get the full path of the file
	fullPath = downloadData[3]

	# get the stats for the file
	fileStat = os.stat(downloadData[4])

	TimeStamp = formatTimeStamp(datetime.datetime.fromtimestamp(int(downloadData[2]))) 

    # write rss item
	rssFile.write("<item>\n")
	rssFile.write("<title>" + downloadData[1] + " vom " + TimeStamp + " </title>\n")
	rssFile.write("<description>" + downloadData[1] + " vom " + TimeStamp + "</description>\n")
	rssFile.write("<link>" + fullPath + "</link>\n")
	rssFile.write("<guid>" + fullPath + "</guid>\n")
	rssFile.write("<pubDate>" + formatDate(datetime.datetime.fromtimestamp(int(downloadData[2]))) + "</pubDate>\n")
	rssFile.write("<enclosure url=\"" + fullPath + "\" length=\"" + str(fileStat[ST_SIZE]) + "\" type=\"audio/mpeg\" />\n")
	rssFile.write("</item>\n")

#end for loop

# write rss footer
rssFile.write("</channel>\n")
rssFile.write("</rss>")
rssFile.close()
print "RSS/podcast create : " + rssFileName
