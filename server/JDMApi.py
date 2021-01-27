from JDMResponse import *
from QueryProcessor import *
from ResponseFormatter import *
from QueryParser import QueryParser

from selectolax.parser import HTMLParser
import requests as r

class JDMApi:
    urlPrefix = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel='
    urlPostfix = '&rel='
    
    def __init__(self):
        self.queryProcessor = QueryProcessor(JDMApi.urlPrefix, JDMApi.urlPostfix)
        self.queue = []

    def submit(self, main_query_str, benchmarkEngine = None):
        main_query = QueryParser(main_query_str).parse()
        self.queue.append((main_query, 0))
        done = []

        if benchmarkEngine:
            benchmarkEngine.begin()
            
        while self.queue:
            current = self.queue.pop()
            query = current[0]
            depth = current[1]
            done.append(self.handle(query, depth))

        if benchmarkEngine:
            benchmarkEngine.end()

        definitions = []
        domain_terms = []
        associations = []
        parts = []

        for execution in done:
            if execution is not None:
                if execution.definition:
                    definitions.append(execution.definition)

                    domain_terms.extend(execution.domain_terms)
                    associations.extend(execution.associations)
                    parts.extend(execution.parts)

        return main_query, main_query.term, definitions, domain_terms, associations, parts

    def handle(self, query, depth):
        response = self.queryProcessor.process(query)
        result = self.QueryExecution(query)

        if not response:
            print("No response for " + query.content)
            return None

        if (not query.properties or (':DEFINITIONS' in query.properties)) and response.definition is not None:
            result.definition = response.definition

        response.refinements.sort()

        for refinement in response.refinements:
            self.queue.append((self.makeQuery(refinement.name), depth + 1))

        if depth == 0:
            if not query.properties:
                result.domain_terms = response.getDomainTerms()
            if not query.properties:
                result.associations = response.getAssociations()
            if not query.properties:
                result.parts = response.getParts()

        return result

    def makeQuery(self, term):
        return QueryParser("'" + term + "'").parse()

    class QueryExecution:
        def __init__(self, query):
            self.query = query
            self.definition = None
            self.domain_terms = []
            self.associations = []
            self.parts = []
