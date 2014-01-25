


class Graph(object):
        """Basic implementation of graph."""

        def __init__(self, nodes):
                self.nodes = nodes


        def addSuccTo(self, thisNode, addedSuccessor):
                """Add given successor to given node. Successor must be a list"""
                # add addedSuccessor to node addedSuccessors
                if self.nodes.get(thisNode) != None:
                        self.nodes[thisNode] += addedSuccessor
                else:
                        self.nodes[thisNode] = addedSuccessor


        def retSuccOf(self, thisNode, retiredSuccessor):
                """Delete successor of given node. retiredSuccessor must be a list"""
                if self.nodes.get(thisNode) != None:
                        # reconstruct the list without content 
                        # of retiredSuccessor
                        self.nodes[thisNode] = [x for x in self.nodes[thisNode] if x not in retiredSuccessor]
                else:
                        pass # nothing to do



        def __str__(self):
                ret = ""
                for node, succ in self.nodes.items():
                        ret += "("+str(node)+"): (" 
                        ret += ", ".join([str(x) for x in succ]) + ")\n"

                return ret






        def shortestPath(self, start, end, path=[]):
                """Return list of nodes, included begin and end node. This list is the shortest path founded in graph"""
                path = path + [start]
                if start == end:
                        return path
                if not self.nodes.has_key(start):
                        return None
                shortest = None
                for node in self.nodes[start]:
                        if node not in path:
                                newpath = self.shortestPath(node, end, path)
                                if newpath != None:
                                        if shortest == None or len(newpath) < len(shortest):
                                                shortest = newpath
                return shortest

