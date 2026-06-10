from src.parser import parse_failed_logins
from src.csv_writer import write_failed_logins_to_csv

def main():
    log_file = "data/sample_auth.log"
    output_file = "output/failed_logins.csv"

    failed_logins = parse_failed_logins(log_file)

    print(f"Found {len(failed_logins)} failed login events")

    write_failed_logins_to_csv(failed_logins, output_file)

    print(f"Results saved to {output_file}")

    
if __name__ == "__main__":
    main()