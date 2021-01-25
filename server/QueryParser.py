from textx import metamodel_from_str, get_children_of_type
from GetQuery import GetQuery

class QueryParser:
    def __init__(self, query):
        self.query = query
        # TODO: Put in a file
        self.grammar = """
        Model: getQuery=GetQuery;
        GetQuery: ':GET' term=STRING properties*=Property;
        Property: ':SYNONYMS' | ':ANTONYMS' | ':DEFINITIONS';
        """


    def parse(self):
        meta_model = metamodel_from_str(self.grammar, classes=[GetQuery])
        model = meta_model.model_from_str(self.query)
        model.getQuery.content = self.query
        return model.getQuery
