from refer import *
from time import clock

def main():
    initial_file = str(sys.argv[1])
    goal_file = str(sys.argv[2])
    mode = str(sys.argv[3])
    output_file = str(sys.argv[4])
    
    initial = read_source(initial_file)
    goal = read_source(goal_file)
    
    explored = []

    if mode == '1':
        result = BFS(initial, goal, explored)
    elif mode == '2':
        result = DFS(initial, goal, explored)
    elif mode == '3':
        result = IDDFS(initial, goal, explored)
    elif mode == '4':
        result = A_STATR(initial, goal, explored)
    else:
        print 'Error'
	
    for state in path(result):
        print state
    print len(path(result))
    print len(explored)
    out_solution(output_file, path(result), len(explored))

if __name__ == '__main__':
    main()
