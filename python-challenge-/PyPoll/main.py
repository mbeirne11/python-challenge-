import csv
#get file path
file_path ="python-challenge-/PyPoll/Resources/election_data.csv"

# define variables 
row_num = 0
total = 0
candidates = []
candidates_totals = []
candidates_info = []
avg_change = 0
greatest_votes = 0
greatest_votes_name = ""
candidate_dict = {}
#open the file
with open(file_path) as csvfile:
    #read the file
    reader = csv.reader(csvfile)
    # find and add candiates to the lists. count number of votes
    for vote in reader:
        if(row_num > 0 and candidates.count(vote[2]) == 0):
            candidates.append(vote[2])
        if(row_num > 0):
            candidates_totals.append(vote[2])
        row_num +=1
    # print(f'Election Results\n-------------------------')
    # print(f'Total Votes: {row_num-1}\n-------------------------')
    # count the votes for each candidate
    for name in candidates:
        total = 0
        total = candidates_totals.count(name)
        # find the winner
        if(total>greatest_votes):
            greatest_votes = total
            greatest_votes_name = name
        percent = total/row_num*100
        candidates_info.append(f'{name}: {percent}% ({total})')
   
    
output_file_path = "python-challenge-/analysis/PyPoll.txt"
with open(output_file_path, "w") as outfile:
    outfile.write(f'Election Results\n-------------------------\n')
    outfile.write(f'Total Votes: {row_num-1}\n-------------------------\n')
    for c in candidates_info:
        outfile.write(f'{c}\n')
    outfile.write(f'-------------------------\nWinner: {greatest_votes_name}\n-------------------------')
    