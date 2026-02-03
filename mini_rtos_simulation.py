import time
from datetime import datetime
import random

# ---- TASK FUNCTIONS ----

def telemetry_task():
    print(f"[{datetime.utcnow()}] Telemetry sent")

def sensor_task():
    value = random.randint(0, 100)
    print(f"[{datetime.utcnow()}] Sensor read: {value}")

def communication_task():
    print(f"[{datetime.utcnow()}] Listening for incoming data")

# ---- SIMPLE RTOS SCHEDULER ----

def scheduler():
    telemetry_interval = 2      # seconds
    sensor_interval = 1         # seconds
    comm_interval = 0.5         # seconds

    last_telemetry = time.time()
    last_sensor = time.time()
    last_comm = time.time()

    print("Mini RTOS simulation started...\n")

    while True:
        now = time.time()

        if now - last_sensor >= sensor_interval:
            sensor_task()
            last_sensor = now

        if now - last_telemetry >= telemetry_interval:
            telemetry_task()
            last_telemetry = now

        if now - last_comm >= comm_interval:
            communication_task()
            last_comm = now

        time.sleep(0.1)

if __name__ == "__main__":
    scheduler()
