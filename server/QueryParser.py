from textx import metamodel_from_str, get_children_of_type
from GetQuery import GetQuery

class QueryParser:
    def __init__(self, queryStr):
        self.queryStr = queryStr
        # TODO: Put in a file
        self.grammar = """
        Model: getQuery=GetQuery | word=STRING;
        GetQuery: ':GET' term=STRING properties*=Property;
        Property: ':SYNONYMS' | ':ANTONYMS' | ':DEFINITIONS';
        """


    def parse(self):
        meta_model = metamodel_from_str(self.grammar, classes=[GetQuery])
        model = meta_model.model_from_str(self.queryStr)

        if model.word:
            self.query_str = ":GET '" + model.word + "'"
            model = meta_model.model_from_str(self.query_str)

        query = model.getQuery
        query.content = self.queryStr

        return query
