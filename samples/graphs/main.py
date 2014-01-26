from graph import Graph

nodes = {
    'A' : ['B', 'E'],
    'B' : ['A', 'F', 'C', 'D'],
    'C' : ['B', 'H'],
    'D' : ['B', 'G'],
    'E' : ['A', 'F'],
    'F' : ['E', 'B', 'G'],
    'G' : ['F', 'D', 'H'],
    'H' : ['C', 'G'],
}


g = Graph(nodes)

print g 



for startNode in g.nodes.keys():
    for endNode in g.nodes.keys():
        shortestPath = g.Dijkstra(startNode,endNode)
        print startNode+"to"+endNode+": ",
        if len(shortestPath) == 0: 
            print "No way !"
        else:
            print ", ".join( shortestPath )
    print "END"

notFoundYet = [0,3,5,8,3,6,10,-1]

minimal = None
for node in notFoundYet:
    print node
    if (node >= 0): 
        if minimal == None or (minimal > node):
                minimal = node

# return
if minimal == None:     
    print "No minimal"
else:
    print "Minimal is "+str(minimal)
