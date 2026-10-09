import subprocess
from collections import Counter

logs = subprocess.run(
    [
        "kubectl",
        "logs",
        "-n",
        "aiops",
        "deployment/anomaly-generator",
        "--tail=200"
    ],
    capture_output=True,
    text=True
).stdout.splitlines()

patterns = Counter()

for log in logs:
    if "database timeout" in log:
        patterns["Database Timeout"] += 1

    if "status=500" in log:
        patterns["HTTP 500"] += 1

    if "latency=5000ms" in log:
        patterns["High Latency"] += 1

print("===== INCIDENT CORRELATION =====")

for name, count in patterns.items():
    print(f"{name}: {count}")

if len(patterns) >= 2:
    print("\nCORRELATED INCIDENT DETECTED")
    print("Multiple symptoms indicate a common database-related failure.")
    print("\nSuggested investigation:")
    print("1. Check database connectivity")
    print("2. Check connection pool")
    print("3. Check database latency")
    print("4. Check application timeout configuration")
