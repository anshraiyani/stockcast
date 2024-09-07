import csv
import json

# Initialize an empty list to store the JSON objects
json_array = []

# Open and read the CSV file
with open('symbols.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through each row in the CSV file
    for row in reader:
        symbol = row['SYMBOL']+".NS"
        # Create a JSON object with the 'key' and 'value'
        json_object = {"key": symbol, "value": symbol}
        # Append the JSON object to the list
        json_array.append(json_object)

# Define the name of the JSON file
json_file_name = 'symbols.json'

# Save the JSON array to the JSON file
with open(json_file_name, 'w') as jsonfile:
    json.dump(json_array, jsonfile, indent=2)

print(f"JSON data has been saved to {json_file_name}")