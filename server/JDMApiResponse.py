#!/usr/bin/env python

class JDMApiResponse:
    def __init__(self, query):
        self.query = query
        self.definitions = []
        self.domain_terms = []
        self.associations = []
        self.parts = []
