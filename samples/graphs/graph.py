# -*- encoding: utf-8 -*-
from queue import Queue

# poids d'une arrête
DISTANCE_BETWEEN_2_NODE = 1


class Graph(object):
    """Basic implementation of graph."""

    def __init__(self, nodes):
        self.nodes = nodes
        self.first = True



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






    #def shortestPath(self, start, end, path=[]):
        #"""Return list of nodes, included begin and end node. This list is the shortest path founded in graph"""
        ## if its the first recursive call, creat a marked dict
        #if len(path) == 0:
            #self.marked = {}
            #for key in self.nodes.iterkeys():
                #self.marked[key] = False
        #path = path + [start]
                            
        #if start == end:
            #return path
        #if self.first:
            #self.first = False
        #if not self.nodes.has_key(start):
            #return None
        #shortest = None
        #for node in self.nodes[start]:
            #if node not in path and not self.marked[node]:
                #self.marked[node] = True
                #newpath = self.shortestPath(node, end, path)
                #if newpath != None:
                    #if shortest == None or len(newpath) < len(shortest):
                        #shortest = newpath
        #return shortest




    def BFS(self, start, end, path=[]):
        """BFS algorithm"""
        queue = Queue()


#Fonction Dijkstra (firstNode, target)
    def Dijkstra(self, start, end):
        """Dijkstra. Return path to end"""
        # Pour n parcourant noeuds
        # for each node of graph
        walked = {}
        previous = {}
        for key in self.nodes.iterkeys():
            walked[key] = -1 # infinity
            previous[key] = None
            
        #Fin pour
        #début.parcouru = 0
        #pasEncoreVu = noeuds
        walked[start] = 0
        notFoundYet = []
        for key in self.nodes.iterkeys():
            notFoundYet.append(key)

        #Tant que pasEncoreVu != liste vide
        #    n1 = minimum(pasEncoreVu)   // Le nœud dans pasEncoreVu avec parcouru le plus petit
        #    pasEncoreVu.enlever(n1)
        while len(notFoundYet) > 0:
            minimalNode = self.nodeAtMinimumDistance(notFoundYet, walked)
        
            # delete minimal from notFoundYet
            tmp = []
            for node in notFoundYet:
                if node != minimalNode: tmp.append(node)
            notFoundYet = tmp
            # Pour n2 parcourant fils(n1)   // Les nœuds reliés à n1 par un arc
            #     Si n2.parcouru > n1.parcouru + distance(n1, n2)   // distance correspond au poids de l'arc reliant n1 et n2
            #         n2.parcouru = n1.parcouru + distance(n1, n2)
            #         n2.précédent = n1   // Dit que pour aller à n2, il faut passer par n1
            #     Fin si
            # Fin pour
            # for each successor of minimal
            for successor in self.nodes[minimalNode]:
                distance = self.distanceBetween(successor, node)
                walkToSucc = walked[successor]
                walkToNode = walked[minimalNode]
                if walkToSucc == -1    or    (walkToSucc > (walkToNode + distance)):
                    walked[successor] = walkToNode + distance
                    previous[successor] = minimalNode

        # Here, all nodes are founded
            


        #Fin tant que
        #chemin = liste vide
        #n = fin
        #Tant que n != début
        path = []
        target = end
        while target != start:
            # chemin.ajouterAvant(n)
            # n = n.précédent
            path = [target] + path
            target = previous[target]

        #Fin tant que
        #chemin.ajouterAvant(début)
        path = [start] + path
        #Retourner chemin
        return path
    # END Dijkstra


    def nodeAtMinimumDistance(self, notFoundYet, distances):
        """Wait for non-empty list of tuple (x,y), keys of distances dictionnary.
        Return the key with the minimum positive value"""
        # found minimal
        minimal = None
        for node in notFoundYet:
            if (distances[node] >= 0): 
                if minimal == None or (distances[minimal] > distances[node]):
                        minimal = node

        # return
        if minimal == -1:       return None
        else:                   return minimal



    def distanceBetween(self, node1, node2):
        return DISTANCE_BETWEEN_2_NODE


