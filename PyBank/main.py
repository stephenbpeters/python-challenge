# PyBank script, by stephen.peters@gmail.com

import os
import csv
# Import date class from datetime module
from datetime import date

# path to data
budgetData = os.path.join('./', 'Resources', 'budget_data.csv')

# read our budget_data file
with open(budgetData, 'r') as csvfile:
    #split on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # declare our variables
    monthCount = 0
    monthProfit = 0
    totalProfit = 0
    prevMonthProfit = 0
    changeProfit = 0
    bigUp = 0
    bigDown = 0
    
    # run through our data
    for row in csvreader:
        monthCount += 1
        monthProfit = int(row[1])
        totalProfit = totalProfit + monthProfit
        changeProfit = monthProfit - prevMonthProfit
        if ( changeProfit > 0 ) and ( changeProfit > bigUp ):
            bigUp = changeProfit
            bigMonth = row[0]
        if ( changeProfit < 0 ) and ( changeProfit < bigDown ):
            bigDown = changeProfit
            badMonth = row[0]
        # save this month's profit number for the next calculation
        prevMonthProfit = monthProfit

# calculate average change in profit
averageChange = totalProfit / monthCount

# print to terminal
print(' ')
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(monthCount))
print('Total: ' + str(totalProfit))
print('Average  Change: ' + str(round(averageChange,2)))
print('Greatest Increase in Profits: ' + bigMonth + ' (' + str(bigUp) + ')')
print('Greatest Decrease in Profits: ' + badMonth + ' (' + str(bigDown) + ')')
print('----------------------------')

# write to report.txt file

# path to report file
pathToFile = os.path.join('./', 'analysis', 'report.txt')

reportFile = open(pathToFile, 'w')
reportFile.write('Financial Analysis\n')
reportFile.write('----------------------------\n')
reportFile.write('Total Months: ' + str(monthCount) + '\n')
reportFile.write('Total: ' + str(totalProfit) + '\n')
reportFile.write('Average  Change: ' + str(round(averageChange,2)) + '\n')
reportFile.write('Greatest Increase in Profits: ' + bigMonth + ' (' + str(bigUp) + ')' + '\n')
reportFile.write('Greatest Decrease in Profits: ' + badMonth + ' (' + str(bigDown) + ')' + '\n')
reportFile.write('----------------------------' + ' \n')
# just for fun, let's print the date and time the report was run
today = date.today()
reportFile.write('This report was run: ')
reportFile.write(str(today) + ' \n')
reportFile.write('----------------------------' + ' \n')
reportFile.close()

# job done!
