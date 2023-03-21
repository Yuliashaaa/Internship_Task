#  2. Counting islands

You have a matrix $M \times N$ that represents a map. There are $2$ possible states on the map: $1$ - islands, $0$ - ocean. 
Your task is to calculate the number of islands in the most effective way. Please write code in Python 3.

## My solution

While implementing this task I decided to use DFS (Depth First Search) Algorithm, because it is an algorithm for searching all the vertices of a graph or tree data structure. We can think about a map of marked islands as about matrix of graph connections. Then, one full start of the DFS algorithm will show us all the connections which are possible from the selected point, which means it will be one island. And we keep going while we will not cover all the points.

The DFS Algorithm works as follows:
1. Start by putting any one of the graph's vertices on top of a stack.
2. Take the top item of the stack and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
4. Keep repeating steps 2 and 3 until the stack is empty.
