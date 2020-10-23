import json

class ResponseFormatter:
    QUERY_KEY = 'query'
    DEFINITION_KEY = 'definition'
    DOMAIN_TERMS_KEY = 'domainTerms'
    ASSOCIATIONS_KEY = 'associations';
    PARTS_KEY = 'parts';
    
    def formatResponse(self, query, definitions, domainTerms, associations, parts):
        resultDict = dict()

        resultDict[ResponseFormatter.QUERY_KEY] = query
        resultDict[ResponseFormatter.DEFINITION_KEY] = definitions
        resultDict[ResponseFormatter.DOMAIN_TERMS_KEY] = [ term.__dict__ for term in domainTerms ]
        resultDict[ResponseFormatter.ASSOCIATIONS_KEY] = [ association.__dict__ for association in associations ]
        resultDict[ResponseFormatter.PARTS_KEY] = [ part.__dict__ for part in parts ]
        
        return json.dumps(resultDict, indent=2)
