
def count_requests_per_ip(parsed_logs):

    ip_counts = {}

    for entry in parsed_logs:
        ip = entry.get("ip", "unknown") 

        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

    return ip_counts

def detect_failed_logins(parsed_logs):

    failed_attempts = {}

    for entry in parsed_logs:
        ip = entry.get("ip", "unknown") 
        endpoint = entry.get("endpoint", "/")
        status = entry.get("status", "200")

        if endpoint == "/login" and status == "401":
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

    return failed_attempts

def sensitive_endpoint_access(parsed_logs):
    sensitive_endpoints = ["/admin", "/config", "/.env", "/wp-admin", "/phpmyadmin"]
    
    sensitive_access = {}

    for entry in parsed_logs:
        ip = entry.get("ip", "unknown") 
        endpoint = entry.get("endpoint", "/")

        if endpoint in sensitive_endpoints:
            
            if ip in sensitive_access:
                sensitive_access[ip].append(endpoint)
            else:
                sensitive_access[ip] = [endpoint]

    return sensitive_access

def high_requests_volume(ip_counts, threshold=10):
    
    suspicious_ips = {}

    for ip, count in ip_counts.items():
        if count > threshold: 
            suspicious_ips[ip] = count 
            
    return suspicious_ips

def detect_404(parsed_logs):
    
    scans = {}

    for entry in parsed_logs:
        ip = entry.get("ip", "unknown") 
        status = entry.get("status", "200")

        if status == "404":
            if ip in scans:
                scans[ip] += 1
            else:
                scans[ip] = 1
    return scans

def detect_server_errors(parsed_logs):
    
    errors = {}

    for entry in parsed_logs:
        ip = entry.get("ip", "unknown") 
        status = entry.get("status", "200")

        if status.startswith("5"):
            if ip in errors:
                errors[ip] += 1
            else:
                errors[ip] = 1
    return errors

def suspicious_methods(parsed_logs):

    suspicious = {}
    allowed_methods = ["GET", "POST"]

    for entry in parsed_logs:
        ip = entry.get("ip", "unknown") 
        method = entry.get("method", "GET")

        if method not in allowed_methods:
            if ip in suspicious:
                suspicious[ip].append(method)
            else:
                suspicious[ip] = [method]

    return suspicious