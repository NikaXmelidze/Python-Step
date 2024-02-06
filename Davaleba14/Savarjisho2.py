
import csv

with open("organizations-100.csv", "r") as csvread:

    reader = csv.DictReader(csvread)
    

    with open("sorted_csv.csv", "w") as sorted_file:
        sorted_lst = sorted(reader, key = lambda l: int(l["Number of employees"]))
        headers = ["Index",	"Organization Id",	"Name",	"Website", "Country", "Description", "Founded",	"Industry",	"Number of employees"]
        writer = csv.DictWriter(sorted_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(sorted_lst)







