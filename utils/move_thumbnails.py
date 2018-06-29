from os.path import join
import json
import optparse
import shutil
import psutil
import os
import sys
from IPython import  utils

parser = optparse.OptionParser()

parser.add_option('-f', '--folder',
    action="store", dest="folder",
    help="folder", default="NOT PROVIDED!")
parser.add_option('-t', '--thumb_size',
    action="store", dest="thumb_size",
    help="thumbnail size", default="128")
parser.add_option('-d', '--dest_folder',
    action="store", dest="dest_folder",
    help="the destination folder", default="128")

options, args = parser.parse_args()

folder = options.folder
dest_folder = options.dest_folder
thumb_size = options.thumb_size

json_file = folder+'/output/plot_data.json'

print("JSON file: ", json_file)

with open(json_file) as json_data:
    d = json.load(json_data)
    centers = d['centroids']
    utils.path.ensure_dir_exists( dest_folder+'output/thumbs/'+thumb_size+'px/' )
    for i in centers: 
    	image = i['img']
    	shutil.copy(folder+'output/thumbs/'+thumb_size+'px/'+image, dest_folder+'output/thumbs/'+thumb_size+'px/'+image)  
