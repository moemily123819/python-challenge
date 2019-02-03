#
# author - Emily Mo
# date - Feb 3, 2019
# course - bootcamp U Miami Data Analytics
#
#  with input file election_data.csv, produce the following analysis :
#
# TThe total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
#
# Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#
#
#
import os
import csv
import operator
#
#

candidates=[]
output_lines=[]
total=[]
vote_percent=[]
vote_results=[]

def search_candidate(candidate):
    try:
        c = (candidates.index(candidate))
        total[c] = total[c]+1
#
#   if not in list, append to the end of the list and retrieve the index again
#
    except ValueError:        
        candidates.append(candidate)
        total.append(1)
        c = (candidates.index(candidate))
         


input_file = os.path.join('../Resources', 'election_data.csv')
with open(input_file, 'r', newline="") as election_data:
    csvreader = csv.reader(election_data, delimiter =',')
    csv_header = next(csvreader)


# Read each row of data after the header    
    for row in csvreader:
        search_candidate(row[2])

total_votes = sum(vote for vote in total)

# 
# calculate the percentage of each candidate 
# percentage in 3 decimal places

for i in range(0, len(candidates)):
    vote_percent.append(float(total[i]) * 100 /total_votes)


#
# zip all the info - candidate + vote_percent + total - into votes
# and then cast votes into vote_results, a list
# 

votes = zip(vote_percent, candidates, total)

vote_results = list(votes)
#
# sort votes_results in descending order of the percentage
# 

vote_results.sort(key=operator.itemgetter(0), reverse=True)

#
# format the election analysis into a list
# winner thru sort above is located in index 0
#  #
output_lines.append('Election Results')
output_lines.append('----------------------------')
output_lines.append(f'Total Votes : {total_votes}')
output_lines.append('----------------------------')

for i in range(0, len(vote_results)):
    dec_places3 = ("{0:.3f}".format(vote_results[i][0]))
    output_lines.append(f'{vote_results[i][1]}  {str(dec_places3)}%  ({str(vote_results[i][2])})')

output_lines.append('----------------------------')
output_lines.append(f'Winner : {vote_results[0][1]}')
output_lines.append('----------------------------')


for outputlines in output_lines:
    print(outputlines)
#
# output file into folder Resources
#

output_file = os.path.join('../Resources/', 'election_output.csv')

with open(output_file, 'w') as election_output_file:
    for outputlines in output_lines:
        election_output_file.write(outputlines + '\n')