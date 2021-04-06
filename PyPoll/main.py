# poll stats script by stephen.peters@gmail.com

import os
import csv
# Import date class from datetime module
from datetime import date

# path to data
pollData = os.path.join('./', 'Resources', 'election_data.csv')

# read our data file
with open(pollData, 'r') as datafile:
    #split on commas
    csvreader = csv.reader(datafile, delimiter=',')
    header = next(csvreader)

# declare our variables
    totalVoters = 0
    # we'll put our candidates in a dictionary
    candies = {}
    votesForCandie = 0
    candieVote = 1
    
    for row in csvreader:
        totalVoters += 1
        currentCandie = row[2]
        if currentCandie in candies:
            candieVote = candies.get(row[2])
            candieVote += 1
            candies.update({row[2]: candieVote})
            candieVote = 1
        else:
            candies.update({row[2]: candieVote })

# time to print our election stats
# let's convert the dictionary to a tuple
candie_stats = list(candies.items())
print('')
print('-------------------------')
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(totalVoters))
print('-------------------------')
# let's convert the dictionary to a tuple
candie_stats = list(candies.items())
# let's see how our candidates performed!
# set our winner variables
winnerName = ''
winnerVotes = 0
for i in range(len(candie_stats)):
    candieSolo = candie_stats[i]
    votePercent = candieSolo[1] / totalVoters
    print(str(candieSolo[0]) + ': ' + '{:.2%}'.format(votePercent) + '% ' + '(' + str(candieSolo[1]) + ')' )
    # let's find the winner
    if candieSolo[1] > winnerVotes:
        winnerName = candieSolo[0]
        winnerVotes = candieSolo[1]
    
print('-------------------------')
print('  Winner: ' + winnerName)
print('-------------------------')
print('')
today = date.today()
print('This report was run: ' + str(today))
print('')

# now to print the report text file

# path to the report file
pathToFile = os.path.join('./', 'analysis', 'report.txt')

reportFile = open(pathToFile, 'w')
reportFile.write('\nElection Results\n')
reportFile.write('-------------------------\n')
reportFile.write('Total Votes: ' + str(totalVoters) + '\n')
reportFile.write('-------------------------\n')
# let's see how our candidates performed! (yes, this could be a function)
# set our winner variables
winnerName = ''
winnerVotes = 0
for i in range(len(candie_stats)):
    candieSolo = candie_stats[i]
    votePercent = candieSolo[1] / totalVoters
    reportFile.write(str(candieSolo[0]) + ': ' + '{:.2%}'.format(votePercent) + '% ' + '(' + str(candieSolo[1]) + ')\n' )
    # let's find the winner
    if candieSolo[1] > winnerVotes:
        winnerName = candieSolo[0]
        winnerVotes = candieSolo[1]
reportFile.write('-------------------------\n')
reportFile.write('  Winner: ' + winnerName + '\n')
reportFile.write('-------------------------\n\n')
reportFile.write('This report was run: ' + str(today) + '\n\n')
reportFile.close()

# job done!
