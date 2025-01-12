###### Dict in robotic

#Depth first search

#        A
#       / \
#      B   C
#     / \    \
#    D   E    F

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []    
}


start = 'A'
goal = 'D'
fronteir = [start]
explored = set() # Use a set for unique (ignore duplicate append)

print(fronteir, explored)

while (len(fronteir)) > 0:
    current = fronteir.pop() 
    print(current)

    if current == goal:
        print("Goal Reach")
        break

    for neighbor in graph[current]:
        fronteir.append(neighbor)

