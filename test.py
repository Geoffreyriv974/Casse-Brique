import csv

score_file = "tableau_scores.csv"

with open(score_file, 'r') as f:
    reader = csv.DictReader(f, dialect=csv.QUOTE_ALL)

    for value in reader:
        print(value)
