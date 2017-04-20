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

    if mode == 'bfs':
        result = BFS(initial, goal, expand)
    elif mode == 'dfs':
        result = DFS(initial, goal, expand)
    elif mode == 'iddfs':
        result = IDDFS(initial, goal, expand)
    elif mode == 'astar':
        result = A_STAR(initial, goal, expand)
    else:
        print 'Error'
	
    if len(path(result)) != 0:
        print 'The path is:'
        for state in path(result):
            print 'left bank: ' + str(state[0]) + ' ' + 'right bank:' + str(state[1])
        print 'The number of nodes on solution is ' + str(len(path(result)))
    else:
        print 'No solution found!'

    print 'The number of explored node is ' + str(len(expand))
    out_solution(output_file, path(result), len(expand))

if __name__ == '__main__':
    main()
