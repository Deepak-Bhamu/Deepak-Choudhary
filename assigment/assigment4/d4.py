import csv

data = [
    ['name', 'address', 'moblieno', 'email'],
    ['deepak', 'jaipur', '7891322425', 'deepakbhamujat@gmail.com'],
    ['ajay', 'ajmer', '7838484878', 'ajayjat@gmail.com'],
    ['amit', 'tonk', '7891352425', 'amit@gmail.com'],
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)



