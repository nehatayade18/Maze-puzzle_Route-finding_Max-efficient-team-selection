#!/usr/local/bin/python3
#
# choose_team.py : Choose a team of maximum skill under a fixed budget
#
# Code by: Kasturi Nikharge knikharg, Vrinda Mathur vrmath, Neha Tayade ntayade
#
# Based on skeleton code by D. Crandall, September 2019
#
import sys

def load_people(filename):
    people=[]
    with open(filename, "r") as file:
        for line in file:
            l = line.split()
            people.append((l[0],float(l[1]), float(l[2])))
    return people

#returns people in order descending order of cost, similar to way given in skeleton,
#even though knapsack algorithm will access last(minimum cost) element first
def approx_solve(people):
    return sorted(people, key=lambda x: x[2], reverse=True)


#calculates the skill level of a team of 'people' having cost constraint 'budget'
def skill_level(people, budget):
    w,s=0, 0
    for p in people:
        w+= p[2]
    if w < budget:
        for p in people:
            s+=p[1]
    return s
        
#solve implements 0-1 knapsack by recursive dynamic programming.
#online resources used for algorithm understanding  and implementation are stated in the report
def solve(p, n, budget):
    #comment block below indicates the initial approach which is correct for calculation of the cost optimal maximum skill level 
    #a team can have under a budget, however the robots being added to the team are not stored 
    #===========================================================================
    # if n==0 or budget==0:
    #     result = 0
    # elif p[n][2] >  budget:
    #     result=solve(p, n-1, budget)
    # else:
    #     team1=p[n][1] + solve(p, n-1, budget-p[n][2])
    #     team2=solve(p, n-1, budget)
    #     if team1 > team2: 
    #         result=team1
    #     else:
    #         result=team2
    #             
    # return result      
    #===========================================================================
    #added to above, with the same methodology, here we store the entire tuple of the robot information 
    #and calculate skill level of the team in a different function
    if p==[] or n==0 or budget==0 :
        return ()
    elif p[n][2] >  budget:
        return solve(p[1:], n-1, budget)  
    else:  
    #team1 is a tuple of robots, where the first robot in tuple is considered to be a part of the team. 
        team1= (p[n],) + solve(p[0:n], n-1, budget-p[n][2])
    #team2 is a tuple of robots without the same first robot above.
        team2= solve(p[0:n], n-1, budget)
    
    #the skill of both team of robots is judged, only if skill of team1 is greater than team2 will the robot be added
    #skill will return as 0 if cost of team is greater than budget
        result=team1 if skill_level(team2, budget) < skill_level(team1, budget) else team2
    return result
        
if __name__ == "__main__":

    #if(len(sys.argv) != 3):
    #    raise Exception('Error: expected 2 command line arguments')

    budget = float(sys.argv[2])
    people = load_people(sys.argv[1])
    #budget = float(100.0)
    #people = load_people("people-small.txt")
    people=approx_solve(people)
    solution=solve(people, len(people)-1, budget)
    
    if len(solution) > 0:
        print("Found a group with",len(solution), "people costing",sum(p[2] for p in solution), "with total skill",sum(p[1] for p in solution)) 
        for s in solution:
            print(s[0], 1.000000)
    else:
        print("Inf") 
