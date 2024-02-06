class Solution(object):

    def printMatrix(self, m):
        for i in m:
            print(i)


    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        not_zero = []

        #make adjacentcy matrix
        adj_matrix = [[0 for i in range(n)] for i in range(n)]
        for [i, j] in edges:
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1
            adj_matrix[i][i] = 1
            adj_matrix[j][j] = 1

        print("Init adj matrix: ")
        self.printMatrix(adj_matrix)

        while True:
            print("\n")
            self.printMatrix(adj_matrix)
            
            node_totals = []
            not_zero = []
            for node in range(n): 
                edge_total = sum(adj_matrix[node])
                print(f"node {node} has {edge_total} edges")
                if edge_total != 0: 
                    node_totals.append(edge_total)
                    not_zero.append(node)

            if all(x == node_totals[0] for x in node_totals):
                break
            
            smallest_connections = n + 1
            smallest_connection_node = edges[0][0]
            for node in range(n):
                neighbor_count = sum(adj_matrix[node])

                if neighbor_count < smallest_connections and neighbor_count != 0: 
                    smallest_connections = neighbor_count
                    smallest_connection_node = node 
                
            print(f"the smallest connection node is {smallest_connection_node}")
            #remove node with lowest connections

            for node in range(n):
                edge_total = sum(adj_matrix[node])
                if edge_total == smallest_connections:
                    adj_matrix[node] = [0 for i in range(n)]
                    for i in range(n): 
                        adj_matrix[i][node] = 0

        print("\n\n")
        return not_zero
        

a = Solution()

print()
print(a.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))