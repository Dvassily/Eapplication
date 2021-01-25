class GetQuery:
    def __init__(self, parent, term, properties):
        self.operation = ':GET'
        self.parent = parent
        self.term = term
        self.properties = properties
        self.content = None

    def toDict(self):
        result = self.__dict__
        del result['parent']
        del result['_tx_position']
        del result['_tx_position_end']
        return result
