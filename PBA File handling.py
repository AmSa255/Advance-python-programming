import csv
import json

with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    students = []

    for row in csv_reader:
        row["RollNo"] = int(row["RollNo"])
        row["Marks"] = int(row["Marks"])
        students.append(row)

with open("students.json", "w") as json_file:
    json.dump(students, json_file, indent=4)

print("CSV data successfully converted into JSON!")
