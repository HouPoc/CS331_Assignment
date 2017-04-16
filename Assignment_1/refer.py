import sys

class state_node ():
    
    def __init__(self, left = None, right = None, parent = None):
        self.left_bank = left
        self.right_bank = right
        self.parent = parent

        
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
        new_child = state_node ([m_l-1,c_l,b_l-1], [m_r,c_r+1,b_r+1], current)
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
            state.append(map(int, line))
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
   
def BFS(initial, goal, explored):
    frontier = [initial]
    while len(frontier) != 0:
        current = frontier.pop(0)
        explored.append(current)
        child_nodes = child_node(current)
        for child in child_nodes:
            if is_not_in(child, frontier) or is_not_in(child, explored):
                if goal_test(child,goal):
                    return child
                frontier.append(child)
        #index +=1
    return False
               
    
    
    
    
    
    
    
    
    
   
    
    
    
    

        
