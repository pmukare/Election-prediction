

@author: Pravin Mukare
"""

def find_election_winner(input_voters):
    
    size = int(input_voters[0])
    if size >= 1 and size <= 10:      
        voters = {}
        for i in input_voters[1:]:
            #print(i)
            if i not in voters:
                voters[i] = 1
            else:
                voters[i] =  voters[i] + 1
                    
        #print(voters)  # to see who got how many votes
        
        votes = 0
        leader = ''
    
        for i in voters.keys():
            if voters[i] > votes:
                leader = i
                votes = voters[i]
                #print(leader)    #to see new leader in each iteration
            elif  voters[i] == votes:
                if i > leader:
                    leader = i
     
        #print('leader',leader,'wins by votes',votes)
        return leader
    

input_voters = [3, 'Victor','Alxe','Alxe']
#input_voters = [10,'Alex','Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary']
#input_voters = [10, 'Victor', 'Veronica', 'Ryan', 'Dave', 'Maria', 'Maria', 'Farah', 'Farah', 'Ryan', 'Veronica']
#input_voters = [10,'Jack','John','Amber','Danny','John','Roy','Harry','Jack','John','Jack','Roy']

print(find_election_winner(input_voters))
