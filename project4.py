import socket  # This allows us to connect to other computers on a network
from datetime import datetime  # To check how long the scan takes

# Show a welcome message
print("=== Simple Network Port Scanner ===")
print("⚠ Only scan IP addresses you are allowed to!")

# Ask the user to enter the IP address they want to scan
target = input("Enter the IP address to scan (example: 127.0.0.1): ")

# Ask the user for the starting port number
start_port = int(input("Enter the starting port number (example: 1): "))

# Ask the user for the ending port number
end_port = int(input("Enter the ending port number (example: 1024): "))

# Save the time when the scan starts
start_time = datetime.now()

# Some known ports with their common service names
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

# Go through each port number one by one
for port in range(start_port, end_port + 1):
    # Create a new socket (like a phone call to a computer port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout (wait only 0.5 seconds to connect, then move on)
    s.settimeout(0.5)

    # Try to connect to the IP and port
    result = s.connect_ex((target, port))

    # If result is 0, that means the port is open
    if result == 0:
        # Check if the port is known, else write 'Unknown service'
        if port in common_ports:
            service = common_ports[port]
        else:
            service = "Unknown service"

        # Show the open port and its service
        print("Port", port, "is OPEN -", service)

    # Close the socket to free resources
    s.close()

# Save the time when scan ends
end_time = datetime.now()

# Show how much time the scan took
print("Scan completed in:", end_time - start_time)