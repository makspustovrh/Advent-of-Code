values = { "r": 12, "g": 13, "b": 14 } # cubes in bag

def check_game(line):
    pulls = line.split(";") # separate the game into pulls
    for pull in pulls:
        cubes = pull.split(",") # separate the cubes pulled
        for cube in cubes:
            cube = cube.split()
            # check if pull is possible
            if int(cube[0]) > values[cube[1][0]]:
                return False
    return True
        

if __name__ == "__main__":
    sum = 0 # variable for sum of IDs
    input_file = "input.txt" # puzzle input
    with open(input_file, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        line = line[:-1].split(":")
        if check_game(line[1]): # check if game is possible
            sum += i+1 # add the ID to sum
    print(sum)