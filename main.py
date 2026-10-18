
from parser import parse_log_file
from detector import (
    count_requests_per_ip, 
    detect_failed_logins, 
    sensitive_endpoint_access, 
    high_requests_volume, 
    detect_404, 
    detect_server_errors, 
    suspicious_methods
)

from report import generate_report

parsed_logs = parse_log_file("sample_log.txt")

ip_counts = count_requests_per_ip(parsed_logs)
failed_logins = detect_failed_logins(parsed_logs)
sensitive_access = sensitive_endpoint_access(parsed_logs)
suspicious_ips = high_requests_volume(ip_counts)
scans = detect_404(parsed_logs)
errors = detect_server_errors(parsed_logs)
suspicious = suspicious_methods(parsed_logs)

generate_report(
    ip_counts,
    failed_logins,
    sensitive_access,
    suspicious_ips,
    scans,
    errors,
    suspicious
)