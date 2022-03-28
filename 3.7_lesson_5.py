average_height ={
    1: [], 2: [], 3: [], 4: [],
    5: [], 6: [], 7: [], 8: [],
    9: [], 10: [], 11: [],
}
with open('dataset_3380_5.txt') as _:
    for lines in _:
        lines = lines.strip().split()
        line = int(lines[0])
        if line in average_height.keys():
            average_height[line].append(lines[1])
            average_height[line].append(int(lines[2]))
print(average_height)
    
    
    
    
