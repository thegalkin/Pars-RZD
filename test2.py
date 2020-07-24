nameSearch = "Янаул"
f = open("ids, stations, roads.txt", "r") 
for line in f:
    if nameSearch in line:
        print(line)

