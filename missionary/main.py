from time import time
from BFS import bfs
from node import Node

initial_state= [3,3,1]

Node.num_of_instances=0
solution=bfs(initial_state)


