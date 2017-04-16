from refer import *


def main():
    #
    #input_file = str(argv [1])
    #goal_file = str(argv[2])
    #mode = str(argv[3])
    #output_file = str(argv[4])
    #
    #Initial States
    #initial_state = read_source(input_file)
    explored = []
    initial = state_node([0,0,0],[3,3,1])
    goal = state_node([3,3,1],[0,0,0])
    #print (goal_test(initial,goal))
    result = BFS(initial, goal, explored)
    print (path(result))
    #print (result)

if __name__ == '__main__':
    main()