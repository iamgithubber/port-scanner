### scanner.py

---

#### Description
`scanner.py` is a simple banner-grabbing port scanner written in Python. It scans a specified range of ports on a target host, attempts to retrieve banners from open ports, and respects a specified rate limit for the number of requests per second.

#### Requirements
- Python 3.x

#### Usage
```bash
python scanner.py -H <target_host> [-p <port_range>] [-t <timeout>] [-r <requests_per_second>]
```

#### Command-Line Arguments
- `-H, --host` (required): Target host (IP address or domain) to scan.
- `-p, --ports` (optional): Range of ports to scan, specified as `start-end` (e.g., `20-80`). Default is `1-1000`.
- `-t, --timeout` (optional): Timeout for each port scan in seconds. Default is `1.0` second.
- `-r, --requests` (optional): Rate limit for requests per second. Default is `1.0` request per second.

#### Example Commands
1. Scan ports 1 to 1000 on host `192.168.1.1` with default timeout and rate limit:
   ```bash
   python scanner.py -H 192.168.1.1
   ```

2. Scan ports 20 to 25 on host `192.168.1.1` with a timeout of 2 seconds per port scan and a rate limit of 5 requests per second:
   ```bash
   python scanner.py -H 192.168.1.1 -p 20-25 -t 2 -r 5
   ```

3. Display help message:
   ```bash
   python scanner.py --help
   ```

#### Output
The script prints the status of each scanned port:
- `"Port <port> is open"` if the port is open.
- `"Banner: <banner>"` if a banner is retrieved from the open port.
- `"No banner retrieved"` if no banner is retrieved from the open port.
- `"Port <port> is closed"` if the port is closed.
- `"Error scanning port <port>: <error_message>"` if an error occurs while scanning the port.

#### Implementation Details
- **Banner Grabbing (`banner_grab`)**: Attempts to retrieve a banner from the specified host and port.
- **Port Scanning (`scan_ports`)**: Scans a range of ports on the specified host, printing the status of each port and respecting the specified timeout and rate limit.

### Notes
- Ensure that you have the necessary permissions to scan the target host.
- Scanning large ranges of ports or using high request rates might be flagged as suspicious activity by network security systems.
- Always use this script responsibly and ethically.
