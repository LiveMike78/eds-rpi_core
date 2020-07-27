# python 3

# imports

import sys
sys.path.insert(0, '/home/ubuntu/eds/lib/')
import eds # Edge Data Store functions

import requests, json, datetime


def get_temperature():
    # get temperature on ubuntu server
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as file:
        reading = file.readline()

    temperature = float(reading) / 1000

    return temperature

# data payload
data = []

# values block, can have 1 to n of these
values = {}

# use .isoformat() function to format correctly
utc_dt = datetime.datetime.utcnow().replace(microsecond=0)
values["timestamp"] = utc_dt.isoformat()+"Z"

# only omit values that are nullable in the container
values["temperature"] = get_temperature()

data.append(values)

eds.create_container("rpi_core", "rpi_core")
eds.send_values("rpi_core", data)
