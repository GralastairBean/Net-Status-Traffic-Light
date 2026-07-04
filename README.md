# Net Status Traffic Light

- A physical [[internet]] status monitor on a [[Raspberry Pi]] Zero, using three LEDs to show your connection status: green for good, yellow for slow, red for offline.
- Pi pings 1.1.1.1 every 3 seconds to check the connection, reading the exit code to know if you're online, and later parsing ping's output to extract the actual **latency** in milliseconds.
- Runs automatically on start via a service so auto starts on crash and reboot.
