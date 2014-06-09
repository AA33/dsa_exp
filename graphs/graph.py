__author__ = 'aanurag'

from sorting_misc.heapsort import heapify, getMinMax
from sorting_misc.priority_queue import PriorityQueue, PriorityQueueElement
from sorting_misc.sorts import less_than
import sys


class graph:
    def __init__(self, num_of_vertices, edges, directed=False):
        #'Adjacency Matrix' representation
        self.adj_list = [[None] * num_of_vertices for x in range(num_of_vertices)]
        self.vertices = set(i for i in range(len(self.adj_list)))
        self.directed = directed
        if not directed:
            for i in range(len(edges)):
                v1, v2, wt = edges[i]
                self.adj_list[v1][v2] = self.adj_list[v2][v1] = wt
        else:
            for i in range(len(edges)):
                v1, v2, wt = edges[i]
                self.adj_list[v1][v2] = wt


    def printAdjMatrix(self):
        for i in range(len(self.adj_list)):
            for j in range(len(self.adj_list)):
                sys.stdout.write(str(self.adj_list[i][j]) + ' ')
            print

    def _neighbors(self, vertex):
        neighbors = set()
        for i, v in enumerate(self.adj_list[vertex]):
            if v:
                neighbors.add(i)
        return neighbors

    def DFS(self):
        if len(self.vertices) > 0:
            visited = set()
            visited.add(0)
            self._DFS(visited, 0)

    def _DFS(self, visited, vertex):
        for n in self._neighbors(vertex):
            if n not in visited:
                visited.add(n)
                print('Visited:' + str(n))
                self._DFS(visited, n)
        return

    def path(self, source, dest):
        visited = set()
        visited.add(source)
        sd_path = []
        self._path(source, dest, visited, sd_path)
        sd_path = sd_path[::-1]
        sd_path = [(b, a) for (a, b) in sd_path]
        return sd_path

    def _path(self, source, dest, visited, on_the_way):
        for n in self._neighbors(source):
            if n not in visited:
                visited.add(n)
                if n == dest:
                    on_the_way.append((n, source))
                    return True
                else:
                    if self._path(n, dest, visited, on_the_way):
                        on_the_way.append((n, source))
                        return True
        return False

    def spanning_tree(self):
        if len(self.vertices) > 0:
            visited = set()
            visited.add(0)
            return self._spanning_tree(visited, 0, [])


    def _spanning_tree(self, visited, vertex, tree):
        for n in self._neighbors(vertex):
            if n not in visited:
                tree.append((vertex, n))
                visited.add(n)
                self._spanning_tree(visited, n, tree)
        return tree


    def cycle(self):
        cyc_path = set()
        visited = set()
        visited.add(0)
        print('Has cycle:' + str(self._cycle(0, visited, cyc_path)))
        return cyc_path

    def _cycle(self, source, visited, cyc_path, parent=''):
        cyc_path.add(source)
        for n in self._neighbors(source):
            if n not in visited:
                visited.add(n)
                found = self._cycle(n, visited, cyc_path, source)
                if not found:
                    cyc_path.remove(n)
                else:
                    return found
            else:
                if n in cyc_path and n != parent:
                    return True
        return False


    def MST(self):
        if len(self.vertices) > 0:
            visited = set()
            visited.add(0)
            mst = []
            while visited != self.vertices:
                wt_arr = []
                wt_dict = {}
                #Add all neighbors to wt_arr
                for v in visited:
                    unvisited_neighbors = self._neighbors(v).difference(visited)
                    for uv in unvisited_neighbors:
                        wt = self.adj_list[v][uv]
                        wt_arr.append(wt)
                        #Handle case of repeated weights
                        if wt not in wt_dict:
                            wt_dict[wt] = [(v, uv)]
                        else:
                            wt_dict[wt] = wt_dict[wt].append((v, uv))
                #Heapify wt array
                heapify(wt_arr, None, less_than)
                #Get min wt
                min_wt = getMinMax(wt_arr, less_than)
                #Get first edge with that min_wt
                (min_v1, min_v2) = wt_dict[min_wt][0]
                #Remove that edge from the wt dict
                wt_dict[min_wt].remove((min_v1, min_v2))
                if len(wt_dict[min_wt]) == 0:
                    del wt_dict[min_wt]
                #Add this edge to MST
                mst.append((min_v1, min_v2, min_wt))
                #Add vertices visited
                visited.add(min_v1)
                visited.add(min_v2)
            return mst

    def hasNegativeWeights(self):
        for i in range(len(self.adj_list)):
            for j in range(i + 1, len(self.adj_list)):
                if self.adj_list[i][j] and self.adj_list[i][j] < 0:
                    print str(i) + ',' + str(j)
                    return True
        return False

    def sssp_Dijkstra(self, vertex):
        if self.directed:
            return "Dijktstra's algorithm only works on undirected graphs."
        if self.hasNegativeWeights():
            return "Dijkstra's algorithm can't run on a graph with negative weights."

        prQueue = PriorityQueue('min')
        for v in self.vertices:
            elem = PriorityQueueElement('INFINITY', v)
            if v == vertex:
                elem.key = 0
            prQueue.addPriorityQueueElement(elem)
        distance = {}
        while not prQueue.empty():
            minElem = prQueue.getMaxOrMin()
            u = minElem.value
            du = minElem.key
            prQueue.deleteMaxOrMin()
            distance[u] = du
            for z in self._neighbors(u):
                dz = prQueue.findPriority(z)
                if dz:
                    if dz > du + self.adj_list[z][u]:
                        dz = du + self.adj_list[z][u]
                        prQueue.setPriority(z, dz)
            prQueue.heapify()
        return distance

    def _setOfEdges(self):
        edges = set()
        for i in range(len(self.adj_list)):
            for j in range(len(self.adj_list)):
                if self.adj_list[i][j]:
                    edges.add((i, j))
        return edges

    def sssp_BellmanFord(self, vertex):
        if not self.directed:
            return "Bellman Ford algorithm only works on directed graphs."
        edges = self._setOfEdges()
        distance = {}
        for v in self.vertices:
            distance[v] = 99999  #Fake infinity
        distance[vertex] = 0
        for i in range(len(self.adj_list)):
            for (v1, v2) in edges:
                if distance[v2] > distance[v1] + self.adj_list[v1][v2]:
                    distance[v2] = distance[v1] + self.adj_list[v1][v2]
        for (v1, v2) in edges:
            if distance[v2] > distance[v1] + self.adj_list[v1][v2]:
                return "Negative weight cycle."
        return distance


#Main
def main():
    print "Let's make a graph!"
    edges_with_weights = [(0, 1, 6), (0, 2, 5), (1, 2, 12), (2, 3, 9), (2, 5, 7), (5, 4, 15), (5, 6, 10), (6, 0, 8),
                          (6, 7, 3),
                          (7, 0, 14)]
    G1 = graph(8, edges_with_weights)
    G1.printAdjMatrix()
    print(G1._setOfEdges())
    print(G1._neighbors(0))
    print(G1.MST())
    G1_MST = graph(8,[(a,b,wt) for (a,b,wt) in G1.MST()])
    print(G1_MST.cycle())
    G1.DFS()
    print(G1.path(0,6))
    print(G1.spanning_tree())
    G3 = graph(8,[(a,b,1) for (a,b) in G1.spanning_tree()])
    print(G1.cycle())
    G2 = graph(8,[(0,1,6),(1,2,12),(2,3,9),(2,5,7),(5,4,15),(5,6,10),(6,7,3),(7,0,14)])
    print(G2.cycle())
    print(G3.cycle())
    print(G1.sssp_Dijkstra(0))
    GDir = graph(8, edges_with_weights, True)
    print(GDir.sssp_BellmanFord(0))


if __name__ == "__main__":
    sys.exit(main())



