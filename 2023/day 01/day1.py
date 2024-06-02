def calibration(line):
    res = []
    for i in line:
        if i.isnumeric():
            res.append(int(i))
    if len(res) < 2:
        return res[0]*10 + res[0]
    return res[0]*10 + res[-1]

if __name__ == "__main__":
    sum = 0
    input_file = "input.txt"
    with open(input_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        sum += calibration(str(line))
    print(sum)