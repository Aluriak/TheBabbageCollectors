# -*- encoding: utf-8 -*-
from queue import Queue
import pickle

# weight of a edge
DISTANCE_BETWEEN_2_NODES = 1


class Graph(object):
    """Basic implementation of graph."""

    def __init__(self, nodes, distanceBetweenTwoNodes = DISTANCE_BETWEEN_2_NODES):
        self.nodes = nodes
        self.first = True
        self.distanceBetweenTwoNodes = distanceBetweenTwoNodes



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



#Fonction Dijkstra (firstNode, target)
    def Dijkstra(self, start, end):
        """Dijkstra. Return path to end"""
        # PICKLE (for work offline with samples)
        #fd = open("RECOVERY_GRAPH", "w")
        #pickle.dump(self.nodes, fd)
        #fd.close()


        # Pour n parcourant noeuds
        # for each node of graph
        walked = {}
        previous = {}
        for key in self.nodes.iterkeys():
            walked[key] = None # infinity
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
        while len(notFoundYet) > 0:
            minimalNode = self.nodeAtMinimumDistance(notFoundYet, walked)
            #print "MINIMAL NODE POPPED: "+str(minimalNode)
        
            if minimalNode == None:
                print "\n\n======ASSERT\n"
                print "notFoundYet = "+str(notFoundYet)+"\n"
                print "\n",
                print "start = "+str(start)
                print "end = "+str(end)
                print "\n",
                for node in notFoundYet:
                    print str(node)+": "+str(walked[node])
                print "\n",
                print "walked = "+str(walked)+"\n"
                print "previous = "+str(previous)+"\n"
                print "\n\n======ASSERT\n\n"
                exit(1)
            # pasEncoreVu.enlever(n1)
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
                distance = self.distanceBetween(successor, minimalNode)
                walkToSucc = walked[successor]
                walkToNode = walked[minimalNode]
                if walkToSucc == None    or    (walkToSucc > (walkToNode + distance)):
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
            if distances[node] != None: 
                if minimal == None or (distances[minimal] > distances[node]):
                        minimal = node

        # return
        return minimal



    def distanceBetween(self, node1, node2):
       """Wait two nodes. Return the minimum distance between these two nodes"""
       return self.distanceBetweenTwoNodes









