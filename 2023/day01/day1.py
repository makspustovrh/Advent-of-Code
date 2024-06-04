def calibration(line):
    res = [] # var for all numbers in line
    for i in line:
        if i.isnumeric(): # find all numbers
            res.append(int(i))
    if len(res) < 2: # if only 1 number in line
        return res[0]*10 + res[0]
    return res[0]*10 + res[-1]

if __name__ == "__main__":
    sum = 0 # var for sum of calibration numbers
    input_file = "input.txt" # puzzle input
    with open(input_file, 'r') as f:
        lines = f.readlines()
    for line in lines: # for each line
        sum += calibration(str(line)) # add the calibration number
    print(sum)