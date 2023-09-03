import matplotlib.pyplot as plt
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

# Define the initial and goal states
initial_state = Node((3, 3, 1))
goal_state = (0, 0, 0)

# Create a set to store visited states
visited_states = set()

# Create a function to generate valid successor states
def successors(state_node):
    successors_list = []
    M, C, B = state_node.name

    # Possible boat movements: 1 or 2 people (at least one missionary or one cannibal)
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2 and (m + c >= 1 or (M - m + C - c) == 0):
                # Define the new state after moving missionaries and cannibals
                new_state = (M - m * B, C - c * B, 1 - B)

                # Check if the number of cannibals is greater than the number of missionaries in any state
                if (new_state[0] > 0 and new_state[0] < new_state[1]) or (new_state[0] < 3 and new_state[0] > new_state[1]):
                    continue  # Skip generating successors for this state

                if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3:
                    # Check if the state has not been visited before
                    if new_state not in visited_states:
                        visited_states.add(new_state)
                        successor_node = Node(new_state, parent=state_node)
                        successors_list.append(successor_node)

    return successors_list

# Create the state space tree using BFS
def create_state_space_tree(initial_node, goal_state):
    queue = [initial_node]

    while queue:
        current_node = queue.pop(0)

        if current_node.name != goal_state:
            for successor in successors(current_node):
                queue.append(successor)

# Create and export the state space tree using UniqueDotExporter
create_state_space_tree(initial_state, goal_state)

# Export to a file
UniqueDotExporter(initial_state, nodeattrfunc=lambda node: 'label="{}"'.format(node.name), edgetypefunc=lambda node, child: "->").to_picture("state_space_tree.png")
