# Deptrh first traversal

## Challenge 38
Write the following method for the Graph class:

- Name: Depth first
- Arguments: Node (Starting point of search)
- Return: A collection of nodes in their pre-order depth-first traversal order
- Program output: Display the collection

## Solution
 def depth_first_search(self, start):
        def pre_order(vertex, collection=[], visited=set()):
            if not vertex or vertex not in self._adjacency_list or vertex in visited:
                return collection
            collection.append(vertex.value)
            visited.add(vertex)
            edge_list = self._adjacency_list[vertex]
            for edge in edge_list:
                pre_order(edge.vertex, collection, visited)
            return collection
        return pre_order(start)



## Collaborators
- Ryan McMillan
- Alec Torres
- Jamal Malik
