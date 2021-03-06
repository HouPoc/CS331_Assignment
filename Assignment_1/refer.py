import sys
import operator

class state_node ():
    
    def __init__(self, left = None, right = None, parent = None, f_value = None):
        self.left_bank = left
        self.right_bank = right
        self.parent = parent
        self.f_value = f_value

        
def goal_test(current, goal):
    for i in range(3):
        if current.left_bank[i] != goal.left_bank[i] or current.right_bank[i] != goal.right_bank[i]:
            return False
    return True

        
def check_balance(action):
    if action.left_bank[0] >= 0 and action.left_bank[1] >= 0 and action.right_bank[0] >= 0 and action.right_bank[1] >= 0:
       if (action.left_bank[0] >= action.left_bank[1] or action.left_bank[0]==0) and (action.right_bank[0] >= action.right_bank[1] or action.right_bank[0]==0):
            return True
    return False


def child_node(current):
    children = []
    m_l = current.left_bank[0]
    c_l = current.left_bank[1]
    b_l = current.left_bank[2]
    m_r = current.right_bank[0]
    c_r = current.right_bank[1]
    b_r = current.right_bank[2]

    if b_l == 1:
		# Put one missionary in the boat
        new_child = state_node ([m_l-1,c_l,b_l-1], [m_r+1,c_r,b_r+1], current)
        if check_balance(new_child):
            children.append(new_child)  
        # Put two missionaries in the boat
        new_child = state_node ([m_l-2,c_l,b_l-1], [m_r+2,c_r,b_r+1], current)
        if check_balance(new_child):
            children.append(new_child) 
        # Put one cannibal in the boat
        new_child = state_node ([m_l,c_l-1,b_l-1], [m_r,c_r+1,b_r+1], current)
        if check_balance(new_child):
            children.append(new_child) 
        # Put one cannibal and one missionary in the boat
        new_child = state_node ([m_l-1,c_l-1,b_l-1], [m_r+1,c_r+1,b_r+1], current)
        if check_balance(new_child):
            children.append(new_child) 
        # Put two cannibals in the boat
        new_child = state_node ([m_l,c_l-2,b_l-1], [m_r,c_r+2,b_r+1], current)
        if check_balance(new_child):
            children.append(new_child) 
    else:
         # Put one missionary in the boat
        new_child = state_node([m_l+1,c_l,b_l+1], [m_r-1,c_r,b_r-1], current)
        if check_balance(new_child):
            children.append(new_child) 
        # Put two missionaries in the boat
        new_child = state_node ([m_l+2,c_l,b_l+1], [m_r-2,c_r,b_r-1], current)
        if check_balance(new_child):
            children.append(new_child) 
        # Put one cannibal in the boat
        new_child = state_node ([m_l,c_l+1,b_l+1], [m_r,c_r-1,b_r-1], current)
        if check_balance(new_child):
            children.append(new_child)
        # Put one cannibal and one missionary in the boat
        new_child = state_node([m_l+1,c_l+1,b_l+1], [m_r-1,c_r-1,b_r-1], current)
        if check_balance(new_child):
            children.append(new_child)  
        # Put two cannibals in the boat
        new_child = state_node([m_l,c_l+2,b_l+1], [m_r,c_r-2,b_r-1], current)
        if check_balance(new_child):
            children.append(new_child)
 
    return children

            
def read_source (file):
    f = open(file,'r')
    state = []
    for line in f:
        if line is not None:
            state.append(map(int, line.split(',')))
    return state_node(state[0],state[1])
    

def is_not_in (target, collection):
    for element in collection:
        if goal_test (target, element):
            return False
    return True
   

def path (terminate_state):
    node = terminate_state
    route = []
    while node is not None:
        route.insert(0,(node.left_bank, node.right_bank))
        node = node.parent
    return route
   
def BFS(initial, goal, expand):
    frontier = [initial]
    explored = {}

    while len(frontier) != 0:
        current = frontier.pop(0)
        explored[create_key(current)] = current
        expand.append(current)
        child_nodes = child_node(current)
        for child in child_nodes:
            if goal_test(child, goal):
                return child
            key = create_key(child)
            if is_not_in(child, frontier) and (not explored.has_key(key)):
                frontier.append(child)
    return False


def DFS(initial, goal, expand):
    frontier = [initial]
    explored = {}

    while len(frontier) != 0:
        current = frontier.pop(0)
        if goal_test(current, goal):
            return current
        explored[create_key(current)] = current
        expand.append(current)
        child_nodes = child_node(current)
        i = 0
        for child in child_nodes:
            key = create_key(child)
            if is_not_in(child, frontier) and (not explored.has_key(key)):
                frontier.insert(i, child)
                i += 1
    return False


def IDDFS(initial, goal, expand):
    for depth in range(100000):
    	explored = {}
    	frontier = [initial]
    	result = R_DLS(initial, goal, depth, explored, expand, frontier)
    	if result != 'cutoff':
        	return result


def R_DLS(current, goal, limit, explored, expand, frontier):
	temp = []
	key = create_key(current)
	explored[key] = current

	if len(frontier) != 0:
		frontier.pop(0)

	if goal_test(current, goal):
		return current
	elif limit == 0:
		return 'cutoff'
	else:
		cutoff_occurred = False
		expand.append(current)
        child_nodes = child_node(current)
        
        i = 0
        for child in child_nodes:
        	key = create_key(child)
        	if is_not_in(child, frontier) and (not explored.has_key(key)):
        		frontier.insert(i, child)
        		temp.insert(i, child)
        		i += 1

        for child in temp:
			result = R_DLS(child, goal, limit - 1, explored, expand, frontier)
			if result == 'cutoff':
				cutoff_occurred = True
			elif result is not None:
				return result
        
        if cutoff_occurred:
            return 'cutoff'
        else:
            return None


def A_STAR(initial, goal, expand):
    explored = {}
    initial.f_value = 0 + heuristic(initial, goal)
    frontier = [initial]
    while len(frontier) != 0:
        current = frontier.pop(0)
        if goal_test(current, goal):
            return current
        expand.append(current)
        explored[create_key(current)] = current
        child_nodes = child_node(current)
        for child in child_nodes:
            key = create_key(child)
            if is_not_in(child, frontier) and (not explored.has_key(key)):
                store_priority_list(child, initial, goal, frontier)
    return False


def store_priority_list(node, initial, goal, frontier):
    node.f_value = path_cost(node) + heuristic(node, goal) 
    frontier.append(node)
    frontier.sort(key = operator.attrgetter('f_value'))


def heuristic(node, goal):
    return (goal.left_bank[0] - node.left_bank[0]) + (goal.left_bank[1] - node.left_bank[1])


def path_cost(node):
    return len(path(node)) - 1


def create_key(node):
    return str(node.left_bank[0]) + str(node.left_bank[1]) + str(node.left_bank[2]) + str(node.right_bank[0]) + str(node.right_bank[1]) + str(node.right_bank[2])


def out_solution (file, path, expand):
    f = open(file, 'w')
    if len(path) != 0:
        for state in path:   
            f.write('Left Bank: ' + str(state[0][0]) + ' missionaries, ' + str(state[0][1]) + ' cannibal, '+ str(state[0][2]) + ' boat ' + ' Right Bank: ' + str(state[1][0]) + ' missionaries, ' + str(state[1][1]) + ' cannibals, ' + str(state[1][2]) + ' boat\n')
        f.write('The number of nodes on solution is ' + str(len(path)) + '\n')
    else:
        f.write('No solution found\n')     
    f.write('The number of nodes expanded is ' + str(expand) + '\n')
    f.close()
