import commands

# ASSUMED THAT THIS COMMAND HAS ALREADY BEEN RUN
# sudo mkdir /mnt/usb
# sudo chmod 770 /mnt/usb

ret_code = commands.getstatusoutput("sudo mount /dev/sda1 /mnt/usb")
print (ret_code)
