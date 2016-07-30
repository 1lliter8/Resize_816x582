"""
Take an argument of a directory
Make a new directory within this directory named 816x582
Take each image in the directory and resize to 816x582
	Don't resize things smaller than that
	Maintain size ratio
		Calculate which side to use as yardstick then resize
		Crop extra size down using centre as bar
Save each image to the new directory with the same filename
"""

from PIL import Image
import sys, os

workingpath = sys.argv[1]
outdir = workingpath + "\\816x582"

try:
	os.makedirs(outdir)
except:
	pass

imagelist = []

for f in os.listdir(workingpath):
	if f.endswith(".jpg"):
		imagelist.append(os.path.join(workingpath, f))
	
for f in imagelist:
	filename = os.path.basename(f)
	outfile = outdir + "\\" + filename
	
	image = Image.open(f)
	xsize, ysize = image.size
	newimage_cropped = ""
	
	origratio = float(xsize) / float(ysize)
	targratio = float(816) / float(582)
	
	if xsize >= 816 and ysize >= 582:
		if origratio > targratio:
			# Resize using height as max, crop width
			ratio =  float(582) / float(ysize)
			newimage = image.resize((int(xsize * ratio), int(ysize * ratio)))
			x2size, y2size = newimage.size
			pad = (x2size - 816) / 2
			newimage_cropped = newimage.crop((pad, 0, pad + 816, 582))
		else:
			# Resize using width as max, crop height
			ratio =  float(816) / float(xsize)
			newimage = image.resize((int(xsize * ratio), int(ysize * ratio)))
			x2size, y2size = newimage.size
			pad = (y2size - 582) / 2
			newimage_cropped = newimage.crop((0, pad, 816, pad + 582))
			
		newimage_cropped.save(outfile, "JPEG")
	else:
		str(xsize) + "x" + str(ysize)
		print str(filename) + " is " + str(xsize) + "x" + str(ysize) + "px, smaller than 816x582px. Find a larger version."