import json

class ResponseFormatter:
    # Response keys
    STATUS_KEY = 'status'

    # For query results
    TERM_KEY = 'term'
    QUERY_KEY = 'query'
    DEFINITIONS_KEY = 'definitions'
    DOMAIN_TERMS_KEY = 'domainTerms'
    ASSOCIATIONS_KEY = 'associations';
    PARTS_KEY = 'parts';

    # For query parsing results
    COMMAND_KEY = 'command'
    TERM_KEY = 'term'
    PROPERTIES_KEY = 'properties'
    ## Error cases
    COLUMN_KEY = 'column'

    # Status codes
    STATUS_ERROR = 0
    STATUS_OK = 1

    def formatQueryResult(self, apiResponse):
        result_dict = dict()

        result_dict[ResponseFormatter.STATUS_KEY] = ResponseFormatter.STATUS_OK
        result_dict[ResponseFormatter.TERM_KEY] = apiResponse.query.term
        result_dict[ResponseFormatter.QUERY_KEY] = apiResponse.query.toDict()
        result_dict[ResponseFormatter.DEFINITIONS_KEY] = apiResponse.definitions
        result_dict[ResponseFormatter.DOMAIN_TERMS_KEY] = [ term.__dict__ for term in apiResponse.domain_terms ]
        result_dict[ResponseFormatter.ASSOCIATIONS_KEY] = [ association.__dict__ for association in apiResponse.associations ]
        result_dict[ResponseFormatter.PARTS_KEY] = [ part.__dict__ for part in apiResponse.parts ]

        return json.dumps(result_dict, indent=2)

    def formatQueryParsingResult(self, query):
        result_dict = dict()

        result_dict[ResponseFormatter.STATUS_KEY] = ResponseFormatter.STATUS_OK
        result_dict[ResponseFormatter.COMMAND_KEY] = query.__class__.__name__
        result_dict[ResponseFormatter.TERM_KEY] = query.term
        result_dict[ResponseFormatter.PROPERTIES_KEY] = query.properties

        return json.dumps(result_dict, indent=2)

    def formatQueryParsingError(self, error):
        result_dict = dict()

        result_dict[ResponseFormatter.STATUS_KEY] = ResponseFormatter.STATUS_ERROR
        result_dict[ResponseFormatter.COLUMN_KEY] = error.col

        return json.dumps(result_dict, indent=2)
