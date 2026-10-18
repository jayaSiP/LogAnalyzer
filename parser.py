import re

def parse_log_file(filename):

        # Regex pattern to capture IP, timestamp, method, endpoint, and status
    pattern = r'(\d+\.\d+\.\d+\.\d+) .* \[(.*?)\] "(.*?) (.*?) .*?" (\d{3})'

        # Empty list to store parsed logs
    parsed_logs = []

        # Open file and attempt to match the pattern
    with open(filename, "r") as log_file:
        for line in log_file:

            line = line.strip()

        # Skip empty lines or comment lines
            if not line or line.startswith("#"):
                continue

            match = re.search(pattern, line)

        # Attempt to match the pattern
            if match:
                ip = match.group(1)
                timestamp = match.group(2)
                method = match.group(3)
                endpoint = match.group(4)
                status = match.group(5)
    
        # Store in a dictionary
                entry = {
                "ip": ip,
                "timestamp": timestamp,
                "method": method,
                "endpoint": endpoint,
                "status": status
                }
    
        # Store extracted data
                parsed_logs.append(entry)
            else:
                print("Line did not match the pattern.")

    return(parsed_logs)