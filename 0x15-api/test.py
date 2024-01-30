import csv
import requests
import sys

# Data to be written to the CSV file
ur = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
res = requests.get(ur)

# Open the CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    
    # Write the data to the CSV file
    csv_writer.writerows(res.json().items())
