import csv

# with open("H:\\Python\\ukazka\\ukladani\\data.csv", "r") as file:
#     reader = csv.reader(file, delimiter=";")
#     for x in reader:
#         print(x)

with open("H:\\Python\\ukazka\\ukladani\\data.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Hokus", "pokus"])