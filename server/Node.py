from functools import total_ordering

@total_ordering
class Node:
    def __init__(self, nodeId, name, nodeType, weight, formattedName = None, isRefinement = False):
        self.nodeId = nodeId
        self.name = name
        self.nodeType = nodeType
        self.weight = weight
        self.formattedName = formattedName
        self.isRefinement = isRefinement
        
    def __eq__(self, other):
        return self.nodeId == self.nodeId

    def __ne__(self, other):
        return self.nodeId != self.nodeId
        
    def __lt__(self, other):
        return ((self.weight, self.name) < (other.weight, other.name))

