from src.parser import parse_failed_logins

def main():
    print("Program started")

    log_file = "data/sample_auth.log"

    failed_logins = parse_failed_logins(log_file)

    print(f"Found {len(failed_logins)} failed login events")

    for login in failed_logins:
        print(login)

    
if __name__ == "__main__":
    main()