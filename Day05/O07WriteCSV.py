
import csv
colnames = ['empid', 'empname', 'age', 'dept', 'salary']

data = [
    ['501', 'Jack', '28', 'HR', '65000'],
    ['235', 'Jill', '34', 'FIN', '35000'],
    ['150', 'John', '26', 'AC', '25000'],
    ['325', 'Jai', '21', 'DEV', '55000'],
    ['450', 'Guru', '38', 'DEV', '85000'],
    ['182', 'Sita', '32', 'PRC', '75000'],
    ['297', 'Gita', '36', 'SUP', '60000']
]

with open("empresults.csv", "w", newline="") as CSVW:

    empWriter = csv.writer(CSVW)
    empWriter.writerow(colnames)

    for row in data:
        empWriter.writerow(row)
