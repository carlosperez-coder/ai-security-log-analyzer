# AI-Assisted Security Log Analyzer

A Python-based security log analysis tool that parses Linux-style authentication logs, extracts failed login attempts, detects possible brute-force activity, and generates structured incident reports with AI-assisted summaries.

## Features

- Parses authentication-style log files
- Extracts timestamps, usernames, IP addresses, and failed login events
- Exports failed login activity to CSV
- Detects possible brute-force attacks using threshold-based analysis
- Generates a structured incident report
- Uses the OpenAI API to create a beginner-friendly security incident summary

## Project Structure

```text
ai-security-log-analyzer/
├── data/
│   └── sample_auth.log
├── output/
│   └── failed_logins.csv
├── reports/
│   ├── incident_report.txt
│   └── ai_summary.txt
├── src/
│   ├── parser.py
│   ├── csv_writer.py
│   ├── detector.py
│   ├── reporter.py
│   └── ai_summary.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```
