#!/usr/bin/env python
import os

print "Hello youtube -- downloader"


videos = ['https://www.youtube.com/watch?v=R0P-u-K772A',
		 "https://www.youtube.com/watch?v=XUgFKIo41R4"
	]

cmd = """ youtube-dl  --get-filename -o "%(title)s.%(ext)s" """
   
for v in videos:
	cmd = cmd + v
	print cmd
	os.system(cmd)

## youtube-dl --get-filename -o "%(title)s.%(ext)s" BaW_je
## youtube-dl --get-filename -o "%(title)s.%(ext)s" BaW_jenozKc --restrict-filenames

###
#
#
#    get list of videos searched
#    loop through the array
#    download them 
#    and send them to the thing .....
#
#   #### extra : training the extractor
#
