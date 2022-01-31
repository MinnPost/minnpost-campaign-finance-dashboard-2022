import csv
import json

output = []
rows = []

with open("2022 Camfi Data - camfi.csv", "r") as f:
  reader = csv.reader(f)
  for row in reader:
    rows.append(row)
  
headings = rows[0]
for row in rows[1:]:
  this_row = {}
  for i in range (0, len(row)):
    this_row[headings[i]] = row[i]
  output.append(this_row)

with open("camfi.json", "w") as f:
  f.write(json.dumps(output))