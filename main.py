from src.parser import parse_failed_logins
from src.csv_writer import write_failed_logins_to_csv
from src.detector import detect_brute_force
from src.reporter import generate_incident_report
from src.ai_summary import generate_ai_summary

def main():
    log_file = "data/sample_auth.log"
    output_file = "output/failed_logins.csv"
    report_output_file = "reports/incident_report.txt"

    failed_logins = parse_failed_logins(log_file)

    print(f"Found {len(failed_logins)} failed login events")

    write_failed_logins_to_csv(failed_logins, output_file)

    print(f"Results saved to {output_file}")

    suspicious_ips = detect_brute_force(failed_logins, threshold=5)

    print("\nSuspicious IPs:")
    for item in suspicious_ips:
        print(item)

    generate_incident_report(failed_logins, suspicious_ips, report_output_file)
    print(f"\nIncident report saved to {report_output_file}")

    ai_summary = generate_ai_summary(failed_logins, suspicious_ips)

    print("\nAI Summary:")
    print(ai_summary)
    
    with open("reports/ai_summary.txt", "w") as summary_file:
        summary_file.write(ai_summary)

    print("\nAI summary saved to reports/ai_summary.txt")
    
if __name__ == "__main__":
    main()