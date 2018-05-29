# Directions: Add try/except statements to catch the error. Identify the error
# and make a comment on the line above where you find it, but do not fix it.

# Geog 565 2016 Assignment 5 Part 2
# Name: Alina Luce  
# Date: 05/11/2018
# This script unsucessfully attempts to buffer the parks.shp file.

import arcpy
from arcpy import env
env.overwriteOutput = True
# you may need to change this path to your own Exercise11 folder
env.workspace = r"C:\EsriPress\Python\Data\Exercise11"
#again, both these need to be more robust locations in order to function
in_features = r"C:\EsriPress\Python\Data\Exercise11\parks.shp"
out_features = r"C:\EsriPress\Python\Data\Exercise11\parks_buf.shp"

#missing parameters at end
arcpy.Buffer_analysis(in_features, out_features)

try:
   in_features = r"C:\EsriPress\Python\Data\Exercise11\parks.shp"
    out_features = r"C:\EsriPress\Python\Data\Exercise11\parks_buf.shp"
except ExecuteError:
    print "Missing buffer parameters setting"
        
Print "Code completed"
