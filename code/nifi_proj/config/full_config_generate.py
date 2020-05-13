from collections import defaultdict
from pathlib import Path
import random
import json
import uuid
import sys

#When this script is called old files are deleted
for p in Path(".").glob("delayed_flow_*.config"):
    p.unlink()


#Predefined constants
MIN_DELAY = 5               
MAX_DELAY = 300
MIN_DELAY_MIDDLE = 305
MAX_DELAY_MIDDLE = 420
MIN_GOALS = 30
MIDDLE_GOAL = 19
MAX_GOALS = 30
MIN_NODES = 6
MAX_NODES = 6
NODE_TYPES = ["n1", "n2", "n3", "n4", "n5", "n6"]
TASK_TYPES = ["type_a", "type_b", "type_c"]
LOAD_TYPES = [1, 2, 3]
 
 #Choose a random number of goals
goals_count = random.randint(MIN_GOALS,MAX_GOALS)
print ("\n\nWill generate " + str(goals_count) + " goals\n")
generated_goals = {}

#All the generated goals are saved in global_result variable
global_result = defaultdict(dict)
global_result['nodes_count'] = 0
global_result['tasks_count'] = 0
global_result['task_type_count']['type_a'] = 0
global_result['task_type_count']['type_b'] = 0
global_result['task_type_count']['type_c'] = 0

#Start generating the goals 
for goal_id in range(0,goals_count):
    print ("Generating goal number [ " + str(goal_id) + " ]\n")
    nodes = random.randint(MIN_NODES,MAX_NODES)
    random_delay = random.randint(MIN_DELAY, MAX_DELAY)
    if (goal_id>MIDDLE_GOAL):
        random_delay = random.randint(MIN_DELAY_MIDDLE, MAX_DELAY_MIDDLE)
    global_result['nodes_count'] += nodes
    flow_node = ""
    flow_goal = ""
    current_goal = {}
    if (goal_id):
        current_goal['delay'] = random_delay
    else:
        current_goal['delay'] = 3
    current_goal['nodes_count'] = nodes
    current_goal['type_a_count'] = 0
    current_goal['type_b_count'] = 0
    current_goal['type_c_count'] = 0
    current_goal['flow_node_head_last'] = "n" + str( random.randint(1,6))
    for node_id in range(0,nodes):
        #Generate random attributes for the current goal
        flow_name = "Goal number " + str(uuid.uuid4()).split('-')[0]
        
        node_type = random.choice(NODE_TYPES)

        flow_node = flow_node + str(node_type)

        task_type = random.choice(TASK_TYPES)

        if task_type == 'type_a':
            global_result['task_type_count']['type_a'] += 1
            current_goal['type_a_count'] +=1
        if task_type == 'type_b':
            global_result['task_type_count']['type_b'] += 1
            current_goal['type_b_count'] +=1
        if task_type == 'type_c':
            global_result['task_type_count']['type_c'] += 1
            current_goal['type_c_count'] +=1
        flow_goal = flow_goal + str(task_type) + ":" + str(random.choice(LOAD_TYPES))
        if node_id < nodes-1:
            flow_node = flow_node + ","
            flow_goal = flow_goal + ","
    #Print some human readable information in the console
    print ("This goals will have " + str(nodes) + " nodes \n")
    print ("The nodes are " + str(flow_node) + "\n")
    print ("The goals are " + str(flow_goal) + "\n\n")
    current_goal["flow_name"] = flow_name
    current_goal["flow_node"] = flow_node
    current_goal["flow_goal"] = flow_goal
    generated_goals[goal_id] = current_goal
    global_result["goals"][goal_id] = current_goal
    print ("\n\n")
    #Save each goal file into a file
    with open('delayed_flow_' + str(goal_id) +  '.config', 'w') as json_file:
        json.dump(current_goal, json_file)