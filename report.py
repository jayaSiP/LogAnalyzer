
def generate_report(
    ip_counts,
    failed_logins,
    sensitive_access,
    suspicious_ips,
    scans,
    errors,
    suspicious_methods
):
    
    print("\n===== LOG ANALYSIS REPORT =====\n")

    print("Total Requests Per IP:")
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip}: {count}")
    print()

    print("Failed Login Attempts:")
    if failed_logins:
        for ip, count in sorted(failed_logins.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip}: {count} failed logins")
    else:
        print("None detected")
    print()

    print("Sensitive Endpoint Access:")
    if sensitive_access:
        for ip, endpoints in sensitive_access.items():
            print(f"{ip}: accessed {endpoints}")
    else:
        print("None detected")
    print()

    print("High Request Volume:")
    if suspicious_ips:
        for ip, count in sorted(suspicious_ips.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip}: {count} requests")
    else:
        print("None detected")
    print()

    print("404 Scanning Activity:")
    if scans:
        for ip, count in sorted(scans.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip}: {count} HTTP 404 responses")
    else:
        print("None detected")
    print()

    print("Server Errors (5xx):")
    if errors:
        for ip, count in sorted(errors.items(), key=lambda x: x[1], reverse=True):
            print(f"{ip}: {count} server errors")
    else:
        print("None detected")
    print()

    print("Suspicious HTTP Methods:")
    if suspicious_methods:
        for ip, methods in suspicious_methods.items():
            print(f"{ip}: {methods}")
    else:
        print("None detected")
    print()

    print("===== END OF REPORT =====")