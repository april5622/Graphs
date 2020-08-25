class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

def get_parents(child, ancestors):
    parents = []
    #first integer is parent, second is child
    #loop over ancestors at 0 index
    for ancestor in ancestors:
        # if child is child which is the second integer
        if ancestor[1] == child:
            parents.append(ancestor[0])
    return parents

        
def earliest_ancestor(ancestors, starting_node):
    #do DFS
    # create a stack
    stack = Stack()
    # create a visited set
    visited = set()
    # create a list for parents
    parents = []
    # starting node to Stack
    stack.push(starting_node)

    # while stack not empty
    while stack.size() > 0:
        # pop current node off stack
        current_node = stack.pop()
        # if node has not been visited:
        if current_node not in visited:
            # add current node to visted set
            visited.add(current_node)
            # temporary parents is get parents of current node and ancestors
            temparents = get_parents(current_node, ancestors)
            # if temparents
            if temparents:
                # it is parents
                parents = temparents
                # add the node to the new list 
                for p in parents:
                    stack.push(p)
    if len(parents) == 0:
        return -1
    # return the lowest value
    return min(parents)
