import csv
import random
import os

# Output path
output_file = os.path.join("data", "bugs.csv")

# Label definitions with associated keywords and teams
label_info = {
    "Authentication": {
        "keywords": ["login", "logout", "session", "credentials", "token", "authentication"],
        "team": "Backend"
    },
    "UI": {
        "keywords": ["button", "layout", "responsive", "style", "dropdown", "alignment"],
        "team": "Frontend"
    },
    "Backend": {
        "keywords": ["API", "endpoint", "logic", "controller", "database", "exception"],
        "team": "Backend"
    },
    "Security": {
        "keywords": ["XSS", "SQL injection", "encryption", "csrf", "unauthorized", "access control"],
        "team": "Security"
    },
    "DevOps": {
        "keywords": ["deployment", "CI/CD", "pipeline", "logs", "monitoring", "cron job"],
        "team": "DevOps"
    },
    "Analytics": {
        "keywords": ["dashboard", "chart", "report", "KPI", "metric", "tracking"],
        "team": "Data"
    },
    "Database": {
        "keywords": ["query", "SQL", "index", "migration", "foreign key", "join"],
        "team": "Database"
    },
    "Performance": {
        "keywords": ["latency", "load time", "optimize", "slow", "caching", "timeout"],
        "team": "Backend"
    },
    "Notifications": {
        "keywords": ["email", "push", "webhook", "alert", "notification", "template"],
        "team": "Frontend"
    }
}

# Severity and priority levels
severities = ["Low", "Medium", "High", "Critical"]
priorities = ["P3", "P2", "P1", "P0"]

# Generate synthetic bug reports (30 per label)
bug_reports = []
for label, props in label_info.items():
    for i in range(30):
        keyword = random.choice(props["keywords"])
        title = f"{label} Bug #{i+1}"
        description = f"The system fails to handle '{keyword}' properly in the {label.lower()} module."
        severity = random.choice(severities)
        priority = random.choice(priorities)
        team = props["team"]

        bug_reports.append({
            "title": title,
            "description": description,
            "label": label,
            "severity": severity,
            "priority": priority,
            "team": team
        })

# Write bug reports to CSV
os.makedirs("data", exist_ok=True)
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["title", "description", "label", "severity", "priority", "team"])
    writer.writeheader()
    writer.writerows(bug_reports)

print(f"✅ Smart bug reports written to '{output_file}'")