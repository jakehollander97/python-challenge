#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import necessary libraries
import csv
from pathlib import Path

#import csv file from directory into notebook
poll_csv = Path("03-Python_homework_assignment_PyPoll_Resources_election_data.csv")

#create variables for each candidate and initiate a tracker for their votes
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#with and for loop that creates a counter system that adds each vote to the correct candidate
with open(poll_csv, newline = "", encoding = "utf-8") as elections:
    csvreader = csv.reader(elections, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        if row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

#creating a dictionary that correlates the number of votes to each candidate     
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

candidates_votes = dict(zip(candidates, votes))
key = max(candidates_votes, key = candidates_votes.get)

#calculate the percentage of each candidate vs the total amount of votes, rounded to 3 decimal places
khan_percent = round((khan_votes/total_votes)*100, 3)
correy_percent = round((correy_votes/total_votes)*100, 3)
li_percent = round((li_votes/total_votes)*100, 3)
otooley_percent = round((otooley_votes/total_votes)*100, 3)

#Print statements to display results
print(f"Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print("----------------------------")
print(f"Winner: {key}")
print("----------------------------")

#create a new .txt file that displays the same results that were printed
output_file = Path("Election_Results.txt")
with open(output_file, "w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write("----------------------------")
    