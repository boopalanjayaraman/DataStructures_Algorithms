import math
import heapq

from helpers import Map, load_map #, show_map

class NodePathCostMap:
    def __init__(self, node, path_to_this, cost_so_far):
        self.node = node
        self.path = path_to_this
        self.cost_so_far = cost_so_far

class PathCostMap:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost

class NextIntersection:
    def __init__(self, intersection, frontier_cost, estimated_cost, h_cost):
        self.intersection = intersection
        self.frontier_cost = frontier_cost
        self.estimated_cost = estimated_cost
        self.h_cost = h_cost

def shortest_path(M,start,goal):
    print("shortest path called")
    
    global min_total_cost_so_far 
    global min_cost_path 

    min_total_cost_so_far = None
    min_cost_path = []

    map_graph = M
    intersec_current_index = start
    intersec_goal_index = goal

    possible_paths = []
    distances = []
    visited_intersections = dict()
    #visited_intersections[start] = NodePathCostMap(start, [start], 0)

    path = []
    #path.append(start)

    get_possible_next_intersections(intersec_current_index, intersec_goal_index, map_graph, visited_intersections, [*path], 0, possible_paths)
    
    for possible_path in possible_paths:
        print('path: ', possible_path.path, ', cost:', possible_path.cost, '\n')

    #return possible_paths[0].path
    return min_cost_path

def print_msg(*args):
    #print(args)
    pass

min_total_cost_so_far = None
min_cost_path = []

def get_possible_next_intersections(intersec_current_index, intersec_goal_index, map_graph, visited_intersections, current_path, current_cost, paths):

    #if this was not visited already
    if intersec_current_index not in visited_intersections:
        print_msg('this was *not* visited before. Node: ', intersec_current_index, ', current_path:', current_path, '\n')
        current_path.append(intersec_current_index)
        visited_intersections[intersec_current_index] = NodePathCostMap(intersec_current_index, [*current_path], current_cost)
    else:
        #see if this path now has a smaller cost than the one visited before
        print_msg('Oh, this was visited before. Node: ', intersec_current_index, ', current_path:', current_path, '\n')

        node_visited_in_past = visited_intersections[intersec_current_index]
        if current_cost < node_visited_in_past.cost_so_far:
            print_msg('Oh, but seems cost is less this time. Node: ', intersec_current_index, '\n')
            current_path.append(intersec_current_index)
            node_visited_in_past.cost_so_far = current_cost
            node_visited_in_past.path = [*current_path]
        else:
            return

    global min_total_cost_so_far
    global min_cost_path

    if intersec_current_index == intersec_goal_index:
        current_path_cost_map = PathCostMap(current_path, current_cost)
        #paths.append(current_path)
        paths.append(current_path_cost_map)

        if  min_total_cost_so_far == None:
            min_total_cost_so_far = current_cost
            min_cost_path = current_path
        elif current_cost < min_total_cost_so_far:
            min_total_cost_so_far = current_cost
            min_cost_path = current_path

        print_msg('added path. ', current_path)
        return

    print_msg('get possible next intersections for: ', intersec_current_index)

    #get distances      
    h_distances = get_next_step_distances(intersec_current_index, intersec_goal_index, map_graph) 

    while(len(h_distances) > 0):
        (h_distance, next_step_intersection) = heapq.heappop(h_distances)

        next_step = next_step_intersection.intersection
        next_step_cost = next_step_intersection.frontier_cost
        full_path_cost = current_cost + next_step_cost

        print_msg('next intersection by distance -  ', next_step, ', distance: ', h_distance, '\n')

        if min_total_cost_so_far == None or full_path_cost < min_total_cost_so_far: 
            print_msg('full path cost is less than min total cost so far, so proceeding.')
            #get possible next intersections recursively

            get_possible_next_intersections(next_step, intersec_goal_index, map_graph, visited_intersections, [*current_path], full_path_cost, paths)

            

def get_next_step_distances(intersec_current_index, intersec_goal_index, map_graph):

    if intersec_current_index == intersec_goal_index:
        next_step_intersection = NextIntersection(intersec_current_index, 0, 0, 0)
        return [(0, next_step_intersection)]

    h_distances = [] # available for debugging purposes
    heapq.heapify(h_distances)

    for next_step in map_graph.roads[intersec_current_index]:
        # distance to the next step
        frontier_distance  = get_distance_cost(map_graph.intersections[intersec_current_index], map_graph.intersections[next_step])
        # heuristic value (smart guess)
        estimated_distance = get_distance_cost(map_graph.intersections[next_step], map_graph.intersections[intersec_goal_index])
        # calculate h 
        h_distance =  frontier_distance + estimated_distance
        next_step_intersection = NextIntersection(next_step, frontier_distance, estimated_distance, h_distance)
        heapq.heappush(h_distances, (h_distance, next_step_intersection))

    return h_distances


def get_distance_cost(intersection1, intersection2):
    #x1,y1
    x1 = intersection1[0]
    y1 = intersection1[1]
    #x2,y2
    x2 = intersection2[0]
    y2 = intersection2[1]
    #calculate the distance between co-ordinates using formula
    distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))

    return distance

#if __name__ == "__main__":

#THIS CODE WORKS WITH ONLY networkx==1.11
#Uninstalled networkx==2.3 and installed networkx==1.11
#Created a new conda environment boopy3 to run this program
#installed networkx in that. Could not install plotly since it is deprecated. Commented graphing modules.
# Can see a libraries version by --> import networkx; print(networkx.__version__)
# THIS pickle FILE is dumped using version 1.11 and hence could not be opened in 2.3 since some attributes were missing

map_40 = load_map('map-40.pickle')
map_10 = load_map('map-10.pickle')


path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)


path = shortest_path(map_40, 8, 24)
if path == [8, 14, 16, 37, 12, 17, 10, 24]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)


path = shortest_path(map_40, 8, 14)
if path == [8, 14]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)
