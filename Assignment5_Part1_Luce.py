# Directions: Fix the syntax errors in this script. When you find them, make a
# comment above the line describing the problem and how you fixed it.

# Geog 565 2016 Assignment 5 Part 1
# Name: Alina Luce  
# Date: 05/11/2018
# This script prints the name of each park in the parks.shp file

import arcpy
from arcpy import env
# you may need to change this path to point to your own Exercise11 folder
env.workspace = "C:/EsriPress/Python/Data/Exercise11"
# Variable FC needed to be lower case, not all caps- needed to match. And path was inadequate, needed to be more robust. 
fc = r"C:\EsriPress\Python\Data\Exercise11\parks.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
#Colon missing below to start loop
for field in fields:
    #one equals sign does not set up a check, it sets an absolute- need to make it correct by adding a second =
    if field.name == "PARK_NAME":
        for row in rows:
          print "Park Name = {0}".format(row.getValue(field.name))
