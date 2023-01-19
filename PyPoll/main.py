import os
import csv
# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath) as file:
    csv_reader = csv.reader(file, delimiter=',')
    csv_header = next(csv_reader)

   # print(f"CSV Header: {csv_header}")
    f"Election Results"
    print("Election Results")
    f""
    print("")

    f"---------------------------------------------"
    print("-----------------------------------")
    #creating an Arrary
    Ballot_ID = []
        
    for row in csv_reader:
        Ballot_ID.append(row[2])
     #print(Ballot_ID)

    #Total Votes: 369711
    Total_Votes = len(Ballot_ID)
    print ("Total Votes:",Total_Votes)

    f""
    print("")

    f"---------------------------------------------"
    print("-----------------------------------")
    
    # #candidate_value = "Charles Casper Stockham"
    # with open(csvpath, 'r') as file_handler:
    #  candidate1 = file_handler.read()
    # print("Charles Casper Stockham: ",candidate1.count("Charles Casper Stockham"))

    # with open(csvpath, 'r') as file_handler:
    #  candidate2 = file_handler.read()
    # print("Diana DeGette: ",candidate2.count("Diana DeGette"))

    # with open(csvpath, 'r') as file_handler:
    #   candidate3 = file_handler.read()
    # print("Raymon Anthony Doane: ",candidate3.count("Raymon Anthony Doane"))
    # { } is used for dictionary
    Votes_per_candidate = {}
    for each_candidate in Ballot_ID:
        if not Votes_per_candidate.get(each_candidate):
            Votes_per_candidate[each_candidate]=1
        else:
            Votes_per_candidate[each_candidate]+=1
    #print(Votes_per_candidate)
    for candidate,votes in Votes_per_candidate.items():
        print(f"{candidate}: {round((votes/Total_Votes * 100 ),3)}% ({votes})")

    f"---------------------------------------------"
    print("-----------------------------------")
    
    # find the winner
    #winner = list[candidate1.count,candidate2.count,candidate3.count]()
    #print(winner)

    winner = max(set(Ballot_ID),key=Ballot_ID.count)
    print("Winner: ",winner)
  
#output file
with open ("analysis.txt","w") as txt:
    txt.write(f"Election Results\n")
    txt.write(f"---------------------------------------------\n")
    txt.write (f"Total Votes:{Total_Votes}\n")
    txt.write(f"---------------------------------------------\n")
    for candidate,votes in Votes_per_candidate.items():
        txt.write(f"{candidate}: {round((votes/Total_Votes * 100 ),3)}% {votes}\n")
    txt.write(f"---------------------------------------------\n")
    txt.write(f"Winner: {winner}")