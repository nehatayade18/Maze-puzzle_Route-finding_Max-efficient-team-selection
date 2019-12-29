
#!/usr/local/bin/python3
# route.py : Road trip!
#
# Code by: Kasturi Nikharge (knikharg), Vrinda Mathur(vrmath), Neha Tayade (ntayade)

#from math import radians, cos, sin, asin, sqrt
         
import heapq
import sys 
class Graph(object):
    def __init__(self,graph):
        if graph == None:
            graph = {}
        self.graph = graph
        
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node]=[]
    
    def add_edge(self,node1,node2,length,speed,highway_name):
        gas_gallons=float(length)/(float(400/150) * float(speed) * float(1-(float(speed)/150))**4)
        if node1 in self.graph:
            self.graph[node1].append((node2,length,float(length)/float(speed),gas_gallons))
        else:
            self.graph[node1] = [(node2,length,float(length)/float(speed),gas_gallons)]
        if node2 in self.graph:
            self.graph[node2].append((node1,length,float(length)/float(speed),gas_gallons))
        else:
            self.graph[node2] = [(node1,length,float(length)/float(speed),gas_gallons)]
            
    def edges(self,node):
        return self.graph[node]

  
#from cmath import nan
#===============================================================================
# def heuristic(c1,c2): 
#     b=0
#     r = 3956 # Radius of earth in kilometers. Use 3956 for miles
#     #lat1, lat2, lon1, lon2 = 0
#     for list in citylist:
#         if c1 in list:
#             lat1=float(list[1])
#             lon1=float(list[2])
#         elif c2 in list:
#             lat2=float(list[1])
#             lon2=float(list[2])
#     if(lat1!= nan and lat2!=nan and lon1!=nan and lon2!=nan):
#         lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
#         lat_dist = lat2 - lat1
#         lon_dist = lon2 - lon1
#         a = sin(lat_dist/2)**2 + cos(lat1) * cos(lat2) * sin(lon_dist/2)**2
#         b = 2 * asin(sqrt(a))
#     return float(b * r)           
#===============================================================================

#gets successors for current and pops out the one with least fN     
def successors(fN,route_so_far,distance,time,total_gas_gallons):
    city=route_so_far.split()[-1]
    possible_path=g.edges(city)
    if sysargv2 =="time":
        return [(time + float(node[1])/float(node[2]),*node,) for node in  possible_path]
    elif sysargv2 == "mpg":
        return [ (total_gas_gallons + node[3],*node) for node in  possible_path]
    elif sysargv2 == "distance":
        return [ (distance + float(node[1]), *node) for node in  possible_path]
    elif sysargv2 == "segments":
        return [ (len(str(route_so_far).split())+1, *node) for node in  possible_path]
        
def solve(graph):
    queue=[]
    blank=" "
    heapq.heappush(queue, (0,city1,0,0,0))
    while len(queue)>0:
        (fN,route_so_far,total_distance,total_time,total_gas_gallons) = heapq.heappop(queue)
        
        for (fN_path,path,distance,time,gas_gallons) in successors(fN,route_so_far,total_distance,total_time,total_gas_gallons):
            if path.split()[-1]== city2:
                return(len(route_so_far.split()),float(distance) + float(total_distance),float(time)+float(total_time), float(total_gas_gallons) + float(gas_gallons),route_so_far + blank + path)
            heapq.heappush(queue,(fN_path,route_so_far + blank + path,float(total_distance) + float(distance),float(total_time) + float(time),float(total_gas_gallons) +float(gas_gallons)))
    return False
    
            

if __name__ == "__main__":
    if(len(sys.argv) != 4):
        raise(Exception("Error: expected 3 arguments"))
    sysargv2 =sys.argv[3]
    city1 = sys.argv[1]
    city2 = sys.argv[2]
    #citylist=[]
    
    #===========================================================================
    # with open("city-gps", 'r') as file:
    #     for line in file:
    #         citylist.append([str(i) for i in line.split()])
    #===========================================================================
    g = Graph({})
    with open("road-segments.txt", 'r') as file:
        for line in file:
            segment=[str(i) for i in line.split()]
            g.add_edge(segment[0], segment[1],segment[2],segment[3],segment[4])
    if city1==city2:
        print("Inf")
    else:
        output=solve(g.graph)
        print(str(int(output[0])) + " "+ str(int(output[1])) + " " + str(round(output[2],4)) + " " + str(round(output[3],4)) + " " + str(output[4]))
        
    
