# Net Status Traffic Light

- A physical [[internet]] status monitor on a [[Raspberry Pi]] Zero, using three LEDs to show your connection status: green for good, yellow for slow, red for offline.
- Pi pings 1.1.1.1 every 3 seconds to check the connection, reading the exit code to know if you're online, and later parsing ping's output to extract the actual **latency** in milliseconds.
- Runs automatically on start via a service so auto starts on crash and reboot.

# Version 1
## Firmware
- Script name "internet.py"
- GPIO...
	- green = LED(17)
	- red = LED(27)
	- yellow = LED(22)
- The script is running on a headless Pi so need to SSH in via Raspi Connect [here.](https://connect.raspberrypi.com/devices)
- To edit the script...
	- `sudo systemctl stop internet-led.service` (to stop it)
	- `nano internet.py` (opens editor)
	- ctl+o -> enter -> ctl+x (saves and closes)
	- `sudo systemctl restart internet-led.service` (to restart the service after editing)
## Hardware
- Have a basic box but need to re-design with new goals...
	- USB-C inlet
	- USB-C power to raspi
	- vertical
	- 3 rubber feet