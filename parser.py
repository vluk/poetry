import csv

with open("kaggle_poem_dataset.csv", "r") as dataset:
    reader = csv.reader(dataset, delimiter = ",", quotechar="\"")
    with open("delimited.txt", "w") as delimited:
        for row in reader:
            if len(row[-1]) < 1000 and not "launch audio" in row[2].lower():
                    delimited.write("\n")
                    delimited.write("<|startoftext|>")
                    delimited.write("\n")
                    delimited.write(row[2])
                    delimited.write(" by ")
                    delimited.write(row[1])
                    delimited.write("\n")
                    delimited.write("\n")
                    delimited.write(row[-1])
                    delimited.write("\n")
                    delimited.write("<|endoftext|>")
