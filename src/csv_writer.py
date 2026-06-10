import csv

def write_failed_logins_to_csv(failed_logins, output_file):
    fieldnames = ["timestamp", "username", "ip", "status"]

    with open(output_file, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(failed_logins)