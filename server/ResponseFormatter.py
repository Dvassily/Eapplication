import json

class ResponseFormatter:
    QUERY_KEY = 'query'
    DEFINITION_KEY = 'definition'
    DOMAIN_TERMS_KEY = 'domainTerms'
    
    def formatResponse(self, query, definitions, domainTerms):
        resultDict = dict()

        resultDict[ResponseFormatter.QUERY_KEY] = query
        resultDict[ResponseFormatter.DEFINITION_KEY] = definitions
        resultDict[ResponseFormatter.DOMAIN_TERMS_KEY] = [ term.__dict__ for term in domainTerms ]
    
        return json.dumps(resultDict, indent=2)
