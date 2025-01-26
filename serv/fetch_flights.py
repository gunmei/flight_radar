from FlightRadar24 import FlightRadar24API
import re

# Парсинг данных
def parse_flight_data(data):
    pattern = r"<\((?P<aircraft>[A-Za-z0-9]+)\) ?(?P<registration>B-[A-Za-z0-9\-]+)? ?-? ?Altitude: (?P<altitude>\d+)? -? ?Ground Speed: (?P<ground_speed>\d+)? -? ?Heading: (?P<heading>\d+)?"
    match = re.match(pattern, data)
    if match:
        return {key: value for key, value in match.groupdict().items() if value is not None}
    return {}

def get_flights():
    return china_aircraft

fr_api = FlightRadar24API()
flights = fr_api.get_flights()
china_aircraft = []

for v in flights:
    parse_data = parse_flight_data(str(v))
    
    if parse_data:
        key = parse_data.keys()
        if parse_data["aircraft"] != "GRND" and 'registration' in key: 
            china_aircraft.append(parse_data)
