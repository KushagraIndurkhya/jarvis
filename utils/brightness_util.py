import os
import subprocess
def change_brightness(val):
    monitor = subprocess.check_output('xrandr | grep " connected" | cut -f1 -d " "', shell=True).decode("utf-8").rstrip('\n')
    val=str(val)
    command = "xrandr --output {} --brightness {}".format(monitor,val)
    os.system(command)