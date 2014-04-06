#--------------Definitions-----------------

#Name of the show
showname="Testshow"

#Length of the show in Seconds
lentgh=8

#Public path on server
filepath="/home/pi/Radiorecorder/records"

#Path for logfiles and scripts
logfilepath="/home/pi/Radiorecorder"

#address of the radiostream
stream="http://www.wdr.de/wdrlive/media/fhe.m3u"

#Public accessible URL for podcastfiles
URL="http://cosmovisionas.de/records/"

#--------------Script-----------------

#creating timestamps
filename=$showname$(date +"_%Y-%m-%d_%H-%M")
UnixTime=$(date +%s)

#start recording
streamripper "$stream" -a "$filename" -A -d "$filepath" -l "$length"

#creating new log in radio-logfile
echo "|$showname|$UnixTime|$URL$filename.mp3|$filepath/$filename.mp3|" >> $logfilepath/recorder.log

#update podcast rss
python $logfilepath/rssgenerator.py

#removing *.cue files
rm $filepath/*.cue
