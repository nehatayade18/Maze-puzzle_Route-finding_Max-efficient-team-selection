
#!/usr/local/bin/python3
# solve_luddy.py : Sliding tile puzzle solver
#
# Code by: Kasturi Nikharge (knikharg), Vrinda Mathur(vrmath), Neha Tayade (ntayade)
#
# Based on skeleton code by D. Crandall, September 2019
#
import heapq
import sys
import math
MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }
#MOVES_L = { "RRD": (-1, -2), "RRU": (1, -2), "LLD": (-1, 2), "LLU": (1, 2),"DDR": (-2,-1),"DDL": (-2,1),"UUR": (2,-1),"UUL": (2,1) }
#Moves for Luddy 
MOVES_L = { "H": (-1, -2), "F": (1, -2), "G": (-1, 2), "E": (1, 2),"D": (-2,-1),"C": (-2,1),"B": (2,-1),"A": (2,1) }
visited=[]
#heuristic function which calculates f(s). Manhattan distance is used for h(s) and moves till current state for g(s)
def heuristic(state,move):
    fN= len(move)-1 
    goal_state=sorted(state[:])
    goal_state.remove(0)
    for i in range(len(state)):
        if state[i]!=i+1 and state[i]!=0:
            #fN+= abs(i - (state[i]-1))
            #fN+=1
            curr_row,curr_col=ind2rowcol(i)
            row,col=ind2rowcol(goal_state.index(state[i]))
            fN+=abs(curr_row-row) +abs(curr_col-col)
    return (fN,state,move)

def rowcol2ind(row, col):
    return row*4 + col

def ind2rowcol(ind):
    return (int(ind/4), ind % 4)

def valid_index(row, col):
    return 0 <= row <= 3 and 0 <= col <= 3

def swap_ind(list, ind1, ind2):
    swapped= list[0:ind1] + (list[ind2],) + list[ind1+1:ind2] + (list[ind1],) + list[ind2+1:]
    return swapped

def swap_tiles(state, row1, col1, row2, col2):
    return swap_ind(state, *(sorted((rowcol2ind(row1,col1), rowcol2ind(row2,col2)))))

def printable_board(row):
    return [ '%3d %3d %3d %3d'  % (row[j:(j+4)]) for j in range(0, 16, 4) ]

#get moves for circular if it falls out of board
def CIRC_MOVES(row,col):
    if row>3 and col>3:
        return (-3,-3)
    elif row<0 and col<0:
        return(3,3)
    elif row>3 and col<0:
        return (-3,3)
    elif row<0 and col>3:
        return (3,-3)
    elif row>3:
        return (-3,0)
    elif row<0:
        return (3,0)
    elif col>3:
        return (0,-3)
    elif col<0:
        return (0,3)

def circ_moves_swap(state,empty_row,empty_col,i,j,c):
    if empty_row+i>3 or empty_row+i<0 or empty_col+j >3 or empty_col+j<0:
        i,j=CIRC_MOVES(empty_row+i,empty_col+j)
    return (swap_tiles(state, empty_row, empty_col, int(empty_row)+i, empty_col+j), c)
    
# return a list of possible successor states
def successors(state):
    (empty_row, empty_col) = ind2rowcol(state.index(0)) 
    if sysargv2 == "original":
        return [heuristic(state,move) for (state,move ) in [ (swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c) 
            for (c, (i, j)) in MOVES.items() if valid_index(empty_row+i, empty_col+j) ] if state not in visited]
    elif sysargv2 == "circular":
        return [heuristic(state,move) for (state,move ) in [ circ_moves_swap(state,empty_row,empty_col,i,j,c)
             for (c, (i, j)) in MOVES.items() ] if state not in visited]
    else:
        return [heuristic(state,move) for (state,move ) in [ (swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c) 
            for (c, (i, j)) in MOVES_L.items() if valid_index(empty_row+i, empty_col+j) ] if state not in visited]
        
# check if we've reached the goal
def is_goal(state):
    return sorted(state[:-1]) == list(state[:-1]) and state[-1]==0
    
# The solver! - using BFS right now
def solve(initial_board):
    #queue=PriorityQueue()
    #queue._put((0,initial_board, ""))
    queue=[]
    heapq.heappush(queue, (0,initial_board, ""))
    while len(queue)>0:
        #(fN,state, route_so_far) =queue._get()
        (fN,state, route_so_far) = heapq.heappop(queue)
        visited.append(state)
        for (fN,succ, move) in successors( state ):
            if is_goal(succ):
                return( route_so_far + move )
            heapq.heappush(queue,(fN, succ, route_so_far + move))
    return False

# return sum of tiles that  precedes another tile with a lower number on it
def inversion_count(state):
    inv=0
    i=0
    while i<len(state):
            j=0
            while j<i:
                if state[j] > state[i] and state[i]!=0 and state[j]!=0:
                    inv+=1
                j+=1
            i+=1
    return inv
    
#check if state is solvable i.e if 
def is_solvable(state):
    copy_state=state[:]
    copy_state.reverse()
    return True if ((((math.floor(copy_state.index(0) + 1)/4))%2 == 0 and inversion_count(state)%2!=0) or (((math.floor(copy_state.index(0) +1)/4))%2 != 0 and inversion_count(state)%2==0))  else False

# test cases
if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise(Exception("Error: expected 2 arguments"))
    sysargv2 = sys.argv[2]
   
    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != 16:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))
    print("Solving...")
    if is_solvable(start_state) :
        route = solve(tuple(start_state))
        print("Solution found in " + str(len(route))   + " move(s):" + "\n" + route) if route else print("Inf")
    else:
        print("Inf")
    