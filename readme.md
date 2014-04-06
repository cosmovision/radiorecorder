## Radiorecorder & Podcast generator

These short scripts enable you to record radioshows from a webstream, store them on a server and generate a rss-file to download them as a podcast with a podcatcher.

###Installing

To use these scripts, install streamripper on your webserver (in my case a Raspberry Pi):  
```bash
sudo apt-get install streamripper
```
Copy the two files `recorder.sh` and `rssgenerator.py` to your webserver and config the definitions in both files (filepaths, URLs, Names, etc.).
If you want to record ore than one show, copy, rename and edit the file `recorder.sh`.
To start the recording, execute the shellscript on the server:
```bash
bash recorder.sh
```
To start a recording at a certain file, add a cronjob on your server. For example, if you want to record a show every Saturday on 15:00, open the crontab
```bash
crontab -e
```
and add the following line (the file `recorder-testshow.sh` has to contain all the information about the show, such as URL, length, etc.):
```
00 15 * * sat bash /home/pi/recorder/recorder-testshow.sh 
```
This script will start streamripper and generate a new version of the podcast RSS-file.