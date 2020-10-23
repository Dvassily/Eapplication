from JDMResponse import *
from CSVModel import *

from selectolax.parser import HTMLParser
import urllib.parse
import requests as r

class QueryProcessor:
    def __init__(self, urlPrefix, urlPostfix):
        self.urlPrefix = urlPrefix
        self.urlPostfix = urlPostfix
    
    def process(self, query):
        query = urllib.parse.quote_plus(query, encoding='iso-8859-1')
        html = r.get(self.buildUrl(query))
        tree = HTMLParser(html.text)
        codeTag = tree.css_first('CODE')

        if not codeTag:
            return None
        
        codeText = codeTag.text()

        definitionTag = tree.css_first('def')
        definition = ''
        if definitionTag:
            definitionTag = definitionTag.text()
        
        return self.analyze(query, codeText, definition)
            
    def buildUrl(self, term):
        return self.urlPrefix + term + self.urlPostfix

    def analyze(self, query, code, definition):
        response = JDMResponse()
        
        response.definition = definition
        code.replace(definition, '')
        
        csv_lines = code.split('\n')
        csv_lines = [ line for line in csv_lines if (not line.startswith('//') and len(line) > 0)]
        csv_ds = csv.reader(csv_lines, delimiter=';')

        for entry in csv_ds:
            key = entry[0]
            if (key == CSVModel.KEY_NODE):
                node = self.handleNode(entry, query)
                response.terms.append(node)
                
                if node.isRefinement:
                    response.refinements.append(node)
            
            elif (key == CSVModel.KEY_RELATION):
                relation = self.handleRelation(entry)
                response.relations.append(relation)

        return response
                
    def handleNode(self, entry, query):
        depth = len(query.split('>'))

        nodeType = int(entry[CSVModel.INDEX_NODE_TYPE])
        nodeId = int(entry[CSVModel.INDEX_NODE_ID])
        nodeWeight = int(entry[CSVModel.INDEX_NODE_WEIGHT])
        formattedName = None
        isRefinement = False
        name = None
        
        if nodeType == CSVModel.NODE_TYPE_TERM:
            name = entry[CSVModel.INDEX_NODE_NAME]
            
            if len(entry) > 5:
                formattedName = entry[CSVModel.INDEX_NODE_FORMATTED_NAME]
                formattedName = formattedName.replace('\'', '')

                if ">" in formattedName and (len(formattedName.split('>')) > depth) and formattedName.startswith(query + ">"):
                    isRefinement = True

        return Node(nodeId, name, nodeType, nodeWeight, formattedName, isRefinement)


    def handleRelation(self, entry):
        relationId = int(entry[CSVModel.INDEX_RELATION_TYPE])
        node1 = int(entry[CSVModel.INDEX_RELATION_NODE1])
        node2 = int(entry[CSVModel.INDEX_RELATION_NODE2])
        relationType = int(entry[CSVModel.INDEX_RELATION_TYPE])

        return Relation(relationId, node1, node2, relationType)
