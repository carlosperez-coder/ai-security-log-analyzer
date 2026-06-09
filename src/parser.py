import re


def parse_failed_logins(file_path):
    failed_logins = []

    with open(file_path, "r") as log_file:
        for line in log_file:
            if "Failed password" not in line:
                continue

            timestamp = line[:15].strip()

            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if "invalid user" in line:
                user_match = re.search(r"invalid user (\S+)", line)
            else:
                user_match = re.search(r"Failed password for (\S+)", line)

            if ip_match and user_match:
                event = {
                    "timestamp": timestamp,
                    "username": user_match.group(1),
                    "ip": ip_match.group(1),
                    "status": "failed"
                }

                failed_logins.append(event)

    return failed_logins