# first get all lines from file
with open('test_data.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

# finally, write lines in the file
with open('no_space.ur', 'w') as f:
    f.writelines(lines)
