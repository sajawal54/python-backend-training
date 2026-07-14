import csv

from pathlib import Path

file_path = Path(__file__).parent / "students.csv"
# with open(file_path , "r") as file:
#   reader = csv.reader(file)

#   next(reader)

#   for row in reader:
#    print("Name: " , row[0] )
#    print("Marks: " , row[1] )
#    print("City: " , row[2] )

with open(file_path , "r") as file:
  reader = csv.DictReader(file)

  next(reader)

  for row in reader:
   print(row["Name"])
   print(row["Marks"])
   print(row["City"])