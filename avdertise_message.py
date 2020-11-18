import subprocess
import time

# Import for logging logs
from log import Log

Log = Log.capture_log()

std_out, std_err = subprocess.Popen('sudo hciconfig hci0 up', stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    shell=True).communicate()
Log.info("hciconfig hci0 up -> {}".format(std_out))

std_out, std_err = subprocess.Popen('sudo hciconfig hci0 leadv 3', stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    shell=True).communicate()
Log.info("hciconfig hci0 leadv 3 -> {}".format(std_out))

for i in range(1,21):
    Log.info("Started broadcasting the message for time {0}".format(i))
    std_out, std_err = subprocess.Popen(
        'sudo hcitool -i hci0 cmd 0x08 0x0008 1c 02 01 06 03 03 aa fe 14 16 aa fe 10 00 02 '
        '63 69 72 63 75 69 74 64 69 67 65 73 74 07 00 00 00', stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=True).communicate()
    time.sleep(5)

Log.info("hcitool -i hci0 cmd  -> {}".format(std_out))
