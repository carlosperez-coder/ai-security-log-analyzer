def generate_incident_report(failed_logins, suspicious_ips, output_file):
    with open(output_file, "w") as report_file:
        report_file.write("Security Incident Report\n")
        report_file.write("========================\n\n")

        report_file.write(f"Total failed login attempts: {len(failed_logins)}\n")
        report_file.write(f"Suspicious IPs detected: {len(suspicious_ips)}\n\n")

        if not suspicious_ips:
            report_file.write("No suspicious IPs were detected based on the current threshold.\n")
            return
        
        report_file.write("Suspicious Activity Details\n")
        report_file.write("===========================\n\n")

        for item in suspicious_ips:
            report_file.write(f"Suspicious IP: {item['ip']}\n")
            report_file.write(f"Failed attempts: {item['failed_attempts']}\n")
            report_file.write(f"Targeted users: {', '.join(item['targeted_users'])}/n")
            report_file.write(f"Threat type: {item['threat_type']}\n")

            report_file.write("Recommended next steps:\n")
            report_file.write("- Review authentication logs for successful logins from this IP.\n")
            report_file.write("- Check whether any targeted accounts were compromised.\n")
            report_file.write("- Consider blocking the IP if activity is unauthorized.\n")
            report_file.write("- Continue monitoring for repeated failed login attempts.\n\n")
