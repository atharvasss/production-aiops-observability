import re
from collections import Counter

import subprocess

result = subprocess.run(
    [
        "kubectl",
        "logs",
        "-n",
        "aiops",
        "deployment/anomaly-generator",
        "--tail=100"
    ],
    capture_output=True,
    text=True
)

logs = result.stdout.splitlines()

errors = []
latencies = []

for line in logs:
    if "ERROR" in line:
        errors.append(line)

    match = re.search(r"latency=(\d+)ms", line)
    if match:
        latencies.append(int(match.group(1)))

print("===== AIOps Analysis =====")

print(f"Total log entries: {len(logs)}")
print(f"Errors detected: {len(errors)}")

if latencies:
    avg = sum(latencies) / len(latencies)
    print(f"Average latency: {avg:.2f}ms")
    print(f"Maximum latency: {max(latencies)}ms")

if errors:
    print("\nANOMALY DETECTED")
    print("Pattern: database timeout / elevated latency")
    print("Probable impact: increased request latency and HTTP 500 errors")
    print("Recommended action: investigate database connectivity and timeout configuration")
else:
    print("\nNo anomaly detected")
