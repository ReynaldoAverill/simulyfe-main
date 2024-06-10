import csv
from pathlib import Path

# Specify the path to your CSV file
csv_file_path = Path(__file__).parent / "data_pompa.csv"

# Initialize empty lists to store the data
flow_data = []
pwm_data = []

# Read the CSV file and store data in the lists
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        flow_data.append(int(row['Flow']))
        pwm_data.append(int(row['PWM']))

# Convert the lists into a dictionary
flow_pwm_dict = dict(zip(flow_data, pwm_data))

# Print the dictionary to verify
print("Flow to PWM Dictionary:", flow_pwm_dict)
print(flow_pwm_dict[51])