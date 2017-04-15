import refer


def main():
    #
    input_file = str(argv [1])
    goal_file = str(argv[2])
    mode = str(argv[3])
    output_file = str(argv[4])
    #
    #Initial States
    initial_state = read_source(input_file)