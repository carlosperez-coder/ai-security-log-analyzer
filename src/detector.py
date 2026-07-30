def detect_brute_force(failed_logins, threshold=5):
    ip_activity = {}

    for event in failed_logins:
        ip = event["ip"]
        username = event["username"]

        if ip not in ip_activity:
            ip_activity[ip] = {
                "failed_attempts" : 0, 
                "targeted_users": set()    
            }

        ip_activity[ip]["failed_attempts"] += 1
        ip_activity[ip]["targeted_users"].add(username) 

    suspicious_ips = []

    for ip, activity in ip_activity.items():
        if activity["failed_attempts"] >= threshold:
            suspicious_ips.append({
                "ip": ip,
                "failed_attempts": activity["failed_attempts"],
                "targeted_users": sorted(list(activity["targeted_users"])),
                "threat_type": "Possible brute-force attack"
            })

    return suspicious_ips