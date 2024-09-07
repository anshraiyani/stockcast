import csv
import json
from datetime import datetime
import time

csv_file = 'reliance.csv'
json_file = 'public/candlestick/reliance.json'

data = []

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # Assuming the first row contains column headers
    for row in csvreader:
        date_str = row[0].split("+")[0]
        print(date_str)
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')  # Adjust the date format as needed
        # print(date)
        unix_timestamp = int(time.mktime(date_obj.timetuple()))
        print(unix_timestamp)
        open_price = round(float(row[1]),2)
        high_price = round(float(row[2]),2)
        low_price = round(float(row[3]),2)
        close_price = round(float(row[4]),2)
        
        data_point = {
            "x": unix_timestamp,
            "y": [open_price, high_price, low_price, close_price]
        }
        data.append(data_point)

# Write the data to a JSON file
with open(json_file, 'w') as jsonfile:
    json.dump(data[-150:], jsonfile, indent=2)

print("Conversion complete. JSON data saved to", json_file)
