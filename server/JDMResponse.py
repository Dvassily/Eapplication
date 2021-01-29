from Node import *
from Relation import *
from CSVModel import *

from selectolax.parser import HTMLParser
import csv
import re
import urllib.parse

class JDMResponse:
    def __init__(self):
        self.query_str = None
        self.definition = None
        self.refinements = []
        self.terms = []
        self.relations = []
        self.parts = []
        
    def getTerms(self):
        return [ term for term in self.terms if term.weight > 0 ]
        
    def getDomainTerms(self):
        relationDestNodes = [ relation.node2 for relation in self.relations if relation.relationType == CSVModel.RELATION_TYPE_DOMAIN]
        return [ term for term in self.getTerms() if term.nodeId in relationDestNodes ]
        
    def getAssociations(self):
        relationDestNodes = [ relation.node2 for relation in self.relations if relation.relationType == CSVModel.RELATION_TYPE_ASSOCIATION]
        return [ term for term in self.getTerms() if term.nodeId in relationDestNodes ]

    def getParts(self):
        relationDestNodes = [ relation.node2 for relation in self.relations if relation.relationType == CSVModel.RELATION_TYPE_HAS_PART]
        return [ term for term in self.getTerms() if term.nodeId in relationDestNodes ]        

    def getAntonyms(self):
        relationDestNodes = [ relation.node2 for relation in self.relations if relation.relationType == CSVModel.RELATION_TYPE_ANTONYM]
        return [ term for term in self.getTerms() if term.nodeId in relationDestNodes ]        
