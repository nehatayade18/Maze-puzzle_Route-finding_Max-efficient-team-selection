# Assignment 1

# PART 1
## Assumptions
For the search abstraction, we have assumed that the board remains an n*n or square matrix where n is 4 i.e. that it is a 15puzzle.

## General plan adopted
We have implemented A* algorithm to solve this weighed graph of puzzle board and determine which of the paths to choose and extend as it  returns a least-cost path from source state to goal state. A* minimizes f(n)=g(n)+h(n) where g(n) is the cost of the path from the start node to n(ie, current node), and h(n) is a heuristic function. Earlier, for all the valid moves, each neighbour index was traversed to calculate the placements for blank tile while trying to reach from the source cell to the target cell. To avoid the unnecessary successor checks, we implemented a heuristic check of Manhattan distance calculation to find the target state efficienly with the least possible moves. To return the most cost effective node, we have applied the concept of priority queue to perform repeated selection of nodes in the sense that it pushes in all the possible successor values for the current node and pops out the least manhattan distance move on first priority. Also, to avoid the backtracking of check on the explored nodes, a list of all the visited sets are preserved in order to avoid their heuristic check multiple times. 
The heuristic function h(n) is admissible since it takes the shortest displacement and thus, never overestimates the cost to reach the goal in the sense that it is the smallest distance between any two points. Also A* is guaranteed to terminate and complete if a solution exists as it tends to explore the whole set of connected nodes.

A* explores the branches exponentially till the depth of the solution in an approach similar to best-first search which almost guarantees completeness for the closed graph paths. The heuristic of manhattan chosen allows us to prune away the branches that are cost intensive that otherwise would be considered in other uninformed search algorithms.

## Type of moves

1. Original:
Moves allowed for this type of model requires the blank space to be moved, one place at a time, in one of the four standard directions in the 2D map grid. The successor state funtion gives the list of heuristic distances for all the valid moves specified and exchanges the empty tile with the shortest distance. The heap queue decides to pop out the least heuristic distance edge value along with the associated cost. This algorithm continues until the goal node has value lower than any node of the queue. Another check condition of permutation inversion is added to the code to check the even-odd parity of the row of blank tile from bottom of the search graph and total of the number of inversions of individual enities of the puzzle from their goal positions. If this method of obtaining the goal state is selected, the nodes get appended to the route in series to give the shortest path and cost so far.

2. Circular:
A new method of path finding is used in which used,here  moves of the original model along with the wrap around moves for the edges. Also at the corners two wrapping options were possible for the adjacent edges. In this case, we passed both the move distances to the heuristic for the succesor node values and selected the one with least manhattan count. Permutation inversion is checked for the parities of blank tile position and the number of inversions and for the even-odd combination or vice-versa the condition of whether the board is solvable or not is checked. Also, the board was checked for the edges at the boundaries and based on the wrapping constraint the blank tile was shifted by giving it displacement of coordinates that get added to the current ones. Based on the successors in the priority queue and check of visited node sets, the node with the least heuristic is selected to swap the blank tile with the chosen node.

3. Luddy:
This model supports diagonal movement of the blank tile,for example two steps right and one up,one to the left and two down, etc and then find the shortest manhattan distance between two nodes using the heuristic function that checks if the ith index corresponds to the (i+1)th tile value. For all the valid successor values the heuristic is checked and the priority queue returns the node with the least cost and appends it to the route. This position is selcted and swapped with the position coordinates of the blank tile. This continues till the goal state is reached.

Code changes:
* CIRC_MOVES method is added to give moves for circular variant when the current move is greater than or less the board index. 
* inversion_count method gives the inversion count of the current state which is then clubbed with the row position of the empty from the bottom. This makes the decision whether the board is solvable or not.
* heuristic method is added which calculates f(s) = g(s) + h(s). The path cost till current state and estimated cost required to traverse till the destination using Manhattan distance.


# PART 2
## General plan adopted
In part two, we are given the source, destination and the cost function. We have implemented A* algorithm, which traverses through a generated graph and then chooses the next node based on the minimum value of f(s) = g(s) + h(s). The heuristic function h(s) is admissible since it takes the shortest displacement and thus, never overestimates the cost to reach the goal. Also A* is guaranteed to terminate and complete if a solution exists as it tends to explore the whole set of connected nodes. 

## Types of cost function
1. Segments
Segments considers the least number of edges to the next node. Also, the number of edges explored till now.

2. Distance
For distance we have considered, the length bof road segment till the current node and length to the next node. 

3. Mpg 
Inorder to maximize the mpg, we have to minimize the number of gallons. So miles/mpg gives us the total gallons. Gallons used till current node and gallons required to travel till the next is used as an estimate.

4. Time 
Time taken to travel is calculated by speed/distance. Time taken till current node and time to travle to the next is used as an estimated.

Generation of graph was understood by referring to https://www.python-course.eu/graphs_python.php.

# PART 3 
## General plan adopted
0-1 Knapsack algorithm was implemented to create a team of maximum skill uner a certain budget. A naive recursive algorithm was used to to attain a the team of robots. The problem has an *optimal substructure* where 2 cases are considered: 
(1) A team with robot i, the robot considered. 
(2) A team without robot i
If the value that is skill level of case(1) is greater than skill level of case(2), then robot i is added to the team.
The *base case* in this recursive solution is that is that budget=0 or number of robots in p that is the subset of robots being considered as a team is 0 then that recursion is exited.  
It is important to note that an appropriate solution is only obtained when the robots are considered in descending order of their cost. ('people' tuple in descending order of cost, and 'solve(p, n, budget)' goes from last to first robot in 'people' implying that it considers the robot having highest cost first)

## Progress Report
### *(1)* 
Reading the question it only implied that the team (each robot having a certain cost), with the greatest skill must be created, with the basic constraint of a budget. Naturally "greedy solution" was thought of adding robots to the team in decreasing order of skill.
### *(2)*
On further discussion, the conclusion was reached that mutiple robots, having a greater skill level together, could be added for the same or lower cost so a different algorithm was implemented.
### *(3)* 
The 0-1 Knapsack algorithm, was oncluded upon, so that robots added would be whole and not in fractions. Online resources of:
* https://www.youtube.com/watch?v=xOlhR_2QCXY
* https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
were used to understand the 0-1 Knapsack recursive algorithm.
### *(4)* 
While these algorithms, solved the question of what is the maximum skill that the team can have, another obstacle arised to save the robots that were being added to the team. For this, 1 idea and 1 syntax were influenced by https://rosettacode.org/wiki/Knapsack_problem/0-1#Brute_force_algorithm . The idea to calculate the skill level in a separate function and focus on creating the team of robots in function 'solve'. The syntax that the code above helped the understand of creating a tuple of robots with a help of a ','. Without it, the excecution kept giving "TypeError: unsupported operand type(s) for +=: 'int' and 'str'."


## Code changes :
* Storing of a robot, their skill and cost in a *tuple rather than dictionary*, as a matter of preference as a newcomer to Python.
* implemented completely solve(people, budget) method to implement recursive solution to keep track of robots added to the team rather than approx_solve(people, budget) which was not the cost optimised solution to the problem. 
* approx_solve(people) now only returns tuple of robots in decreasing order of cost now
* addition of skill_level(p, budget) which returns the skill for a certain group of robots (p) if their cost is below under the budget otherwise returns 0
* If there is no team of robots formed that is there are 0 robots returned, the answer is *Inf* 

