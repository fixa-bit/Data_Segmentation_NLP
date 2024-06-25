# first get all lines from file
with open('test_data_v2.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

# finally, write lines in the file
with open('no_space_v2.ur', 'w') as f:
    f.writelines(lines)
