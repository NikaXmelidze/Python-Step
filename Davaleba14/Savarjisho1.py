import csv

with open("titanic.csv", "r") as csvread:
    reader = csv.DictReader(csvread)


    with open("survivors.csv", "w") as survivors:
        headers = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
        writer = csv.DictWriter(survivors, fieldnames=headers)
        writer.writeheader()
        for row in reader:
            if row["Survived"] == "1":
                writer.writerow(row)