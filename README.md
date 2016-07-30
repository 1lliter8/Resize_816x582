# Resize_816x582
Resizes all images in a directory to 816x582.jpg

##Usage##

This is command line script that takes a single argument of the directory of images you want to resize. It creates a new directory in the path which it saves all the resized images to.

This tool preserves the image ratio, so it needs images bigger than 816x582 to work and will print to console the ones that are too small. It's designed to work on landscape-shot images of hotels and their interiors that have have very little to be lost from this hard-and-fast approach to resizing.

The only reason this tool exists is because I couldn't find a single GIMP batch resize/crop tool that could make the decisions that would make sure all resultant images were 816x582 exactly, regardless of how tall or wide they were or what their aspect ratio was.
