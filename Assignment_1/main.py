from refer import *
from time import clock

def main():
    initial_file = str(sys.argv[1])
    goal_file = str(sys.argv[2])
    mode = str(sys.argv[3])
    output_file = str(sys.argv[4])
    
    initial = read_source(initial_file)
    goal = read_source(goal_file)
    expand = []

    if mode == '1':
        result = BFS(initial, goal, expand)
    elif mode == '2':
        result = DFS(initial, goal, expand)
    elif mode == '3':
        result = IDDFS(initial, goal, expand)
    elif mode == '4':
        result = A_STAR(initial, goal, expand)
    else:
        print 'Error'
	
    for state in path(result):
        print state
    print len(path(result))
    print len(expand)
    out_solution(output_file, path(result), len(expand))

if __name__ == '__main__':
    main()
