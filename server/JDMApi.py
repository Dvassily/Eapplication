from JDMResponse import *
from QueryProcessor import *
from ResponseFormatter import *

from selectolax.parser import HTMLParser
import requests as r

class JDMApi:
    urlPrefix = 'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel='
    urlPostfix = '&rel='
    
    def __init__(self):
        self.queryProcessor = QueryProcessor(JDMApi.urlPrefix, JDMApi.urlPostfix)
    
    def submit(self, mainQuery, benchmarkEngine = None):
        definitions = {}
        domainTerms = []
        queue = [ (mainQuery, 0) ]
        
        if benchmarkEngine:
            benchmarkEngine.begin()
            
        while queue:
            query = queue.pop()
            term = query[0]
            depth = query[1]
            response = self.queryProcessor.process(term)

            if not response:
                continue
            
            if response.definition is not None:
                definitions[term] = response.definition

            response.refinements.sort()
            for refinement in response.refinements:
                queue.append((refinement.formattedName, depth + 1))

            if depth == 0:
                domainTerms = response.getDomainTerms()

        if benchmarkEngine:
            benchmarkEngine.end()

        return ResponseFormatter().formatResponse(term, definitions, domainTerms)

        print('Termes associés : ')
        domainTerms.sort(reverse=True)

        for term in domainTerms:
            print(" - " + term.name + ", poids=" + str(term.weight))
        print(len(domainTerms))
