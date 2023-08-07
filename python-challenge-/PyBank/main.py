import csv
# get file path
file_path = "python-challenge-/PyBank/Resources/budget_data.csv"
# declare variables
row_num = -1
total = 0
total_change = 0
avg_change = 0
greatest_inc = 0
greatest_inc_date = ""
greatest_dec = 0
greatest_dec_date = ""
change = 0
profit = 0
# open the file
with open(file_path) as csvfile:
# read the file
    reader = csv.reader(csvfile)
    for row in reader:
        # store values of the date and profit
        if(row_num> 0 ):
            change = int(row[1]) - profit
        if(row_num > -1):
            date = row[0]
            profit = int(row[1])
            total += profit
        # find the greatest increase and decrease in profits
        if(change > greatest_inc):
            greatest_inc = change
            greatest_inc_date = date
        if(change < greatest_dec):
            greatest_dec = change
            greatest_dec_date = date
        total_change += change
        row_num +=1
avg_change = total_change/(row_num -1)
# print(f'Financial Analysis\n---------------------')
# print(f'Total Months: {row_num}')
# print(f'Total: {total}')
# print(f'Average Change: {avg_change}')
# print(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})')
# print(f'Greatest Increase in Profits: {greatest_dec_date} (${greatest_dec})')
output_file_path = "python-challenge-/analysis/PyBank.txt"
with open(output_file_path, "w") as outfile:
    outfile.write(f'Financial Analysis\n---------------------\n')
    outfile.write(f'Total Months: {row_num}\n')
    outfile.write(f'Total: ${total}\n')
    outfile.write(f'Average Change: ${avg_change}\n')
    outfile.write(f'Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})\n')
    outfile.write(f'Greatest Increase in Profits: {greatest_dec_date} (${greatest_dec})')