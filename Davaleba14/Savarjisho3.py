import csv

with open("organizations-100.csv", "r") as csvread:

    reader = csv.DictReader(csvread)

    
    
    with open("ssl_companies.csv", "w") as companies:
        headers = ["Organization Id", "Name",  "Website", "Industry", "Number of employees"]
        writer = csv.DictWriter(companies, fieldnames=headers, extrasaction='ignore')
        writer.writeheader()
        for row in reader:
            if "https" in row['Website']:
                writer.writerow(row)