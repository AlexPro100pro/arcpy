# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# F1.py
# Created on: 2018-04-19 12:16:01.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
US_Cities = r"E:\Python\arcpy_folder1\p_5\PythEveryone10_11\Lesson1\Lesson1\us_cities.shp"
Buffered_cities = "E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\Lesson1\\Lesson1\\USA.gdb\\us_cities_Buffer_1"
US_Roads = r"E:\Python\arcpy_folder1\p_5\PythEveryone10_11\Lesson1\Lesson1\us_roads.shp"
Buffered_roads = "E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\Lesson1\\Lesson1\\USA.gdb\\us_roads_Buffer_1"
Intersected_buffers = "E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\Lesson1\\Lesson1\\USA.gdb\\us_buffer_interset1_1"
US_Boundaries = r"E:\Python\arcpy_folder1\p_5\PythEveryone10_11\Lesson1\Lesson1\us_boundaries.shp"
Suitable_land = "E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\Lesson1\\Lesson1\\USA.gdb\\suitable_land_2"


# Process: Buffer the cities
arcpy.Buffer_analysis(US_Cities, Buffered_cities, "10 Miles", "FULL", "ROUND", "ALL", "", "GEODESIC")

# Process: Buffer the roads
arcpy.Buffer_analysis(US_Roads, Buffered_roads, "10 Miles", "FULL", "ROUND", "ALL", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis("E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\Lesson1\\Lesson1\\USA.gdb\\us_cities_Buffer_1 #;E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\Lesson1\\Lesson1\\USA.gdb\\us_roads_Buffer_1 #", Intersected_buffers, "ALL", "", "INPUT")

# Process: Clip
arcpy.Clip_analysis(Intersected_buffers, US_Boundaries, Suitable_land, "")

