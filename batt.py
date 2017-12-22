#!/#!/usr/bin/env python3
import batinfo

bat = batinfo.Batteries()
capacity = bat.stat[0].capacity
status = bat.stat[0].status 
update = bat.update()

update
print ("Battery:",status,"at",capacity,"%")
print (status)

# bat.stat
# bat.stat[0]
# bat.stat[0].capacity
# print bat.stat[0]
# bat.stat[0].manufacturer
# bat.stat[0].technology
# bat.stat[0].charge_full
# bat.stat[0].charge_now
# bat.update()

