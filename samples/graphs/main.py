from graph import Graph

nodes = {
        'A' : ['B', 'E'],
        'B' : ['A'],
}


g = Graph(nodes)

g.addSuccTo('A', 'D')
g.addSuccTo('D', 'B')
g.retSuccOf('A', 'C')
g.retSuccOf('A', 'E')
g.retSuccOf('B', 'E')

g.addSuccTo('C', 'A')
g.addSuccTo('E', 'C')
g.addSuccTo('B', 'E')
g.addSuccTo('A', 'B')
print g 



for startNode in g.nodes.keys():
        for endNode in g.nodes.keys():
                shortestPath = g.shortestPath(startNode,endNode)
                print startNode+"to"+endNode+": ",
                if shortestPath == None: 
                        print "No way !"
                else:
                        print ", ".join( shortestPath )
        print ""

