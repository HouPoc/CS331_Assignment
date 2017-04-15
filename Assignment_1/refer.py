import sys


class state_node ():
    
    def __init__(self, left = None, right = None, parent = None, child = None):
        self.left_bank = left
        self.right_bank = right
        self.parent = parent
        self.child = child
        
def goal_test(current, goal):
    if current.left_bank == goal.left_bank and current.right_bank == goal.left_bank:
        return True
    else:
        return False        
        
def child_node(current,frontier):
    m_l = current.left_bank[0]
    c_l = current.left_bank[1]
    b_l = current.left_bank[2]
    m_r = current.left_bank[0]
    c_r = current.left_bank[1]
    b_r = current.left_bank[2]
    # Move from left to right
    if b_l == 1:
    # Put one missionary in the boat
        if m_l >= 1 and (m_l-1) > c_l and (m_r+1) > c_r:
            m_l -= 1
            m_r += 1
            b_l = 0
            b_r = 1
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)        
    # Put two missionaries in the boat
        if m_l >= 2 and (m_l-2) > c_l and (m_r+2) > c_r:
            m_l -= 2
            m_r += 2
            b_l = 0
            b_r = 1
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)      
    # Put one cannibal in the boat
        if c_l >= 1 and m_l > (c_l-1) and m_r > (c_r+1):
            c_l -= 1
            c_r += 1
            b_l = 0
            b_r = 1
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child) 
            
    # Put one cannibal and one missionary in the boat
        if m_l >= 1 and c_l >= 1 and (m_l-1) > (c_l - 1) and (m_r+1) > (c_r+1):
            c_l -= 1
            m_l -= 1
            m_r += 1
            c_r += 1
            b_l = 0
            b_r = 1
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)
        
    # Put two cannibals in the boat
        if c_l >= 2 and m_l > (c_l-2) and m_r > (c_r+2):
            c_l -= 2
            c_r += 2
            b_l = 0
            b_r = 1
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
    # Move from right to left:
    else:
    # Put one missionary in the boat
        if m_r >= 1 and (m_r-1) > c_r and (m_l+1) > c_l:
            m_l += 1
            m_r -= 1
            b_l = 1
            b_r = 0
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)        
    # Put two missionaries in the boat
        if m_r >= 2 and (m_r-2) > c_r and (m_l+2) > c_l:
            m_l += 2
            m_r -= 2
            b_l = 1
            b_r = 0
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)      
    # Put one cannibal in the boat
        if c_r >= 1 and m_r > (c_r-1) and m_l > (c_l+1):
            c_l += 1
            c_r -= 1
            b_l = 1
            b_r = 0
            new_child = state_node ([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child) 
            
    # Put one cannibal and one missionary in the boat
        if m_r >= 1 and c_r >= 1 and (m_r-1) > (c_r-1) and (m_l+1) > (c_l+1):
            c_l += 1
            m_l += 1
            m_r -= 1
            c_r -= 1
            b_l = 1
            b_r = 0
            new_child = state_node([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)
        
    # Put two cannibals in the boat
        if c_r >= 2 and m_r > (c_r-2) and m_l > (c_l+2):
            c_l += 2
            c_r -= 2
            b_l = 1
            b_r = 0
            new_child = state_node([m_l,c_l,b_l], [m_r,c_r,b_r], current)
            frontier.append(new_child)

def read_source (file):
    f = open(file,'r')
    state = []
    for line in f:
        if line is not None:
            state.append(map(int, line))
    return state_node(state[0],state[1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
