#!/bin/bash
# Written by jared.bernard@gmail.com
# script to check battery and notify all terminals and KDE notifcation if
# battery goes below 15%
# batt.log file created in current directory.
# Use crontab to set up scheduled task. My default is 3 mins.

# pull battery % level as whole number. Used for condition. 
blevel=$(acpi -b | cut -d' ' -f4 | cut -d% -f1)
# pull battery % level as %. Used in log. 
bper=$(acpi -b | cut -d, -f2)
# timestamp used for log file.
btime=$(date "+%F %T")
# pull status of Charging, Discharging or Full. 
plug=$(acpi -b | cut -d, -f1 | cut -d' ' -f3)
# log file
blog="$HOME/bin/batt.log"

if [ $blevel -gt 15 ] || [ "$plug" = "Charging" ]
then
	echo "$btime Battery is $plug at $bper." >> $blog
else	
	if [ $blevel -lt 7 ] && [ "$plug" != "Charging" ]
	then
		echo "Battery is critical at $bper and has not been plugged in.
		Shutting Down in 1 min." >> $blog
		# If run at normal user, need to add stickbit to shutdown
		# command. sudo chmod a+s /sbin/shutdown
		shutdown -h 60 #add loop so if plugged in shutdown will stop.
	else
		echo "Battery is critical at $bper. Plug in laptop immediately." | wall
		echo "$btime Battery is CRITICAL $plug at $bper." >> $blog
		#Change this line if not using KDE.
		kdialog --passivepopup "Battery is critical at $bper. Plug in laptop immediately" 20
	fi
fi
