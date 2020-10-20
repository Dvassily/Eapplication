class Relation:
    def __init__(self, relationId, node1, node2, relationType):
        self.relationId = relationId
        self.node1 = node1
        self.node2 = node2
        self.relationType = relationType

    def __eq__(self, other):
        return self.relationId == self.relationId

    def __ne__(self, other):
        return self.relationId != self.relationId
        
    def __lt__(self, other):
        return self.weight < other.weight


