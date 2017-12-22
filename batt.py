#!/#!/usr/bin/env python3
# Written by DataThinkMonkey https://github.com/DataThinkMonkey/batt 
# script to check battery and notify all terminals and KDE notifcation if
# battery goes below 15%
# batt.log file created in current directory.
# Use crontab to set up scheduled task. My default is 3 mins.

# import batinfo for battery detail and datetime for timestamp.
import batinfo, datetime

# Variables for battery info.
bat = batinfo.Batteries()
capacity = bat.stat[0].capacity
status = bat.stat[0].status 
update = bat.update()
# Variables for date and time used for log file.
btime = datetime.datetime.now().strftime("%Y-%m-%d %T")
# Log status
lstatus = btime + " Battery is " + status + " at " + str(capacity) 
# create the log file a=apend and +=if does not already exist. Other options are w=write, or r=read.
blog = open("/home/jared/batt.log","a+")

update
if capacity > 15 or status == "Charging":
    # Write message to log. Carriage return and new line.
    blog.write("\r\n" + lstatus)
    # Close file after used.
    blog.close()
elif capacity < 7 and status != "Charging":
    blog.write("\r\nBattery is critical at" + capacity + "and has not been plugged in.\nShutting Down in 1 minute. ")
    blog.close()
else:
    blog.write("\r\nBattery is critical at" + capacity + "Plug in laptop immediately.")
    blog.close()
