# This read_starter file constantly looks for a new file in the json dumps folder
# if there is a new file in this folder then it will automatically trigger the json_read.py file
# This method of executing the file will be done until a command is generated from the bot side to 
# automate this step or upon building a jenkins pipeline.  

# Strategy 1: This script will be run using a cron job that runs every minute ( * * * * * ) 
# Strategy 2: This script will be run by a Lambda trigger.

import os

os.system("python3 json_read.py")