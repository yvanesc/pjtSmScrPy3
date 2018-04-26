import commands

# ASSUMED THAT THIS COMMAND HAS ALREADY BEEN RUN
# sudo mkdir /mnt/usb
# sudo chmod 770 /mnt/usb

MOUNT_DIR = "/mnt/usb"

def run_command(command):
    # start = time.time()
    ret_code, output = commands.getstatusoutput(command)
    if ret_code == 1:
        raise Exception("FAILED: %s" % command)
    # end = time.time()
    # print "Finished in %s seconds" % (end - start)
    return output.splitlines() 


def uuid_from_line(line):
    start_str = "UUID=\""
    example_uuid = "6784-3407"
    uuid_start = line.index(start_str) + len(start_str)
    uuid_end = uuid_start + len(example_uuid)
    return line[uuid_start: uuid_end]

output = run_command("blkid | grep LABEL | grep -v boot")
# ['/dev/sda1: LABEL="KINGSTON" UUID="6784-3407" TYPE="vfat" PARTUUID="459720e1-01"']
for usb_device in output:
    command = "mount --uuid %s %s" % (uuid_from_line(usb_device), MOUNT_DIR)
    run_command(command)
    break
