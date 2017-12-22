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
# Variable for date and time.
year = datetime.datetime.now().strftime("%Y")
mon = datetime.datetime.now().strftime("%m")
day = datetime.datetime.now().strftime("%d")
time = datetime.datetime.now().strftime("%T")
# timestamp used for log file.
btime = year + "-" + mon + "-" + day + " " + time 
# Log status
lstatus = btime + " Battery is " + status + " at " + str(capacity) + repr("%.") 

update
if capacity > 15 or status == "Charging":
    print (lstatus)
elif capacity < 7 and status != "Charging":
    print ("Battery is critical at" + capacity + "and has not been plugged in.\nShutting Down in 1 minute. ")
else:
    print ("Battery is critical at" + capacity + "Plug in laptop immediately.")


# bat.stat
# bat.stat[0]
# bat.stat[0].capacity
# print bat.stat[0]
# bat.stat[0].manufacturer
# bat.stat[0].technology
# bat.stat[0].charge_full
# bat.stat[0].charge_now
# bat.update()

