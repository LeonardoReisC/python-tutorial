import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "data.csv"

# reading a csv file
with CSV_PATH.open("r") as file:
    # reader = csv.reader(file)  # returns a list
    reader = csv.DictReader(file)  # return a dict

    for line in reader:
        print(line['Name'], line['Age'], line['Address'])

# writing in csv file
customers = [
    {
        'Name': 'Leonardo',
        'Age': 20,
        'Address': 'Praca Dr. Emilio da Silveira, 398, Alfenas'
    },
    {
        'Name': 'Fernando',
        'Age': 20,
        'Address': 'Av. Brasil, 212, Porto Alegre'
    },
]

with CSV_PATH.open('w') as file:
    columns = customers[0].keys()

    # writer = csv.writer(file)  # works with lists
    writer = csv.DictWriter(
        file,
        fieldnames=columns)

    writer.writeheader()

    for customer in customers:
        writer.writerow(customer)
