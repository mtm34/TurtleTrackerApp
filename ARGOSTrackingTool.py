#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Margaret Morrison (margaret.t.morrison@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Ask user for a search date
user_date = input("Enter a date (M/D/YYYY):")

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary objects
date_dict= {}
coord_dict ={}

#Iterate through all lines in the LineList
for lineString in line_list[17:]:
    if lineString[0] in ("#","u"):
        continue
    
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0] #ARGOS tracking record ID
    obs_date = lineData[2]  #Observation Date
    obs_lc = lineData[4]    #Observation Location Class
    #option: Skip lc values NOT 1, 2, or 3
    #if obs_lc not in ("1","2","3"):
     #   continue
    obs_lat = lineData[6]   #Observation Latitude
    obs_long = lineData[7]  #Observation Longtitude
   
    
    #Only print obs_lc values of 1,2,3
    if obs_lc in ("1","2","3"):
        #Add to date and coordinate dictionary objects
        date_dict[record_id] = obs_date
        coord_dict[record_id] = obs_lat, obs_long
 
#Create empty list to hold matching keys
matching_keys = []
#Loop through items in date dict and collect keys for matching 
for date_item in date_dict.items():
    #Get the date of the item
    the_key, the_date = date_item
    #See if the date matches the user date
    if the_date == user_date:
        #Add key to list
        matching_keys.append(the_key)

#Reveal location for each key in matching keys
for matching_key in matching_keys:
    obs_lat, obs_long = coord_dict[matching_key]
    print(obs_lat, obs_long)
    #Print the location of sara
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_long} on {user_date}")
