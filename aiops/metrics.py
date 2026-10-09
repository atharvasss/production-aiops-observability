import time

incident_created = time.time()

print("Incident detected.")
print(f"Detection timestamp: {incident_created}")

print("\nExample SRE measurement:")
print("MTTD = Detection Time - Incident Start Time")
print("MTTR = Recovery Time - Incident Start Time")
