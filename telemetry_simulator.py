import random
import time
from datetime import datetime

def generate_telemetry():
    telemetry_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(-20, 80), 2),
        "battery_level": round(random.uniform(20, 100), 2),
        "signal_strength": round(random.uniform(-120, -30), 2)
    }
    return telemetry_data

def validate_telemetry(data):
    return (
        -40 <= data["temperature"] <= 85 and
        0 <= data["battery_level"] <= 100 and
        -150 <= data["signal_strength"] <= 0
    )

def run_simulation(iterations=10):
    print("Starting satellite telemetry simulation...\n")
    for _ in range(iterations):
        data = generate_telemetry()
        if validate_telemetry(data):
            print("VALID:", data)
        else:
            print("INVALID:", data)
        time.sleep(1)

if __name__ == "__main__":
    run_simulation()
