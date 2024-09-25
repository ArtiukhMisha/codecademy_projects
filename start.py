import csv

with open ('python-portfolio-project-starter-files/insurance.csv') as ins_csv_file:
    l = csv.DictReader(ins_csv_file)
    