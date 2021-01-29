from JDMResponse import *
from QueryProcessor import *
from ResponseFormatter import *
from QueryParser import QueryParser
from JDMApiResponse import JDMApiResponse

from selectolax.parser import HTMLParser
import requests as r

class JDMApi:
    urlPrefix = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel='
    urlPostfix = '&rel='
    
    def __init__(self):
        self.queryProcessor = QueryProcessor(JDMApi.urlPrefix, JDMApi.urlPostfix)
        self.queue = []

    def submit(self, main_query_str, benchmarkEngine = None):
        main_query_str = self.quoteTerms(main_query_str)
        main_query = QueryParser(main_query_str).parse()
        self.queue.append((main_query, 0))
        responses = []

        if benchmarkEngine:
            benchmarkEngine.begin()
            
        while self.queue:
            current = self.queue.pop()
            query = current[0]
            depth = current[1]
            response = self.queryProcessor.process(query)

            if response:
                responses.append(response)

                for refinement in response.refinements:
                    self.queue.append((self.makeQuery(refinement.name), depth + 1))

        result = self.merge(responses, main_query)

        if benchmarkEngine:
            benchmarkEngine.end()

        return result

    def merge(self, responses, query):
        result = JDMApiResponse(query)

        for response in responses:
            if response.query_str == query.content:
                if not query.properties:
                    result.domain_terms.extend(response.getDomainTerms())
                if not query.properties:
                    result.associations.extend(response.getAssociations())
                if not query.properties:
                    result.parts.extend(response.getParts())

            if (not query.properties or (':DEFINITIONS' in query.properties)) and response.definition is not None:
                result.definitions.append(response.definition)


        return result

    def quoteTerms(self, query):
        return ' '.join([ (keyword if keyword.startswith(':') else ("'" + keyword + "'")) for keyword in query.split(' ') ])

    def makeQuery(self, term):
        return QueryParser(self.quoteTerms(term)).parse()
