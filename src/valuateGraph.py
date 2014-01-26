import graph
import jacky


class ValuateGraph(graph.Graph):
    """ValuateGraph is a Graph that have a reference to Jacky"""


    def __init__(self, nodes, refToJacky, distanceBetweenTwoNodes = graph.DISTANCE_BETWEEN_2_NODES):
        self.jacky = refToJacky
        super(ValuateGraph, self).__init__(nodes, distanceBetweenTwoNodes)


    def distanceBetween(self, node1, node2):
       """Wait two nodes. Return the avaluation of node2"""
       return self.jacky.evalNode(node2) + super(ValuateGraph, self).distanceBetween(node1, node2)




