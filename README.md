# batt
Laptop battery log generator and warning.
Script to check battery and notify all terminals and KDE notifcation if
battery goes below 15%.

Two version exist, Bash and Python. The Bash version requires acpi to be installed, while the Python version requires the batinfo and datetime modules.

batt.log file created in current directory.

Use crontab to set up scheduled task. My configuration is set to run every 3 mins. 
```
*/3 * * * *     /home/jared/bin/batt.sh
```

To-do
1. Have script identify setuid for the /sbin/shutdown and show message and log. Possibly have script prompt to change for you.
2. Have script support other desktop environments.
3. Add startup to add cronjob. 
4. Provide settings for batt level percentage for prompt and shutdown. 
5. Stop Shutdown if plugged in. 
