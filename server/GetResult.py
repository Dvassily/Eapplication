#!/usr/bin/env python

class GetResult:
    def __init__(self, query, term, definitions, domain_terms, associations, parts):
        self.query = query
        self.term = term
        self.definitions = definitions
        self.domain_terms = domain_terms
        self.associations = associations
        self.parts = parts
