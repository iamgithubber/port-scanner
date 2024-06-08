import socket
import sys
import argparse
import time

def banner_grab(host, port, timeout):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((host, port))
        banner = s.recv(1024).decode().strip()
        return banner
    except Exception as e:
        return str(e)
    finally:
        s.close()

def scan_ports(host, start_port, end_port, timeout, requests_per_second):
    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
                banner = banner_grab(host, port, timeout)
                if banner:
                    print(f"Banner: {banner}")
                else:
                    print("No banner retrieved")
            else:
                print(f"Port {port} is closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            s.close()
        
        time.sleep(1 / requests_per_second)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Banner Grabbing Port Scanner")
    parser.add_argument('-H', '--host', required=True, help='Target host (IP address or domain)')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range to scan (e.g., 20-80)')
    parser.add_argument('-t', '--timeout', type=float, default=1.0, help='Timeout for each port scan (seconds)')
    parser.add_argument('-r', '--requests', type=float, default=1.0, help='Requests per second (rate limit)')

    args = parser.parse_args()

    target_host = args.host
    port_range = args.ports
    timeout = args.timeout
    requests_per_second = args.requests

    try:
        start_port, end_port = map(int, port_range.split('-'))
    except ValueError:
        print("Invalid port range. Please specify as start-end (e.g., 20-80).")
        sys.exit(1)

    scan_ports(target_host, start_port, end_port, timeout, requests_per_second)
