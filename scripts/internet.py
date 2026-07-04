import subprocess
import time
import signal
import sys
from gpiozero import LED

# set GPIO pins for status LEDs
green = LED(17)
red = LED(27)
yellow = LED(22)

# If a ping > threshold = "slow" = yellow light
SLOW_THRESHOLD = 100

def get_latency():
    # Returns latency in ms if online, or None if the ping failed
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", "1.1.1.1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )
    if result.returncode != 0:
        return None

    output = result.stdout.decode()
    # Find the "time=" part of ping's output
    if "time=" in output:
        after = output.split("time=")[1]      # everything after "time="
        number = after.split(" ")[0]          # the number, before the space
        return float(number)
    return None

def all_off():
    green.off()
    red.off()
    yellow.off()

def shutdown(signum, frame):
    # Runs when the script is told to stop (Ctrl+C or service stop)
    all_off()
    sys.exit(0)

# Catch both Ctrl+C (SIGINT) and systemd's stop signal (SIGTERM)
signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

while True:
    latency = get_latency()
    print(latency)

    all_off()
    if latency is None:
        red.on()                  # offline
    elif latency > SLOW_THRESHOLD:
        yellow.on()               # online but slow
    else:
        green.on()                # online and fast

    time.sleep(3)                 # check every 3 seconds