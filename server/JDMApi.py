from JDMResponse import *
from QueryProcessor import *
from ResponseFormatter import *
from QueryParser import QueryParser
from JDMApiResponse import JDMApiResponse
from JDMCache import JDMCache

from selectolax.parser import HTMLParser
import requests as r

class JDMApi:
    urlPrefix = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel='
    urlPostfix = '&rel='

    def __init__(self):
        self.queryProcessor = QueryProcessor(JDMApi.urlPrefix, JDMApi.urlPostfix)
        self.queue = []
        self.cache = JDMCache()

    def submit(self, main_query_str, benchmarkEngine = None, with_cache = False):
        main_query_str = self.quoteTerms(main_query_str)
        main_query = QueryParser(main_query_str).parse()

        if benchmarkEngine:
            benchmarkEngine.begin()

        from_cache = self.getFromCache(main_query)

        if with_cache and from_cache is not None:
            if benchmarkEngine:
                benchmarkEngine.end()

            return from_cache

        self.queue.append((main_query, 0))
        responses = []

        if benchmarkEngine:
            benchmarkEngine.begin()

        while self.queue:
            current = self.queue.pop()
            query = current[0]
            depth = current[1]
            in_cache = False
            response = self.queryProcessor.process(query)

            if with_cache:
                self.cache.insert(query, response, query.content == main_query_str)

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
                if not query.properties:
                    result.synonyms.extend(response.getSynonyms())
                if not query.properties:
                    print(response.getAntonyms())
                    result.antonyms.extend(response.getAntonyms())

            if (not query.properties or (':DEFINITIONS' in query.properties)) and response.definition is not None:
                result.definitions.append(response.definition)


        return result

    def getFromCache(self, query):
        response = JDMApiResponse(query)

        definitions = self.cache.findDefinitions(query.term)

        if not definitions:
            return None

        domain_terms = self.cache.findDomainTerms(query.term)

        if not domain_terms:
            return None

        associations = self.cache.findAssociations(query.term)

        if not associations:
            return None

        parts = self.cache.findParts(query.term)

        if not parts:
            return None

        synonyms = self.cache.findSynonyms(query.term)

        if not synonyms:
            return None

        antonyms = self.cache.findAntonyms(query.term)

        if not antonyms:
            return None

        response.definitions = definitions
        response.domain_terms = domain_terms
        response.associations = associations
        response.parts = parts
        response.synonyms = synonyms
        response.antonyms = antonyms

        return response

    def quoteTerms(self, query):
        return ' '.join([ (keyword if keyword.startswith(':') else ("'" + keyword + "'")) for keyword in query.split(' ') ])

    def makeQuery(self, term):
        return QueryParser(self.quoteTerms(term)).parse()
