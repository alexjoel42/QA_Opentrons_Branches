'''
- Builtin 
list, dict, tuple, set 
- Userdefined 
stcack, queue, tree, graph

When selecting an algorithm think "What shape causes the fewest ammount of steps. 
O(n) When you remove the first item from a list, that means that each item must move up in the list order


Stack: linear 
Last element added the first one to be removed. This is essentially like how Alex eats cupcakes
He eats the bottom half first and then adds the top half to the bottom half 
You delete bottom add the top 
This gets done in a few ways:
list, collections.deque, LifoQueue
This can be used if you want to efficiently call from a list of functions or revert behavior.


Queue: linear 
Queue is a linear data structure first in and first out.
It's first come first serve.
This one the coding is important since the list way that's intuitive is at O(n) and you actually want 

Conceptualize, queue is for a customer who is happy pathing through a limited resource. 
stack is for a computer engine that wants to  do the same thing over and over again. 
deque (O(1)) or queue.Queue to organize you. 

Trees: 
This is our first non-linear data structure. A collection of elements are connected to each other 
There is exactly one path between any two nodes. 

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
This seems to be 

The Root: The boss. The very top node (like your "C:" drive or "Documents" folder).

Nodes: The circles. Each node holds some data (like a number or a filename).

Edges: The lines connecting the circles. These are the relationships.

Children: The nodes directly below another node.

Parents: The node directly above.

Leaves: The "dead ends." Nodes at the very bottom that don't have any children.


The Rule: Each parent can have a maximum of 2 children (Left child and Right child).


Graph: 
- nodes are vertices and edges called arcs
- Valid graph finite set of nodes and edges. 
- Vertex 


Linked list: 
- Data element is connected to another one via pointers
- Python doesn't have linked lists in its standard library
- Implementation has to be done using lists manually.

Connection of elements in a chain structure. Sequence connected to move around and access things as required


Variables = one value per one variable. 

'''

sample_list = [5,6,7, 'hell', 6.953]

sample_tuple = (1,3,3)


print('what is an array')

